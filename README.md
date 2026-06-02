# 🏭 Warehouse Automation & Tracking System

A modern desktop-based Database Management System (DBMS) project developed using Python, CustomTkinter, and MySQL. The system enables warehouse administrators to efficiently manage products, suppliers, inventory, incoming stock, outgoing stock, and warehouse utilization through an interactive graphical user interface.

---

## 📌 Project Overview

The Warehouse Automation & Tracking System is designed to digitize and simplify warehouse operations. It provides a centralized platform for maintaining product information, supplier details, inventory records, stock movement tracking, and warehouse capacity monitoring while ensuring data integrity through a MySQL database.

---

## 🎯 SDG Goal

### SDG 9 – Industry, Innovation and Infrastructure

This project contributes to:

* 🏭 Efficient warehouse operations
* 📦 Smart inventory management
* 🚚 Improved supply chain tracking
* 📊 Data-driven warehouse decision making
* ⚙️ Automation of stock management processes

---

## 🛠️ Technology Stack

| Layer                 | Technology            |
| --------------------- | --------------------- |
| Frontend              | Python CustomTkinter  |
| GUI Components        | Tkinter (TTK Widgets) |
| Backend               | Python                |
| Database              | MySQL                 |
| Database Connectivity | MySQL Connector       |
| IDE                   | MAC Terminal          |

---

## ✨ Features

### 📦 Product Management

* Add new products
* View product details
* Manage product categories
* Track product pricing

### 🚚 Supplier Management

* Add supplier information
* View supplier records
* Maintain supplier contacts

### 📊 Inventory Management

* Monitor stock levels
* View inventory across warehouses
* Track inventory updates

### ⬇ Incoming Stock Management

* Record incoming stock
* Update inventory automatically
* Track supplier deliveries

### ⬆ Outgoing Stock Management

* Dispatch products
* Monitor stock movement
* Prevent insufficient stock dispatch

### ⚠ Low Stock Alert

* Identify products with low inventory
* Prevent stock shortages
* Improve replenishment planning

### 🏭 Warehouse Utilization

* Monitor warehouse capacity
* Track used and available storage
* Optimize warehouse space

### 🧾 Order Monitoring

* View order details
* Track order quantities
* Monitor order status

### 🎨 Modern User Interface

* Dark-themed dashboard
* Responsive layout
* Interactive tables
* User-friendly navigation
* Professional CustomTkinter design

---

## 📂 Project Structure

```text
warehouse-automation-system/
│
├── ADV3_frontend.py
├── warehouse_backend1.py
│
├── db/
│   └── WarehouseDB.sql
│
└── README.md
```

---

## 🗄️ Database Schema

### PRODUCT

Stores product information.

| Field      | Type        |
| ---------- | ----------- |
| product_id | Primary Key |
| name       | VARCHAR     |
| category   | VARCHAR     |
| price      | DECIMAL     |

### SUPPLIER

Stores supplier details.

| Field       | Type        |
| ----------- | ----------- |
| supplier_id | Primary Key |
| name        | VARCHAR     |
| contact     | VARCHAR     |

### WAREHOUSE

Stores warehouse information.

| Field        | Type        |
| ------------ | ----------- |
| warehouse_id | Primary Key |
| location     | VARCHAR     |
| capacity     | INT         |

### INVENTORY

Stores inventory records.

| Field        | Type        |
| ------------ | ----------- |
| inventory_id | Primary Key |
| product_id   | Foreign Key |
| warehouse_id | Foreign Key |
| quantity     | INT         |
| last_updated | TIMESTAMP   |

### INCOMING_STOCK

Tracks incoming stock entries.

### OUTGOING_STOCK

Tracks dispatched stock records.

### ORDERS

Stores customer order information.

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/warehouse-automation-system.git
cd warehouse-automation-system
```

### Step 2: Install Dependencies

```bash
pip install customtkinter
pip install mysql-connector-python
```

Or

```bash
pip install -r requirements.txt
```

### Step 3: Start MySQL Server

Ensure MySQL Server is running.

Default configuration used:

```python
host='localhost'
user='root'
password='IG@1234'
database='WarehouseDB'
```

Update the Python files if your credentials are different.

### Step 4: Create Database

Run the SQL script provided in:

```text
WarehouseDB.sql
```

This will create:

```text
WarehouseDB
```

along with all required tables.

### Step 5: Run Application

```bash
python ADV3_frontend.py
```

---

## 🏗️ System Architecture

```text
CustomTkinter GUI
        │
        ▼
Python Application
        │
        ▼
 MySQL Connector
        │
        ▼
  MySQL Database
```

---

## 📸 Application Modules

### Product Dashboard

* View products
* Add new products
* Manage categories

### Supplier Dashboard

* View suppliers
* Add supplier information

### Inventory Dashboard

* Monitor stock levels
* View warehouse inventory

### Incoming Stock Module

* Record stock arrivals
* Update inventory automatically

### Dispatch Stock Module

* Record outgoing stock
* Manage warehouse dispatches

### Low Stock Monitoring

* Identify critical inventory levels
* Generate stock alerts

### Warehouse Utilization Dashboard

* Monitor capacity usage
* Optimize storage allocation

### Order Dashboard

* View customer orders
* Track order fulfillment status

---

## 🔐 Database Features

* Relational Database Design
* Primary Keys
* Foreign Keys
* Data Integrity
* Transaction Management
* SQL Query Optimization
* Inventory Tracking Automation

---

## 🚀 Future Enhancements

* User Authentication System
* Barcode Integration
* QR Code Inventory Tracking
* Automated Reordering System
* PDF Report Generation
* Cloud Database Integration
* Email Notifications
* Real-time Analytics Dashboard
* Multi-Warehouse Management
* Mobile Application Support

---

## 👨‍💻 Developed By

Computer Science Engineering (CSE) Mini Project for DBMS 

**Warehouse Automation & Tracking System using Python, CustomTkinter, and MySQL.**

---

## 📜 License

This project is developed for educational and academic purposes.
