import psycopg2

query = """
        CREATE TABLE product2
        (
            id       SERIAL PRIMARY KEY,
            name     VARCHAR        NOT NULL,
            price    numeric(10, 2) NOT NULL,
            quantity INT            NOT NULL

        ); \
        """


class Product:
    def __init__(self):
        self.conn = psycopg2.connect("dbname= 'usmonov' user='postgres' host='localhost' password='1'")
        self.cur = self.conn.cursor()

        self.conn.autocommit = True

    def show_product(self):
        self.cur.execute(
            "SELECT * FROM product2;"
        )

        for row in self.cur.fetchall():
            print(f"id : {row[0]}, name: {row[1]}, price: {row[2]}, quantity: {row[3]}")

    def add_product(self, name, price, quantity):
        query_ = """
                 INSERT INTO product2(name, price, quantity)
                 VALUES (%s, %s, %s); \
                 """
        self.cur.execute(query_, (name, price, quantity))
        print('Product was added!')

    def remove_product(self, id_):
        query2 = """
                 DELETE
                 FROM product2
                 where id = %s \
                 """
        self.cur.execute(query2, (id_,))
        print('Product was removed!')

    def update_product(self, id_, name_):
        query3 = """
                 UPDATE product2
                 SET name = %s
                 where id = %s \
                 """
        self.cur.execute(query3, (name, id_))
        print('Product was updated!')


product = Product()

while True:
    try:
        choice = int(input("1: see categories\n"
                           "2: add products\n"
                           "3: remove product\n"
                           "4: change the product\n"
                           "CHOOSE: "))
    except ValueError:
        print('Error!, enter a number!')
        continue

    if choice == 1:
        product.show_product()

    elif choice == 2:
        name = input('enter name: ')
        price = float(input('enter price: '))
        quan = int(input('enter quantity: '))
        product.add_product(name, price, quan)


    elif choice == 3:
        try:
            id__ = int(input('enter the id which you want to remove: '))
        except ValueError:
            print('enter a number!')
            continue

        product.remove_product(id__)

    elif choice == 4:
        id_2 = int(input('enter the id: '))
        name = input('enter the name you want to change: ')
        product.update_product(id_2, name)

    else:
        print('Wrong number!!, Try again!')
        continue
