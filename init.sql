CREATE DATABASE IF NOT EXISTS test_db;

USE test_db;

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content VARCHAR(255) NOT NULL
);

INSERT INTO messages (content) VALUES ('Hello, World!');
INSERT INTO messages (content) VALUES ('This is to test my knowledge');
