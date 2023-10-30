-- :name get_user_login_by_email :one
SELECT name, email, is_confirmed, uuid FROM users WHERE email = :email