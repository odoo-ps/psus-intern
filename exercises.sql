-- KEYWORDS = uppercase
-- user-made info = lowercase, snake_case
-- if KEYWORD, use "" to denote different

-- create new table "name" with given column names and value types
CREATE TABLE "user" (
    id SERIAL PRIMARY KEY, -- INT -> each entry, id++
    -- PRIMARY KEY -> unique identifier for each entry row
    name VARCHAR(100), -- VARCHAR -> TEXT with size constraint
    email VARCHAR(255),
    password TEXT,
    age INT
);

-- put information into table "user"
INSERT INTO "user" (email, name, age, password) VALUES ('alac@odoo.com', 'Alexa', 25, '1501');
INSERT INTO "user" (email, name, age, password) VALUES ('wawa@odoo.com', 'Wawa', 5, 'wowo');
-- ' denotes values/data, " denotes metadata? (in syntax)

-- select information
-- * denotes all columns, not rows
-- WHERE keyword is condition statement
SELECT * FROM "user" WHERE name = 'alac';

-- update information
UPDATE "user" SET age = 26 WHERE id = 1;
SELECT age FROM "user" WHERE id = 1;

-- remove information
DELETE FROM "user" WHERE id = 2;

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    content TEXT,
    user_id INT,
    CONSTRAINT fk_user -- specifies a constraint on user_id
        FOREIGN KEY(user_id) -- a foreign key (nonlocal id)
            REFERENCES "user"(id) -- that points to id from table user
);