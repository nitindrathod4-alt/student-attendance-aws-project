CREATE DATABASE IF NOT EXISTS studentdb;
USE studentdb;

CREATE TABLE IF NOT EXISTS students(
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(100) NOT NULL,
 roll_no VARCHAR(30) NOT NULL UNIQUE,
 attendance DECIMAL(5,2) DEFAULT 0,
 result VARCHAR(30) DEFAULT 'Pending'
);

INSERT INTO students(name,roll_no,attendance,result) VALUES
('Rahul Patil','STU001',88.50,'Pass'),
('Amit Shinde','STU002',76.00,'Pass'),
('Sneha More','STU003',92.00,'Pass'),
('Pooja Jadhav','STU004',64.50,'Pass');

SELECT * FROM students;
