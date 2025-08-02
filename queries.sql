-- database query
CREATE DATABASE pass_generator_db;

-- table query
CREATE TABLE password_table (
  username VARCHAR(20) PRIMARY KEY,
  user_login_hashed_password TEXT NOT NULL,
  passwords TEXT[]
); 