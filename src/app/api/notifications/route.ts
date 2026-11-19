import { NextRequest, NextResponse } from "next/server";
import { createClient } from "@supabase/supabase-js";
import { getCurrentAccount, toErrorResponse } from "@/lib/auth/account";

function getAdminClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
  );
}

const UUID_RE =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

export async function DELETE(request: NextRequest) {
  let ctx;
  try {
    ctx = await getCurrentAccount();
  } catch (err) {
    return toErrorResponse(err);
  }

  const singleId = request.nextUrl.searchParams.get("id")?.trim();
  if (singleId && !UUID_RE.test(singleId)) {
    return NextResponse.json({ error: "Invalid notification id" }, { status: 400 });
  }

  let query = getAdminClient()
    .from("notifications")
    .delete({ count: "exact" })
    .eq("account_id", ctx.accountId)
    .eq("user_id", ctx.userId)
    .not("read_at", "is", null);

  if (singleId) {
    query = query.eq("id", singleId);
  }

  const { error, count } = await query;
  if (error) {
    console.error("[api/notifications DELETE] Failed:", error);
    return NextResponse.json(
      { error: "Failed to delete read notifications" },
      { status: 500 },
    );
  }

  return NextResponse.json({ ok: true, deleted: count ?? 0 });
}
