# -*- coding: utf-8 -*-
"""
Generador del sitio web Apple Showroom:
Auditoría Crítica y Plan Maestro — CRM Limpio + Centro de Mando Independiente + Torre de Control
Explicado como para un niño de 12 años, usando el mismo diseño Apple Showroom con animaciones mejoradas.
"""
import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="artifact-type" content="narrative">
  <meta name="design-style" content="showroom">
  <title>Animallium 2026 — CRM Limpio, Centro de Mando y Torre de Control</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      color-scheme: light;

      /* Page and surfaces (Showroom - exact Apple Light palette) */
      --background: #fbfbfd;
      --surface-container-low: #f5f5f7;
      --surface-container: #e8e8ed;
      --surface-container-high: #dcdce1;

      /* Ink */
      --on-surface: #1d1d1f;
      --on-surface-variant: #6e6e73;

      /* Rules */
      --outline: #d2d2d7;
      --outline-variant: #e5e5ea;

      /* Accents */
      --primary: #006bd6;
      --primary-hover: #0058b0;
      --on-primary: #ffffff;
      --primary-container: #e8f1fd;
      --on-primary-container: #0058b0;
      --secondary: #bf4800;
      --secondary-container: #fdf0e6;
      --tertiary: #1d1d1f;
      --error: #d70015;
      --error-container: #fdebec;
      --on-error: #ffffff;

      /* Semantic */
      --positive: #248a3d;
      --positive-container: #eaf6ed;
      --warning: #b25000;
      --warning-container: #fef4e6;
      --purple: #8944ab;
      --purple-container: #f5eef9;

      /* Glass header tokens */
      --glass-bg: rgba(251, 251, 253, 0.80);
      --glass-border: rgba(210, 210, 215, 0.55);

      /* Data series */
      --data-1: #006bd6;
      --data-2: #bf4800;
      --data-3: #248a3d;
      --data-4: #8944ab;
      --data-context: #aeaeb2;

      /* Fonts */
      --font-headline: 'Inter Tight', -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
      --font-label: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;

      /* Type scale (Narrative) */
      --display-size: clamp(2.5rem, 1.4rem + 4.2vw, 4.5rem);
      --headline-size: clamp(1.875rem, 1.25rem + 2.2vw, 2.75rem);
      --subhead-size: clamp(1.18rem, 1.02rem + 0.55vw, 1.42rem);
      --body-size: clamp(1.02rem, 0.98rem + 0.2vw, 1.1rem);
      --label-size: clamp(0.78rem, 0.74rem + 0.14vw, 0.84rem);

      /* Spacing scale (4pt base) */
      --space-xs: 0.25rem;
      --space-sm: 0.5rem;
      --space-md: 1rem;
      --space-lg: 1.5rem;
      --space-xl: 2.5rem;
      --space-2xl: 4rem;
      --space-3xl: 5.5rem;

      /* Shape */
      --rounded: 9999px;
      --rounded-md: 1rem;
      --rounded-lg: 1.35rem;
      --rounded-full: 9999px;

      /* Effects */
      --headline-tracking: -0.035em;
      --section-tracking: -0.025em;
      --figure-tracking: -0.03em;
      --tile-shadow-hover: 0 12px 32px rgb(0 0 0 / 0.08);
      --tile-shadow-strong: 0 18px 42px rgb(0 107 214 / 0.12);
      --chevron: " \203A";

      /* Focus */
      --focus: #006bd6;

      /* Motion (Apple Spring curves) */
      --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
      --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
      --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
      --dur-micro: 140ms;
      --dur-short: 260ms;
      --dur-long: 580ms;
    }

    *, *::before, *::after { box-sizing: border-box; }
    html, body {
      overflow-x: clip;
      margin: 0;
      padding: 0;
      background-color: var(--background);
      color: var(--on-surface);
      font-family: var(--font-body);
      font-size: var(--body-size);
      line-height: 1.58;
      -webkit-font-smoothing: antialiased;
      scroll-behavior: smooth;
    }
    button, input, select { font-family: inherit; }
    code {
      font-family: var(--font-mono);
      font-size: 0.86em;
      background: var(--surface-container);
      color: var(--on-surface);
      padding: 2px 7px;
      border-radius: 6px;
    }

    /* Scroll reading progress bar */
    .scroll-progress {
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      width: 0%;
      background: linear-gradient(90deg, var(--primary), var(--purple), var(--secondary));
      z-index: 1200;
      transition: width 80ms linear;
      border-radius: 0 99px 99px 0;
    }

    .page-grid {
      display: grid;
      gap: var(--space-lg);
      padding: 0 var(--space-lg);
      max-width: 1140px;
      margin: 0 auto;
    }
    .page-grid * { min-width: 0; }

    :focus-visible {
      outline: 3px solid var(--focus);
      outline-offset: 2px;
    }

    /* Sticky Apple glass header */
    .top-header {
      position: sticky;
      top: 0;
      z-index: 900;
      background: var(--glass-bg);
      backdrop-filter: saturate(180%) blur(22px);
      -webkit-backdrop-filter: saturate(180%) blur(22px);
      border-bottom: 1px solid var(--glass-border);
      padding: var(--space-sm) var(--space-lg);
      transition: box-shadow var(--dur-short) var(--ease-out);
    }
    .top-header.scrolled {
      box-shadow: 0 6px 24px rgb(0 0 0 / 0.05);
    }
    .top-nav {
      max-width: 1140px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: var(--space-md);
      flex-wrap: wrap;
      min-height: 44px;
    }
    .brand-mark {
      display: inline-flex;
      align-items: center;
      gap: var(--space-sm);
      font-family: var(--font-headline);
      font-weight: 700;
      font-size: 1.02rem;
      letter-spacing: -0.02em;
      color: var(--on-surface);
      text-decoration: none;
    }
    .brand-mark svg {
      transition: transform var(--dur-short) var(--ease-spring);
    }
    .brand-mark:hover svg {
      transform: rotate(90deg) scale(1.06);
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 2px;
      flex-wrap: wrap;
    }
    .nav-pill {
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: var(--space-xs) 12px;
      border-radius: var(--rounded);
      font-size: var(--label-size);
      font-weight: 500;
      color: var(--on-surface-variant);
      text-decoration: none;
      transition: background-color var(--dur-short) var(--ease-out), color var(--dur-short) var(--ease-out), transform var(--dur-micro) var(--ease-out);
    }
    .nav-pill:hover {
      background-color: var(--surface-container-low);
      color: var(--on-surface);
      transform: translateY(-1px);
    }
    .nav-badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 5px 13px;
      border-radius: var(--rounded);
      background: var(--primary-container);
      color: var(--on-primary-container);
      font-size: var(--label-size);
      font-weight: 600;
    }
    .live-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--positive);
      display: inline-block;
      animation: pulseDot 2s ease-in-out infinite;
    }
    @keyframes pulseDot {
      0%, 100% { transform: scale(1); opacity: 1; box-shadow: 0 0 0 0 rgba(36, 138, 61, 0.45); }
      50% { transform: scale(1.2); opacity: 0.85; box-shadow: 0 0 0 6px rgba(36, 138, 61, 0); }
    }

    /* Tonal bands */
    .band {
      padding-block: var(--space-2xl);
      background-color: var(--background);
      position: relative;
    }
    .band.alt {
      background-color: var(--surface-container-low);
    }
    .band.alt .tile {
      background-color: var(--background);
    }

    /* Subtle Hero ambient aura (Apple light showroom style) */
    .hero-aura {
      position: absolute;
      top: -60px;
      left: 50%;
      transform: translateX(-50%);
      width: min(920px, 95vw);
      height: 360px;
      background: radial-gradient(ellipse at center, rgba(0, 107, 214, 0.08) 0%, rgba(137, 68, 171, 0.05) 40%, rgba(191, 72, 0, 0.03) 65%, transparent 78%);
      filter: blur(42px);
      pointer-events: none;
      animation: auraBreathe 9s ease-in-out infinite;
    }
    @keyframes auraBreathe {
      0%, 100% { transform: translateX(-50%) scale(1); opacity: 0.85; }
      50% { transform: translateX(-50%) scale(1.07); opacity: 1; }
    }

    /* Centered headline stack */
    .headline-stack {
      text-align: center;
      padding-block: var(--space-lg) var(--space-xl);
      max-width: 840px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
    }
    .headline-stack.hero-stack {
      padding-block: var(--space-xl) var(--space-lg);
    }
    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      font-family: var(--font-label);
      font-size: var(--label-size);
      font-weight: 600;
      color: var(--secondary);
      background: var(--secondary-container);
      padding: 5px 14px;
      border-radius: var(--rounded);
      margin-bottom: var(--space-md);
      animation: floatSoft 4.2s ease-in-out infinite;
    }
    @keyframes floatSoft {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-3px); }
    }
    .headline-stack h1 {
      font-family: var(--font-headline);
      font-size: var(--display-size);
      font-weight: 700;
      letter-spacing: var(--headline-tracking);
      line-height: 1.04;
      color: var(--on-surface);
      margin: 0;
    }
    .headline-gradient {
      background: linear-gradient(120deg, var(--primary) 0%, var(--purple) 52%, var(--secondary) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-size: 200% auto;
      animation: shimmerText 7s ease-in-out infinite alternate;
    }
    @keyframes shimmerText {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }
    .headline-stack h2 {
      font-family: var(--font-headline);
      font-size: var(--headline-size);
      font-weight: 700;
      letter-spacing: var(--section-tracking);
      line-height: 1.08;
      color: var(--on-surface);
      margin: 0;
    }
    .headline-stack .lede {
      font-size: var(--subhead-size);
      color: var(--on-surface-variant);
      max-width: 52ch;
      margin: var(--space-md) auto 0;
      line-height: 1.46;
    }

    /* Hero kinetic entrance */
    .hero-anim {
      opacity: 0;
      transform: translateY(20px);
      animation: heroEnter 0.8s var(--ease-out) forwards;
    }
    .hero-anim.d1 { animation-delay: 80ms; }
    .hero-anim.d2 { animation-delay: 180ms; }
    .hero-anim.d3 { animation-delay: 300ms; }
    .hero-anim.d4 { animation-delay: 420ms; }
    @keyframes heroEnter {
      to { opacity: 1; transform: translateY(0); }
    }

    /* Prose column */
    .prose-measure {
      max-width: 68ch;
      margin: 0 auto var(--space-xl);
      color: var(--on-surface);
    }
    .prose-measure p { margin: 0 0 var(--space-md); }
    .prose-measure p:last-child { margin-bottom: 0; }
    .prose-measure strong { font-weight: 600; color: var(--on-surface); }

    /* Actions */
    .action-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: var(--space-md);
      flex-wrap: wrap;
      margin-top: var(--space-lg);
    }
    .btn-primary {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: var(--space-sm);
      min-height: 46px;
      background: var(--primary);
      color: var(--on-primary);
      border-radius: var(--rounded);
      font-family: var(--font-label);
      font-size: 0.94rem;
      font-weight: 600;
      padding: var(--space-sm) var(--space-lg);
      border: 0;
      cursor: pointer;
      text-decoration: none;
      box-shadow: 0 6px 20px rgba(0, 107, 214, 0.24);
      transition: background-color var(--dur-short) var(--ease-out), transform var(--dur-short) var(--ease-spring), box-shadow var(--dur-short) var(--ease-out);
    }
    .btn-primary:hover {
      background: var(--primary-hover);
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 10px 26px rgba(0, 107, 214, 0.34);
    }
    .btn-primary:active { transform: scale(0.97); }
    .btn-secondary {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: var(--space-sm);
      min-height: 46px;
      background: var(--surface-container);
      color: var(--on-surface);
      border-radius: var(--rounded);
      font-family: var(--font-label);
      font-size: 0.94rem;
      font-weight: 500;
      padding: var(--space-sm) var(--space-lg);
      border: 0;
      cursor: pointer;
      text-decoration: none;
      transition: background-color var(--dur-short) var(--ease-out), transform var(--dur-short) var(--ease-spring);
    }
    .btn-secondary:hover {
      background: var(--surface-container-high);
      transform: translateY(-2px);
    }
    .btn-secondary:active { transform: scale(0.97); }
    .link-more {
      display: inline-flex;
      align-items: center;
      min-height: 44px;
      color: var(--primary);
      font-weight: 600;
      text-decoration: none;
      font-size: 0.96rem;
      transition: transform var(--dur-short) var(--ease-out);
    }
    .link-more::after {
      content: var(--chevron);
      margin-left: var(--space-xs);
      transition: transform var(--dur-short) var(--ease-spring);
      display: inline-block;
    }
    .link-more:hover { text-decoration: underline; }
    .link-more:hover::after { transform: translateX(4px); }

    /* Borderless rounded tiles */
    .tile {
      background: var(--surface-container-low);
      border-radius: var(--rounded-lg);
      padding: var(--space-xl) var(--space-lg);
      border: 0;
      transition: transform var(--dur-short) var(--ease-spring), box-shadow var(--dur-short) var(--ease-out), background-color var(--dur-short) var(--ease-out);
    }
    .tile:hover {
      transform: translateY(-4px);
      box-shadow: var(--tile-shadow-hover);
    }
    .tile.figure {
      text-align: center;
      padding: var(--space-lg);
    }
    .tile.figure .label {
      font-size: var(--label-size);
      font-weight: 600;
      color: var(--on-surface-variant);
      margin-bottom: var(--space-xs);
    }
    .tile.figure .value {
      font-family: var(--font-headline);
      font-size: clamp(2.1rem, 1.5rem + 2vw, 3rem);
      font-weight: 800;
      letter-spacing: var(--figure-tracking);
      line-height: 1.08;
      color: var(--on-surface);
      font-variant-numeric: tabular-nums;
      margin-bottom: var(--space-xs);
    }
    .tile.figure .caption {
      font-size: 0.88rem;
      color: var(--on-surface-variant);
      font-weight: 500;
      max-width: 28ch;
      margin: 0 auto;
    }

    /* Grids */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr));
      gap: var(--space-md);
      margin-top: var(--space-lg);
    }
    .two-col-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: var(--space-lg);
    }
    .three-col-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
      gap: var(--space-lg);
    }

    /* Chips & Icons */
    .chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: var(--rounded);
      font-size: var(--label-size);
      font-weight: 600;
      background: var(--primary-container);
      color: var(--on-primary-container);
    }
    .chip.orange { background: var(--secondary-container); color: var(--secondary); }
    .chip.green { background: var(--positive-container); color: var(--positive); }
    .chip.purple { background: var(--purple-container); color: var(--purple); }
    .chip.red { background: var(--error-container); color: var(--error); }
    .chip.neutral { background: var(--surface-container); color: var(--on-surface-variant); }

    .card-head {
      display: flex;
      align-items: center;
      gap: var(--space-md);
      margin-bottom: var(--space-md);
    }
    .icon-circle {
      width: 48px;
      height: 48px;
      border-radius: var(--rounded-full);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: transform var(--dur-short) var(--ease-spring);
    }
    .tile:hover .icon-circle {
      transform: scale(1.1) rotate(-4deg);
    }
    .icon-circle.blue { background: var(--primary-container); color: var(--primary); }
    .icon-circle.orange { background: var(--secondary-container); color: var(--secondary); }
    .icon-circle.green { background: var(--positive-container); color: var(--positive); }
    .icon-circle.purple { background: var(--purple-container); color: var(--purple); }
    .icon-circle.red { background: var(--error-container); color: var(--error); }

    .tile h3 {
      font-family: var(--font-headline);
      font-size: 1.32rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.18;
      margin: 0;
      color: var(--on-surface);
    }
    .tile-subtitle {
      font-size: 0.88rem;
      color: var(--on-surface-variant);
      margin: 2px 0 0;
    }

    .feature-list {
      list-style: none;
      padding: 0;
      margin: var(--space-md) 0 0;
      display: grid;
      gap: var(--space-sm);
    }
    .feature-list li {
      display: flex;
      align-items: flex-start;
      gap: var(--space-sm);
      font-size: 0.95rem;
      line-height: 1.45;
    }
    .dot-mark {
      width: 8px;
      height: 8px;
      border-radius: var(--rounded-full);
      margin-top: 7px;
      flex-shrink: 0;
    }
    .dot-blue { background: var(--primary); }
    .dot-orange { background: var(--secondary); }
    .dot-green { background: var(--positive); }
    .dot-purple { background: var(--purple); }
    .dot-red { background: var(--error); }

    /* Interactive Animated Architecture Diagram */
    .arch-stage {
      background: var(--background);
      border-radius: var(--rounded-lg);
      padding: var(--space-xl);
      box-shadow: 0 2px 16px rgb(0 0 0 / 0.03);
    }
    .arch-diagram-wrap {
      position: relative;
      display: grid;
      gap: var(--space-md);
    }
    .arch-top-row {
      display: flex;
      justify-content: center;
    }
    .arch-node {
      background: var(--surface-container-low);
      border-radius: var(--rounded-lg);
      padding: var(--space-lg);
      border: 2px solid transparent;
      cursor: pointer;
      text-align: left;
      width: 100%;
      transition: transform var(--dur-short) var(--ease-spring), box-shadow var(--dur-short) var(--ease-out), border-color var(--dur-short) var(--ease-out), background-color var(--dur-short) var(--ease-out);
      position: relative;
    }
    .arch-node.tower-main {
      max-width: 700px;
      background: linear-gradient(135deg, #f0f6ff 0%, #f8f2fc 55%, #fff6ef 100%);
    }
    .arch-node:hover {
      transform: translateY(-4px);
      box-shadow: var(--tile-shadow-hover);
    }
    .arch-node.active {
      border-color: var(--primary);
      background: var(--background);
      box-shadow: var(--tile-shadow-strong);
      transform: translateY(-3px);
    }
    .arch-node.active-orange { border-color: var(--secondary); box-shadow: 0 16px 36px rgb(191 72 0 / 0.12); }
    .arch-node.active-green { border-color: var(--positive); box-shadow: 0 16px 36px rgb(36 138 61 / 0.12); }
    .arch-node.active-purple { border-color: var(--purple); box-shadow: 0 16px 36px rgb(137 68 171 / 0.12); }

    .arch-domain {
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--on-surface-variant);
      margin-top: 4px;
      display: inline-block;
    }
    .arch-cables-svg {
      width: 100%;
      height: 78px;
      display: block;
      overflow: visible;
    }
    .cable-track {
      fill: none;
      stroke: var(--outline);
      stroke-width: 2.5;
      stroke-dasharray: 6 6;
    }
    .cable-pulse {
      fill: none;
      stroke-width: 3;
      stroke-dasharray: 10 18;
      stroke-linecap: round;
      animation: flowDash 1.4s linear infinite;
    }
    .cable-pulse.reverse {
      animation: flowDashRev 1.8s linear infinite;
    }
    @keyframes flowDash {
      from { stroke-dashoffset: 28; }
      to { stroke-dashoffset: 0; }
    }
    @keyframes flowDashRev {
      from { stroke-dashoffset: 0; }
      to { stroke-dashoffset: 28; }
    }
    .arch-bottom-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: var(--space-md);
    }
    .arch-inspector {
      margin-top: var(--space-lg);
      background: var(--surface-container-low);
      border-radius: var(--rounded-lg);
      padding: var(--space-lg);
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: var(--space-lg);
      align-items: start;
      animation: softPop 0.35s var(--ease-out);
    }
    @keyframes softPop {
      from { opacity: 0; transform: translateY(8px) scale(0.99); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
    .soft-pop {
      animation: softPop 0.32s var(--ease-out);
    }

    /* Segmented control */
    .segmented-wrap {
      display: flex;
      justify-content: center;
      margin-bottom: var(--space-xl);
    }
    .segmented {
      display: inline-flex;
      background: var(--surface-container);
      padding: 4px;
      border-radius: var(--rounded);
      gap: 4px;
      flex-wrap: wrap;
      justify-content: center;
    }
    .seg-btn {
      min-height: 40px;
      padding: var(--space-xs) var(--space-lg);
      border-radius: var(--rounded);
      border: 0;
      background: transparent;
      color: var(--on-surface-variant);
      font-size: 0.9rem;
      font-weight: 500;
      cursor: pointer;
      transition: background-color var(--dur-short) var(--ease-in-out), color var(--dur-short) var(--ease-in-out), box-shadow var(--dur-short) var(--ease-in-out), transform var(--dur-micro) var(--ease-out);
    }
    .seg-btn[aria-selected="true"] {
      background: var(--background);
      color: var(--on-surface);
      font-weight: 600;
      box-shadow: 0 3px 10px rgb(0 0 0 / 0.09);
    }
    .seg-btn:hover:not([aria-selected="true"]) { color: var(--on-surface); }

    /* Comparator */
    .comparator-shell {
      background: var(--background);
      border-radius: var(--rounded-lg);
      padding: var(--space-xl);
      margin-top: var(--space-xl);
    }
    .question-pills {
      display: flex;
      flex-wrap: wrap;
      gap: var(--space-sm);
      justify-content: center;
      margin-bottom: var(--space-xl);
    }
    .q-pill {
      min-height: 42px;
      padding: var(--space-xs) var(--space-md);
      border-radius: var(--rounded);
      border: 0;
      background: var(--surface-container-low);
      color: var(--on-surface);
      font-size: 0.89rem;
      font-weight: 500;
      cursor: pointer;
      transition: background-color var(--dur-short) var(--ease-out), color var(--dur-short) var(--ease-out), transform var(--dur-short) var(--ease-spring), box-shadow var(--dur-short) var(--ease-out);
    }
    .q-pill:hover { background: var(--surface-container); transform: translateY(-2px); }
    .q-pill.active {
      background: var(--primary);
      color: var(--on-primary);
      box-shadow: 0 6px 16px rgb(0 107 214 / 0.25);
    }
    .comp-result-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: var(--space-md);
      align-items: stretch;
    }
    .comp-screen {
      background: var(--surface-container-low);
      border-radius: var(--rounded-lg);
      padding: var(--space-lg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: var(--space-md);
      transition: box-shadow var(--dur-short) var(--ease-out), transform var(--dur-short) var(--ease-spring);
    }
    .comp-screen.highlighted {
      box-shadow: 0 0 0 2px var(--primary), var(--tile-shadow-hover);
      transform: translateY(-3px);
      background: var(--background);
    }
    .comp-status {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: var(--label-size);
      font-weight: 600;
      padding: 4px 10px;
      border-radius: var(--rounded);
      width: fit-content;
    }
    .status-yes { background: var(--positive-container); color: var(--positive); }
    .status-no { background: var(--error-container); color: var(--error); }
    .status-partial { background: var(--warning-container); color: var(--warning); }
    .comp-answer-box {
      background: var(--background);
      border-radius: var(--rounded-md);
      padding: var(--space-md);
      font-size: 0.93rem;
      border: 1px solid var(--outline-variant);
    }
    .comp-summary-banner {
      margin-top: var(--space-lg);
      background: var(--primary-container);
      color: var(--on-surface);
      border-radius: var(--rounded-md);
      padding: var(--space-md) var(--space-lg);
      display: flex;
      align-items: flex-start;
      gap: var(--space-md);
    }

    /* Simulator */
    .sim-shell {
      background: var(--surface-container-low);
      border-radius: var(--rounded-lg);
      padding: var(--space-xl);
    }
    .sim-controls {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: var(--space-md);
      margin-bottom: var(--space-lg);
    }
    .event-buttons { display: flex; flex-wrap: wrap; gap: var(--space-sm); }
    .event-btn {
      min-height: 42px;
      padding: var(--space-xs) var(--space-md);
      border-radius: var(--rounded);
      border: 0;
      background: var(--background);
      color: var(--on-surface);
      font-size: 0.87rem;
      font-weight: 500;
      cursor: pointer;
      transition: all var(--dur-short) var(--ease-spring);
    }
    .event-btn:hover { background: var(--surface-container); transform: translateY(-2px); }
    .event-btn.active {
      background: var(--on-surface);
      color: var(--background);
      box-shadow: 0 6px 18px rgb(0 0 0 / 0.16);
    }

    /* Animated progress bar above 4 flow stations */
    .sim-progress-track {
      height: 5px;
      background: var(--surface-container);
      border-radius: var(--rounded);
      overflow: hidden;
      margin: var(--space-md) 0 var(--space-sm);
    }
    .sim-progress-fill {
      height: 100%;
      width: 25%;
      background: linear-gradient(90deg, var(--primary), var(--purple));
      border-radius: var(--rounded);
      transition: width 0.45s var(--ease-out), background 0.3s ease;
    }
    .sim-progress-fill.chaos {
      background: linear-gradient(90deg, var(--warning), var(--error));
    }

    .flow-stage-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: var(--space-md);
      margin: var(--space-md) 0 var(--space-lg);
    }
    .flow-node {
      background: var(--background);
      border-radius: var(--rounded-md);
      padding: var(--space-md);
      display: flex;
      flex-direction: column;
      gap: var(--space-xs);
      opacity: 0.48;
      transform: translateY(6px) scale(0.98);
      transition: opacity var(--dur-short) var(--ease-out), transform var(--dur-short) var(--ease-spring), box-shadow var(--dur-short) var(--ease-out);
      cursor: pointer;
    }
    .flow-node.reached { opacity: 0.92; transform: translateY(0) scale(1); }
    .flow-node.current {
      opacity: 1;
      transform: translateY(-4px) scale(1.02);
      box-shadow: 0 0 0 2px var(--primary), var(--tile-shadow-hover);
    }
    .flow-node.chaos.current {
      box-shadow: 0 0 0 2px var(--error), var(--tile-shadow-hover);
    }
    .step-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      border-radius: var(--rounded-full);
      background: var(--surface-container);
      color: var(--on-surface);
      font-size: 0.82rem;
      font-weight: 700;
      transition: transform var(--dur-short) var(--ease-spring), background-color var(--dur-short) var(--ease-out);
    }
    .flow-node.current .step-badge {
      background: var(--primary);
      color: var(--on-primary);
      transform: scale(1.12);
    }
    .flow-node.chaos.current .step-badge { background: var(--error); color: var(--on-error); }
    .flow-node h4 {
      font-family: var(--font-headline);
      font-size: 1rem;
      font-weight: 700;
      margin: var(--space-xs) 0 0;
    }
    .flow-node p {
      font-size: 0.84rem;
      color: var(--on-surface-variant);
      margin: 0;
      line-height: 1.4;
    }

    .sim-output-panel {
      background: var(--background);
      border-radius: var(--rounded-md);
      padding: var(--space-lg);
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: var(--space-lg);
      align-items: start;
    }
    .sim-metrics-mini {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: var(--space-sm);
    }
    .mini-stat {
      background: var(--surface-container-low);
      border-radius: var(--rounded-md);
      padding: var(--space-md);
      transition: transform var(--dur-short) var(--ease-spring);
    }
    .mini-stat:hover { transform: translateY(-2px); }
    .mini-stat .m-label { font-size: 0.78rem; color: var(--on-surface-variant); font-weight: 500; }
    .mini-stat .m-val {
      font-family: var(--font-headline);
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-top: 2px;
      color: var(--on-surface);
    }

    /* 10 Audit Traps Grid */
    .traps-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: var(--space-md);
    }
    .trap-card {
      background: var(--background);
      border-radius: var(--rounded-lg);
      padding: var(--space-lg);
      display: flex;
      flex-direction: column;
      gap: var(--space-sm);
      transition: transform var(--dur-short) var(--ease-spring), box-shadow var(--dur-short) var(--ease-out), opacity var(--dur-short) var(--ease-out);
    }
    .trap-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--tile-shadow-hover);
    }
    .trap-card.hidden-item { display: none; }
    .trap-kid-box {
      background: var(--surface-container-low);
      border-radius: var(--rounded-md);
      padding: 12px 14px;
      font-size: 0.92rem;
    }
    .trap-fix-box {
      background: var(--positive-container);
      color: #165927;
      border-radius: var(--rounded-md);
      padding: 10px 14px;
      font-size: 0.89rem;
      font-weight: 500;
    }

    /* Bento Grid */
    .filter-row {
      display: flex;
      justify-content: center;
      gap: var(--space-sm);
      flex-wrap: wrap;
      margin-bottom: var(--space-xl);
    }
    .bento-grid {
      display: grid;
      grid-template-columns: repeat(6, minmax(0, 1fr));
      gap: var(--space-lg);
    }
    .bento-card {
      background: var(--background);
      border-radius: var(--rounded-lg);
      padding: var(--space-lg);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: var(--space-md);
      transition: transform var(--dur-short) var(--ease-spring), box-shadow var(--dur-short) var(--ease-out), opacity var(--dur-short) var(--ease-out);
      text-align: left;
      border: 0;
    }
    .bento-card:hover {
      transform: translateY(-5px) scale(1.01);
      box-shadow: var(--tile-shadow-hover);
    }
    .bento-card.selected {
      box-shadow: 0 0 0 2px var(--primary), var(--tile-shadow-strong);
      transform: translateY(-3px);
    }
    .bento-card.dimmed { opacity: 0.34; }
    .bento-span-3 { grid-column: span 3; }
    .bento-span-2 { grid-column: span 2; }
    .bento-span-4 { grid-column: span 4; }

    .bento-spotlight {
      margin-top: var(--space-xl);
      background: var(--background);
      border-radius: var(--rounded-lg);
      padding: var(--space-xl);
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: var(--space-xl);
      align-items: start;
      box-shadow: 0 6px 24px rgb(0 0 0 / 0.04);
    }
    .analogy-quote {
      background: var(--surface-container-low);
      border-radius: var(--rounded-md);
      padding: var(--space-md);
      margin-top: var(--space-md);
      border-left: 3px solid var(--secondary);
    }

    /* Interactive Phase Roadmap */
    .phase-shell {
      background: var(--surface-container-low);
      border-radius: var(--rounded-lg);
      padding: var(--space-xl);
    }
    .phase-tabs {
      display: grid;
      grid-template-columns: repeat(6, minmax(0, 1fr));
      gap: var(--space-sm);
      margin-bottom: var(--space-lg);
    }
    .phase-tab {
      background: var(--background);
      border: 2px solid transparent;
      border-radius: var(--rounded-md);
      padding: 12px 10px;
      cursor: pointer;
      text-align: left;
      transition: all var(--dur-short) var(--ease-spring);
    }
    .phase-tab:hover { transform: translateY(-3px); box-shadow: var(--tile-shadow-hover); }
    .phase-tab.active {
      border-color: var(--primary);
      box-shadow: var(--tile-shadow-strong);
      transform: translateY(-3px);
    }
    .phase-num {
      font-family: var(--font-headline);
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .phase-tab-title {
      font-family: var(--font-headline);
      font-size: 0.96rem;
      font-weight: 700;
      color: var(--on-surface);
      margin-top: 2px;
    }
    .phase-tab-time {
      font-size: 0.78rem;
      color: var(--on-surface-variant);
      margin-top: 2px;
    }
    .phase-detail-card {
      background: var(--background);
      border-radius: var(--rounded-lg);
      padding: var(--space-xl);
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: var(--space-xl);
      align-items: start;
    }

    /* Animated Bars */
    .chart-tile {
      margin-top: var(--space-xl);
      padding: var(--space-xl);
    }
    .bar-list { display: grid; gap: var(--space-md); }
    .bar-row {
      display: grid;
      grid-template-columns: minmax(190px, 250px) minmax(0, 1fr) 86px;
      gap: var(--space-md);
      align-items: center;
    }
    .bar-label { font-size: 0.95rem; font-weight: 600; color: var(--on-surface); }
    .bar-sub { display: block; font-size: 0.82rem; color: var(--on-surface-variant); font-weight: 400; }
    .bar-track {
      height: 16px;
      background: var(--surface-container);
      border-radius: var(--rounded);
      overflow: hidden;
    }
    .bar-fill {
      height: 100%;
      width: 0%;
      border-radius: var(--rounded);
      transition: width 1.1s var(--ease-out);
    }
    .bar-fill.primary { background: linear-gradient(90deg, var(--primary), #3392ff); }
    .bar-fill.secondary { background: linear-gradient(90deg, var(--secondary), #eb7528); }
    .bar-fill.green { background: linear-gradient(90deg, var(--positive), #3bc25c); }
    .bar-fill.purple { background: linear-gradient(90deg, var(--purple), #b46fd6); }
    .bar-val {
      font-family: var(--font-headline);
      font-weight: 700;
      font-variant-numeric: tabular-nums;
      text-align: right;
      color: var(--on-surface);
    }

    /* Interactive Decision Cards */
    .decisions-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
      gap: var(--space-lg);
    }
    .decision-card {
      background: var(--background);
      border-radius: var(--rounded-lg);
      padding: var(--space-lg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: var(--space-md);
      transition: transform var(--dur-short) var(--ease-spring), box-shadow var(--dur-short) var(--ease-out);
    }
    .decision-card:hover { transform: translateY(-4px); box-shadow: var(--tile-shadow-hover); }
    .step-number {
      font-family: var(--font-headline);
      font-size: 2rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: var(--primary);
      line-height: 1;
      margin-bottom: var(--space-xs);
    }
    .choice-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .choice-btn {
      padding: 6px 12px;
      border-radius: var(--rounded);
      border: 1.5px solid var(--outline);
      background: var(--background);
      color: var(--on-surface);
      font-size: 0.83rem;
      font-weight: 500;
      cursor: pointer;
      transition: all var(--dur-short) var(--ease-spring);
    }
    .choice-btn:hover { border-color: var(--primary); }
    .choice-btn.picked {
      background: var(--primary);
      border-color: var(--primary);
      color: var(--on-primary);
      transform: scale(1.03);
    }

    /* Footer */
    .sources-footer {
      border-top: 1px solid var(--outline-variant);
      padding: var(--space-xl) var(--space-lg);
      max-width: 1140px;
      margin: 0 auto;
      color: var(--on-surface-variant);
      font-size: 0.86rem;
    }
    .sources-footer h3 {
      font-family: var(--font-headline);
      font-size: 1rem;
      font-weight: 700;
      color: var(--on-surface);
      margin: 0 0 var(--space-sm);
    }

    /* Enhanced Scroll Reveal Animations with stagger */
    .reveal {
      opacity: 0;
      transform: translateY(22px) scale(0.985);
      transition: opacity 0.68s var(--ease-out), transform 0.68s var(--ease-out);
    }
    .reveal.visible {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
    .stagger-1 { transition-delay: 60ms; }
    .stagger-2 { transition-delay: 140ms; }
    .stagger-3 { transition-delay: 220ms; }
    .stagger-4 { transition-delay: 300ms; }

    /* Responsive */
    @media (max-width: 960px) {
      .comp-result-grid,
      .two-col-grid,
      .sim-output-panel,
      .bento-spotlight,
      .arch-bottom-row,
      .arch-inspector,
      .traps-grid,
      .phase-detail-card {
        grid-template-columns: 1fr;
      }
      .arch-cables-svg { display: none; }
      .flow-stage-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .phase-tabs { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .bento-span-3, .bento-span-2, .bento-span-4 { grid-column: span 6; }
    }
    @media (max-width: 640px) {
      .page-grid { padding: 0 var(--space-md); }
      .band { padding-block: var(--space-xl); }
      .flow-stage-grid, .phase-tabs { grid-template-columns: 1fr; }
      .bar-row { grid-template-columns: 1fr; gap: var(--space-xs); }
      .bar-val { text-align: left; }
      .sim-metrics-mini { grid-template-columns: 1fr; }
      .nav-badge { display: none; }
    }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
      .reveal, .hero-anim { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>

  <div class="scroll-progress" id="scroll-progress"></div>

  <!-- Barra superior estilo Apple con desenfoque -->
  <header class="top-header" id="top-header">
    <nav class="top-nav" aria-label="Navegación principal">
      <a href="#inicio" class="brand-mark">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
          <path d="M14 17.5h7M17.5 14v7"></path>
        </svg>
        <span>Animallium · Plan Maestro</span>
      </a>
      <div class="nav-links">
        <a href="#arquitectura" class="nav-pill">1. Los 4 Sistemas</a>
        <a href="#simulador" class="nav-pill">2. Simulador</a>
        <a href="#trampas" class="nav-pill">3. 10 Trampas</a>
        <a href="#glosario" class="nav-pill">4. Piezas Bento</a>
        <a href="#roadmap" class="nav-pill">5. Plan por Fases</a>
        <a href="#decisiones" class="nav-pill">6. Decisiones</a>
      </div>
      <span class="nav-badge"><span class="live-dot"></span> Auditoría Real 2026</span>
    </nav>
  </header>

  <main>
    <!-- HERO -->
    <section id="inicio" class="band">
      <div class="hero-aura"></div>
      <div class="page-grid">
        <div class="headline-stack hero-stack">
          <span class="eyebrow hero-anim d1">Explicado fácil · Para un niño de 12 años</span>
          <h1 class="hero-anim d2">Cuatro piezas limpias.<br><span class="headline-gradient">Una sola Torre de Control.</span></h1>
          <p class="lede hero-anim d3">
            Sacamos el Centro de Mando del CRM para que cada programa haga una sola cosa increíble, y ponemos encima una Torre de Control que une WhatsApp, negocios de WCFM, citas de FluentBooking y robots de IA — listo para crecer de 0 a 200+ aliados sin caos.
          </p>
          <div class="action-row hero-anim d4">
            <a href="#arquitectura" class="btn-primary">Explorar los 4 Sistemas</a>
            <a href="#simulador" class="btn-secondary">Probar el Simulador</a>
            <a href="#roadmap" class="link-more">Ver camino por fases</a>
          </div>
        </div>

        <div class="kpi-grid">
          <div class="tile figure reveal stagger-1">
            <div class="label">Sistemas separados</div>
            <div class="value" data-count="4" data-suffix="">4</div>
            <p class="caption">CRM, WordPress, Centro de Mando y Torre de Control. Cero revoltijo.</p>
          </div>
          <div class="tile figure reveal stagger-2">
            <div class="label">Meta de aliados (MDM)</div>
            <div class="value" data-count="200" data-prefix="0 → " data-suffix="+">0 → 200+</div>
            <p class="caption">Hoy hay 0 negocios y 0 citas: empezamos con reglas perfectas desde el #1.</p>
          </div>
          <div class="tile figure reveal stagger-3">
            <div class="label">Copias innecesarias</div>
            <div class="value" data-count="0" data-suffix=" copias">0 copias</div>
            <p class="caption">Zero-Copy: la Torre lee el dato vivo donde vive, sin fotocopias viejas.</p>
          </div>
          <div class="tile figure reveal stagger-4">
            <div class="label">Trampas atrapadas antes</div>
            <div class="value" data-count="10" data-suffix="">10</div>
            <p class="caption">Errores reales de código, moneda y seguridad que corregimos en el plano.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CAPÍTULO 1: LOS 4 SISTEMAS + DIAGRAMA ANIMADO -->
    <section id="arquitectura" class="band alt">
      <div class="page-grid">
        <div class="headline-stack reveal">
          <span class="eyebrow">Capítulo 1 · El nuevo mapa</span>
          <h2>Cada edificio hace su trabajo.<br>La Torre los mira a todos.</h2>
          <p class="lede">
            Imagina un parque gigante de mascotas. Antes teníamos la oficina de camiones metida adentro del mostrador de chat. Ahora cada equipo tiene su propia casa y arriba construimos un mirador de cristal. <strong>Toca cualquier edificio</strong> para ver qué hace.
          </p>
        </div>

        <!-- Diagrama Interactivo con cables SVG animados -->
        <div class="arch-stage reveal">
          <div class="arch-diagram-wrap">
            <!-- Arriba: Torre de Control -->
            <div class="arch-top-row">
              <button type="button" class="arch-node tower-main active" id="sys-card-0" onclick="selectSystem(0)">
                <div style="display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap;">
                  <div style="display:flex; align-items:center; gap:12px;">
                    <div class="icon-circle blue">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
                    </div>
                    <div>
                      <span class="chip">Sistema 4 · NUEVO · El Mirador de Cristal</span>
                      <h3 style="margin-top:4px;">Torre de Control Global</h3>
                      <span class="arch-domain">torre.animallium.pet</span>
                    </div>
                  </div>
                  <div style="display:flex; gap:6px; flex-wrap:wrap;">
                    <span class="chip">Nexora TanStack</span>
                    <span class="chip green">Zero-Copy + MDM + Write-Back</span>
                  </div>
                </div>
                <p style="margin:12px 0 0; font-size:0.93rem; color:var(--on-surface-variant);">
                  El cerebro arriba de todo. Une a los 200+ aliados, compara pesos (COP) y dólares (USD) sin equivocarse y manda alertas limpias de regreso.
                </p>
              </button>
            </div>

            <!-- Cables animados SVG -->
            <svg class="arch-cables-svg" viewBox="0 0 900 78" preserveAspectRatio="none" aria-hidden="true">
              <!-- Izquierda: Torre <-> WACRM -->
              <path d="M 350 4 C 350 42, 150 36, 150 74" class="cable-track"/>
              <path d="M 350 4 C 350 42, 150 36, 150 74" class="cable-pulse" stroke="#006bd6"/>
              <!-- Centro: Torre <-> WordPress -->
              <path d="M 450 4 L 450 74" class="cable-track"/>
              <path d="M 450 4 L 450 74" class="cable-pulse reverse" stroke="#248a3d"/>
              <!-- Derecha: Torre <-> Centro de Mando -->
              <path d="M 550 4 C 550 42, 750 36, 750 74" class="cable-track"/>
              <path d="M 550 4 C 550 42, 750 36, 750 74" class="cable-pulse" stroke="#8944ab"/>
              <!-- Etiquetas en cables -->
              <rect x="168" y="25" width="150" height="22" rx="11" fill="#e8f1fd"/>
              <text x="243" y="40" text-anchor="middle" fill="#0058b0" font-size="11" font-weight="600" font-family="Inter, sans-serif">JWT Supabase + Alertas</text>

              <rect x="374" y="25" width="152" height="22" rx="11" fill="#eaf6ed"/>
              <text x="450" y="40" text-anchor="middle" fill="#248a3d" font-size="11" font-weight="600" font-family="Inter, sans-serif">Puente SQL + Webhooks</text>

              <rect x="582" y="25" width="160" height="22" rx="11" fill="#f5eef9"/>
              <text x="662" y="40" text-anchor="middle" fill="#8944ab" font-size="11" font-weight="600" font-family="Inter, sans-serif">Red Privada root_default</text>
            </svg>

            <!-- Abajo: 3 Sistemas Operativos -->
            <div class="arch-bottom-row">
              <button type="button" class="arch-node" id="sys-card-1" onclick="selectSystem(1)">
                <div class="card-head" style="margin-bottom:8px;">
                  <div class="icon-circle blue" style="width:40px;height:40px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                  </div>
                  <div>
                    <span class="chip">Sistema 1</span>
                    <h3 style="font-size:1.12rem;margin-top:2px;">WACRM Puro</h3>
                  </div>
                </div>
                <span class="arch-domain">crm.animallium.pet</span>
                <p style="margin:8px 0 0; font-size:0.86rem; color:var(--on-surface-variant);">
                  El mostrador rápido de WhatsApp, contactos, embudos B2C/B2B, <strong>Monitor Nodos IA</strong> (conversaciones), notificaciones y logo propio. 0% Centro de Mando.
                </p>
              </button>

              <button type="button" class="arch-node" id="sys-card-2" onclick="selectSystem(2)">
                <div class="card-head" style="margin-bottom:8px;">
                  <div class="icon-circle green" style="width:40px;height:40px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/></svg>
                  </div>
                  <div>
                    <span class="chip green">Sistema 2</span>
                    <h3 style="font-size:1.12rem;margin-top:2px;">WordPress Vivo</h3>
                  </div>
                </div>
                <span class="arch-domain">animallium.pet</span>
                <p style="margin:8px 0 0; font-size:0.86rem; color:var(--on-surface-variant);">
                  El centro comercial: tiendas WCFM, citas FluentBooking, Pasaporte Phygital y hasta historia clínica SOAP (Plan 3).
                </p>
              </button>

              <button type="button" class="arch-node" id="sys-card-3" onclick="selectSystem(3)">
                <div class="card-head" style="margin-bottom:8px;">
                  <div class="icon-circle purple" style="width:40px;height:40px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6v6H9z"/></svg>
                  </div>
                  <div>
                    <span class="chip purple">Sistema 3 · INDEPENDIENTE</span>
                    <h3 style="font-size:1.12rem;margin-top:2px;">Centro de Mando</h3>
                  </div>
                </div>
                <span class="arch-domain">mando.animallium.pet</span>
                <p style="margin:8px 0 0; font-size:0.86rem; color:var(--on-surface-variant);">
                  El taller secreto: Dropi Scout, borradores de tienda, propuestas B2B, creativos y Logística &amp; Fulfillment Dropi (100% fuera del CRM).
                </p>
              </button>
            </div>
          </div>

          <!-- Inspector dinámico del sistema seleccionado -->
          <div class="arch-inspector" id="arch-inspector">
            <div>
              <span class="chip" id="insp-chip">Sistema 4 · Torre de Control</span>
              <h3 id="insp-title" style="font-family:var(--font-headline); font-size:1.55rem; margin:10px 0 6px;">Torre de Control Global</h3>
              <p id="insp-kid" style="margin:0 0 14px; font-size:0.97rem;"></p>
              <div style="background:var(--background); border-radius:var(--rounded-md); padding:14px 16px; border-left:3px solid var(--primary);">
                <strong style="display:block; font-size:0.84rem; color:var(--primary); margin-bottom:4px;">Cómo lo entendería un niño de 12 años:</strong>
                <span id="insp-analogy" style="font-size:0.93rem;"></span>
              </div>
            </div>
            <div style="display:grid; gap:12px;">
              <div style="background:var(--background); border-radius:var(--rounded-md); padding:14px 16px;">
                <strong style="display:block; font-size:0.84rem; color:var(--positive); margin-bottom:6px;">Qué SÍ vive aquí</strong>
                <p id="insp-yes" style="margin:0; font-size:0.9rem; color:var(--on-surface-variant);"></p>
              </div>
              <div style="background:var(--background); border-radius:var(--rounded-md); padding:14px 16px;">
                <strong style="display:block; font-size:0.84rem; color:var(--error); margin-bottom:6px;">Qué NO debe vivir aquí</strong>
                <p id="insp-no" style="margin:0; font-size:0.9rem; color:var(--on-surface-variant);"></p>
              </div>
            </div>
          </div>
        </div>

        <!-- Comparador interactivo de 3 sistemas -->
        <div class="comparator-shell reveal" id="comparador">
          <div class="headline-stack" style="padding-block: 0 var(--space-md);">
            <span class="chip">Juego de preguntas rápidas</span>
            <h3 style="font-family: var(--font-headline); font-size: var(--subhead-size); margin: var(--space-sm) 0 0;">¿Qué pantalla debo abrir para cada pregunta?</h3>
            <p style="color: var(--on-surface-variant); margin: var(--space-xs) auto 0; max-width: 54ch; font-size: 0.94rem;">
              Toca una pregunta real de Animallium y mira en qué edificio se responde sin confundir a nadie.
            </p>
          </div>

          <div class="question-pills" id="question-pills-row">
            <button type="button" class="q-pill active" onclick="selectQuestion(0)">¿A qué cliente de WhatsApp respondo hoy?</button>
            <button type="button" class="q-pill" onclick="selectQuestion(1)">¿Cuánta plata real ganamos (COP vs USD)?</button>
            <button type="button" class="q-pill" onclick="selectQuestion(2)">¿De qué negocio es este calendario de citas?</button>
            <button type="button" class="q-pill" onclick="selectQuestion(3)">¿Cómo subo productos de Dropi a la tienda?</button>
            <button type="button" class="q-pill" onclick="selectQuestion(4)">¿Por qué un aliado B2B no ha abierto tienda?</button>
            <button type="button" class="q-pill" onclick="selectQuestion(5)">¿Cómo cambio el logo y borro notificaciones?</button>
          </div>

          <div class="comp-result-grid">
            <div class="comp-screen" id="comp-crm-card">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:6px;">
                  <strong>1. WACRM</strong>
                  <span class="comp-status status-yes" id="crm-status-badge">Aquí sí</span>
                </div>
                <p style="font-size:0.84rem; color:var(--on-surface-variant); margin:0 0 12px;">crm.animallium.pet</p>
              </div>
              <div class="comp-answer-box" id="crm-answer-text"></div>
            </div>

            <div class="comp-screen" id="comp-mando-card">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:6px;">
                  <strong>2. Centro de Mando</strong>
                  <span class="comp-status status-no" id="mando-status-badge">No le toca</span>
                </div>
                <p style="font-size:0.84rem; color:var(--on-surface-variant); margin:0 0 12px;">mando.animallium.pet</p>
              </div>
              <div class="comp-answer-box" id="mando-answer-text"></div>
            </div>

            <div class="comp-screen" id="comp-torre-card">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:6px;">
                  <strong>3. Torre de Control</strong>
                  <span class="comp-status status-partial" id="torre-status-badge">Visión global</span>
                </div>
                <p style="font-size:0.84rem; color:var(--on-surface-variant); margin:0 0 12px;">torre.animallium.pet</p>
              </div>
              <div class="comp-answer-box" id="torre-answer-text"></div>
            </div>
          </div>

          <div class="comp-summary-banner" id="comp-verdict-box">
            <div class="icon-circle blue" style="width:36px; height:36px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            </div>
            <div>
              <strong style="display:block; font-size:0.94rem;">Regla fácil para recordar</strong>
              <span id="comp-verdict-text" style="font-size:0.93rem;"></span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CAPÍTULO 2: SIMULADOR INTERACTIVO -->
    <section id="simulador" class="band">
      <div class="page-grid">
        <div class="headline-stack reveal">
          <span class="eyebrow">Capítulo 2 · Simulador en vivo</span>
          <h2>Mira viajar un dato real de Animallium en 4 estaciones.</h2>
          <p class="lede">
            Elige una situación real que va a pasar cuando lleguen tus primeros 200 negocios y compara nuestra <strong>Torre Moderna</strong> frente a intentar <strong>meter todo en el CRM</strong>.
          </p>
        </div>

        <div class="sim-shell reveal">
          <div class="sim-controls">
            <div>
              <div style="font-size:0.82rem; font-weight:600; color:var(--on-surface-variant); margin-bottom:6px;">1. Elige una misión real de Animallium:</div>
              <div class="event-buttons" id="sim-event-buttons">
                <button type="button" class="event-btn active" onclick="selectSimEvent(0)">Nace la Veterinaria #1</button>
                <button type="button" class="event-btn" onclick="selectSimEvent(1)">Admin crea un calendario</button>
                <button type="button" class="event-btn" onclick="selectSimEvent(2)">Venta + Reembolso + Gasto IA</button>
                <button type="button" class="event-btn" onclick="selectSimEvent(3)">Aliado parado 5 días</button>
              </div>
            </div>

            <div>
              <div style="font-size:0.82rem; font-weight:600; color:var(--on-surface-variant); margin-bottom:6px;">2. Modo a comparar:</div>
              <div class="segmented" role="tablist">
                <button type="button" class="seg-btn" id="arch-modern" role="tab" aria-selected="true" onclick="setSimArch('modern')">Torre Separada (Plan Nuevo)</button>
                <button type="button" class="seg-btn" id="arch-legacy" role="tab" aria-selected="false" onclick="setSimArch('legacy')">Todo pegado al CRM (Caos)</button>
              </div>
            </div>
          </div>

          <div class="sim-progress-track">
            <div class="sim-progress-fill" id="sim-progress-fill"></div>
          </div>

          <div class="flow-stage-grid" id="sim-flow-grid">
            <div class="flow-node reached current" id="sim-node-0" onclick="goToSimStep(0)" tabindex="0" role="button">
              <span class="step-badge">1</span>
              <h4 id="node-title-0">Señal</h4>
              <p id="node-desc-0">Ocurre un evento real.</p>
            </div>
            <div class="flow-node" id="sim-node-1" onclick="goToSimStep(1)" tabindex="0" role="button">
              <span class="step-badge">2</span>
              <h4 id="node-title-1">Puente + MDM</h4>
              <p id="node-desc-1">Viaja limpio sin duplicar.</p>
            </div>
            <div class="flow-node" id="sim-node-2" onclick="goToSimStep(2)" tabindex="0" role="button">
              <span class="step-badge">3</span>
              <h4 id="node-title-2">Capa Semántica</h4>
              <p id="node-desc-2">Aplica reglas exactas.</p>
            </div>
            <div class="flow-node" id="sim-node-3" onclick="goToSimStep(3)" tabindex="0" role="button">
              <span class="step-badge">4</span>
              <h4 id="node-title-3">Write-Back</h4>
              <p id="node-desc-3">Avisa y actúa en 1 clic.</p>
            </div>
          </div>

          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:var(--space-md); margin-bottom:var(--space-lg);">
            <div style="display:flex; gap:var(--space-sm); flex-wrap:wrap;">
              <button type="button" class="btn-primary" onclick="advanceSimStep()">Siguiente estación ›</button>
              <button type="button" class="btn-secondary" onclick="runFullSimulation()">▶ Reproducir viaje completo</button>
            </div>
            <span id="sim-step-counter" style="font-size:0.88rem; font-weight:600; color:var(--on-surface-variant);">Paso 1 de 4</span>
          </div>

          <div class="sim-output-panel" id="sim-output-panel">
            <div>
              <span class="chip green" id="sim-stage-chip">Estación 1</span>
              <h4 id="sim-detail-headline" style="font-family:var(--font-headline); font-size:1.3rem; margin:10px 0 8px;"></h4>
              <p id="sim-detail-body" style="margin:0 0 14px; font-size:0.95rem;"></p>
              <div style="background:var(--surface-container-low); border-radius:var(--rounded-md); padding:14px 16px; font-size:0.9rem;">
                <strong style="display:block; margin-bottom:4px;" id="sim-action-title">Qué hace el sistema automáticamente:</strong>
                <span id="sim-action-text"></span>
              </div>
            </div>

            <div class="sim-metrics-mini">
              <div class="mini-stat">
                <div class="m-label">Velocidad</div>
                <div class="m-val" id="sim-metric-time">1.2 s</div>
              </div>
              <div class="mini-stat">
                <div class="m-label">Copias creadas</div>
                <div class="m-val" id="sim-metric-copies">0</div>
              </div>
              <div class="mini-stat">
                <div class="m-label">Estado del CRM</div>
                <div class="m-val" id="sim-metric-crm" style="font-size:1.02rem;">Súper rápido</div>
              </div>
              <div class="mini-stat">
                <div class="m-label">Exactitud</div>
                <div class="m-val" id="sim-metric-risk" style="font-size:1.02rem;">100% exacta</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CAPÍTULO 3: LAS 10 TRAMPAS REALES QUE ATRAPAMOS -->
    <section id="trampas" class="band alt">
      <div class="page-grid">
        <div class="headline-stack reveal">
          <span class="eyebrow">Capítulo 3 · Auditoría con lupa</span>
          <h2>10 trampas ocultas que atrapamos antes de empezar.</h2>
          <p class="lede">
            Revisamos línea por línea tu código real de WordPress, el CRM y el motor de IA. Como un mecánico que revisa el avión antes de despegar, encontramos 10 detalles que habrían fallado y ya tenemos la solución exacta.
          </p>
        </div>

        <div class="filter-row reveal" id="trap-filters">
          <button type="button" class="q-pill active" onclick="filterTraps('all', this)">Todas (10)</button>
          <button type="button" class="q-pill" onclick="filterTraps('wp', this)">WordPress & Hooks (3)</button>
          <button type="button" class="q-pill" onclick="filterTraps('money', this)">Dinero COP/USD (1)</button>
          <button type="button" class="q-pill" onclick="filterTraps('sec', this)">Seguridad & Auth (3)</button>
          <button type="button" class="q-pill" onclick="filterTraps('arch', this)">Limpieza & Velocidad (3)</button>
        </div>

        <div class="traps-grid reveal" id="traps-grid">
          <!-- 1 -->
          <article class="trap-card" data-tcat="wp">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip orange">Trampa #1 · WordPress</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">WCFM & FluentBooking</span>
            </div>
            <h3>El timbre que no existía</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> El plan anterior quería escuchar un timbre llamado <code>wcfmmp_new_vendor_registered</code>… ¡pero ese botón no existe en WCFM! Nadie habría avisado cuando llegara un negocio nuevo.
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> Conectamos los timbres reales del código: <code>wcfmmp_new_store_created</code>, <code>wcfm_membership_registration</code>, <code>set_user_role</code> y <code>fluent_booking/after_create_calendar</code>.
            </div>
          </article>

          <!-- 2 -->
          <article class="trap-card" data-tcat="money">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip red">Trampa #2 · Dinero</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">COP vs. USD</span>
            </div>
            <h3>Sumar manzanas (COP) con naranjas (USD)</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> Las ventas están en pesos colombianos (COP), el gasto de IA está en dólares (USD), y los precios de WCFM están guardados como texto. Restarlos directo habría dado números falsos y además contado 2 veces los pedidos de Dropi.
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> Convertimos texto a número decimal, filtramos cancelados y reembolsos, usamos <code>total_commission</code>, excluimos la tienda propia del GMV de terceros y separamos COP y USD (con TRM configurable).
            </div>
          </article>

          <!-- 3 -->
          <article class="trap-card" data-tcat="wp">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip green">Trampa #3 · Hallazgo oro</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">animallium-connect.php</span>
            </div>
            <h3>¡El mapa secreto de Clínica Plan 3 ya existía!</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> Encontramos la copia viva de 5.340 líneas del plugin: ¡ya trae 4 tablas médicas (pacientes, SOAP, sala de espera y grooming)! Pero tenía un link viejo al dominio <code>.com</code> y una clave débil de prueba.
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> Aprovechamos ese 4.º mundo clínico para futuras vistas de la Torre, corregimos la URL <code>.com → .pet</code> y en el nuevo puente exigimos clave segura con <code>hash_equals()</code> solo por header.
            </div>
          </article>

          <!-- 4 -->
          <article class="trap-card" data-tcat="sec">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip">Trampa #4 · Llave Maestra</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">Supabase RPC</span>
            </div>
            <h3>La puerta que solo abre con tu carné</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> La función de métricas del CRM (<code>dashboard_overview</code>) revisa <em>quién eres</em> (<code>auth.uid()</code>). Si un robot sin carné intenta leerla, la puerta le responde «Error 42501: no pasas».
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> La Torre usará el mismo inicio de sesión del CRM (<strong>SSO Supabase Auth</strong>). Así entras con un solo usuario y la Torre lee métricas en vivo (Zero-Copy) sin copiar tablas.
            </div>
          </article>

          <!-- 5 -->
          <article class="trap-card" data-tcat="sec">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip purple">Trampa #5 · Alertas</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">Write-Back</span>
            </div>
            <h3>No confundir el megáfono con el walkie-talkie</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> <code>/api/v1/messages</code> le escribe por WhatsApp al cliente afuera, no al vendedor adentro. Y la campana interna del CRM hoy solo acepta 5 tipos fijos de aviso.
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> WhatsApp (<code>/api/v1/messages</code>) queda para clientes/aliados; las alertas internas del equipo salen por Telegram hoy y luego en la campana del CRM añadiendo el tipo <code>control_tower_alert</code>.
            </div>
          </article>

          <!-- 6 -->
          <article class="trap-card" data-tcat="sec">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip red">Trampa #6 · Seguridad</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">animallium-ai-core</span>
            </div>
            <h3>6 candados que faltaban en el Centro de Mando</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> Al sacar el Centro de Mando a su propia casa descubrimos contraseñas guardadas sin disfrazar en cookies, puertas CORS abiertas a todo el mundo (<code>*</code>), 6 links viejos a <code>n8n</code> y una pestaña que también se llamaba «Torre de Control».
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> Sesión firmada con candado HMAC/JWT, CORS solo para tus dominios, URL configurable, webhooks firmados y renombramos Pestaña 5 a <em>«Logística & Fulfillment Dropi»</em>.
            </div>
          </article>

          <!-- 7 -->
          <article class="trap-card" data-tcat="arch">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip">Trampa #7 · Tests CRM</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">4 idiomas + .env</span>
            </div>
            <h3>El diccionario de los 4 idiomas parejos</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> El CRM tiene un inspector automático (<code>messages.test.ts</code>) que revisa que inglés, español, coreano y portugués tengan las mismas palabras. Si borras el menú solo en español, el test salta en rojo.
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> Borramos <code>centroMando</code> en los 4 archivos a la vez (conservando <code>nodosIa</code> en los 4), dejamos <code>X-Frame-Options: DENY</code> global (con <code>SAMEORIGIN</code> solo para el iframe de Nodos IA) y recortamos el proxy únicamente a <code>dashboard</code> y <code>api/dashboard/</code>.
            </div>
          </article>

          <!-- 8 -->
          <article class="trap-card" data-tcat="wp">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip orange">Trampa #8 · Calendarios</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">FluentBooking</span>
            </div>
            <h3>El apellido equivocado en el calendario</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> Un archivo viejo buscaba la columna <code>author_id</code> en FluentBooking, pero la columna real se llama <code>user_id</code>. Además encontramos una pista valiosa: <code>_fluent_booking_event_id</code>.
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> Corregimos <code>author_id → user_id</code> y usamos nuestra tabla MDM <code>business_calendar_links</code> para que un calendario funcione igual si lo creó el Admin o el negocio.
            </div>
          </article>

          <!-- 9 -->
          <article class="trap-card" data-tcat="arch">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip purple">Trampa #9 · Regla 03</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">Enfoque paso a paso</span>
            </div>
            <h3>Querer armar 5 castillos el primer día</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> La Regla 03 del documento avisa: no conectes toda la compañía el día 1. Hacer 5 pantallas gigantes a la vez demora semanas y trae errores.
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> Partimos Fase 2 en <strong>Fase 2A</strong> (una sola misión estrella: Red de Aliados 0→200+ con MDM + WCFM + Citas) y <strong>Fase 2B</strong> (resto de pantallas transversales).
            </div>
          </article>

          <!-- 10 -->
          <article class="trap-card" data-tcat="arch">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="chip green">Trampa #10 · Turbo interno</span>
              <span style="font-size:0.8rem; color:var(--on-surface-variant);">Docker root_default</span>
            </div>
            <h3>¡Ya tienes un túnel secreto de alta velocidad!</h3>
            <div class="trap-kid-box">
              <strong>Para 12 años:</strong> En tu servidor VPS todos tus contenedores ya comparten una autopista privada llamada <code>root_default</code>. ¡No hace falta salir a internet para que la Torre hable con el motor de IA!
            </div>
            <div class="trap-fix-box">
              ✅ <strong>Escudo:</strong> Conectamos la nueva Torre directamente a <code>root_default</code>: velocidad en milisegundos, máxima seguridad y candado HTTPS automático con Caddy.
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- CAPÍTULO 4: GLOSARIO BENTO GRID DE TU TORRE -->
    <section id="glosario" class="band">
      <div class="page-grid">
        <div class="headline-stack reveal">
          <span class="eyebrow">Capítulo 4 · Las 6 piezas del cerebro</span>
          <h2>Cómo funciona tu Torre por dentro, sin palabras raras.</h2>
          <p class="lede">
            Toca cualquier tarjeta del Bento Grid para abrir su explicación para 12 años y ver exactamente qué pieza técnica de Animallium la hace realidad.
          </p>
        </div>

        <div class="filter-row reveal" id="glossary-filters">
          <button type="button" class="q-pill active" onclick="filterGlossary('all', this)">Todas (6)</button>
          <button type="button" class="q-pill" onclick="filterGlossary('control', this)">Mirador y Acción</button>
          <button type="button" class="q-pill" onclick="filterGlossary('data', this)">Datos y Verdad</button>
          <button type="button" class="q-pill" onclick="filterGlossary('ai', this)">Reglas e IA</button>
        </div>

        <div class="bento-grid reveal" id="bento-glossary-grid">
          <button type="button" class="bento-card bento-span-3 selected" data-cat="control" id="bcard-0" onclick="selectGlossaryCard(0)">
            <div>
              <span class="chip" style="margin-bottom:8px;">La pantalla maestra</span>
              <h3 style="font-size:1.4rem; margin:0 0 6px;">Single Pane of Glass</h3>
              <p style="margin:0; color:var(--on-surface-variant); font-size:0.93rem;">Tu mirador único en <code>torre.animallium.pet</code></p>
            </div>
            <span style="font-size:0.86rem; font-weight:600; color:var(--primary);">Ver analogía y pieza real ›</span>
          </button>

          <button type="button" class="bento-card bento-span-3" data-cat="data" id="bcard-1" onclick="selectGlossaryCard(1)">
            <div>
              <span class="chip green" style="margin-bottom:8px;">El gran libro de la verdad</span>
              <h3 style="font-size:1.4rem; margin:0 0 6px;">MDM · Registro Dorado (0→200+)</h3>
              <p style="margin:0; color:var(--on-surface-variant); font-size:0.93rem;"><code>business_entities</code> + <code>business_calendar_links</code></p>
            </div>
            <span style="font-size:0.86rem; font-weight:600; color:var(--primary);">Cómo resuelve los calendarios ›</span>
          </button>

          <button type="button" class="bento-card bento-span-2" data-cat="data" id="bcard-2" onclick="selectGlossaryCard(2)">
            <div>
              <span class="chip neutral" style="margin-bottom:8px;">Sin fotocopias</span>
              <h3 style="font-size:1.22rem; margin:0 0 6px;">Zero-Copy + Puente WP</h3>
              <p style="margin:0; color:var(--on-surface-variant); font-size:0.9rem;">Supabase · Postgres · Bridge SQL</p>
            </div>
            <span style="font-size:0.86rem; font-weight:600; color:var(--primary);">Explorar ›</span>
          </button>

          <button type="button" class="bento-card bento-span-2" data-cat="ai" id="bcard-3" onclick="selectGlossaryCard(3)">
            <div>
              <span class="chip orange" style="margin-bottom:8px;">El árbitro del dinero</span>
              <h3 style="font-size:1.22rem; margin:0 0 6px;">Capa Semántica COP/USD</h3>
              <p style="margin:0; color:var(--on-surface-variant); font-size:0.9rem;">Fórmulas oficiales sin errores</p>
            </div>
            <span style="font-size:0.86rem; font-weight:600; color:var(--primary);">Explorar ›</span>
          </button>

          <button type="button" class="bento-card bento-span-2" data-cat="control" id="bcard-4" onclick="selectGlossaryCard(4)">
            <div>
              <span class="chip purple" style="margin-bottom:8px;">El botón que actúa</span>
              <h3 style="font-size:1.22rem; margin:0 0 6px;">Efecto Dominó + Write-Back</h3>
              <p style="margin:0; color:var(--on-surface-variant); font-size:0.9rem;">WhatsApp · Telegram · Campana</p>
            </div>
            <span style="font-size:0.86rem; font-weight:600; color:var(--primary);">Explorar ›</span>
          </button>

          <button type="button" class="bento-card bento-span-4" data-cat="ai" id="bcard-5" onclick="selectGlossaryCard(5)">
            <div>
              <span class="chip" style="margin-bottom:8px;">Paso final · Regla 02</span>
              <h3 style="font-size:1.32rem; margin:0 0 6px;">BI Agéntico Gobernado (Copiloto sin alucinaciones)</h3>
              <p style="margin:0; color:var(--on-surface-variant); font-size:0.93rem;">Una IA que responde preguntas difíciles usando SOLO tus fórmulas oficiales aprobadas.</p>
            </div>
            <span style="font-size:0.86rem; font-weight:600; color:var(--primary);">Ver cómo funciona ›</span>
          </button>

          <div class="bento-card bento-span-2" style="background:linear-gradient(135deg, var(--primary), #004ea0); color:var(--on-primary); cursor:default;">
            <div>
              <span style="font-size:0.82rem; opacity:0.85; font-weight:600;">Promesa clave</span>
              <h3 style="font-size:1.22rem; color:var(--on-primary); margin:6px 0;">Nada ya hecho se rompe</h3>
              <p style="margin:0; font-size:0.9rem; opacity:0.92;">Tu botón de eliminar notificaciones leídas y tu cambio de logo/nombre en el CRM siguen intactos.</p>
            </div>
          </div>
        </div>

        <div class="bento-spotlight reveal" id="glossary-spotlight">
          <div>
            <span class="chip" id="spot-chip">La pantalla maestra</span>
            <h3 id="spot-title" style="font-family:var(--font-headline); font-size:1.65rem; margin:10px 0 4px;">Single Pane of Glass</h3>
            <p id="spot-subtitle" style="color:var(--on-surface-variant); margin:0 0 14px; font-weight:500;"></p>
            <p id="spot-desc" style="margin:0;"></p>
            <div class="analogy-quote">
              <strong style="display:block; font-size:0.86rem; color:var(--secondary); margin-bottom:4px;">Analogía de 5 segundos (para 12 años):</strong>
              <span id="spot-analogy" style="font-size:0.94rem;"></span>
            </div>
          </div>
          <div style="display:grid; gap:12px;">
            <div style="background:var(--surface-container-low); border-radius:var(--rounded-md); padding:16px;">
              <strong style="display:block; font-size:0.86rem; margin-bottom:6px;">Qué problema te quita de encima</strong>
              <p id="spot-problem" style="margin:0; font-size:0.92rem; color:var(--on-surface-variant);"></p>
            </div>
            <div style="background:var(--surface-container-low); border-radius:var(--rounded-md); padding:16px;">
              <strong style="display:block; font-size:0.86rem; margin-bottom:6px;">Cómo se construye en Animallium</strong>
              <p id="spot-tech" style="margin:0; font-size:0.9rem; color:var(--on-surface); font-weight:500;"></p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CAPÍTULO 5: PLAN DE EJECUCIÓN POR FASES -->
    <section id="roadmap" class="band alt">
      <div class="page-grid">
        <div class="headline-stack reveal">
          <span class="eyebrow">Capítulo 5 · El camino paso a paso</span>
          <h2>De cero desorden a una Torre de nivel mundial.</h2>
          <p class="lede">
            Respetando las 3 Reglas de Oro del documento, avanzamos en 6 pasos ordenados. <strong>Toca cada fase</strong> para ver qué entregamos, qué archivos tocamos y cómo verificamos que todo funcione perfecto.
          </p>
        </div>

        <!-- BANNER DE LA PLANTILLA OFICIAL SELECCIONADA -->
        <div class="reveal" style="background:linear-gradient(135deg, #ffffff 0%, #f0f4fc 100%); border:1px solid #d2d2d7; border-radius:var(--rounded-lg); padding:28px 32px; margin-bottom:28px; box-shadow:0 4px 20px rgba(0,0,0,0.03);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:16px; margin-bottom:18px;">
            <div>
              <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                <span class="chip green">Plantilla Oficial Confirmada</span>
                <span class="chip neutral">Archivo: nexoratanstack-10.rar</span>
              </div>
              <h3 style="font-family:var(--font-headline); font-size:1.6rem; margin:0 0 6px; color:var(--on-surface);">Nexora TanStack — El Chasis de la Torre</h3>
              <p style="margin:0; font-size:0.95rem; color:var(--on-surface-variant); max-width:760px;">
                Evaluada contra 4 alternativas y seleccionada oficialmente: comparte la misma estética moderna que WACRM (React 19 + Tailwind CSS + Shadcn + Lucide) y añade la potencia de <strong>TanStack Table v9</strong> para filtrar cientos de aliados y citas en milisegundos sin lag.
              </p>
            </div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <span style="font-size:0.78rem; font-weight:700; background:#e8f1fd; color:#0058b0; padding:4px 10px; border-radius:9999px;">React 19.2</span>
              <span style="font-size:0.78rem; font-weight:700; background:#eaf6ed; color:#248a3d; padding:4px 10px; border-radius:9999px;">TanStack Table v9</span>
              <span style="font-size:0.78rem; font-weight:700; background:#f5eef9; color:#8944ab; padding:4px 10px; border-radius:9999px;">Tailwind v4</span>
              <span style="font-size:0.78rem; font-weight:700; background:#fef4e6; color:#b25000; padding:4px 10px; border-radius:9999px;">@workspace/ui</span>
            </div>
          </div>
          
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px; margin-top:14px;">
            <div style="background:#ffffff; border:1px solid #e5e5ea; border-radius:var(--rounded-md); padding:14px 16px;">
              <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                <div style="width:8px; height:8px; border-radius:50%; background:#006bd6;"></div>
                <strong style="font-size:0.88rem; color:var(--on-surface);">Módulo «Companies»</strong>
              </div>
              <p style="margin:0; font-size:0.82rem; color:var(--on-surface-variant); line-height:1.4;">
                ➔ Se adapta directamente como el <strong>Directorio Dorado MDM</strong> (0→200+ Aliados, IDs WCFM/CRM/Dropi y buscador instantáneo).
              </p>
            </div>
            <div style="background:#ffffff; border:1px solid #e5e5ea; border-radius:var(--rounded-md); padding:14px 16px;">
              <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                <div style="width:8px; height:8px; border-radius:50%; background:#248a3d;"></div>
                <strong style="font-size:0.88rem; color:var(--on-surface);">Módulo «Calendar»</strong>
              </div>
              <p style="margin:0; font-size:0.82rem; color:var(--on-surface-variant); line-height:1.4;">
                ➔ Se conecta al <strong>Monitor FluentBooking</strong> para visualizar citas semanales/mensuales filtrables por veterinario o negocio.
              </p>
            </div>
            <div style="background:#ffffff; border:1px solid #e5e5ea; border-radius:var(--rounded-md); padding:14px 16px;">
              <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                <div style="width:8px; height:8px; border-radius:50%; background:#bf4800;"></div>
                <strong style="font-size:0.88rem; color:var(--on-surface);">Dashboard & Analytics</strong>
              </div>
              <p style="margin:0; font-size:0.82rem; color:var(--on-surface-variant); line-height:1.4;">
                ➔ Muestra las <strong>Tarjetas de la Capa Semántica</strong> (GMV WCFM vs Ventas Dropi vs Comisiones vs Costos IA en USD).
              </p>
            </div>
            <div style="background:#ffffff; border:1px solid #e5e5ea; border-radius:var(--rounded-md); padding:14px 16px;">
              <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                <div style="width:8px; height:8px; border-radius:50%; background:#8944ab;"></div>
                <strong style="font-size:0.88rem; color:var(--on-surface);">Tasks & Orders</strong>
              </div>
              <p style="margin:0; font-size:0.82rem; color:var(--on-surface-variant); line-height:1.4;">
                ➔ Controla el <strong>Fulfillment de Pedidos Dropi</strong> y alertas de despachos sin guía >24h.
              </p>
            </div>
          </div>
        </div>

        <div class="phase-shell reveal">
          <div class="phase-tabs" id="phase-tabs">
            <button type="button" class="phase-tab active" onclick="selectPhase(0)">
              <div class="phase-num">Fase 0</div>
              <div class="phase-tab-title">CRM Limpio</div>
              <div class="phase-tab-time">1–2 días</div>
            </button>
            <button type="button" class="phase-tab" onclick="selectPhase(1)">
              <div class="phase-num">Fase 1</div>
              <div class="phase-tab-title">Mando Libre</div>
              <div class="phase-tab-time">2–4 días</div>
            </button>
            <button type="button" class="phase-tab" onclick="selectPhase(2)">
              <div class="phase-num">Fase 2A</div>
              <div class="phase-tab-title">Torre MVP</div>
              <div class="phase-tab-time">Sem. 2–3</div>
            </button>
            <button type="button" class="phase-tab" onclick="selectPhase(3)">
              <div class="phase-num">Fase 2B</div>
              <div class="phase-tab-title">Expansión</div>
              <div class="phase-tab-time">Sem. 4–5</div>
            </button>
            <button type="button" class="phase-tab" onclick="selectPhase(4)">
              <div class="phase-num">Fase 3</div>
              <div class="phase-tab-title">Write-Back</div>
              <div class="phase-tab-time">Sem. 6–7</div>
            </button>
            <button type="button" class="phase-tab" onclick="selectPhase(5)">
              <div class="phase-num">Fase 4</div>
              <div class="phase-tab-title">BI Agéntico</div>
              <div class="phase-tab-time">Sem. 8+</div>
            </button>
          </div>

          <div class="phase-detail-card" id="phase-detail-card">
            <div>
              <span class="chip" id="ph-chip">Fase 0 · 1–2 días</span>
              <h3 id="ph-title" style="font-family:var(--font-headline); font-size:1.6rem; margin:10px 0 8px;"></h3>
              <p id="ph-kid" style="margin:0 0 14px; font-size:0.96rem;"></p>
              <ul class="feature-list" id="ph-steps"></ul>
            </div>
            <div style="display:grid; gap:14px;">
              <div style="background:var(--surface-container-low); border-radius:var(--rounded-md); padding:16px;">
                <strong style="display:block; font-size:0.86rem; color:var(--positive); margin-bottom:6px;">Qué queda funcionando al terminar esta fase</strong>
                <p id="ph-outcome" style="margin:0; font-size:0.92rem; color:var(--on-surface);"></p>
              </div>
              <div style="background:var(--surface-container-low); border-radius:var(--rounded-md); padding:16px;">
                <strong style="display:block; font-size:0.86rem; color:var(--primary); margin-bottom:6px;">Pruebas de calidad obligatorias</strong>
                <p id="ph-qa" style="margin:0; font-size:0.9rem; color:var(--on-surface-variant);"></p>
              </div>
            </div>
          </div>
        </div>

        <!-- Gráfico animado de madurez del ecosistema -->
        <div class="tile chart-tile reveal" id="maturity-chart">
          <div style="margin-bottom:var(--space-lg);">
            <span class="chip green" style="margin-bottom:8px;">Evolución del ecosistema</span>
            <h3 style="font-size:1.3rem;">Cómo sube el superpoder de tu empresa en cada etapa</h3>
            <p style="color:var(--on-surface-variant); font-size:0.92rem; margin:4px 0 0;">
              Porcentaje de control real, velocidad comercial y escalabilidad rumbo a 200+ negocios aliados.
            </p>
          </div>
          <div class="bar-list">
            <div class="bar-row">
              <div class="bar-label">Fase 0 + 1 · Orden y Seguridad <span class="bar-sub">CRM 100% limpio + Centro de Mando independiente</span></div>
              <div class="bar-track"><div class="bar-fill primary" data-width="35%"></div></div>
              <div class="bar-val">Base 35%</div>
            </div>
            <div class="bar-row">
              <div class="bar-label">Fase 2A · Torre MVP (Aliados) <span class="bar-sub">MDM 0→200+ + WCFM + FluentBooking + Capa Semántica</span></div>
              <div class="bar-track"><div class="bar-fill green" data-width="68%"></div></div>
              <div class="bar-val">Salto 68%</div>
            </div>
            <div class="bar-row">
              <div class="bar-label">Fase 2B + 3 · Torre Activa <span class="bar-sub">Zero-Copy WACRM + Dropi + Efecto Dominó + Write-Back</span></div>
              <div class="bar-track"><div class="bar-fill secondary" data-width="90%"></div></div>
              <div class="bar-val">Nivel 90%</div>
            </div>
            <div class="bar-row">
              <div class="bar-label">Fase 4 · BI Agéntico Gobernado <span class="bar-sub">Copiloto de IA conectado a reglas certificadas</span></div>
              <div class="bar-track"><div class="bar-fill purple" data-width="100%"></div></div>
              <div class="bar-val">100% Pro</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CAPÍTULO 6: LAS 6 DECISIONES CONFIRMADAS -->
    <section id="decisiones" class="band">
      <div class="page-grid">
        <div class="headline-stack reveal">
          <span class="eyebrow">Capítulo 6 · Plan Confirmado ✅</span>
          <h2>6 decisiones aprobadas. Listos para encender motores.</h2>
          <p class="lede">
            Todas tus definiciones quedaron bloqueadas en el plan maestro v3. Solo falta tu «dale» para ejecutar la Fase 0 y el chequeo del VPS.
          </p>
        </div>

        <div class="decisions-grid reveal">
          <article class="decision-card">
            <div>
              <div class="step-number">01</div>
              <h3>Los 3 nombres de tus casas (DNS)</h3>
              <p style="font-size:0.92rem; color:var(--on-surface-variant); margin:8px 0 12px;">
                Cada sistema tendrá su propia puerta web con candado HTTPS automático en Caddy.
              </p>
            </div>
            <div class="choice-pills">
              <span class="chip green">✅ Confirmado: crm / mando / torre .animallium.pet</span>
            </div>
          </article>

          <article class="decision-card">
            <div>
              <div class="step-number">02</div>
              <h3>Monitor Nodos IA se queda en el CRM</h3>
              <p style="font-size:0.92rem; color:var(--on-surface-variant); margin:8px 0 12px;">
                Porque los nodos (Ani, Sofi, Triage, Camila) atienden tus chats de WhatsApp. Sale solo el Centro de Mando, y el proxy se recorta al mínimo seguro.
              </p>
            </div>
            <div class="choice-pills">
              <span class="chip green">✅ Confirmado: Nodos IA en CRM · Mando aparte</span>
            </div>
          </article>

          <article class="decision-card">
            <div>
              <div class="step-number">03</div>
              <h3>Una sola llave para entrar (SSO)</h3>
              <p style="font-size:0.92rem; color:var(--on-surface-variant); margin:8px 0 12px;">
                Tu mismo usuario Admin de Supabase Auth abre CRM, Torre y Centro de Mando (y habilita Zero-Copy directo).
              </p>
            </div>
            <div class="choice-pills">
              <span class="chip green">✅ Confirmado: SSO Supabase Auth</span>
            </div>
          </article>

          <article class="decision-card">
            <div>
              <div class="step-number">04</div>
              <h3>Libro Dorado (MDM) en el VPS</h3>
              <p style="font-size:0.92rem; color:var(--on-surface-variant); margin:8px 0 12px;">
                El esquema <code>control_tower</code> para los 200+ aliados vivirá en el PostgreSQL del VPS (cero costo extra, red interna <code>root_default</code>).
              </p>
            </div>
            <div class="choice-pills">
              <span class="chip green">✅ Confirmado: PostgreSQL del VPS</span>
            </div>
          </article>

          <article class="decision-card">
            <div>
              <div class="step-number">05</div>
              <h3>Ventas propias vs. Aliados (WCFM)</h3>
              <p style="font-size:0.92rem; color:var(--on-surface-variant); margin:8px 0 12px;">
                Separación contable estricta entre Dropshipping propio y terceros WCFM, más separación COP vs. USD de IA.
              </p>
            </div>
            <div class="choice-pills">
              <span class="chip green">✅ Confirmado: 0 doble conteo COP/USD</span>
            </div>
          </article>

          <article class="decision-card">
            <div>
              <div class="step-number">06</div>
              <h3>Chequeo en vivo del VPS y Hostinger</h3>
              <p style="font-size:0.92rem; color:var(--on-surface-variant); margin:8px 0 12px;">
                Antes de Fase 1/2 revisamos <code>/root/Caddyfile</code>, RAM libre en VPS <code>62.72.24.151</code>, el <code>vendor_id</code> propio y el plugin de <code>/dropi/orders</code>.
              </p>
            </div>
            <div class="choice-pills">
              <span class="chip green">✅ Confirmado: Auditoría VPS + Fase 0</span>
            </div>
          </article>
        </div>
      </div>
    </section>
  </main>

  <footer class="sources-footer">
    <h3>Base técnica auditada y veracidad garantizada</h3>
    <p style="margin:0;">
      Documento construido cruzando los principios de <em>El Gran Panel de Control Empresarial (CRM vs. Sistemas Globales)</em> contra el código real verificado en <code>d:\ESCRITORIO\wacrm</code> (Next.js + Supabase + 1.697 tests), <code>d:\ESCRITORIO\Animallium_Master\animallium-ai-core</code> (FastAPI + PostgreSQL VPS) y el espejo local de plugins WordPress (<code>wc-frontend-manager</code>, <code>wc-multivendor-marketplace</code>, <code>wcfm-marketplace-rest-api</code>, <code>fluent-booking-pro</code> y <code>animallium-connect</code> de 5.340 líneas). Sin secretos ni credenciales expuestas.
    </p>
  </footer>

  <script>
    // =====================================================
    // 1. INSPECTOR DE LOS 4 SISTEMAS
    // =====================================================
    const systemsData = [
      {
        chip: 'Sistema 4 · NUEVO · Torre de Control',
        chipClass: 'chip',
        activeClass: 'active',
        title: 'Torre de Control Global (torre.animallium.pet)',
        kid: 'Es una aplicación nueva e independiente que vive encima de tus otros 3 programas. No reemplaza al CRM ni a WordPress: los observa a todos al mismo tiempo, une a tus 200+ aliados en un Libro Dorado (MDM) y calcula tus ganancias reales sin equivocarse de moneda.',
        analogy: 'Como la torre de cristal de un aeropuerto: el controlador no maneja un avión por uno, mira todas las pistas, el clima y los pasajeros para avisar si algo se va a retrasar.',
        yes: 'Resumen ejecutivo COP/USD, Directorio Maestro de Aliados (0→200+), mapeo de calendarios FluentBooking, monitor de citas, salud del CRM, alertas de efecto dominó y botones Write-Back.',
        no: 'Chats uno a uno con clientes, edición manual de borradores de productos Dropi ni almacenamiento duplicado de todas las conversaciones.'
      },
      {
        chip: 'Sistema 1 · CRM Conversacional + Nodos IA',
        chipClass: 'chip',
        activeClass: 'active',
        title: 'WACRM + Monitor Nodos IA (crm.animallium.pet)',
        kid: 'Sacamos el Centro de Mando pesado (Dropi, borradores y logística), pero DEJAMOS el Monitor Visual de Nodos IA dentro del CRM porque esos nodos (Ani, Sofi, Triage, Camila) son los que atienden tus conversaciones de WhatsApp en tiempo real.',
        analogy: 'Es el tablero del carro de carreras: te muestra velocidad, mapa hacia el cliente y el radar de tus robots copilotos que responden el chat, sin distraerte con cajas de bodega ni contabilidad.',
        yes: 'Bandeja de WhatsApp, Contactos, Embudos B2C/B2B, Difusiones, Flujos, Agentes IA, Monitor Nodos IA (bajo bandera modular y proxy acotado), Notificaciones «Eliminar leídas» y Logo/Nombre.',
        no: 'Centro de Mando (6 capas), Dropi Scout, borradores WooCommerce, propuestas B2B ni cálculo de comisiones multi-vendor.'
      },
      {
        chip: 'Sistema 2 · Tienda, Aliados y Citas',
        chipClass: 'chip green',
        activeClass: 'active active-green',
        title: 'WordPress + WCFM + FluentBooking (animallium.pet)',
        kid: 'Es el centro comercial público donde entran los tutores de mascotas y los negocios aliados. Le agregamos un pequeño puente seguro (animallium-control-bridge) que le responde a la Torre en milisegundos.',
        analogy: 'Es el parque comercial con locales (WCFM), recepción de turnos para peluquería/veterinaria (FluentBooking) y consultorios médicos (SOAP Plan 3).',
        yes: 'Tiendas y comisiones WCFM, catálogo de productos WooCommerce, calendarios y citas FluentBooking, Pasaporte Phygital e Historias Clínicas SOAP.',
        no: 'Reportes pesados cruzados con WhatsApp o costos de IA que pondrían lenta la tienda cuando un cliente está pagando.'
      },
      {
        chip: 'Sistema 3 · Taller Operativo Independiente',
        chipClass: 'chip purple',
        activeClass: 'active active-purple',
        title: 'Centro de Mando + AI Core (mando.animallium.pet)',
        kid: 'Se independiza 100% del CRM con su propia dirección web y candados nuevos (SSO Supabase Auth). Aquí el equipo de operaciones caza productos en Dropi, aprueba borradores, genera propuestas B2B y controla la logística.',
        analogy: 'Es el taller de ingeniería en la parte de atrás: donde se preparan los paquetes, se arman los catálogos y se controlan las guías antes de salir al público.',
        yes: 'Sourcing Dropi Plan A/B/C, borradores WooCommerce, propuestas B2B, suite creativa, Logística & Fulfillment Dropi (antes Pestaña 5) y motor backend FastAPI.',
        no: 'Vivir incrustado dentro del menú del CRM, guardar contraseñas en texto plano o tener webhooks sin firma.'
      }
    ];

    function selectSystem(idx) {
      const data = systemsData[idx];
      if (!data) return;
      for (let i = 0; i < 4; i++) {
        const el = document.getElementById('sys-card-' + i);
        if (!el) continue;
        el.classList.remove('active', 'active-orange', 'active-green', 'active-purple');
        if (i === idx) {
          data.activeClass.split(' ').forEach(c => el.classList.add(c));
        }
      }
      const insp = document.getElementById('arch-inspector');
      if (insp) {
        insp.classList.remove('soft-pop');
        void insp.offsetWidth;
        insp.classList.add('soft-pop');
      }
      document.getElementById('insp-chip').textContent = data.chip;
      document.getElementById('insp-chip').className = data.chipClass;
      document.getElementById('insp-title').textContent = data.title;
      document.getElementById('insp-kid').textContent = data.kid;
      document.getElementById('insp-analogy').textContent = data.analogy;
      document.getElementById('insp-yes').textContent = data.yes;
      document.getElementById('insp-no').textContent = data.no;
    }

    // =====================================================
    // 2. COMPARADOR DE 3 SISTEMAS
    // =====================================================
    const comparatorQuestions = [
      {
        crmStatus: 'Aquí se responde', crmClass: 'status-yes',
        crmText: 'Abres el Inbox de WACRM: ves el chat en vivo, etiquetas, notas privadas y en qué etapa del embudo está ese cliente.',
        mandoStatus: 'No es para chatear', mandoClass: 'status-no',
        mandoText: 'El Centro de Mando trabaja detrás de escena (Dropi, borradores y robots), no es un chat de asesores.',
        torreStatus: 'Solo resumen', torreClass: 'status-partial',
        torreText: 'La Torre solo mira si el equipo está respondiendo rápido (SLA) y te da un enlace directo al CRM si hace falta entrar.',
        verdict: 'Para hablar con personas usa siempre WACRM. Por eso lo dejamos limpio y rapidísimo.'
      },
      {
        crmStatus: 'Dato incompleto', crmClass: 'status-no',
        crmText: 'El CRM solo ve promesas de venta en el embudo; no conoce comisiones WCFM, reembolsos ni facturas de IA en dólares.',
        mandoStatus: 'Solo su pedazo', mandoClass: 'status-partial',
        mandoText: 'Solo conoce el margen de Dropi y el gasto de tokens IA en USD, pero no cruza comisiones de los 200 negocios de WCFM.',
        torreStatus: 'Cifra exacta', torreClass: 'status-yes',
        torreText: 'Aplica la Capa Semántica oficial: separa COP de USD, resta reembolsos, evita contar doble Dropi y te da la ganancia neta real.',
        verdict: 'La Torre de Control es el único árbitro del dinero de toda la empresa.'
      },
      {
        crmStatus: 'No ve calendarios', crmClass: 'status-no',
        crmText: 'El CRM guarda al contacto y su trato B2B, pero no controla qué calendarios existen adentro de WordPress.',
        mandoStatus: 'No administra MDM', mandoClass: 'status-no',
        mandoText: 'El Centro de Mando no lleva el directorio maestro de negocios ni sus sedes de citas.',
        torreStatus: 'Resuelto en 1 clic', torreClass: 'status-yes',
        torreText: 'Su Registro Dorado (MDM) detecta cada calendario nuevo de FluentBooking y permite vincularlo al negocio correcto en 1 clic, aunque lo haya creado el Admin.',
        verdict: 'Así puedes pasar de 0 a 200+ negocios sin perder nunca a quién pertenece cada cita.'
      },
      {
        crmStatus: 'Ya no vive aquí', crmClass: 'status-no',
        crmText: 'Sacamos esto del CRM para que los vendedores no se pierdan entre botones de bodegas y proveedores.',
        mandoStatus: 'Su casa oficial', mandoClass: 'status-yes',
        mandoText: 'En mando.animallium.pet ejecutas Dropi Scout, revisas borradores WooCommerce, creativos y logística con candados propios.',
        torreStatus: 'Solo vigila salud', torreClass: 'status-partial',
        torreText: 'La Torre vigila si un pedido Dropi lleva más de 24h sin guía y te lleva con 1 clic al Centro de Mando para resolverlo.',
        verdict: 'Operación pesada en Centro de Mando; vigilancia ejecutiva en Torre de Control.'
      },
      {
        crmStatus: 'Solo ve el trato', crmClass: 'status-partial',
        crmText: 'El CRM sabe que el trato B2B se marcó «Ganado» hace 5 días, pero no sabe si ya montó productos en WCFM.',
        mandoStatus: 'Punto ciego', mandoClass: 'status-no',
        mandoText: 'El Centro de Mando no cruza embudos comerciales B2B contra calendarios de FluentBooking.',
        torreStatus: 'Detecta y avisa', torreClass: 'status-yes',
        torreText: 'Cruza WACRM + WCFM + FluentBooking, detecta el retraso de 5 días y dispara una alerta Write-Back a Telegram/CRM y WhatsApp.',
        verdict: 'Ese es el poder del Efecto Dominó: ver un problema entre sistemas distintos antes de perder al aliado.'
      },
      {
        crmStatus: '100% intacto aquí', crmClass: 'status-yes',
        crmText: 'En /notifications sigues teniendo «Eliminar leídas» y en Configuración → Apariencia cambias el logo y nombre cuando quieras.',
        mandoStatus: 'Independiente', mandoClass: 'status-no',
        mandoText: 'Separar el Centro de Mando no toca para nada tu configuración visual ni tus notificaciones del CRM.',
        torreStatus: 'Independiente', torreClass: 'status-no',
        torreText: 'La Torre es un proyecto aparte; nunca pisa lo que ya construimos y certificamos en WACRM.',
        verdict: 'Cero retrocesos: limpiamos lo que sobraba y blindamos todo lo que ya funciona bien.'
      }
    ];

    function selectQuestion(idx) {
      const item = comparatorQuestions[idx];
      if (!item) return;
      document.querySelectorAll('#question-pills-row .q-pill').forEach((btn, i) => {
        btn.classList.toggle('active', i === idx);
      });

      const pairs = [
        ['crm', item.crmStatus, item.crmClass, item.crmText],
        ['mando', item.mandoStatus, item.mandoClass, item.mandoText],
        ['torre', item.torreStatus, item.torreClass, item.torreText]
      ];
      pairs.forEach(([key, st, cls, txt]) => {
        const badge = document.getElementById(key + '-status-badge');
        const box = document.getElementById(key + '-answer-text');
        const card = document.getElementById('comp-' + key + '-card');
        if (badge) { badge.textContent = st; badge.className = 'comp-status ' + cls; }
        if (box) { box.textContent = txt; }
        if (card) { card.classList.toggle('highlighted', cls === 'status-yes'); }
      });
      document.getElementById('comp-verdict-text').textContent = item.verdict;
    }

    // =====================================================
    // 3. SIMULADOR ANIMADO DE 4 ESTACIONES
    // =====================================================
    const simEvents = [
      {
        name: 'Nace la Veterinaria #1',
        modern: [
          {
            chip: 'Estación 1 · Alta en WordPress',
            headline: 'Una clínica veterinaria se registra en WCFM',
            body: 'El dueño llena su registro de tienda en animallium.pet. Al instante suena el timbre real wcfmmp_new_store_created.',
            action: 'El puente animallium-control-bridge manda un aviso seguro (HMAC) a la Torre en menos de un segundo.',
            time: '0.4 s', copies: '0', crm: 'Enlazado B2B', risk: 'Orden total'
          },
          {
            chip: 'Estación 2 · Registro Dorado (MDM)',
            headline: 'La Torre crea su ficha única en el Libro Dorado',
            body: 'En control_tower.business_entities nace la Veterinaria #1 uniendo su Deal B2B de WACRM, su tienda WCFM y su teléfono +57.',
            action: 'Queda lista para sumar ventas, productos y calendarios sin duplicarse nunca, aunque crezcas a 200+ negocios.',
            time: '1.0 s', copies: '0', crm: 'Ficha ligada', risk: '0 duplicados'
          },
          {
            chip: 'Estación 3 · Zero-Copy',
            headline: 'Aparece al instante en el Directorio Maestro',
            body: 'Sin esperar cargas nocturnas, la Torre consulta en vivo cuántos productos subió y si ya tiene calendario de citas.',
            action: 'La Capa Semántica la marca en estado «Onboarding» hasta que tenga ≥1 producto o ≥1 calendario activo.',
            time: '1.6 s', copies: '0', crm: 'Sincronizado', risk: 'Medido en vivo'
          },
          {
            chip: 'Estación 4 · Write-Back',
            headline: 'Bienvenida automática por WhatsApp y guía al equipo',
            body: 'La Torre avisa al equipo en Telegram y ofrece 1 clic para enviar mensaje de bienvenida por WhatsApp vía WACRM.',
            action: 'El CRM sigue liviano y tu red de aliados arranca perfecta desde el negocio #1.',
            time: '2.1 s', copies: '0', crm: 'Alerta lista', risk: '100% control'
          }
        ],
        legacy: [
          {
            chip: 'Estación 1 · Alta aislada',
            headline: 'La clínica se registra, pero nadie en el CRM se entera',
            body: 'El registro queda guardado solo dentro de las tablas de WordPress mientras el equipo comercial sigue mirando un embudo viejo.',
            action: 'Alguien tiene que copiar a mano el nombre y el teléfono desde WordPress hacia el CRM.',
            time: '5 horas', copies: '1 copia manual', crm: 'Desconectado', risk: 'Olvido'
          },
          {
            chip: 'Estación 2 · Teléfono sin +57',
            headline: 'Se crea un contacto duplicado',
            body: 'En WhatsApp estaba como 57300... y en WordPress quedó como 300... Ahora el CRM cree que son dos personas distintas.',
            action: 'Las conversaciones y el historial del negocio quedan partidos por la mitad.',
            time: '1 día', copies: '3 copias', crm: 'Duplicado', risk: 'Alto'
          },
          {
            chip: 'Estación 3 · CRM pesado',
            headline: 'Intentan meter tablas de tienda dentro del CRM',
            body: 'El menú del CRM se llena de pestañas de contabilidad y tiendas que confunden a los asesores de WhatsApp.',
            action: 'Los vendedores dejan de actualizar datos porque el sistema se siente lento y complejo.',
            time: '2 días', copies: '6 copias', crm: 'Sobrecargado', risk: 'Baja adopción'
          },
          {
            chip: 'Estación 4 · Caos al crecer',
            headline: 'Con 50 negocios ya nadie confía en las cifras',
            body: 'Cada panel muestra un número distinto de aliados activos y toca hacer hojas de Excel cada viernes.',
            action: 'Reuniones eternas para cuadrar listas a mano.',
            time: '5 días', copies: '10+ Excels', crm: 'En conflicto', risk: 'Crítico'
          }
        ]
      },
      {
        name: 'Admin crea un calendario FluentBooking',
        modern: [
          {
            chip: 'Estación 1 · Hook de calendario',
            headline: 'Tú (Admin) creas un calendario para «Clínica Patitas»',
            body: 'Aunque lo creaste con tu usuario Administrador (user_id = 1) y no con la cuenta del negocio, se dispara fluent_booking/after_create_calendar.',
            action: 'El puente avisa de inmediato a la Torre de Control que existe un calendario nuevo.',
            time: '0.3 s', copies: '0', crm: 'Sin impacto', risk: 'Detectado'
          },
          {
            chip: 'Estación 2 · Cola Inteligente MDM',
            headline: 'Aparece en «Calendarios sin asignar»',
            body: 'La Torre revisa si hay un producto con _fluent_booking_event_id para sugerirte el negocio; si no, te lo muestra en la cola limpia.',
            action: 'Jamás atribuye esas citas al Administrador por error.',
            time: '0.9 s', copies: '0', crm: 'Limpio', risk: 'Cero error'
          },
          {
            chip: 'Estación 3 · Vínculo en 1 clic',
            headline: 'Lo conectas a «Clínica Patitas» en 5 segundos',
            body: 'Se guarda la fila en business_calendar_links (calendar_id → business_id). Incluso puedes vincular varias sedes al mismo negocio.',
            action: 'Todas las citas futuras y pasadas de ese calendario suman 100% a Clínica Patitas.',
            time: '5 s', copies: '0', crm: 'Consistente', risk: 'Atribución 100%'
          },
          {
            chip: 'Estación 4 · Métrica viva',
            headline: 'El Monitor de Citas muestra asistencia real por negocio',
            body: 'Cada cita agendada, completada o cancelada actualiza el porcentaje de cumplimiento del aliado al instante.',
            action: 'Funciona perfecto tanto si los calendarios los crea el negocio como si los creas tú.',
            time: 'Instantáneo', copies: '0', crm: 'Alineado', risk: 'Controlado'
          }
        ],
        legacy: [
          {
            chip: 'Estación 1 · Creación manual',
            headline: 'El Admin crea 15 calendarios para 15 clínicas',
            body: 'En la base de datos de FluentBooking, los 15 calendarios quedan con user_id = 1 (el Administrador).',
            action: 'No existe ninguna tabla que diga a qué clínica pertenece cada uno.',
            time: '1 hora', copies: '0', crm: 'Ciego', risk: 'Oculto'
          },
          {
            chip: 'Estación 2 · Bug de columna',
            headline: 'El script viejo busca author_id y falla',
            body: 'La columna real es user_id, no author_id. Y como todos son del Admin, el cruce automático se rompe.',
            action: 'Las métricas de las 15 clínicas aparecen en CERO citas.',
            time: '1 día', copies: '2 tablas', crm: 'Engañoso', risk: 'Alto'
          },
          {
            chip: 'Estación 3 · Reportes rotos',
            headline: 'Todas las citas aparecen como «Animallium Central»',
            body: 'Cuando una clínica pregunta cuántas citas recibió este mes, nadie puede darle un número confiable.',
            action: 'Toca entrar calendario por calendario a contar citas con calculadora.',
            time: '3 días', copies: '5 Excels', crm: 'Desfasado', risk: 'Muy alto'
          },
          {
            chip: 'Estación 4 · Escalabilidad rota',
            headline: 'Imposible manejar 200 negocios así',
            body: 'A medida que llegan más clínicas, el trabajo manual explota y se pierden citas canceladas sin seguimiento.',
            action: 'Pérdida de confianza de los aliados.',
            time: '1 semana', copies: '12+ Excels', crm: 'Saturado', risk: 'Crítico'
          }
        ]
      },
      {
        name: 'Venta + Reembolso + Gasto IA',
        modern: [
          {
            chip: 'Estación 1 · Tres monedas/fuentes',
            headline: 'Ocurre venta WCFM, reembolso parcial y consumo de IA',
            body: 'WordPress registra una venta con comisión en COP, luego un reembolso parcial, y el AI Core registra tokens gastados en USD.',
            action: 'Cada sistema guarda su dato oficial en su propia base sin mezclarse.',
            time: '0.5 s', copies: '0', crm: 'Intacto', risk: 'Registrado'
          },
          {
            chip: 'Estación 2 · Limpieza SQL',
            headline: 'El puente convierte VARCHAR a decimal y filtra basura',
            body: 'CAST(... AS DECIMAL(12,2)) ignora pedidos cancelados o en papelera (is_trashed = 0), descuenta refunded_amount y usa total_commission.',
            action: 'Además excluye el vendor_id de tienda propia para no contar dos veces Dropi.',
            time: '1.1 s', copies: '0', crm: 'Sin ruido', risk: 'Exactitud contable'
          },
          {
            chip: 'Estación 3 · Capa Semántica COP/USD',
            headline: 'Pesos con pesos, dólares con dólares',
            body: 'Muestra GMV y Take-rate en COP, gasto de IA en USD, y solo consolida el neto usando la TRM oficial configurada.',
            action: 'Cero alucinaciones financieras: la cifra cuadra al centavo con WooCommerce.',
            time: '1.5 s', copies: '0', crm: 'Verificado', risk: '0 errores'
          },
          {
            chip: 'Estación 4 · Tablero Ejecutivo',
            headline: 'Ves tu ganancia real en una sola pantalla',
            body: 'Sabes exactamente cuánto dejó Marketplace, cuánto dejó Dropi y cuánto costó la IA ese mes.',
            action: 'Listo para tomar decisiones de precios y presupuesto con datos reales.',
            time: '1.9 s', copies: '0', crm: 'Transparente', risk: 'Control total'
          }
        ],
        legacy: [
          {
            chip: 'Estación 1 · Suma ingenua',
            headline: 'Una fórmula mezcla COP con USD sin convertir',
            body: 'Resta 15 USD de IA a 150.000 COP de ventas como si fueran la misma moneda.',
            action: 'La utilidad sale mal calculada desde el primer día.',
            time: '1 hora', copies: '1 copia', crm: 'Confuso', risk: 'Alto'
          },
          {
            chip: 'Estación 2 · Doble conteo',
            headline: 'Un pedido de Dropi se suma dos veces',
            body: 'Como pasó por WooCommerce y también por orders_fulfillment, el tablero infla las ventas al doble.',
            action: 'Crees que ganaste el doble de lo que realmente entró al banco.',
            time: '1 día', copies: '3 copias', crm: 'Inflado', risk: 'Severo'
          },
          {
            chip: 'Estación 3 · Pedidos cancelados',
            headline: 'No se restan reembolsos ni papelera',
            body: 'Los pedidos cancelados siguen sumando en el GMV porque nadie filtró order_status ni refunded_amount.',
            action: 'El reporte del CRM no coincide con WooCommerce.',
            time: '2 días', copies: '5 Excels', crm: 'Sin confianza', risk: 'Muy alto'
          },
          {
            chip: 'Estación 4 · Abandono',
            headline: 'El equipo deja de mirar las métricas',
            body: 'Cuando el número no cuadra con el banco, nadie vuelve a abrir el dashboard.',
            action: 'Vuelven a exportar CSVs a mano cada semana.',
            time: '4 días', copies: '8+ CSVs', crm: 'Ignorado', risk: 'Crítico'
          }
        ]
      },
      {
        name: 'Aliado B2B parado 5 días',
        modern: [
          {
            chip: 'Estación 1 · Señal en WACRM',
            headline: 'El trato B2B se cerró «Ganado» hace 5 días',
            body: 'El asesor comercial hizo su trabajo perfecto en el CRM y marcó al nuevo aliado como cerrado.',
            action: 'La Torre lee ese estado en vivo (Zero-Copy) usando el conector de Supabase.',
            time: '0.4 s', copies: '0', crm: 'Deal Ganado', risk: 'Monitoreado'
          },
          {
            chip: 'Estación 2 · Cruce entre mundos',
            headline: 'La Torre revisa WCFM y FluentBooking',
            body: 'Descubre que han pasado 5 días y el aliado todavía tiene 0 productos publicados y 0 calendarios activos.',
            action: 'Se dispara la regla de Efecto Dominó: «Riesgo de abandono en Onboarding».',
            time: '1.1 s', copies: '0', crm: 'Riesgo hallado', risk: 'Alerta temprana'
          },
          {
            chip: 'Estación 3 · Acción Write-Back',
            headline: 'Alerta limpia al equipo + botón de rescate',
            body: 'La Torre manda un aviso inmediato a Telegram (y campana del CRM en Fase 3) con botón 1-clic para ayudarle por WhatsApp.',
            action: 'Usa POST /api/v1/messages de WACRM con plantilla oficial de acompañamiento.',
            time: '1.8 s', copies: '0', crm: 'Aviso entregado', risk: 'Mitigado'
          },
          {
            chip: 'Estación 4 · Aliado activado',
            headline: 'El negocio sube sus productos hoy mismo',
            body: 'El dueño agradece el apoyo rápido, activa su tienda y agenda su primera cita esa misma semana.',
            action: 'Rescataste una alianza que se habría enfriado en silencio.',
            time: 'Mismo día', copies: '0', crm: 'Cliente feliz', risk: 'Controlado'
          }
        ],
        legacy: [
          {
            chip: 'Estación 1 · Silo comercial',
            headline: 'El vendedor cierra el trato y celebra',
            body: 'En el CRM todo aparece en verde como «Ganado», así que nadie vuelve a mirar esa tarjeta.',
            action: 'El equipo comercial pasa al siguiente prospecto.',
            time: 'Día 1', copies: '0', crm: 'Falso verde', risk: 'Invisible'
          },
          {
            chip: 'Estación 2 · Silencio en WordPress',
            headline: 'El dueño del negocio se traba subiendo su logo',
            body: 'Como nadie vigila WordPress frente al CRM, el aliado abandona el registro a mitad de camino.',
            action: 'Pasan 2 semanas sin que nadie note que su tienda está vacía.',
            time: '15 días', copies: '0', crm: 'Sin noticias', risk: 'Alto'
          },
          {
            chip: 'Estación 3 · Descubrimiento tardío',
            headline: 'Al fin de mes ven que no vendió nada',
            body: 'En el cierre mensual alguien nota que de 20 negocios cerrados, solo 6 están vendiendo.',
            action: 'Toca llamar uno por uno para averiguar qué pasó.',
            time: '30 días', copies: '4 listas', crm: 'Desactualizado', risk: 'Muy alto'
          },
          {
            chip: 'Estación 4 · Aliado perdido',
            headline: 'El negocio ya perdió el entusiasmo',
            body: 'Se desperdició todo el esfuerzo de captación B2B porque nadie vio el bloqueo a tiempo.',
            action: 'Churn temprano evitable.',
            time: '45 días', copies: '6+ listas', crm: 'Pérdida', risk: 'Crítico'
          }
        ]
      }
    ];

    let simState = { eventIdx: 0, arch: 'modern', stepIdx: 0 };
    let simTimer = null;

    function renderSimulator() {
      const ev = simEvents[simState.eventIdx];
      if (!ev) return;
      const steps = simState.arch === 'modern' ? ev.modern : ev.legacy;
      const current = steps[simState.stepIdx];
      if (!current) return;

      document.querySelectorAll('#sim-event-buttons .event-btn').forEach((btn, i) => {
        btn.classList.toggle('active', i === simState.eventIdx);
      });
      document.getElementById('arch-modern').setAttribute('aria-selected', simState.arch === 'modern' ? 'true' : 'false');
      document.getElementById('arch-legacy').setAttribute('aria-selected', simState.arch === 'legacy' ? 'true' : 'false');

      const fill = document.getElementById('sim-progress-fill');
      if (fill) {
        fill.style.width = ((simState.stepIdx + 1) * 25) + '%';
        fill.classList.toggle('chaos', simState.arch === 'legacy');
      }

      for (let i = 0; i < 4; i++) {
        const node = document.getElementById('sim-node-' + i);
        const nTitle = document.getElementById('node-title-' + i);
        const nDesc = document.getElementById('node-desc-' + i);
        if (node) {
          node.classList.toggle('reached', i <= simState.stepIdx);
          node.classList.toggle('current', i === simState.stepIdx);
          node.classList.toggle('chaos', simState.arch === 'legacy');
        }
        if (nTitle && steps[i]) nTitle.textContent = steps[i].chip.split('·')[1] ? steps[i].chip.split('·')[1].trim() : steps[i].chip;
        if (nDesc && steps[i]) nDesc.textContent = steps[i].headline;
      }

      const panel = document.getElementById('sim-output-panel');
      if (panel) {
        panel.classList.remove('soft-pop');
        void panel.offsetWidth;
        panel.classList.add('soft-pop');
      }

      const chipEl = document.getElementById('sim-stage-chip');
      chipEl.textContent = current.chip;
      chipEl.className = simState.arch === 'modern' ? 'chip green' : 'chip red';
      document.getElementById('sim-detail-headline').textContent = current.headline;
      document.getElementById('sim-detail-body').textContent = current.body;
      document.getElementById('sim-action-title').textContent = simState.arch === 'modern' ? 'Qué hace tu Torre automáticamente:' : 'Qué pasa cuando todo está mezclado:';
      document.getElementById('sim-action-text').textContent = current.action;
      document.getElementById('sim-step-counter').textContent = `Paso ${simState.stepIdx + 1} de 4 — ${ev.name}`;
      document.getElementById('sim-metric-time').textContent = current.time;
      document.getElementById('sim-metric-copies').textContent = current.copies;
      document.getElementById('sim-metric-crm').textContent = current.crm;
      document.getElementById('sim-metric-risk').textContent = current.risk;
    }

    function selectSimEvent(idx) {
      if (simTimer) { clearInterval(simTimer); simTimer = null; }
      simState.eventIdx = idx;
      simState.stepIdx = 0;
      renderSimulator();
    }
    function setSimArch(arch) {
      if (simTimer) { clearInterval(simTimer); simTimer = null; }
      simState.arch = arch;
      renderSimulator();
    }
    function goToSimStep(step) {
      if (simTimer) { clearInterval(simTimer); simTimer = null; }
      simState.stepIdx = step;
      renderSimulator();
    }
    function advanceSimStep() {
      if (simTimer) { clearInterval(simTimer); simTimer = null; }
      simState.stepIdx = (simState.stepIdx + 1) % 4;
      renderSimulator();
    }
    function runFullSimulation() {
      if (simTimer) { clearInterval(simTimer); simTimer = null; }
      simState.stepIdx = 0;
      renderSimulator();
      simTimer = setInterval(() => {
        if (simState.stepIdx < 3) {
          simState.stepIdx += 1;
          renderSimulator();
        } else {
          clearInterval(simTimer);
          simTimer = null;
        }
      }, 1150);
    }

    // =====================================================
    // 4. FILTRO DE LAS 10 TRAMPAS
    // =====================================================
    function filterTraps(cat, btnEl) {
      document.querySelectorAll('#trap-filters .q-pill').forEach(p => p.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');
      document.querySelectorAll('#traps-grid .trap-card').forEach(card => {
        const match = cat === 'all' || card.getAttribute('data-tcat') === cat;
        card.classList.toggle('hidden-item', !match);
        if (match) {
          card.classList.remove('soft-pop');
          void card.offsetWidth;
          card.classList.add('soft-pop');
        }
      });
    }

    // =====================================================
    // 5. BENTO GRID SPOTLIGHT
    // =====================================================
    const glossaryItems = [
      {
        chip: 'La pantalla maestra', chipClass: 'chip',
        title: 'Single Pane of Glass (Torre de Control)',
        subtitle: 'Tu ventana única en torre.animallium.pet',
        desc: 'Es una web aparte, elegante y rápida, construida sobre la plantilla oficial Nexora TanStack, donde ves en un solo vistazo cómo van tus negocios aliados, ventas, citas, atención en WhatsApp y gasto de robots sin abrir 6 pestañas distintas.',
        analogy: 'Como el vidrio gigante del puente de mando de una nave espacial: el capitán ve combustible, rumbo, escudos y pasajeros en una sola pantalla.',
        problem: 'Acaba con los puntos ciegos y evita sobrecargar el CRM de los vendedores con gráficas gerenciales.',
        tech: 'Plantilla oficial Nexora TanStack (React 19.2 + TanStack Table v9 + Tailwind v4 + @workspace/ui) en Docker (red root_default), Caddy HTTPS automático y SSO Supabase Auth (roles owner/admin).'
      },
      {
        chip: 'El gran libro de la verdad', chipClass: 'chip green',
        title: 'MDM · Registro Dorado (0 → 200+ Aliados)',
        subtitle: 'Esquema control_tower (business_entities + business_calendar_links)',
        desc: 'Guarda la ficha maestra única de cada veterinaria, petshop o peluquería aliada y la conecta con su trato B2B en el CRM, su tienda WCFM y todos sus calendarios de FluentBooking.',
        analogy: 'Como la cédula oficial de un colegio: garantiza que «Clínica Patitas», «Patitas Norte» y el calendario que creó el Admin sean siempre el mismo negocio.',
        problem: 'Resuelve de raíz el problema de calendarios creados por Admin vs. Vendor y evita duplicados al escalar a 200+ aliados.',
        tech: 'Tablas business_entities + business_calendar_links + auto-detección con fluent_booking/after_create_calendar y _fluent_booking_event_id.'
      },
      {
        chip: 'Sin fotocopias viejas', chipClass: 'chip neutral',
        title: 'Zero-Copy + Puente Seguro WordPress',
        subtitle: 'Leer el dato vivo en su casa original',
        desc: 'La Torre no duplica tus bases de datos cada noche. Lee Supabase con tu sesión, lee PostgreSQL del VPS por red interna y consulta WordPress por un puente SQL súper rápido con caché corta invalidada por webhooks.',
        analogy: 'En vez de sacarle fotocopias al cuaderno de tu amigo (que se quedan viejas), ambos miran el mismo cuaderno digital compartido al instante.',
        problem: 'Elimina las cifras contradictorias entre paneles y evita poner lenta la tienda pública animallium.pet.',
        tech: 'JWT Supabase → dashboard_overview · Red Docker root_default → Postgres VPS · Micro-plugin animallium-control-bridge con hash_equals() / HMAC.'
      },
      {
        chip: 'El árbitro del dinero', chipClass: 'chip orange',
        title: 'Capa Semántica COP / USD',
        subtitle: 'Una sola definición oficial de cada métrica',
        desc: 'Es el reglamento matemático escrito en código: convierte montos VARCHAR a decimales, resta reembolsos, excluye tienda propia del GMV de terceros y nunca mezcla pesos colombianos (COP) con dólares (USD) de IA.',
        analogy: 'Como el árbitro de un partido con el reglamento en la mano: nadie puede inventar goles ni sumar puntos de otro deporte.',
        problem: 'Garantiza que las ganancias de la Torre cuadren al 100% con WooCommerce, Dropi y tus facturas de IA.',
        tech: 'Fórmulas versionadas en backend: CAST(DECIMAL), filtro is_trashed=0 & is_refunded=0, total_commission real y TRM configurable.'
      },
      {
        chip: 'El botón que sí actúa', chipClass: 'chip purple',
        title: 'Efecto Dominó + Write-Back Gobernado',
        subtitle: 'De mirar problemas a resolverlos en 1 clic',
        desc: 'Cuando un evento en un sistema afecta a otro (ej. trato ganado sin tienda en 5 días, o aliado con >20% citas canceladas), la Torre avisa al instante y permite ejecutar la solución desde ahí mismo.',
        analogy: 'No es solo una alarma que suena: tiene un botón rojo seguro que manda el mensaje de ayuda sin que tengas que correr a otro edificio.',
        problem: 'Evita perder aliados nuevos o clientes por demoras invisibles entre departamentos.',
        tech: 'WhatsApp externo vía POST /api/v1/messages · Alertas internas vía Telegram + ampliación futura de notifications_type_check en WACRM.'
      },
      {
        chip: 'Paso final · Regla 02', chipClass: 'chip',
        title: 'BI Agéntico Gobernado',
        subtitle: 'Inteligencia Artificial que nunca adivina cifras',
        desc: 'Solo cuando el Registro Dorado y la Capa Semántica ya estén cerrados, encendemos un copiloto de IA al que le preguntas en español normal («¿qué ciudad tiene más cancelaciones?») y responde usando solo herramientas certificadas.',
        analogy: 'Como un asistente superinteligente que solo puede usar tu calculadora oficial, así que jamás se inventa un resultado.',
        problem: 'Cero alucinaciones de IA y trazabilidad completa de cada número que te muestra.',
        tech: 'Function Calling estricto sobre endpoints de la Capa Semántica (nunca SQL libre sin gobernanza).'
      }
    ];

    function selectGlossaryCard(idx) {
      const item = glossaryItems[idx];
      if (!item) return;
      for (let i = 0; i < 6; i++) {
        const card = document.getElementById('bcard-' + i);
        if (card) card.classList.toggle('selected', i === idx);
      }
      const spot = document.getElementById('glossary-spotlight');
      if (spot) {
        spot.classList.remove('soft-pop');
        void spot.offsetWidth;
        spot.classList.add('soft-pop');
      }
      const chip = document.getElementById('spot-chip');
      chip.textContent = item.chip;
      chip.className = item.chipClass;
      document.getElementById('spot-title').textContent = item.title;
      document.getElementById('spot-subtitle').textContent = item.subtitle;
      document.getElementById('spot-desc').textContent = item.desc;
      document.getElementById('spot-analogy').textContent = item.analogy;
      document.getElementById('spot-problem').textContent = item.problem;
      document.getElementById('spot-tech').textContent = item.tech;
    }

    function filterGlossary(cat, btnEl) {
      document.querySelectorAll('#glossary-filters .q-pill').forEach(p => p.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');
      let first = -1;
      for (let i = 0; i < 6; i++) {
        const card = document.getElementById('bcard-' + i);
        if (!card) continue;
        const match = cat === 'all' || card.getAttribute('data-cat') === cat;
        card.classList.toggle('dimmed', !match);
        if (match && first === -1) first = i;
      }
      if (first !== -1) selectGlossaryCard(first);
    }

    // =====================================================
    // 6. ROADMAP INTERACTIVO POR FASES
    // =====================================================
    const phasesData = [
      {
        chip: 'Fase 0 · 1–2 días · Limpieza Quirúrgica + Chequeo VPS',
        chipClass: 'chip',
        title: 'Retirar Centro de Mando (Conservando Nodos IA) + Chequeo VPS',
        kid: 'Sacamos solo el Centro de Mando del menú del CRM, pero dejamos el Monitor Visual de Nodos IA porque gobierna tus chats de WhatsApp. Además hacemos la revisión en vivo del VPS y Hostinger.',
        steps: [
          'Eliminar /centro-mando y /vista/centro-mando; conservar /nodos-ia y /vista/nodos-ia bajo bandera modular para owner/admin.',
          'Recortar el proxy /api/animallium-proxy estrictamente a dashboard y api/dashboard/ (0 rutas de Dropi, propuestas o pedidos).',
          'Limpiar sidebar.tsx (dejar Monitor Nodos IA limpio bajo Agentes de IA), header.tsx, middleware.ts y borrar centroMando en los 4 idiomas (en, es, ko, pt).',
          'Auditar en vivo /root/Caddyfile, RAM/Docker del VPS 62.72.24.151, el vendor_id de tienda propia y el plugin de /dropi/orders en Hostinger.'
        ],
        outcome: 'CRM limpio en crm.animallium.pet con Monitor Nodos IA acotado, notificaciones read-delete y logo/nombre intactos, más diagnóstico en vivo del VPS listo.',
        qa: 'npm run typecheck + npm test (todos en verde, incluyendo middleware, next-config e i18n) + npm run build + prueba visual en vivo.'
      },
      {
        chip: 'Fase 1 · 2–4 días · Independencia + Blindaje',
        chipClass: 'chip purple',
        title: 'Independizar el Centro de Mando en mando.animallium.pet',
        kid: 'El taller de operaciones y los robots ganan su propia casa con puerta segura y candados nuevos. Además reparamos dos cables viejos en WordPress para dejar todo impecable.',
        steps: [
          'Revisar /root/Caddyfile y memoria RAM en el VPS 62.72.24.151; publicar mando.animallium.pet con redirect 301 desde n8n.',
          'Cambiar cookie en texto plano por sesión firmada HMAC/JWT, eliminar ?token=, cerrar CORS abierto (*) y firmar webhooks.',
          'Corregir URLs en proposals.py, Portal y Centro_Mando_Animallium.html; renombrar Pestaña 5 a «Logística & Fulfillment Dropi».',
          'Corregir en WordPress el link .com de soap_created y el bug author_id → user_id en animallium-fluent-booking-link.php.'
        ],
        outcome: 'Centro de Mando y Monitor Nodos IA operando 100% independientes y blindados sin necesitar el proxy del CRM.',
        qa: 'Login seguro probado en mando.animallium.pet, verificación de propuestas públicas, pruebas CORS y smoke test de citas.'
      },
      {
        chip: 'Fase 2A · Semanas 2–3 · Regla 03 (Vertical Slice #1)',
        chipClass: 'chip green',
        title: 'Torre de Control MVP: Red de Aliados (0 → 200+)',
        kid: 'Seguimos la Regla 03: empezamos por una sola misión estrella — ver crecer y rendir a tus negocios aliados uniendo CRM B2B + WCFM + FluentBooking sobre la plantilla oficial confirmada: Nexora TanStack.',
        steps: [
          'Desempaquetar y configurar Nexora TanStack (React 19.2 + TanStack Table v9 + Tailwind v4 + @workspace/ui) en d:\\ESCRITORIO\\animallium-control-tower para torre.animallium.pet.',
          'Mapear módulos listos: Companies ➔ Directorio Maestro MDM, Calendar ➔ Citas FluentBooking, Analytics ➔ Resumen Financiero COP/USD.',
          'Activar SSO con Supabase Auth (solo roles owner/admin) y crear el esquema MDM control_tower en PostgreSQL del VPS.',
          'Desplegar micro-plugin animallium-control-bridge en WordPress con 4 endpoints SQL agregados + webhooks reales verificados.',
          'Entregar las 2 vistas clave: (1) Resumen Ejecutivo COP/USD y (2) Directorio Maestro de Aliados con tabla TanStack virtualizada y vinculación de calendarios en 1 clic.'
        ],
        outcome: 'Desde el negocio #1 ya tienes tu mirador oficial ultra-rápido, con diseño idéntico en calidad a WACRM, cifras exactas y vinculación de calendarios en 1 clic.',
        qa: 'Prueba de carga sintética con 200 negocios y 2.000 citas/órdenes (<400ms) + cuadre financiero exacto contra WCFM.'
      },
      {
        chip: 'Fase 2B · Semanas 4–5 · Visión 360° Completa',
        chipClass: 'chip',
        title: 'Expansión Transversal de la Torre',
        kid: 'Con el primer piso probado y firme, conectamos las demás pantallas para ver citas, WhatsApp, Dropi y consumo de IA desde el mismo cristal.',
        steps: [
          'Monitor de Servicios y Citas (FluentBooking): agenda multi-negocio, cancelaciones/no-show por ciudad y base lista para Clínica SOAP (Plan 3).',
          'Pulso Comercial WACRM (Zero-Copy): llama a dashboard_overview con tu JWT Supabase + enlaces directos al CRM.',
          'Pulso Operativo, Dropshipping y Costo IA: lectura interna de orders_fulfillment, auditorías Dropi y gasto USD de ai_token_usage.'
        ],
        outcome: 'Control global de toda la operación de Animallium en un solo lugar, sin duplicar bases de datos.',
        qa: 'Verificación Zero-Copy con sesión real de usuario, tiempos de carga y enlaces profundos hacia CRM y Centro de Mando.'
      },
      {
        chip: 'Fase 3 · Semanas 6–7 · Torre Activa',
        chipClass: 'chip orange',
        title: 'Detección de Efecto Dominó + Write-Back Gobernado',
        kid: 'La Torre deja de ser solo una tele para mirar: ahora detecta problemas entre edificios y te ofrece botones seguros para resolverlos en segundos.',
        steps: [
          'Reglas automáticas: Deal B2B ganado sin tienda >5 días, calendario nuevo sin asignar, aliado con cancelaciones >20% y pedido Dropi sin guía >24h.',
          'Write-Back externo a clientes/aliados vía POST /api/v1/messages en WACRM (plantillas oficiales).',
          'Write-Back interno por Telegram + migración mínima en WACRM ampliando notifications_type_check para avisar en la campana del CRM.'
        ],
        outcome: 'Rescatas aliados y pedidos en riesgo antes de que el cliente reclame.',
        qa: 'Pruebas de disparo de cada regla sin falsos positivos y control de permisos solo para roles autorizados.'
      },
      {
        chip: 'Fase 4 · Semanas 8+ · Regla 02',
        chipClass: 'chip purple',
        title: 'BI Agéntico Gobernado (Copiloto sin alucinaciones)',
        kid: 'Ahora sí, con todas las reglas claras y los datos ordenados, sumamos un copiloto de IA al que le preguntas como si fuera un amigo analista.',
        steps: [
          'Conectar un asistente conversacional dentro de la Torre exclusivamente a herramientas certificadas de la Capa Semántica.',
          'Mostrar siempre de qué sistema y fórmula salió cada cifra (trazabilidad total).',
          'Bloquear SQL libre no auditado para garantizar 0% números inventados.'
        ],
        outcome: 'Tomas decisiones estratégicas preguntando en español natural con respaldo matemático exacto.',
        qa: 'Batería de preguntas de negocio comparadas contra consultas exactas de la Capa Semántica.'
      }
    ];

    function selectPhase(idx) {
      const p = phasesData[idx];
      if (!p) return;
      document.querySelectorAll('#phase-tabs .phase-tab').forEach((tab, i) => {
        tab.classList.toggle('active', i === idx);
      });
      const card = document.getElementById('phase-detail-card');
      if (card) {
        card.classList.remove('soft-pop');
        void card.offsetWidth;
        card.classList.add('soft-pop');
      }
      const chip = document.getElementById('ph-chip');
      chip.textContent = p.chip;
      chip.className = p.chipClass;
      document.getElementById('ph-title').textContent = p.title;
      document.getElementById('ph-kid').textContent = p.kid;
      document.getElementById('ph-outcome').textContent = p.outcome;
      document.getElementById('ph-qa').textContent = p.qa;

      const ul = document.getElementById('ph-steps');
      ul.innerHTML = '';
      p.steps.forEach(st => {
        const li = document.createElement('li');
        li.innerHTML = `<span class="dot-mark dot-blue"></span><span>${st}</span>`;
        ul.appendChild(li);
      });
    }

    // =====================================================
    // 7. TARJETAS DE DECISIÓN INTERACTIVAS
    // =====================================================
    function pickChoice(btn) {
      const group = btn.parentElement;
      if (!group) return;
      group.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('picked'));
      btn.classList.add('picked');
    }

    // =====================================================
    // 8. ANIMACIONES DE SCROLL, CONTADORES Y BARRAS
    // =====================================================
    function animateCounter(el) {
      const target = parseInt(el.getAttribute('data-count'), 10);
      if (isNaN(target)) return;
      const prefix = el.getAttribute('data-prefix') || '';
      const suffix = el.getAttribute('data-suffix') || '';
      if (target === 0) {
        el.textContent = prefix + '0' + suffix;
        return;
      }
      const duration = 900;
      const start = performance.now();
      function step(now) {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const val = Math.round(eased * target);
        el.textContent = prefix + val + suffix;
        if (progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }

    document.addEventListener('DOMContentLoaded', function () {
      selectSystem(0);
      selectQuestion(0);
      renderSimulator();
      selectGlossaryCard(0);
      selectPhase(0);

      // Teclado accesible para estaciones del simulador
      for (let i = 0; i < 4; i++) {
        const node = document.getElementById('sim-node-' + i);
        if (node) {
          node.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ') {
              e.preventDefault();
              goToSimStep(i);
            }
          });
        }
      }

      // Barra de progreso de lectura + sombra en header
      window.addEventListener('scroll', function () {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0;
        const bar = document.getElementById('scroll-progress');
        if (bar) bar.style.width = pct + '%';
        const hdr = document.getElementById('top-header');
        if (hdr) hdr.classList.toggle('scrolled', scrollTop > 16);
      }, { passive: true });

      // IntersectionObserver para reveals, contadores y barras
      const reveals = document.querySelectorAll('.reveal');
      if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver(function (entries, observer) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible');
              // Animar contadores si los contiene
              entry.target.querySelectorAll('[data-count]').forEach(animateCounter);
              // Animar barras si es el gráfico de madurez
              entry.target.querySelectorAll('.bar-fill[data-width]').forEach(bar => {
                bar.style.width = bar.getAttribute('data-width');
              });
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.12 });
        reveals.forEach(el => io.observe(el));
      } else {
        reveals.forEach(el => el.classList.add('visible'));
        document.querySelectorAll('.bar-fill[data-width]').forEach(bar => {
          bar.style.width = bar.getAttribute('data-width');
        });
      }
    });
  </script>
</body>
</html>
'''

def main():
    desktop_path = r"C:\Users\Giovanni Anchique\OneDrive\Escritorio\Plan_Torre_de_Control_Animallium_Apple.html"
    workspace_path = r"d:\ESCRITORIO\wacrm\Plan_Torre_de_Control_Animallium_Apple.html"

    with open(desktop_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"[OK] Creado en Escritorio: {desktop_path}")

    with open(workspace_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"[OK] Creado en Workspace: {workspace_path}")

if __name__ == "__main__":
    main()
