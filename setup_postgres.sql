-- PostgreSQL Setup Script for Result Management App
-- This script creates the required user and database

-- Create user 'postgres' with password 'password'
CREATE USER postgres WITH PASSWORD 'password';

-- Create database 'result_management' owned by 'postgres'
CREATE DATABASE result_management OWNER postgres;

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE result_management TO postgres;

-- Connect to the new database
\c result_management;

-- Grant all privileges on all tables to the user
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO postgres;

-- Exit
\q 