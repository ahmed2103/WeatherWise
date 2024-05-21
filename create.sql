CREATE DATABASE IF NOT EXISTS CREATE DATABASE WeatherWise;
CREATE USER IF NOT EXISTS 'weather_dev'@'localhost' IDENTIFIED BY 'weather_dev_pass';
GRANT ALL PRIVILEGES ON WeatherWise.* TO 'weather_dev'@'localhost';
GRANT SELECT ON `Performance_schema`.* TO 'weather_dev'@'localhost';
FLUSH PRIVILEGES;