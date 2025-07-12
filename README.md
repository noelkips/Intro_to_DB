# Intro_to_DBGreat! Here's the **enhanced `README.md`** including:

* ✅ Task breakdown with details
* 🏷️ Markdown badge shields
* 💾 SQL code snippets
* 📁 File structure

You can copy-paste this directly to your `Intro_to_DB` repo.

---

````markdown
# 📚 Intro_to_DB: MySQL Bookstore Project

![MySQL](https://img.shields.io/badge/SQL-MySQL-blue?logo=mysql)
![Status](https://img.shields.io/badge/status-in--progress-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Author](https://img.shields.io/badge/author-Noel%20Langat-blueviolet)

> A foundational database project that demonstrates schema design, SQL scripting, and database automation using Python. We simulate the backend of a dream online bookstore.

---

## 📁 Project Structure

```bash
Intro_to_DB/
├── alx_book_store.sql        # ✅ Task 0: Schema creation
├── MySQLServer.py            # ✅ Task 1: Create DB using Python
├── task_2.sql                # ✅ Task 2: Create tables
├── task_3.sql                # ✅ Task 3: List all tables
├── task_4.sql                # ✅ Task 4: Print books table schema
├── task_5.sql                # ✅ Task 5: Insert first customer
├── task_6.sql                # ✅ Task 6: Insert more customers
````

---

## ✅ Tasks Breakdown

### 🧱 Task 0: Create Schema for Bookstore

**File:** `alx_book_store.sql`

Creates database and tables:

```sql
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE authors (
  author_id INT PRIMARY KEY,
  author_name VARCHAR(215)
);

CREATE TABLE books (
  book_id INT PRIMARY KEY,
  title VARCHAR(130),
  author_id INT,
  price DOUBLE,
  publication_date DATE,
  FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(215),
  email VARCHAR(215),
  address TEXT
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_details (
  orderdetailid INT PRIMARY KEY,
  order_id INT,
  book_id INT,
  quantity DOUBLE,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id)
);
```

---

### 🐍 Task 1: Create Database with Python

**File:** `MySQLServer.py`

```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password'
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
```

---

### 🏗️ Task 2: Create All Tables

**File:** `task_2.sql`

```sql
USE alx_book_store;
-- (Copy the table creation SQL from task 0 here or reuse)

-- e.g.
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(215),
  email VARCHAR(215),
  address TEXT
);
```

---

### 📋 Task 3: List All Tables

**File:** `task_3.sql`

```sql
USE alx_book_store;
SHOW TABLES;
```

> ✅ Make sure to use `USE alx_book_store;` to avoid check failure.

---

### 📄 Task 4: Print Full Description of `books` Table

**File:** `task_4.sql`

```sql
USE alx_book_store;
SHOW CREATE TABLE books;
```

> ❌ `DESCRIBE` or `EXPLAIN` not allowed.

---

### 👤 Task 5: Insert First Customer

**File:** `task_5.sql`

```sql
USE alx_book_store;

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
```

✅ Must include all fields and match values exactly.

---

### 👥 Task 6: Insert Multiple Customers

**File:** `task_6.sql`

```sql
USE alx_book_store;

INSERT INTO customer (customer_id, customer_name, email, address) VALUES
(2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');
```

---

## 🧪 How to Run

```bash
# Run MySQL shell and load scripts
mysql -u root -p < alx_book_store.sql
mysql -u root -p < task_2.sql
mysql -u root -p < task_3.sql
...

# Or run Python DB script
python MySQLServer.py
```

---

## 🚀 Author

**Noel Kiprono Langat**

> Follow on GitHub · Ask questions · Share improvements

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🏆 Milestone Checklist

| Task                              | Status      |
| --------------------------------- | ----------- |
| Task 0: Create DB schema          | ✅ Completed |
| Task 1: Python DB creation        | ✅ Completed |
| Task 2: Create tables             | ✅ Completed |
| Task 3: List tables               | ✅ Completed |
| Task 4: Describe `books` table    | ✅ Completed |
| Task 5: Insert 1 customer         | ✅ Completed |
| Task 6: Insert multiple customers | ✅ Completed |

---

## 📣 Shoutout

> "Learning databases is building the foundation for scalable systems. Keep going! 💪"

```

