# =========================================================
# WAREHOUSE AUTOMATION & TRACKING SYSTEM
# FRONTEND - CUSTOMTKINTER
# =========================================================

import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector

# =========================================================
# DATABASE CONNECTION
# =========================================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="IG@1234",
    database="WarehouseDB"
)

cursor = db.cursor()

# =========================================================
# APP CONFIGURATION
# =========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1550x900")
app.title("Warehouse Automation & Tracking System")

# =========================================================
# COLORS
# =========================================================

BG_COLOR = "#0f172a"
CARD_COLOR = "#1e293b"
BTN_COLOR = "#2563eb"
HOVER_COLOR = "#1d4ed8"

# =========================================================
# MAIN LAYOUT
# =========================================================

app.configure(fg_color=BG_COLOR)

# =========================================================
# TOP NAVIGATION BAR
# =========================================================

top_bar = ctk.CTkFrame(
    app,
    height=80,
    fg_color="#111827",
    corner_radius=0
)

top_bar.pack(fill="x")

title = ctk.CTkLabel(
    top_bar,
    text="🏭 Warehouse Automation & Tracking System",
    font=("Poppins", 28, "bold")
)

title.pack(side="left", padx=30, pady=20)

# =========================================================
# CONTENT AREA
# =========================================================

content_frame = ctk.CTkFrame(
    app,
    fg_color=BG_COLOR
)

content_frame.pack(fill="both", expand=True)

# =========================================================
# TABLE FRAME
# =========================================================

table_frame = ctk.CTkFrame(
    content_frame,
    fg_color=CARD_COLOR,
    corner_radius=20
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

# =========================================================
# TREEVIEW
# =========================================================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="#1e293b",
    foreground="white",
    rowheight=35,
    fieldbackground="#1e293b",
    font=("Poppins", 12)
)

style.configure(
    "Treeview.Heading",
    background="#2563eb",
    foreground="white",
    font=("Poppins", 13, "bold")
)

tree = ttk.Treeview(table_frame)

tree.pack(fill="both", expand=True, padx=20, pady=20)

# =========================================================
# CLEAR TABLE
# =========================================================

def clear_table():

    tree.delete(*tree.get_children())


# =========================================================
# VIEW PRODUCTS
# =========================================================

def view_products():

    clear_table()

    tree["columns"] = ("ID", "Name", "Category", "Price")

    tree.heading("#0", text="")
    tree.column("#0", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=200)

    cursor.execute("SELECT * FROM Product")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


# =========================================================
# VIEW SUPPLIERS
# =========================================================

def view_suppliers():

    clear_table()

    tree["columns"] = ("Supplier ID", "Name", "Contact")

    tree.heading("#0", text="")
    tree.column("#0", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=300)

    cursor.execute("SELECT * FROM Supplier")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


# =========================================================
# VIEW INVENTORY
# =========================================================

def view_inventory():

    clear_table()

    tree["columns"] = (
        "Product",
        "Warehouse",
        "Quantity",
        "Updated"
    )

    tree.heading("#0", text="")
    tree.column("#0", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=300)

    query = """
    SELECT 
        p.name,
        w.location,
        i.quantity,
        i.last_updated
    FROM Inventory i
    JOIN Product p
        ON i.product_id = p.product_id
    JOIN Warehouse w
        ON i.warehouse_id = w.warehouse_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


# =========================================================
# VIEW ORDERS
# =========================================================

def view_orders():

    clear_table()

    tree["columns"] = (
        "Order ID",
        "Product",
        "Quantity",
        "Status"
    )

    tree.heading("#0", text="")
    tree.column("#0", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=300)

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
        tree.insert("", "end", values=row)


# =========================================================
# LOW STOCK ALERT
# =========================================================

def low_stock_alert():

    clear_table()

    tree["columns"] = (
        "Product",
        "Warehouse",
        "Remaining Stock"
    )

    tree.heading("#0", text="")
    tree.column("#0", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=350)

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

    for row in rows:
        tree.insert("", "end", values=row)


# =========================================================
# WAREHOUSE UTILIZATION
# =========================================================

def warehouse_utilization():

    clear_table()

    tree["columns"] = (
        "Warehouse",
        "Capacity",
        "Used Capacity"
    )

    tree.heading("#0", text="")
    tree.column("#0", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=350)

    query = """
    SELECT 
        w.location,
        w.capacity,
        SUM(i.quantity)
    FROM Warehouse w
    JOIN Inventory i
        ON w.warehouse_id = i.warehouse_id
    GROUP BY w.warehouse_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)

