CREATE DATABASE WarehouseDB;
USE WarehouseDB;

CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    name VARCHAR(50),
    category VARCHAR(50),
    price INT
);

CREATE TABLE Warehouse (
    warehouse_id INT PRIMARY KEY,
    location VARCHAR(50),
    capacity INT
);

CREATE TABLE Inventory (
    inventory_id INT PRIMARY KEY,
    product_id INT,
    warehouse_id INT,
    quantity INT,
    last_updated TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id)
);

CREATE TABLE Supplier (
    supplier_id INT PRIMARY KEY,
    name VARCHAR(50),
    contact VARCHAR(15)
);

CREATE TABLE Incoming_Stock (
    entry_id INT PRIMARY KEY,
    supplier_id INT,
    product_id INT,
    quantity INT,
    date DATE,
    FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

CREATE TABLE Outgoing_Stock (
    dispatch_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    destination VARCHAR(50),
    date DATE,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    status VARCHAR(20),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

INSERT INTO Product VALUES
(1, 'Laptop', 'Electronics', 60000),
(2, 'Phone', 'Electronics', 25000),
(3, 'Tablet', 'Electronics', 30000),
(4, 'Headphones', 'Accessories', 2000),
(5, 'Keyboard', 'Accessories', 1500),
(6, 'Mouse', 'Accessories', 800),
(7, 'Monitor', 'Electronics', 12000);

INSERT INTO Warehouse VALUES
(1, 'Bangalore', 1000),
(2, 'Chennai', 800),
(3, 'Hyderabad', 900),
(4, 'Mumbai', 1200),
(5, 'Delhi', 1100),
(6, 'Pune', 700),
(7, 'Kolkata', 850);

INSERT INTO Supplier VALUES
(1, 'ABC Suppliers', '9876543210'),
(2, 'XYZ Traders', '9123456780'),
(3, 'Global Tech', '9012345678'),
(4, 'Prime Supplies', '9988776655'),
(5, 'Fast Delivery Co', '8899776655'),
(6, 'TechSource', '7766554433'),
(7, 'SupplyHub', '6655443322');

INSERT INTO Inventory VALUES
(1, 1, 1, 50, NOW()),
(2, 2, 2, 40, NOW()),
(3, 3, 3, 30, NOW()),
(4, 4, 4, 100, NOW()),
(5, 5, 5, 80, NOW()),
(6, 6, 6, 60, NOW()),
(7, 7, 7, 20, NOW());

INSERT INTO Incoming_Stock VALUES
(1, 1, 1, 20, '2026-04-01'),
(2, 2, 2, 15, '2026-04-02'),
(3, 3, 3, 10, '2026-04-03'),
(4, 4, 4, 50, '2026-04-04'),
(5, 5, 5, 40, '2026-04-05'),
(6, 6, 6, 30, '2026-04-06'),
(7, 7, 7, 25, '2026-04-07');

INSERT INTO Outgoing_Stock VALUES
(1, 1, 10, 'Hyderabad', '2026-04-08'),
(2, 2, 5, 'Delhi', '2026-04-09'),
(3, 3, 7, 'Mumbai', '2026-04-10'),
(4, 4, 20, 'Chennai', '2026-04-11'),
(5, 5, 15, 'Pune', '2026-04-12'),
(6, 6, 10, 'Kolkata', '2026-04-13'),
(7, 7, 8, 'Bangalore', '2026-04-14');

INSERT INTO Orders VALUES
(1, 1, 2, 'Pending'),
(2, 2, 1, 'Completed'),
(3, 3, 3, 'Pending'),
(4, 4, 5, 'Shipped'),
(5, 5, 4, 'Completed'),
(6, 6, 6, 'Pending'),
(7, 7, 2, 'Shipped');

SELECT * FROM Product;

SELECT * FROM Orders;

SELECT p.name, w.location, i.quantity
FROM Inventory i
JOIN Product p ON i.product_id = p.product_id
JOIN Warehouse w ON i.warehouse_id = w.warehouse_id;

SELECT p.name, SUM(i.quantity) AS total_stock
FROM Inventory i
JOIN Product p ON i.product_id = p.product_id
GROUP BY p.name;

SELECT s.name AS supplier, p.name AS product, i.quantity, i.date
FROM Incoming_Stock i
JOIN Supplier s ON i.supplier_id = s.supplier_id
JOIN Product p ON i.product_id = p.product_id;

SELECT o.order_id, p.name, o.quantity, o.status
FROM Orders o
JOIN Product p ON o.product_id = p.product_id;

ALTER TABLE Incoming_Stock
ADD warehouse_id INT,
ADD FOREIGN KEY (warehouse_id)
REFERENCES Warehouse(warehouse_id);

ALTER TABLE Outgoing_Stock
ADD warehouse_id INT,
ADD FOREIGN KEY (warehouse_id)
REFERENCES Warehouse(warehouse_id);

DELIMITER //

CREATE TRIGGER trg_incoming_stock
AFTER INSERT ON Incoming_Stock
FOR EACH ROW
BEGIN

    UPDATE Inventory
    SET quantity = quantity + NEW.quantity,
        last_updated = NOW()
    WHERE product_id = NEW.product_id
    AND warehouse_id = NEW.warehouse_id;

END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER trg_outgoing_stock
AFTER INSERT ON Outgoing_Stock
FOR EACH ROW
BEGIN

    UPDATE Inventory
    SET quantity = quantity - NEW.quantity,
        last_updated = NOW()
    WHERE product_id = NEW.product_id
    AND warehouse_id = NEW.warehouse_id;

END //

DELIMITER ;

INSERT INTO Incoming_Stock
VALUES (8, 1, 1, 10, '2026-05-01', 1);

SELECT * FROM Inventory
WHERE product_id = 1;

drop database WarehouseDB;
