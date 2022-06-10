-- Create database
CREATE DATABASE excercisies IF NOT EXISTS;

-- Create table statement
CREATE TABLE "user"(
  id SERIAL PRIMARY KEY,
  name VARCHAR (100)
  email VARCHAR (255),
  password TEXT,
  age INT
);

-- Create table with foreign key and setted to delete on cascade 

CREATE TABLE post (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100)
  body VARCHAR(255)
  user_id INT,
  CONSTRAINT fk_user  FOREIGN KEY(user_id) REFERENCES "user"(id)
  ON DELETE CASCADE
);

-- Insert into table statement
INSERT INTO "user"(
  name,
  email,
  age,
  password
) VALUES (
  "Atzin Herrera",
  "atzin@fake.com",
  23,
  "afakepassword"
);

INSERT INTO post(
  title,
  body,
  user_id
) VALUES (
  "A comment",
  "This is a random comment",
  1
);

-- Update data from a table
UPDATE "user" SET age = 24 WHERE id = 1;

-- Basic select from table statement
SELECT * FROM "user";

-- Select just the desired cols from a table
SELECT id, name, email FROM "user" WHERE id;

-- Select and joining tables
SELECT * FROM "user" JOIN post ON post.user_id = "user".id WHERE id = 1;

-- Delete table all data from a table
DELETE FROM "user";

-- Delete a record from a table
DELETE FROM "user" WHERE id = 1;

-- Drop database
DROP DATABASE excercisies;