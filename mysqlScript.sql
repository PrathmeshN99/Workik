CREATE DATABASE discord_bot_db;
USE discord_bot_db;

CREATE TABLE auth_tokens (
    server_id BIGINT PRIMARY KEY,
    token VARCHAR(255) NOT NULL
);


INSERT INTO auth_tokens (server_id, token) VALUES (1184427500307234887, 'MTE4NDQyNTEyODAxNzI4NTE3MQ.GyYpQw.ZM2zEfMLt1DsMKh5Lxs_benl2UoaYlohWyhuOY');
