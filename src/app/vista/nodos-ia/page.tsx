import { notFound, redirect } from "next/navigation";
import { requireRole } from "@/lib/auth/account";

export default async function StandaloneNodosIaPage() {
  if (process.env.NEXT_PUBLIC_ENABLE_ANIMALLIUM_OS !== "true") {
    notFound();
  }

  try {
    await requireRole("admin");
  } catch {
    redirect("/dashboard");
  }

  return (
    <main className="h-screen w-screen overflow-hidden bg-slate-950">
      <iframe
        src="/api/animallium-proxy/dashboard"
        className="h-full w-full border-0"
        title="Monitor Visual de Nodos IA (Vista Independiente)"
      />
    </main>
  );
}
