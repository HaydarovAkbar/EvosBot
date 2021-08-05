import sqlite3
from mtelegrambotlar.EvosBot.evos_postgras import EvosPostgras

db = "evosSQLsqlte3.db"


class EvosSQL3:
    def product_select(self):
        try:
            connation = sqlite3.connect(db)
            cursor = connation.cursor()
            cursor.execute('SELECT * FROM products')
            a = cursor.fetchall()
            connation.close()
            return a
        except Exception as e:
            print("Siz qayerdadir adashdingiz", e)

    def update_price(self, id, price):
        try:
            connation = sqlite3.connect(db)
            cursor = connation.cursor()
            cursor.execute(f"UPDATE products SET price = {price} WHERE product_id = {id}")
            connation.commit()
            connation.close()

        except Exception as e:
            print("Siz qayerdadir adashdingiz!", e)

    def delete_price(self, id):
        try:
            connation = sqlite3.connect(db)
            cursor = connation.cursor()
            cursor.execute("DELETE FROM products WHERE product_id = {}".format(id))
            connation.commit()
            connation.close()

        except Exception as e:
            print("Siz qayerdadir adashdingiz dustm", e)

    def category_select(self):
        try:
            connation = sqlite3.connect(db)
            cursor = connation.cursor()
            cursor.execute("SELECT * FROM category")
            a = cursor.fetchall()
            connation.close()
            return a
        except Exception as e:
            print("Sizda bazi bir muammolar bor ->", e)

    def category_update(self, id, name):
        try:
            connation = sqlite3.connect(db)
            cursor = connation.cursor()
            cursor.execute("UPDATE category SET category_name = {} WHERE category_id = {}".format(name, id))
            connation.commit()
            connation.close()
        except Exception as e:
            print("Sizda muammo bor!", e)

    def create_db(self):
        try:
            connation = sqlite3.connect(db)
            cursor = connation.cursor()
            cursor.execute("CREATE TABLE buyList(id INREGER,product_name VARCHAR(255),date VARCHAR(255),count INTEGER)")
            connation.commit()
            connation.close()
        except Exception as e:
            print("Sizda muammo bor ekan", e)


if __name__ == '__main__':
    pos = EvosPostgras()
    sql = EvosSQL3()
    for item in sql.category_select():
        print(item[1])
        pos.insertcategory(item[0], item[1], item[2])
