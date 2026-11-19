/**
 * Client-side branding override helpers for the CRM sidebar header.
 *
 * Precedence:
 *   1. User override saved in Settings -> Appearance (`localStorage`)
 *   2. Deployment-level env defaults (`NEXT_PUBLIC_APP_NAME` / `NEXT_PUBLIC_APP_LOGO_URL`)
 *   3. Workspace account name (when renamed) or localized fallback title
 */

export const BRAND_NAME_KEY = "wacrm.brandName";
export const BRAND_LOGO_KEY = "wacrm.brandLogoUrl";
export const BRAND_UPDATED_EVENT = "wacrm:brand-updated";

export interface BrandConfig {
  name: string;
  logoUrl: string;
}

export function getEnvBrandDefaults(): BrandConfig {
  return {
    name: (process.env.NEXT_PUBLIC_APP_NAME || "").trim(),
    logoUrl: (process.env.NEXT_PUBLIC_APP_LOGO_URL || "").trim(),
  };
}

export function readStoredBrand(): BrandConfig {
  if (typeof window === "undefined") return { name: "", logoUrl: "" };
  try {
    return {
      name: (localStorage.getItem(BRAND_NAME_KEY) || "").trim(),
      logoUrl: (localStorage.getItem(BRAND_LOGO_KEY) || "").trim(),
    };
  } catch {
    return { name: "", logoUrl: "" };
  }
}

export function saveStoredBrand(name: string, logoUrl: string): void {
  if (typeof window === "undefined") return;
  try {
    const cleanName = name.trim();
    const cleanLogo = logoUrl.trim();
    if (cleanName) localStorage.setItem(BRAND_NAME_KEY, cleanName);
    else localStorage.removeItem(BRAND_NAME_KEY);

    if (cleanLogo) localStorage.setItem(BRAND_LOGO_KEY, cleanLogo);
    else localStorage.removeItem(BRAND_LOGO_KEY);

    window.dispatchEvent(new CustomEvent(BRAND_UPDATED_EVENT));
  } catch {
    // Ignore storage quota / private mode failures gracefully.
  }
}