# =========================================================
# POPUP FORM
# =========================================================

def popup_form(title_text, labels, submit_function):

    form = ctk.CTkToplevel(app)
    form.geometry("500x600")
    form.title(title_text)

    entries = []

    title = ctk.CTkLabel(
        form,
        text=title_text,
        font=("Poppins", 24, "bold")
    )

    title.pack(pady=20)

    for label in labels:

        ctk.CTkLabel(
            form,
            text=label,
            font=("Poppins", 14)
        ).pack(pady=5)

        entry = ctk.CTkEntry(
            form,
            width=300,
            height=40
        )

        entry.pack(pady=5)

        entries.append(entry)

    def submit():
        values = [e.get() for e in entries]
        submit_function(values)
        form.destroy()

    submit_btn = ctk.CTkButton(
        form,
        text="Submit",
        width=200,
        height=45,
        command=submit,
        fg_color=BTN_COLOR,
        hover_color=HOVER_COLOR
    )

    submit_btn.pack(pady=30)

# =========================================================
# ADD PRODUCT
# =========================================================

def add_product():

    def submit(values):

        sql = """
        INSERT INTO Product
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(sql, values)
        db.commit()

        messagebox.showinfo(
            "Success",
            "Product Added Successfully"
        )

    popup_form(
        "Add Product",
        ["Product ID", "Name", "Category", "Price"],
        submit
    )

# =========================================================
# ADD SUPPLIER
# =========================================================

def add_supplier():

    def submit(values):

        sql = """
        INSERT INTO Supplier
        VALUES (%s,%s,%s)
        """

        cursor.execute(sql, values)
        db.commit()

        messagebox.showinfo(
            "Success",
            "Supplier Added Successfully"
        )

    popup_form(
        "Add Supplier",
        ["Supplier ID", "Name", "Contact"],
        submit
    )

# =========================================================
# INCOMING STOCK
# =========================================================

def add_incoming_stock():

    def submit(values):

        sql = """
        INSERT INTO Incoming_Stock
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, values)
        db.commit()

        messagebox.showinfo(
            "Success",
            "Incoming Stock Added & Inventory Updated"
        )

    popup_form(
        "Add Incoming Stock",
        [
            "Entry ID",
            "Supplier ID",
            "Product ID",
            "Quantity",
            "Date",
            "Warehouse ID"
        ],
        submit
    )

# =========================================================
# OUTGOING STOCK
# =========================================================

def dispatch_stock():

    def submit(values):

        sql = """
        INSERT INTO Outgoing_Stock
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, values)
        db.commit()

        messagebox.showinfo(
            "Success",
            "Stock Dispatched Successfully"
        )

    popup_form(
        "Dispatch Stock",
        [
            "Dispatch ID",
            "Product ID",
            "Quantity",
            "Destination",
            "Date",
            "Warehouse ID"
        ],
        submit
    )

# =========================================================
# BUTTON NAVIGATION BAR
# =========================================================

# =========================================================
# BUTTON NAVIGATION BAR
# =========================================================

nav_frame = ctk.CTkFrame(
    app,
    height=70,
    fg_color="#0f172a",
    corner_radius=0
)

nav_frame.pack(fill="x", pady=5)

buttons = [

    ("View Products", view_products),
    ("Add Product", add_product),
    ("View Suppliers", view_suppliers),
    ("Add Supplier", add_supplier),
    ("View Inventory", view_inventory),
    ("Incoming Stock", add_incoming_stock),
    ("Dispatch Stock", dispatch_stock),
    ("Low Stock", low_stock_alert),
    ("Utilization", warehouse_utilization),
    ("View Orders", view_orders),
    ("Exit", app.destroy)

]

# =========================================================
# BUTTON STYLE
# =========================================================

for text, cmd in buttons:

    btn = ctk.CTkButton(

        nav_frame,
        text=text,
        command=cmd,

        width=120,
        height=40,

        fg_color=BTN_COLOR,
        hover_color=HOVER_COLOR,

        font=("Poppins", 12, "bold"),

        corner_radius=10

    )

    btn.pack(
        side="left",
        padx=4,
        pady=10,
        expand=True
    )

# =========================================================
# START WITH INVENTORY
# =========================================================

view_inventory()

# =========================================================
# RUN APP
# =========================================================

app.mainloop()
