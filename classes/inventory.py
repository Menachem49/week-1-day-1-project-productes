from classes.product import Product

class Inventory:
    def __init__(self):
        self.__products = []
        

    def add(self, new_product: Product):
        # for product in self.__products:
        #     if product.name == new_product.name:
        #         raise ValueError(f"{new_product.name} already exists")
        if self.find(new_product.name):
            raise ValueError(f"{new_product.name} already exists")
        self.__products.append(new_product) 

    def find(self, product_name):
        for product in self.__products:
            if product.name == product_name:
                return product
        return None

    def by_value(self):
        return sorted(self.__products, key=lambda p : p.total_value, reverse=True)

    @property
    def total_value(self):
        # sum_ = 0
        # for product in self.__products:
        #     sum_ += product.total_value
        return sum(product.total_value for product in self.__products)



