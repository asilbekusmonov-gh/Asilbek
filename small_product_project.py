class Product:
    def init(self):
        self.conn = psycopg2.connect(" dbname='usmonov' user='postgres' host='localhost'  password ='1'")
        self.cur = self.conn.cursor()

        self.conn.autocommit = True

    def show_product(self):
        query = """
                SELECT *
                FROM product; \
 \
                """
        self.cur.execute(query)
        row = self.cur.fetchall()
        for r in row:
            print(f" id: {r[0]}, name: {r[1]}, price: {r[2]}, quantity: {r[3]}")

    def add_product(self, name, price, quantity):
        self.cur.execute(
            "insert into product(name, price, quantity) Values (%s, %s, %s);",
            (name, price, quantity)
        )
        print('Product added!')

    def delete_product(self, id_):
        self.cur.execute(
            "DELETE FROM product where id = %s;",
            (id_,)
        )
        print('Product was removed!')

    def update_product(self, id_, name):
        self.cur.execute(
            "UPDATE product set name = %s where id = %s;",
            (name, id_)

        )
        print('product was updated!')


product = Product()
# query = """
#
#         create table product
#         (
#             id       SERIAL PRIMARY KEY,
#             name     VARCHAR NOT NULL,
#             price    NUMERIC(10, 2),
#             quantity INT     NOT NULL
#
#         ); \
#
#
#         """
#
# query2 = """
#
#          ALTER TABLE product
#              ALTER COLUMN price SET not null \
#
#
#          """

while True:
    try:
        categories = int(input("1: see categories,\n"
                               "2: add products,\n"
                               "3: remove product,\n"
                               "4: change the product\n"
                               "CHOOSE: "))
    except ValueError:
        print('please enter a number!')
        continue

    if categories == 1:
        product.show_product()
    elif categories == 2:
        name = input('enter name: ')
        price = float(input('enter price: '))
        quan = int(input('enter quantity: '))
        product.add_product(name, price, quan)

    elif categories == 3:
        try:
            id_ = int(input('enter the id of product: '))
        except ValueError:
            print('enter a number')
            continue

        product.delete_product(id_)

    elif categories == 4:
        try:
            id_ = int(input('enter the id of product which you want to change: '))
        except ValueError:
            print('enter int number')
            continue
        name = input('new name: ')
        product.update_product(id_, name)

    else:
        print('Oops, wrong number!!')