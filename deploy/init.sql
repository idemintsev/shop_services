-- Create database
CREATE DATABASE IF NOT EXISTS shop_services;

-- Create warehouses table
CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    name STRING(128) NOT NULL,
    address STRING NOT NULL,
    latitude FLOAT8 NOT NULL,
    longitude FLOAT8 NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL
);

-- Create index
CREATE INDEX idx_warehouses_name ON warehouses (name);

-- Create extensions
CREATE EXTENSION IF NOT EXISTS cube;
CREATE EXTENSION IF NOT EXISTS earthdistance;


--
--select name, earth_distance(
--  ll_to_earth(latitude, longitude),
--  ll_to_earth(29.923880554767383, -81.29407971493576)
--) as distance
--from addresses
--order by distance;