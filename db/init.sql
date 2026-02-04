CREATE DATABASE IF NOT EXISTS appdb;
USE appdb;

CREATE TABLE IF NOT EXISTS counter (
  id INT PRIMARY KEY,
  value INT
);

INSERT IGNORE INTO counter (id, value) VALUES (1, 0);

CREATE TABLE IF NOT EXISTS access_log (
  id INT AUTO_INCREMENT PRIMARY KEY,
  access_time DATETIME,
  client_ip VARCHAR(50),
  server_ip VARCHAR(50)
);
