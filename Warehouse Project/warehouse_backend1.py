import mysql.connector
from mysql.connector import Error
from datetime import datetime

# ======================================================
# DATABASE CONNECTION
# ======================================================

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="IG@1234",
        database="WarehouseDB"
    )

    cursor = db.cursor()

    print("\n✅ Connected to WarehouseDB Successfully")

except Error as e:
    print("❌ Database Connection Error:", e)
    exit()


# ======================================================
# HELPER FUNCTIONS
# ======================================================

def line():
    print("=" * 65)


def pause():
    input("\nPress Enter to continue...")


# ======================================================
# PRODUCT MANAGEMENT
# ======================================================

def view_products():

    line()
    print("📦 PRODUCT LIST")
    line()

    query = "SELECT * FROM Product"

    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        print("No products found")

    else:
        for row in rows:
            print(
                f"ID: {row[0]} | "
                f"Name: {row[1]} | "
                f"Category: {row[2]} | "
                f"Price: ₹{row[3]}"
            )

    pause()


def add_product():

    line()
    print("➕ ADD NEW PRODUCT")
    line()

    try:

        product_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Product Price: "))

        sql = """
        INSERT INTO Product(product_id, name, category, price)
        VALUES (%s, %s, %s, %s)
        """

        values = (product_id, name, category, price)

        cursor.execute(sql, values)
        db.commit()

        print("\n✅ Product Added Successfully")

    except Error as e:
        print("❌ Error:", e)

    pause()


# ======================================================
# SUPPLIER MANAGEMENT
# ======================================================

def view_suppliers():

    line()
    print("🚚 SUPPLIER LIST")
    line()

    cursor.execute("SELECT * FROM Supplier")

    rows = cursor.fetchall()

    for row in rows:
        print(
            f"Supplier ID: {row[0]} | "
            f"Name: {row[1]} | "
            f"Contact: {row[2]}"
        )

    pause()


def add_supplier():

    line()
    print("➕ ADD SUPPLIER")
    line()

    try:

        supplier_id = int(input("Supplier ID: "))
        name = input("Supplier Name: ")
        contact = input("Contact Number: ")

        sql = """
        INSERT INTO Supplier
        VALUES (%s, %s, %s)
        """

        values = (supplier_id, name, contact)

        cursor.execute(sql, values)
        db.commit()

        print("\n✅ Supplier Added Successfully")

    except Error as e:
        print("❌ Error:", e)

    pause()


# ======================================================
# INVENTORY MANAGEMENT
# ======================================================

def view_inventory():

    line()
    print("📊 LIVE INVENTORY STATUS")
    line()

    query = """
    SELECT 
        p.product_id,
        p.name,
        w.location,
        i.quantity,
        i.last_updated
    FROM Inventory i
    JOIN Product p
        ON i.product_id = p.product_id
    JOIN Warehouse w
        ON i.warehouse_id = w.warehouse_id
    ORDER BY i.quantity DESC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    if not rows:
        print("Inventory Empty")

    else:

        for row in rows:

            print(
                f"Product ID: {row[0]} | "
                f"Product: {row[1]} | "
                f"Warehouse: {row[2]} | "
                f"Stock: {row[3]} | "
                f"Updated: {row[4]}"
            )

    pause()


# ======================================================
# INCOMING STOCK
# ======================================================

def add_incoming_stock():

    line()
    print("⬇ ADD INCOMING STOCK")
    line()

    try:

        entry_id = int(input("Entry ID: "))
        supplier_id = int(input("Supplier ID: "))
        product_id = int(input("Product ID: "))
        quantity = int(input("Quantity Added: "))
        warehouse_id = int(input("Warehouse ID: "))

        date = datetime.now().date()

        sql = """
        INSERT INTO Incoming_Stock
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            entry_id,
            supplier_id,
            product_id,
            quantity,
            date,
            warehouse_id
        )

        cursor.execute(sql, values)
        db.commit()

        print("\n✅ Incoming Stock Added")
        print("✅ Inventory Updated Automatically")

    except Error as e:
        print("❌ Error:", e)

    pause()


# ======================================================
# OUTGOING STOCK
# ======================================================

