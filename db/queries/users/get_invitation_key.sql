-- :name get_invitation_key :one
SELECT uuid, user_uuid, is_used, user_email FROM invitation_keys WHERE uuid = :uuid