from shopping_item import ShoppingItem
from grocery_service import GroceryService
from customer import Customer

if __name__ == "__main__":
    article_list = [
        ShoppingItem("T-Shirt", 30),
        ShoppingItem("Branded, limited edition Cap", 100),
    ]
    guest_list = [Customer("Ralf", "Schuhmacher"), Customer("Ali", "Muhammed")]
    grocery_service = GroceryService()
    grocery_service.print_shopping_item_list(article_list)
    grocery_service.print_customer_list(guest_list)