def add_outgoing_stock():

    line()
    print("⬆ DISPATCH STOCK")
    line()

    try:

        dispatch_id = int(input("Dispatch ID: "))
        product_id = int(input("Product ID: "))
        quantity = int(input("Dispatch Quantity: "))
        destination = input("Destination: ")
        warehouse_id = int(input("Warehouse ID: "))

        date = datetime.now().date()

        # CHECK CURRENT STOCK

        check_query = """
        SELECT quantity
        FROM Inventory
        WHERE product_id = %s
        AND warehouse_id = %s
        """

        cursor.execute(check_query, (product_id, warehouse_id))

        result = cursor.fetchone()

        if result is None:
            print("❌ Product not found in inventory")

        elif result[0] < quantity:
            print("❌ Insufficient Stock")

        else:

            sql = """
            INSERT INTO Outgoing_Stock
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = (
                dispatch_id,
                product_id,
                quantity,
                destination,
                date,
                warehouse_id
            )

            cursor.execute(sql, values)
            db.commit()

            print("\n✅ Stock Dispatched Successfully")
            print("✅ Inventory Reduced Automatically")

    except Error as e:
        print("❌ Error:", e)

    pause()


# ======================================================
# LOW STOCK ALERT
# ======================================================

def low_stock_alert():

    line()
    print("⚠ LOW STOCK ALERT")
    line()

    query = """
    SELECT 
        p.name,
        w.location,
        i.quantity
    FROM Inventory i
    JOIN Product p
        ON i.product_id = p.product_id
    JOIN Warehouse w
        ON i.warehouse_id = w.warehouse_id
    WHERE i.quantity < 20
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    if not rows:
        print("✅ No Low Stock Products")

    else:

        for row in rows:

            print(
                f"Product: {row[0]} | "
                f"Warehouse: {row[1]} | "
                f"Remaining Stock: {row[2]}"
            )

    pause()


# ======================================================
# WAREHOUSE UTILIZATION
# ======================================================

def warehouse_utilization():

    line()
    print("🏭 WAREHOUSE UTILIZATION")
    line()

    query = """
    SELECT 
        w.location,
        w.capacity,
        SUM(i.quantity) AS used_capacity
    FROM Warehouse w
    JOIN Inventory i
        ON w.warehouse_id = i.warehouse_id
    GROUP BY w.warehouse_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:

        free_space = row[1] - row[2]

        print(
            f"Warehouse: {row[0]} | "
            f"Capacity: {row[1]} | "
            f"Used: {row[2]} | "
            f"Free Space: {free_space}"
        )

    pause()


# ======================================================
# ORDER MANAGEMENT
# ======================================================

def view_orders():

    line()
    print("🧾 ORDER DETAILS")
    line()

    query = """
    SELECT 
        o.order_id,
        p.name,
        o.quantity,
        o.status
    FROM Orders o
    JOIN Product p
        ON o.product_id = p.product_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:

        print(
            f"Order ID: {row[0]} | "
            f"Product: {row[1]} | "
            f"Quantity: {row[2]} | "
            f"Status: {row[3]}"
        )

    pause()


# ======================================================
# MAIN MENU
# ======================================================

while True:

    line()
    print("🏢 WAREHOUSE AUTOMATION & TRACKING SYSTEM")
    line()

    print("""
1. View Products
2. Add Product
3. View Suppliers
4. Add Supplier
5. View Inventory
6. Add Incoming Stock
7. Dispatch Stock
8. Low Stock Alert
9. Warehouse Utilization
10. View Orders
11. Exit
    """)

    choice = input("Enter Choice: ")

    if choice == "1":
        view_products()

    elif choice == "2":
        add_product()

    elif choice == "3":
        view_suppliers()

    elif choice == "4":
        add_supplier()

    elif choice == "5":
        view_inventory()

    elif choice == "6":
        add_incoming_stock()

    elif choice == "7":
        add_outgoing_stock()

    elif choice == "8":
        low_stock_alert()

    elif choice == "9":
        warehouse_utilization()

    elif choice == "10":
        view_orders()

    elif choice == "11":

        print("\n✅ Exiting Warehouse System")
        break

    else:
        print("\n❌ Invalid Choice")


# ======================================================
# CLOSE DATABASE
# ======================================================

cursor.close()
db.close()

print("✅ Database Connection Closed")
