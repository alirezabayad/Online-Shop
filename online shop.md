# Online Shop
## Project Structure
The system consists of the following main classes:\
- ```Product```
- ```Item```
- ```ItemCart```
- ```ShoppingCart```
- ```Customer```
- ```Seller```
- ```Shop```\
Each class represents a real-world concept in an online shop.
# Class Descriptions
## Product
Represents a product available in the shop.\
Properties:
| Name | Type | Descriptions |
|:----:|:----:|:------------:|
| ```name``` | str | Name of product |
| ```description``` | str | Description of the product |
| ```product_ID``` | int | Unique identifier of the product |
## Item
Represents a sellable item with quantity and price.\
Properties:
| Name | Type | Descriptions |
|:----:|:----:|:------------:|
| ```Product``` | Product | Reference to a Product |
| ```Count``` | int | Quantity of the product |
| ```Price``` | float | Price per unit |
## ItemCart(inherits from Item)
Represents an item inside a shopping cart,linked to a seller.\
Properties:
| Name | Type | Descriptions |
|:----:|:----:|:------------:|
| ```Product``` | Product | Inherited from Item |
| ```Count``` | int | Inherited from Item |
| ```Price``` | float | Inherited from Item |
| ```Seller``` | Seller | Seller of the product |
- Notes:
This class demonstrates inheritance from the Item class.
## ShoppingCart
Represents a shopping cart containing multiple items.\
items(list[ItemCart])–List of items in the cart\
date(str)–Date of the shopping cart creation
## Customer
Represents a customer of the shop.\
name(str)–Customer name\
username(str)–Customer username\
phone_number(int)–Phone number\
E_mail_address(str)–Email address\
favorite_list(list[Product])–List of favorite products\
cart(ShoppingCart)–Current shopping cart\
history(list[ShoppingCart])–Purchase history
## Seller
Represents a seller in the shop.\
name(str)–Seller name\
username(str)–Seller username\
phone_number(int)–Phone number\
E_mail_address(str)–Email address\
items(list[Item])–List of items sold by the seller
## Shop
Represents the main shop system.
customers(list[Customer])–registered customers\
sellers(list[Seller])–registered sellers\
products(list[Product])–available products