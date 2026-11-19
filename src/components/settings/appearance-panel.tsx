"use client";

import { useEffect, useState } from "react";
import {
  Check,
  Image as ImageIcon,
  MessageSquare,
  Moon,
  Palette,
  RotateCcw,
  Save,
  SunMoon,
  Sun,
  Upload,
} from "lucide-react";

import { useTheme } from "@/hooks/use-theme";
import { useAuth } from "@/hooks/use-auth";
import {
  getEnvBrandDefaults,
  readStoredBrand,
  saveStoredBrand,
} from "@/lib/branding";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { MODES, THEMES, type Mode, type ThemeId } from "@/lib/themes";
import { cn } from "@/lib/utils";
import { toast } from "sonner";
import { useTranslations } from "next-intl";
import { SettingsPanelHead } from "./settings-panel-head";

/**
 * Appearance panel — light/dark mode + accent-color picker.
 *
 * Two independent controls: a mode toggle (light / dark) and the
 * accent grid. Either applies + persists immediately. No save button:
 * each change is a single attribute swap on <html>, there's nothing
 * to roll back.
 *
 * Persistence: localStorage only (device-scoped). The boot script in
 * layout.tsx replays both choices before first paint on subsequent
 * loads.
 */
export function AppearancePanel() {
  const { theme, setTheme, mode, setMode } = useTheme();
  const { account, accountRole, refreshProfile } = useAuth();
  const t = useTranslations("Settings.appearance");

  const [brandName, setBrandName] = useState("");
  const [brandLogoUrl, setBrandLogoUrl] = useState("");
  const [savingBrand, setSavingBrand] = useState(false);

  useEffect(() => {
    const saved = readStoredBrand();
    const envDefaults = getEnvBrandDefaults();
    setBrandName(saved.name || envDefaults.name || account?.name || "");
    setBrandLogoUrl(saved.logoUrl || envDefaults.logoUrl || "");
  }, [account?.name]);

  const handleSaveBrand = async (e: React.FormEvent) => {
    e.preventDefault();
    setSavingBrand(true);
    try {
      saveStoredBrand(brandName, brandLogoUrl);
      if (brandName.trim()) {
        document.title = brandName.trim();
      }
      if (
        brandName.trim() &&
        (accountRole === "owner" || accountRole === "admin")
      ) {
        await fetch("/api/account", {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name: brandName.trim() }),
        });
        await refreshProfile();
      }
      toast.success(t("brandSaved"));
    } catch {
      toast.error(t("brandSaveFailed"));
    } finally {
      setSavingBrand(false);
    }
  };

  const handleResetBrand = () => {
    saveStoredBrand("", "");
    const envDefaults = getEnvBrandDefaults();
    setBrandName(envDefaults.name || account?.name || "");
    setBrandLogoUrl(envDefaults.logoUrl || "");
    toast.success(t("brandResetDone"));
  };

  const handleLogoFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    if (file.size > 1_000_000) {
      toast.error(t("brandLogoTooLarge"));
      return;
    }
    const reader = new FileReader();
    reader.onload = () => {
      if (typeof reader.result === "string") {
        setBrandLogoUrl(reader.result);
      }
    };
    reader.readAsDataURL(file);
  };

  return (
    <section className="max-w-3xl animate-in fade-in-50 duration-200">
      <SettingsPanelHead
        title={t("title")}
        description={t("description")}
      />

      <div className="space-y-4">
        <h3 className="flex items-center gap-2 text-sm font-semibold text-foreground">
          <SunMoon className="size-4 text-muted-foreground" />
          {t("mode")}
        </h3>

        <div
          role="radiogroup"
          aria-label={t("colorMode")}
          className="grid max-w-md grid-cols-2 gap-3"
        >
          {MODES.map((m) => (
            <ModeCard
              key={m}
              mode={m}
              isActive={m === mode}
              onPick={() => setMode(m)}
            />
          ))}
        </div>
      </div>

      <div className="mt-8 space-y-4">
        <h3 className="flex items-center gap-2 text-sm font-semibold text-foreground">
          <Palette className="size-4 text-muted-foreground" />
          {t("accentColor")}
        </h3>

        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {THEMES.map((tObj) => (
            <ThemeCard
              key={tObj.id}
              id={tObj.id}
              name={tObj.name}
              tagline={tObj.tagline}
              swatch={tObj.swatch}
              isActive={tObj.id === theme}
              onPick={() => setTheme(tObj.id)}
            />
          ))}
        </div>
      </div>

      <div className="mt-10 border-t border-border pt-8 space-y-4">
        <div>
          <h3 className="flex items-center gap-2 text-sm font-semibold text-foreground">
            <ImageIcon className="size-4 text-muted-foreground" />
            {t("brandTitle")}
          </h3>
          <p className="mt-1 text-xs text-muted-foreground">
            {t("brandDescription")}
          </p>
        </div>

        <form
          onSubmit={handleSaveBrand}
          className="space-y-4 rounded-xl border border-border bg-card p-5"
        >
          <div className="flex items-center gap-3 rounded-lg border border-border/80 bg-muted/40 px-4 py-3">
            {brandLogoUrl.trim() ? (
              <img
                src={brandLogoUrl.trim()}
                alt={brandName || "CRM"}
                className="h-9 w-9 shrink-0 rounded-lg border border-border bg-white object-contain p-0.5"
              />
            ) : (
              <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-primary text-primary-foreground">
                <MessageSquare className="h-4 w-4" />
              </div>
            )}
            <div className="min-w-0">
              <div className="text-[11px] uppercase tracking-wider text-muted-foreground">
                {t("brandPreview")}
              </div>
              <div className="truncate text-sm font-semibold text-foreground">
                {brandName.trim() || "CRM"}
              </div>
            </div>
          </div>

          <div className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-1.5">
              <Label htmlFor="brand-name">{t("brandNameLabel")}</Label>
              <Input
                id="brand-name"
                value={brandName}
                onChange={(e) => setBrandName(e.target.value)}
                placeholder={t("brandNamePlaceholder")}
                maxLength={80}
              />
            </div>

            <div className="space-y-1.5">
              <Label htmlFor="brand-logo-url">{t("brandLogoLabel")}</Label>
              <div className="flex items-center gap-2">
                <Input
                  id="brand-logo-url"
                  value={brandLogoUrl}
                  onChange={(e) => setBrandLogoUrl(e.target.value)}
                  placeholder="https://..."
                />
                <label className="inline-flex h-9 shrink-0 cursor-pointer items-center gap-1.5 rounded-md border border-input bg-background px-3 text-xs font-medium hover:bg-accent">
                  <Upload className="h-3.5 w-3.5" />
                  <span>{t("brandUpload")}</span>
                  <input
                    type="file"
                    accept="image/png,image/jpeg,image/webp,image/svg+xml"
                    onChange={handleLogoFile}
                    className="hidden"
                  />
                </label>
              </div>
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-2 pt-1">
            <Button type="submit" size="sm" disabled={savingBrand}>
              <Save className="h-4 w-4" />
              {savingBrand ? t("brandSaving") : t("brandSave")}
            </Button>
            <Button
              type="button"
              variant="outline"
              size="sm"
              onClick={handleResetBrand}
            >
              <RotateCcw className="h-4 w-4" />
              {t("brandReset")}
            </Button>
          </div>
        </form>
      </div>
    </section>
  );
}

