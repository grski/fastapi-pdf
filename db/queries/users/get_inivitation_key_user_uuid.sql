-- :name get_invitation_key_user_uuid :one
SELECT uuid, user_uuid, is_used, user_email FROM invitation_keys WHERE user_uuid = :user_uuid