-- migrate:up
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    is_confirmed BOOLEAN,
    uuid UUID NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE invitation_keys (
    id SERIAL PRIMARY KEY,
    uuid UUID NOT NULL,
    user_uuid UUID NOT NULL,
    is_used BOOLEAN NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);




-- migrate:down
DROP TABLE IF EXISTS invitation_keys;
DROP TABLE IF EXISTS users;
