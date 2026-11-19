-- ============================================================
-- Migration 060: Broaden notifications to support CRM events
-- Supports: conversation_assigned, new_conversation, new_message,
-- deal_created, ai_handoff
-- ============================================================

-- 1. Relax or expand check constraint on notifications.type
ALTER TABLE notifications DROP CONSTRAINT IF EXISTS notifications_type_check;
ALTER TABLE notifications ADD CONSTRAINT notifications_type_check CHECK (
  type IN ('conversation_assigned', 'new_conversation', 'new_message', 'deal_created', 'ai_handoff')
);

-- 2. Add deal_id column to notifications
ALTER TABLE notifications ADD COLUMN IF NOT EXISTS deal_id UUID REFERENCES deals(id) ON DELETE CASCADE;

-- 3. Trigger on new conversations to alert account owner
CREATE OR REPLACE FUNCTION notify_new_conversation()
RETURNS TRIGGER AS $$
DECLARE
  v_owner UUID;
  v_contact_name TEXT;
BEGIN
  SELECT owner_user_id INTO v_owner FROM accounts WHERE id = NEW.account_id;
  SELECT name INTO v_contact_name FROM contacts WHERE id = NEW.contact_id;
  
  IF v_owner IS NOT NULL THEN
    INSERT INTO notifications (
      account_id,
      user_id,
      type,
      conversation_id,
      contact_id,
      title,
      body
    ) VALUES (
      NEW.account_id,
      v_owner,
      'new_conversation',
      NEW.id,
      NEW.contact_id,
      'Nueva conversación iniciada',
      COALESCE('Cliente: ' || v_contact_name, 'Nueva conversación recibida en WhatsApp')
    );
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

DROP TRIGGER IF EXISTS trg_notify_new_conversation ON conversations;
CREATE TRIGGER trg_notify_new_conversation
AFTER INSERT ON conversations
FOR EACH ROW EXECUTE FUNCTION notify_new_conversation();

-- 4. Trigger on customer messages to alert assigned agent or account owner
CREATE OR REPLACE FUNCTION notify_inbound_message()
RETURNS TRIGGER AS $$
DECLARE
  v_recipient UUID;
  v_conv RECORD;
  v_contact_name TEXT;
BEGIN
  IF NEW.sender_type <> 'customer' THEN
    RETURN NEW;
  END IF;

  SELECT c.id, c.account_id, c.assigned_agent_id, c.contact_id
  INTO v_conv
  FROM conversations c
  WHERE c.id = NEW.conversation_id;

  IF v_conv.id IS NULL THEN
    RETURN NEW;
  END IF;

  v_recipient := v_conv.assigned_agent_id;
  IF v_recipient IS NULL THEN
    SELECT owner_user_id INTO v_recipient FROM accounts WHERE id = v_conv.account_id;
  END IF;

  SELECT name INTO v_contact_name FROM contacts WHERE id = v_conv.contact_id;

  IF v_recipient IS NOT NULL THEN
    INSERT INTO notifications (
      account_id,
      user_id,
      type,
      conversation_id,
      contact_id,
      title,
      body
    ) VALUES (
      v_conv.account_id,
      v_recipient,
      'new_message',
      NEW.conversation_id,
      v_conv.contact_id,
      'Nuevo mensaje de ' || COALESCE(v_contact_name, 'Cliente'),
      SUBSTRING(COALESCE(NEW.content_text, 'Mensaje recibido en WhatsApp'), 1, 120)
    );
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

DROP TRIGGER IF EXISTS trg_notify_inbound_message ON messages;
CREATE TRIGGER trg_notify_inbound_message
AFTER INSERT ON messages
FOR EACH ROW EXECUTE FUNCTION notify_inbound_message();

-- 5. Trigger on new deals to alert account owner (with deal_id)
CREATE OR REPLACE FUNCTION notify_new_deal()
RETURNS TRIGGER AS $$
DECLARE
  v_recipient UUID;
BEGIN
  v_recipient := COALESCE(NEW.assigned_to, NEW.user_id);
  IF v_recipient IS NULL THEN
    SELECT owner_user_id INTO v_recipient FROM accounts WHERE id = NEW.account_id;
  END IF;

  IF v_recipient IS NOT NULL THEN
    INSERT INTO notifications (
      account_id,
      user_id,
      type,
      conversation_id,
      contact_id,
      deal_id,
      title,
      body
    ) VALUES (
      NEW.account_id,
      v_recipient,
      'deal_created',
      NEW.conversation_id,
      NEW.contact_id,
      NEW.id,
      'Nuevo negocio en pipeline',
      SUBSTRING(COALESCE(NEW.title, 'Negocio creado en CRM'), 1, 140)
    );
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

DROP TRIGGER IF EXISTS trg_notify_new_deal ON deals;
CREATE TRIGGER trg_notify_new_deal
AFTER INSERT ON deals
FOR EACH ROW EXECUTE FUNCTION notify_new_deal();
