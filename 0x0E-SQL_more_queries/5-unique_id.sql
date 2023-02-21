-- creates a table called unique_id with (id INT) and (name VARCHAR)

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256))
