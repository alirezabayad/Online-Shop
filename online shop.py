class Product:
    name:str=" "
    descriptions:str=" "
    product_ID:int=0
    def __init__(self,name,descriptions,product_ID):
        self.name=name
        self.descriptions=descriptions
        self.product_ID=product_ID
    def __str__(self):
        return "name:"+str(self.name)+"descriptions:"+str(self.descriptions)+"product_ID:"+str(self.product_ID)
class Item:
    products:Product
    count:int=0
    price:float=0.0
    def __init__(self,products,count,price):
        self.products=products
        self.count=count
        self.price=price
    def __str__(self):
        return "products:"+str(self.products)+"count:"+str(self.count)+"price:"+str(self.price)
class ItemCart(Item):
    seller: "Seller"
    def __init__(self, product, count, price, seller):
        super().__init__(product, count, price)
        self.seller = seller
    def __str__(self):
        return "products:"+str(self.products)+"count:"+str(self.count)+"price:"+str(self.price)+"seller:"+str(self.seller)
class ShoppingCart:
    items:list[ItemCart]
    date:str=" "
    def __init__(self,items,date):
        self.items=items
        self.date=date
    def __str__(self):
        return "items:"+str(self.items)+"date:"+str(self.date)
class Customer:
    name:str=" "
    username:str=" "
    phone_number:int=0
    E_mail_address:str=" "
    favorite_list:list[Product]
    cart:ShoppingCart
    history:list[ShoppingCart]
    def __init__(self,name,username,phone_number,E_mail_address,favorite_list,cart,history):
        self.name=name
        self.username=username
        self.phone_number=phone_number
        self.E_mail_address=E_mail_address
        self.favorite_list=favorite_list
        self.cart=cart
        self.history=history
    def __str__(self):
        return "name"+str(self.name)+"username"+str(self.username)+"phone_number"+str(self.phone_number)+"E_mail_address"+str(self.E_mail_address)+"favorite_list"+str(self.favorite_list)+"cart"+str(self.cart)+"history"+str(self.history)
class Seller:
    name:str=" "
    username:str=" "
    phone_number:int=0
    E_mail_address:str=" "
    items:list[Item]
    def __init__(self,name,username,phone_number,E_mail_address,items):
        self.name=name
        self.username=username
        self.phone_number=phone_number
        self.E_mail_address=E_mail_address
        self.items=items
    def __str__(self):
        return "name"+str(self.name)+"username"+str(self.username)+"phone_number"+str(self.phone_number)+"E_mail_address"+str(self.E_mail_address)+"items:"+str(self.items)
class Shop:
    customers:list[Customer]
    sellers:list[Seller]
    products:list[Product]
    def __init__(self,customers,sellers,products):
        self.customers=customers
        self.sellers=sellers
        self.products=products
    def __str__(self):
        return "customers"+str(self.customers)+"sellers"+str(self.sellers)+"products"+str(self.products)