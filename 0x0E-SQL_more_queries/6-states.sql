-- creates a database called hbtn_0d_usa and a table called states within said DB

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL)
