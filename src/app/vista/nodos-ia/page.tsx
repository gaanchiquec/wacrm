export default function StandaloneNodosIaPage() {
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
