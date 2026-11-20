"use client";

import { useCallback, useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { useAuth } from "@/hooks/use-auth";
import { notificationsAccountFilter } from "@/lib/notifications/unread-count";
import type { Notification } from "@/types";
import {
  Bell,
  CheckCheck,
  Loader2,
  Trash2,
  UserPlus,
  MessageSquare,
  MessageSquarePlus,
  DollarSign,
  Bot,
  ShieldAlert
} from "lucide-react";
import { formatDistanceToNow } from "date-fns";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { toast } from "sonner";
import { useTranslations } from "next-intl";

const TYPE_ICON: Record<Notification["type"], typeof Bell> = {
  conversation_assigned: UserPlus,
  new_conversation: MessageSquarePlus,
  new_message: MessageSquare,
  deal_created: DollarSign,
  ai_handoff: Bot,
  control_tower_alert: ShieldAlert,
};

export default function NotificationsPage() {
  const t = useTranslations("Notifications");
  const router = useRouter();
  const { accountId } = useAuth();
  const [notifications, setNotifications] = useState<Notification[] | null>(
    null,
  );
  const [error, setError] = useState<string | null>(null);
  const [markingAll, setMarkingAll] = useState(false);
  const [clearingRead, setClearingRead] = useState(false);
  const [deletingId, setDeletingId] = useState<string | null>(null);

  const load = useCallback(async () => {
    if (!accountId) return;
    const supabase = createClient();
    const { data, error: fetchErr } = await supabase
      .from("notifications")
      .select("*")
      .eq("account_id", accountId)
      .order("created_at", { ascending: false })
      .limit(100);
    if (fetchErr) {
      setError(fetchErr.message);
      return;
    }
    setNotifications((data ?? []) as Notification[]);
  }, [accountId]);

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    load();
  }, [load]);

  // Realtime — new assignments appear without a refresh, and a
  // "mark all read" fired from another tab/device stays in sync here.
  useEffect(() => {
    if (!accountId) return;
    const supabase = createClient();
    const channel = supabase
      .channel(`notifications-page:${accountId}`)
      .on(
        "postgres_changes",
        {
          event: "*",
          schema: "public",
          table: "notifications",
          filter: notificationsAccountFilter(accountId),
        },
        (payload) => {
          if (payload.eventType === "INSERT") {
            const row = payload.new as Notification;
            setNotifications((prev) => {
              if (!prev) return [row];
              if (prev.some((n) => n.id === row.id)) return prev;
              return [row, ...prev];
            });
          } else if (payload.eventType === "UPDATE") {
            const row = payload.new as Notification;
            setNotifications((prev) =>
              prev?.map((n) => (n.id === row.id ? { ...n, ...row } : n)) ??
              prev,
            );
          } else if (payload.eventType === "DELETE") {
            const oldRow = payload.old as Partial<Notification>;
            setNotifications(
              (prev) => prev?.filter((n) => n.id !== oldRow.id) ?? prev,
            );
          }
        },
      )
      .subscribe();

    return () => {
      supabase.removeChannel(channel);
    };
  }, [accountId]);

  const markRead = useCallback(
    async (id: string) => {
      // Optimistic — the row is already visually "read" by the time the
      // request lands, so the UI doesn't wait on the round-trip.
      setNotifications(
        (prev) =>
          prev?.map((n) =>
            n.id === id && !n.read_at
              ? { ...n, read_at: new Date().toISOString() }
              : n,
          ) ?? prev,
      );
      const supabase = createClient();
      const { error: updateErr } = await supabase
        .from("notifications")
        .update({ read_at: new Date().toISOString() })
        .eq("id", id)
        .is("read_at", null);
      if (updateErr) {
        toast.error(t("markReadFailed"));
        load();
      }
    },
    [load, t],
  );

  const handleClick = useCallback(
    (n: Notification) => {
      if (!n.read_at) markRead(n.id);
      if (n.conversation_id) {
        router.push(`/inbox?c=${n.conversation_id}`);
      } else if (n.deal_id) {
        router.push(`/pipelines`);
      }
    },
    [markRead, router],
  );

  const unreadIds = notifications?.filter((n) => !n.read_at).map((n) => n.id) ?? [];
  const readIds = notifications?.filter((n) => Boolean(n.read_at)).map((n) => n.id) ?? [];

  const markAllRead = useCallback(async () => {
    if (unreadIds.length === 0 || !accountId) return;
    setMarkingAll(true);
    const now = new Date().toISOString();
    setNotifications(
      (prev) => prev?.map((n) => (n.read_at ? n : { ...n, read_at: now })) ?? prev,
    );
    const supabase = createClient();
    const { error: updateErr } = await supabase
      .from("notifications")
      .update({ read_at: now })
      .eq("account_id", accountId)
      .is("read_at", null);
    setMarkingAll(false);
    if (updateErr) {
      toast.error(t("markAllFailed"));
      load();
    }
  }, [unreadIds.length, accountId, load, t]);

  const clearAllRead = useCallback(async () => {
    if (readIds.length === 0 || clearingRead) return;
    setClearingRead(true);
    const prevSnapshot = notifications;
    setNotifications((prev) => prev?.filter((n) => !n.read_at) ?? prev);
    try {
      const res = await fetch("/api/notifications", { method: "DELETE" });
      if (!res.ok) throw new Error("delete_failed");
      toast.success(t("clearReadSuccess"));
    } catch {
      setNotifications(prevSnapshot);
      toast.error(t("clearReadFailed"));
    } finally {
      setClearingRead(false);
    }
  }, [readIds.length, clearingRead, notifications, t]);

  const deleteSingleRead = useCallback(
    async (id: string) => {
      if (deletingId) return;
      setDeletingId(id);
      const prevSnapshot = notifications;
      setNotifications((prev) => prev?.filter((n) => n.id !== id) ?? prev);
      try {
        const res = await fetch(
          `/api/notifications?id=${encodeURIComponent(id)}`,
          { method: "DELETE" },
        );
        if (!res.ok) throw new Error("delete_failed");
      } catch {
        setNotifications(prevSnapshot);
        toast.error(t("clearReadFailed"));
      } finally {
        setDeletingId(null);
      }
    },
    [deletingId, notifications, t],
  );

  if (error) {
    return (
      <div className="flex h-64 flex-col items-center justify-center gap-2">
        <p className="text-sm text-destructive">{error}</p>
        <Button variant="outline" onClick={() => window.location.reload()}>
          {t("retry")}
        </Button>
      </div>
    );
  }

  if (notifications === null) {
    return (
      <div className="flex h-64 items-center justify-center">
        <Loader2 className="h-6 w-6 animate-spin text-primary" />
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-bold text-foreground">{t("title")}</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            {t("description")}
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          <Button
            variant="outline"
            size="sm"
            disabled={unreadIds.length === 0 || markingAll}
            onClick={markAllRead}
          >
            {markingAll ? (
              <Loader2 className="h-4 w-4 animate-spin" />
            ) : (
              <CheckCheck className="h-4 w-4" />
            )}
            {t("markAllRead")}
          </Button>
          <Button
            variant="outline"
            size="sm"
            disabled={readIds.length === 0 || clearingRead}
            onClick={clearAllRead}
          >
            {clearingRead ? (
              <Loader2 className="h-4 w-4 animate-spin" />
            ) : (
              <Trash2 className="h-4 w-4" />
            )}
            {t("clearRead")}
          </Button>
        </div>
      </div>

      {notifications.length === 0 ? (
        <div className="flex h-48 flex-col items-center justify-center rounded-xl border border-dashed border-border bg-muted/40">
          <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-primary/10">
            <Bell className="h-6 w-6 text-primary" />
          </div>
          <p className="mt-3 text-sm font-medium text-foreground">
            {t("emptyTitle")}
          </p>
          <p className="mt-1 text-xs text-muted-foreground">
            {t("emptyDesc")}
          </p>
        </div>
      ) : (
        <ul className="space-y-2">
          {notifications.map((n) => {
            let Icon = TYPE_ICON[n.type] ?? Bell;
            const lowerTitle = (n.title || "").toLowerCase();
            if (n.type === "new_conversation" || lowerTitle.includes("conversación")) {
              Icon = MessageSquarePlus;
            } else if (n.type === "new_message" || lowerTitle.includes("mensaje")) {
              Icon = MessageSquare;
            } else if (n.type === "deal_created" || n.deal_id || lowerTitle.includes("negocio") || lowerTitle.includes("cliente")) {
              Icon = DollarSign;
            } else if (n.type === "ai_handoff") {
              Icon = Bot;
            } else if (n.type === "control_tower_alert" || lowerTitle.includes("[torre de control]")) {
              Icon = ShieldAlert;
            }
            const isUnread = !n.read_at;
            return (
              <li key={n.id} className="relative">
                <div
                  className={cn(
                    "flex w-full items-start gap-3 rounded-xl border p-4 transition-colors",
                    isUnread
                      ? "border-primary/30 bg-primary/5 hover:border-primary/50"
                      : "border-border bg-card hover:border-border/70",
                  )}
                >
                  <button
                    type="button"
                    onClick={() => handleClick(n)}
                    className="flex min-w-0 flex-1 items-start gap-3 text-left"
                  >
                    <div
                      className={cn(
                        "flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-lg",
                        isUnread ? "bg-primary/15" : "bg-muted",
                      )}
                      aria-hidden
                    >
                      <Icon
                        className={cn(
                          "h-5 w-5",
                          isUnread ? "text-primary" : "text-muted-foreground",
                        )}
                      />
                    </div>
                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-2">
                        <span
                          className={cn(
                            "truncate text-sm font-semibold",
                            isUnread ? "text-foreground" : "text-muted-foreground",
                          )}
                        >
                          {n.title}
                        </span>
                        {isUnread && (
                          <span
                            aria-label={t("unread")}
                            className="h-2 w-2 flex-shrink-0 rounded-full bg-primary"
                          />
                        )}
                      </div>
                      {n.body && (
                        <p className="mt-0.5 truncate text-xs text-muted-foreground">
                          {n.body}
                        </p>
                      )}
                      <p className="mt-1 text-[11px] text-muted-foreground/70">
                        {formatDistanceToNow(new Date(n.created_at), {
                          addSuffix: true,
                        })}
                      </p>
                    </div>
                  </button>
                  {!isUnread && (
                    <button
                      type="button"
                      onClick={() => deleteSingleRead(n.id)}
                      disabled={deletingId === n.id}
                      aria-label={t("deleteOne")}
                      title={t("deleteOne")}
                      className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:bg-destructive/10 hover:text-destructive"
                    >
                      {deletingId === n.id ? (
                        <Loader2 className="h-4 w-4 animate-spin" />
                      ) : (
                        <Trash2 className="h-4 w-4" />
                      )}
                    </button>
                  )}
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
