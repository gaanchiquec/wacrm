-- ============================================================
-- Migration 061: Add entity_type to pipelines (deal vs client)
-- Allows B2C Sales pipelines to dynamically adapt labels to
-- "cliente" while B2B Aliados pipelines keep "negocio".
-- ============================================================

ALTER TABLE pipelines
  ADD COLUMN IF NOT EXISTS entity_type TEXT NOT NULL DEFAULT 'deal'
  CHECK (entity_type IN ('deal', 'client'));

-- Set Sales Pipeline (B2C) to entity_type = 'client'
UPDATE pipelines
SET entity_type = 'client'
WHERE id = '9205fb84-71b6-4db6-87f9-5702bc189cae'
   OR name ILIKE '%ventas%';
