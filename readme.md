# Online Shop
## Project Structure
The system consists of the following main classes:
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

Methods:
| Name | Decribtions |
|:----:|:-----------:|
| ```__init__``` | Initializes product information |
| ```__str__``` | Returns product information as string |
## Item
Represents a sellable item with quantity and price.\
Properties:
| Name | Type | Descriptions |
|:----:|:----:|:------------:|
| ```Product``` | Product | Reference to a Product |
| ```Count``` | int | Quantity of the product |
| ```Price``` | float | Price per unit |

Methods:
| Name | Decribtions |
|:----:|:-----------:|
| ```__init__``` | Initializes item data |
| ```__str__``` | Returns item details as string |
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
Properties:
| Name | Type | Descriptions |
|:----:|:----:|:------------:|
| ```Items``` | list[ItemCart] | List of items in the cart |
| ```date``` | str | Date of the shopping cart creation |
## Customer
Represents a customer of the shop.\
Properties:
| Name | Type | Descriptions |
|:----:|:----:|:------------:|
| ```Name``` | str | Customer name |
| ```Username``` | str | Customer username |
| ```phone_number``` | int | Phone number |
| ```E_mail_address``` | str | Email address |
| ```favorite_list``` | list[Product] | List of favorite products |
| ```Card``` | ShoppingCard | Current shopping cart |
| ```history``` | list[ShoppingCard] | Purchase history |
## Seller
Represents a seller in the shop.\
Properties:
| Name | Type | Descriptions |
|:----:|:----:|:------------:|
| ```Name``` | str | Seller name |
| ```Username``` | str | Seller username |
| ```phone_number``` | int | Phone number |
| ```E_mail_address``` | str | Email address |
| ```Items``` | list[Item] | List of items sold by the seller |
## Shop
Represents the main shop system.\
Properties:
| Name | Type | Descriptions |
|:----:|:----:|:------------:|
| ```Customers``` | list[Customer] | Registered customers |
| ```Sellers``` | list[Seller] | Registered sellers |
| ```Products``` | list[Product] | Available products |

Created with ❤️ in Iran