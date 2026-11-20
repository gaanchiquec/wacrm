-- ============================================================
-- Migration 062: Support Control Tower operational alerts in notifications
-- Adds 'control_tower_alert' to notifications_type_check while preserving
-- all existing CRM notification types and DELETE /api/notifications semantics.
-- ============================================================

ALTER TABLE notifications DROP CONSTRAINT IF EXISTS notifications_type_check;
ALTER TABLE notifications ADD CONSTRAINT notifications_type_check CHECK (
  type IN (
    'conversation_assigned',
    'new_conversation',
    'new_message',
    'deal_created',
    'ai_handoff',
    'control_tower_alert'
  )
);
