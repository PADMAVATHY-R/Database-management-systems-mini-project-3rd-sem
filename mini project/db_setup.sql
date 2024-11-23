-- Create Database
CREATE DATABASE ApartmentManagement;

USE ApartmentManagement;

-- Create Tables
CREATE TABLE Residents (
    ResidentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ContactNo VARCHAR(15) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    ApartmentID INT,
    Role ENUM('Owner', 'Tenant') NOT NULL,
    FOREIGN KEY (ApartmentID) REFERENCES Apartments(ApartmentID)
);

CREATE TABLE Apartments (
    ApartmentID INT AUTO_INCREMENT PRIMARY KEY,
    ApartmentNo VARCHAR(10) UNIQUE NOT NULL,
    Type ENUM('1BHK', '2BHK', '3BHK') NOT NULL,
    Rent DECIMAL(10, 2),
    Size INT NOT NULL
);

CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    ResidentID INT,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentType ENUM('Rent', 'Maintenance') NOT NULL,
    FOREIGN KEY (ResidentID) REFERENCES Residents(ResidentID)
);

CREATE TABLE Complaints (
    ComplaintID INT AUTO_INCREMENT PRIMARY KEY,
    ResidentID INT,
    Description TEXT NOT NULL,
    Status ENUM('Pending', 'Resolved') DEFAULT 'Pending',
    SubmissionDate DATE NOT NULL,
    FOREIGN KEY (ResidentID) REFERENCES Residents(ResidentID)
);

CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Role VARCHAR(50) NOT NULL,
    ContactNo VARCHAR(15) NOT NULL
);
