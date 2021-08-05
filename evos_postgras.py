from psycopg2 import connect

HOST = "localhost"
USER = "postgres"
PASS = "akbar2000"
DATABASE = "evosdatabase"


class EvosPostgras:
    def createDB(self):
        try:
            connation = connect(
                user=USER,
                host=HOST,
                password=PASS
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute("CREATE DATABASE EvosDB")
        except Exception as e:
            print("Sizda xato bor", e)

    def createTB(self):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(
                "CREATE TABLE products(product_id INTEGER,product_name VARCHAR(255),category_id INTEGER,price INTEGER)")
        except Exception as e:
            print("Sizda muammo bor!", e)

    def insertproduct(self, product_id, product_name, category_id, price):
        try:
            connation = connect(
                user=USER,
                host=HOST,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(
                f"INSERT INTO products(product_id,product_name,category_id,price) VALUES({product_id},'{product_name}',{category_id},{price})")
        except Exception as e:
            print("sizda muammo bor!", e)

    def insertcategory(self, id, category_name, category_id):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(
                f"INSERT INTO category(id,category_name,category_id) VALUES({id},'{category_name}',{category_id})")
        except Exception as e:
            print("Sizda muammo bor!", e)

    def createTBc(self):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute("CREATE TABLE category(id INTEGER,category_name VARCHAR(255),category_id INTEGER)")
        except Exception as e:
            print("Sizda muammo bor!", e)

    def createTBb(self):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute("CREATE TABLE buylist(id INTEGER,product_name VARCHAR(255),date VARCHAR(255),count INTEGER)")
        except Exception as e:
            print("Sizda muammo bor!", e)

    def selectProduct(self, id):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute("SELECT product_id,product_name,price FROM products WHERE category_id = {}".format(id))
            a = cursor.fetchall()
            return a
        except Exception as e:
            print("Sizda qanaqadr muammo bor!", e)

    def selectCategory(self):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute("SELECT * FROM category")
            a = cursor.fetchall()
            return a
        except Exception as e:
            print("Sizda qandaydir muammo bor!", e)

    def insertBuylist(self, id, product_name, date, count):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(
                f"INSERT INTO buylist(id,product_name,date,count) VALUES({id},'{product_name}','{date}',{count})")

            return True
        except Exception as e:
            print("Sizda muammo bor", e)

    def selectbuy(self, a):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"SELECT * FROM buylist WHERE id = {a}")
            return cursor.fetchall()
        except Exception as e:
            print("sizda >", e)

    def del_buy(self):
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute("DELETE FROM buylist")
        except Exception as e:
            print("sizda >", e)


if __name__ == "__main__":
    db = EvosPostgras()
    # a = db.insertBuylist(1,"moshina","2021/12/12",1)
    db.del_buy()
    # print(db.selectbuy())
