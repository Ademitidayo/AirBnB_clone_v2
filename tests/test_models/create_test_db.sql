-- create_test_db.sql
-- Create a specific database for testing
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Grant all privileges to the test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd123!';

-- Ensure changes take effect
FLUSH PRIVILEGES;
