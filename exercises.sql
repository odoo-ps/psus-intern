-- KEYWORDS = uppercase
-- user-made info = lowercase, snake_case

CREATE TABLE profile(
    id SERIAL PRIMARY KEY, -- INT -> each entry, id++
    -- PRIMARY KEY unique identifier for each entry row
    name VARCHAR(100), -- VARCHAR = TEXT with size constraint
    email VARCHAR(255),
    password TEXT,
    age INT
);