function ModeCard({
  mode,
  isActive,
  onPick,
}: {
  mode: Mode;
  isActive: boolean;
  onPick: () => void;
}) {
  const t = useTranslations("Settings.appearance");
  const isLight = mode === "light";
  const Icon = isLight ? Sun : Moon;
  return (
    <button
      type="button"
      role="radio"
      onClick={onPick}
      aria-checked={isActive}
      aria-label={t("useMode", { mode })}
      className={cn(
        "flex items-center gap-3 rounded-lg border bg-card p-4 text-left transition-colors",
        isActive
          ? "border-primary/60 ring-2 ring-primary/40"
          : "border-border hover:border-border hover:bg-muted/40",
      )}
    >
      <span
        aria-hidden
        className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-muted text-foreground"
      >
        <Icon className="h-4 w-4" />
      </span>
      <span className="flex-1 text-sm font-semibold capitalize text-foreground">
        {mode}
      </span>
      {isActive && (
        <span className="inline-flex items-center gap-1 rounded-full bg-primary/15 px-2 py-0.5 text-[11px] font-medium text-primary">
          <Check className="h-3 w-3" />
          {t("active")}
        </span>
      )}
    </button>
  );
}

function ThemeCard({
  id,
  name,
  tagline,
  swatch,
  isActive,
  onPick,
}: {
  id: ThemeId;
  name: string;
  tagline: string;
  swatch: string;
  isActive: boolean;
  onPick: () => void;
}) {
  const t = useTranslations("Settings.appearance");
  return (
    <button
      type="button"
      onClick={onPick}
      aria-pressed={isActive}
      aria-label={t("useTheme", { name })}
      className={cn(
        "flex flex-col gap-3 rounded-lg border bg-card p-4 text-left transition-colors",
        isActive
          ? "border-primary/60 ring-2 ring-primary/40"
          : "border-border hover:border-border hover:bg-muted/40",
      )}
    >
      <div className="flex items-center justify-between">
        <span
          aria-hidden
          className="h-8 w-8 shrink-0 rounded-full"
          style={{
            background: swatch,
            boxShadow: "inset 0 0 0 1px oklch(1 0 0 / 0.15)",
          }}
        />
        {isActive && (
          <span className="inline-flex items-center gap-1 rounded-full bg-primary/15 px-2 py-0.5 text-[11px] font-medium text-primary">
            <Check className="h-3 w-3" />
            {t("active")}
          </span>
        )}
      </div>
      <div>
        <div className="text-sm font-semibold text-foreground">{name}</div>
        <div className="mt-1 text-xs leading-relaxed text-muted-foreground">
          {tagline}
        </div>
      </div>
      <div
        className="mt-1 flex h-2 overflow-hidden rounded-full"
        aria-hidden
      >
        <span className="flex-1" style={{ background: swatch }} />
        <span className="w-3 bg-muted-foreground/60" />
        <span className="w-3 bg-muted" />
        <span className="w-3 bg-card" />
      </div>
      <span className="sr-only">{t("themeId", { id })}</span>
    </button>
  );
}
