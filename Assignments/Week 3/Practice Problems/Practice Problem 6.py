
class Restaurant:
    '''Class that includes details about a restaurant.'''

    def __init__(self):
        self.set_menu_items()
        self.set_customer_orders()
        self.set_book_table()


    def set_menu_items(self):
        '''Set the menu items to None'''
        self.menu_items = {}
    def get_menu_items(self):
        '''Get all the menu items'''
        return self.menu_items

    def set_book_table(self):
        '''Set the booked tables to None'''
        self.book_table = []
    def get_book_table(self):
        '''Get the booked tables'''
        return self.book_table

    def set_customer_orders(self):
        '''Set the customer orders to None'''
        self.customer_orders = {}
    def get_customer_orders(self):
        '''Get the customer orders'''
        return self.customer_orders

    def add_item_to_menu(self, item, price):
        '''To add items to the menu'''
        self.menu_items[item] = price

    def book_tables(self, customer_name, no_of_people):
        '''For booking tables in the restaurant'''
        table = {"customer name": customer_name, "number of people": no_of_people}
        self.book_table.append(table)

    def customer_order(self, customer_name, items):
        '''To take customer orders'''
        self.customer_orders[customer_name] = items

    def print_menu(self):
        '''Print the menu'''
        print("\nMenu")
        for item, price in self.menu_items.items():
            if not self.menu_items:
                print("No items available in the menu")
            else:
                print(f"{item}: {price} PKR")

    def print_book_table(self):
        '''Print the booked table'''
        print("\nTable reservations")
        for table in self.book_table:
            if not self.book_tables:
                print("No tables reservations yet")
            else:
                print(f"{table["customer name"]}: {table['number of people']} people")

    def print_customer_orders(self):
        '''Print the customer orders'''
        print("\nCustomer orders")
        for name, orders in self.customer_orders.items():
            if not self.customer_orders:
                print("No customer orders yet")
            else:
                print(f"{name}: {orders}")

Customer1 = Restaurant()
Customer1.get_menu_items()
Customer1.get_customer_orders()
Customer1.get_book_table()
Customer1.add_item_to_menu('Pasta', 600)
Customer1.add_item_to_menu('Biryani', 300)
Customer1.book_tables("Usman",5)
Customer1.customer_order("Usman", ['Pasta','Biryani'])
Customer1.print_menu()
Customer1.print_book_table()
Customer1.print_customer_orders()

Customer2 = Restaurant()
Customer2.get_menu_items()
Customer2.get_customer_orders()
Customer2.get_book_table()
Customer2.add_item_to_menu('Karhai', 1000)
Customer2.add_item_to_menu('Pulao', 800)
Customer2.book_tables("Usman",4)
Customer2.customer_order("Usman", ['Karhai'])
Customer2.print_menu()
Customer2.print_book_table()
Customer2.print_customer_orders()