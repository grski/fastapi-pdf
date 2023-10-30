-- :name post_invitation_key :insert
INSERT INTO invitation_keys (uuid, user_uuid, user_email, is_used, created_at, updated_at)
VALUES (:uuid, :user_uuid, :user_email, :is_used, NOW(), NOW());