class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.__quantity = quantity
        

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def price(self) -> str:
        return self._price
    
    @price.setter
    def price(self, price: str) -> None:
        if price <= 0:
            raise ValueError("price must be positive")
        self._price = price

    def add_stock(self, amount)-> None:
        if amount < 1:
            raise ValueError("amount must be positive")
        self.__quantity += amount

    def sell(self, amount)-> None:
        if self.__quantity - amount < 0:
            raise ValueError(f"not enough {self.__name}")
        self.__quantity -= amount

    @property
    def total_value(self):
        return self.price * self.__quantity

    def __str__(self):
        return f'{self.__name}: {self.__quantity} * {self._price} = {self.total_value}'   



if __name__ == "__main__":
    p1 =Product("a",1,10)
    p2 = Product("b",2,20)
    p3 = Product("c",3,30)
    pro = [p1, p2, p3]
    s= (map(lambda p : sum(p.total_value),pro))
    print (list(s))