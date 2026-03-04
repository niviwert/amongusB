--create schema bamba;

--CREATE EXTENSION IF NOT EXISTS "pgcrypto";


--create table bamba.deployments (
--    id UUID DEFAULT uuidv7() PRIMARY KEY,
--    db_name VARCHAR NOT null,
--    status VARCHAR NOT null,
--    username VARCHAR NOT null,
--    creation_time timestamp without time zone not null default (current_timestamp at time zone 'utc')
--);