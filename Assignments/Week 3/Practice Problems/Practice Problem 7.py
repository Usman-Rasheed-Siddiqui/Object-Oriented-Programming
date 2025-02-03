
class Inventory:
    '''To assign and check details for each stock'''      # Initiate count to zero
    def __init__(self):
        self.set_stock_detail()

    def set_item_id(self):
        '''To get ID of an item'''
        self.item_id = input("Enter item's id: ")
    def get_item_id(self):
        '''To set ID of an item'''
        return self.item_id

    def set_item_name(self):
        '''To get name of an item'''
        self.item_name = input("Enter item's name: ")
    def get_item_name(self):
        '''To set name of an item'''
        return self.item_name

    def set_stock_count(self):
        '''Count number of items added into stock'''
        self.stock_count = input("Enter number of items added to stock: ")
    def get_stock_count(self):
        '''Get number of items added into stock'''
        return self.stock_count

    def set_price(self):
        '''To set price of an item'''
        self.price = int(input("Enter price of the item: "))
    def get_price(self):
        '''To get price of an item'''
        return self.price

    def set_stock_detail(self):
        '''To set details of the stock'''
        self.stock_detail = {}
    def get_stock_detail(self):
        '''To get details of the stock'''
        return self.stock_detail

    def stock(self):
        '''Adding item info to a stock dictionary'''
        self.set_item_id()
        self.set_item_name()
        self.set_stock_count()
        self.set_price()
        self.stock_detail[self.item_name] = [self.item_id,self.stock_count, self.price]

    def show_details(self):
        '''Shows Details of the stock'''
        print("\n All Stock Details")
        if not self.stock_detail:
           print("No stock available yet")
        else:
            for item, properties in self.stock_detail.items():
                print(f"{item}:{properties}")

Stock1 = Inventory()    # Creates an instance for 1st stocks
Stock1.stock()
Stock1.stock()
Stock1.show_details()

Stock2 = Inventory()    # Creates an instance for 2nd stocks
Stock2.stock()
Stock2.stock()
Stock2.show_details()
