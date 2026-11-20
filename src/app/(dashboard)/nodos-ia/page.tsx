'use client'

import { ExternalLink, RefreshCw, ShieldAlert } from 'lucide-react'
import { useState } from 'react'
import { useAuth } from '@/hooks/use-auth'

const ANIMALLIUM_OS_ENABLED = process.env.NEXT_PUBLIC_ENABLE_ANIMALLIUM_OS === 'true'

export default function NodosIaPage() {
  const [key, setKey] = useState(0)
  const { accountRole, profileLoading } = useAuth()

  if (!ANIMALLIUM_OS_ENABLED) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center p-6">
        <div className="max-w-md rounded-xl border border-border bg-card p-6 text-center">
          <ShieldAlert className="mx-auto mb-3 h-8 w-8 text-muted-foreground" />
          <h2 className="text-base font-semibold text-foreground">Módulo desactivado</h2>
          <p className="mt-1 text-xs text-muted-foreground">
            El Monitor de Nodos IA no está habilitado en este entorno.
          </p>
        </div>
      </div>
    )
  }

  if (profileLoading) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center text-sm text-muted-foreground">
        Verificando permisos...
      </div>
    )
  }

  if (accountRole !== 'owner' && accountRole !== 'admin') {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center p-6">
        <div className="max-w-md rounded-xl border border-border bg-card p-6 text-center">
          <ShieldAlert className="mx-auto mb-3 h-8 w-8 text-amber-500" />
          <h2 className="text-base font-semibold text-foreground">Acceso restringido</h2>
          <p className="mt-1 text-xs text-muted-foreground">
            Solo administradores y propietarios pueden acceder al Monitor Visual de Nodos IA.
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="flex flex-col h-[calc(100vh-4rem)] w-full overflow-hidden bg-background">
      <div className="flex items-center justify-between px-6 py-2.5 border-b border-border bg-card/60 backdrop-blur-sm">
        <div className="flex items-center gap-3">
          <span className="text-xl">🧠</span>
          <div>
            <h1 className="text-sm font-bold text-foreground">
              Monitor Visual de Nodos IA (Animallium AI Core)
            </h1>
            <p className="text-xs text-muted-foreground">
              Canvas interactivo con Ani (Productos), Sofi (Servicios), Triage Médico y Director Alianzas B2B
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => setKey(prev => prev + 1)}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-border bg-muted/50 hover:bg-muted text-xs font-medium text-foreground transition-colors"
            title="Recargar vista"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span>Recargar</span>
          </button>

          <a
            href="/vista/nodos-ia"
            target="_blank"
            rel="noopener"
            className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-700 text-xs font-bold text-white shadow-sm transition-colors"
          >
            <span>Abrir en Pestaña Nueva</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>
      </div>

      <div className="flex-1 w-full h-full relative">
        <iframe
          key={key}
          src={key === 0 ? '/api/animallium-proxy/dashboard' : `/api/animallium-proxy/dashboard?r=${key}`}
          className="w-full h-full border-0"
          title="Monitor Visual de Nodos IA"
        />
      </div>
    </div>
  )
}
