import sqlite3

class ProductDB:
    def __init__(self):
        self.conn = sqlite3.connect('products.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS products
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL)''')
        self.conn.commit()

    def addProduct(self, name, price, quantity):
        self.c.execute('''INSERT INTO products (name, price, quantity)
            VALUES (?, ?, ?)''', (name, price, quantity))
        self.conn.commit()

    def getProducts(self):
        self.c.execute('''SELECT * FROM products''')
        return self.c.fetchall()

    def getProduct(self, name):
        self.c.execute('''SELECT * FROM products WHERE name=?''', (name,))
        return self.c.fetchone()

    def updateProduct(self, id, name, price, quantity):
        self.c.execute('''UPDATE products SET name=?, price=?, quantity=?
            WHERE id=?''', (name, price, quantity, id))
        self.conn.commit()

    def deleteProduct(self, id):
        self.c.execute('''DELETE FROM products WHERE id=?''', (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

class OrdersDB:
    def __init__(self):
        self.conn = sqlite3.connect('orders.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS orders
            (OrderId INTEGER NOT NULL,
            ProductId INTEGER NOT NULL,
            Price REAL NOT NULL,
            Status TEXT NOT NULL default 'Pending',
            OrderDate datetime NOT NULL default CURRENT_TIMESTAMP,
            DeliveryDate datetime NOT NULL default CURRENT_TIMESTAMP)''')
        self.conn.commit()

    def addOrder(self, orderId, productId, price, status, orderDate, deliveryDate):
        self.c.execute('''INSERT INTO orders (OrderId, ProductId, Price, Status, OrderDate, DeliveryDate)
            VALUES (?, ?, ?, ?, ?, ?)''', (orderId, productId, price, status, orderDate, deliveryDate))
        self.conn.commit()

    def getOrders(self):
        self.c.execute('''SELECT * FROM orders''')
        return self.c.fetchall()

    def getOrder(self, orderId):
        self.c.execute('''SELECT * FROM orders WHERE OrderId=?''', (orderId,))
        return self.c.fetchone()

    def updateOrder(self, orderId, productId, price, status, orderDate, deliveryDate):
        self.c.execute('''UPDATE orders SET OrderId=?, ProductId=?, Price=?, Status=?, OrderDate=?, DeliveryDate=?
            WHERE id=?''', (orderId, productId, price, status, orderDate, deliveryDate))
        self.conn.commit()

    def deleteOrder(self, orderId):
        self.c.execute('''DELETE FROM orders WHERE OrderId=?''', (orderId,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

class delayDB:
    def __init__(self):
        self.conn = sqlite3.connect('delay.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS delay
            (OrderId INTEGER NOT NULL,
            DelayDate datetime NOT NULL default CURRENT_TIMESTAMP,
            DelayReason TEXT NOT NULL default 'Pending')''')

        self.conn.commit()

    def addDelay(self, orderId, delayDate, delayReason):
        self.c.execute('''INSERT INTO delay (OrderId, DelayDate, DelayReason)
            VALUES (?, ?, ?)''', (orderId, delayDate, delayReason))
        self.conn.commit()

    def getDelays(self):
        self.c.execute('''SELECT * FROM delay''')
        return self.c.fetchall()

    def getDelay(self, orderId):
        self.c.execute('''SELECT * FROM delay WHERE OrderId=?''', (orderId,))
        return self.c.fetchone()

    def updateDelay(self, orderId, delayDate):
        self.c.execute('''UPDATE delay SET OrderId=?, DelayDate=?
            WHERE id=?''', (orderId, delayDate))
        self.conn.commit()

    def deleteDelay(self, orderId):
        self.c.execute('''DELETE FROM delay WHERE OrderId=?''', (orderId,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


