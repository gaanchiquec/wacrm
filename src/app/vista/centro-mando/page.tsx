export default function StandaloneCentroMandoPage() {
  return (
    <main className="h-screen w-screen overflow-hidden bg-slate-950">
      <iframe
        src="/api/animallium-proxy/centro-mando"
        className="h-full w-full border-0"
        title="Centro de Mando Animallium (Vista Independiente)"
      />
    </main>
  );
}
