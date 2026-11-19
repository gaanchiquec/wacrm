import { NextRequest, NextResponse } from "next/server";
import { requireRole, toErrorResponse } from "@/lib/auth/account";

const ALLOWED_UPSTREAM_PREFIXES = [
  "centro-mando",
  "dashboard",
  "pack-creativo",
  "Pack_Creativo_Lote_Piloto_Animallium.html",
  "api/dashboard/",
  "api/proposals/",
  "api/scout/",
  "api/actions/",
  "api/dropi/",
  "api/dropshipping/",
  "api/orders/",
  "api/citas/",
];

function isAllowedPath(joinedPath: string): boolean {
  return ALLOWED_UPSTREAM_PREFIXES.some(
    (prefix) => joinedPath === prefix || joinedPath.startsWith(prefix),
  );
}

async function proxyToAiCore(
  request: NextRequest,
  context: { params: Promise<{ path: string[] }> },
) {
  try {
    await requireRole("admin");
  } catch (err) {
    return toErrorResponse(err);
  }

  const { path } = await context.params;
  const joinedPath = (path || []).join("/");

  if (!isAllowedPath(joinedPath)) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  const baseUrl = (
    process.env.ANIMALLIUM_AI_CORE_URL || "https://n8n.animallium.pet"
  ).replace(/\/+$/, "");
  const token =
    process.env.ANIMALLIUM_AI_CORE_TOKEN ||
    process.env.DASHBOARD_PASSWORD ||
    "";

  if (!token) {
    return NextResponse.json(
      { error: "ANIMALLIUM_AI_CORE_TOKEN is not configured on the server" },
      { status: 500 },
    );
  }

  const targetUrl = `${baseUrl}/${joinedPath}${request.nextUrl.search}`;
  const headers = new Headers();
  headers.set("X-Animallium-Token", token);

  const contentType = request.headers.get("content-type");
  if (contentType) headers.set("content-type", contentType);

  const accept = request.headers.get("accept");
  if (accept) headers.set("accept", accept);

  const init: RequestInit = {
    method: request.method,
    headers,
    cache: "no-store",
  };

  if (request.method !== "GET" && request.method !== "HEAD") {
    init.body = await request.arrayBuffer();
  }

  try {
    const upstream = await fetch(targetUrl, init);
    const outHeaders = new Headers();
    const upstreamType = upstream.headers.get("content-type");
    if (upstreamType) outHeaders.set("content-type", upstreamType);
    outHeaders.set("cache-control", "no-store, max-age=0");

    const body = await upstream.arrayBuffer();
    return new NextResponse(body, {
      status: upstream.status,
      headers: outHeaders,
    });
  } catch (err) {
    console.error("[animallium-proxy] Upstream error:", err);
    return NextResponse.json(
      { error: "No se pudo conectar con Animallium AI Core" },
      { status: 502 },
    );
  }
}

export const GET = proxyToAiCore;
export const POST = proxyToAiCore;
export const PUT = proxyToAiCore;
export const PATCH = proxyToAiCore;
export const DELETE = proxyToAiCore;
