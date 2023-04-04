CREATE DATABASE IF NOT EXISTS Quiz;
USE Quiz;
CREATE TABLE Regisztralt(ID int auto_increment,fullname varchar(255),username varchar(255) unique,password varchar(255),email varchar(255),dateOfBirth date,primary key(ID))