from typing import List

from shopping_item import ShoppingItem
from customer import Customer


class GroceryService:
    def print_customer_list(self, customer_list: List[Customer]) -> None:
        print("=========== Customer List ===========")
        sorted_customer_list = sorted(customer_list, key=lambda customer: customer.last_name)
        print("[")
        for i, customer in enumerate(sorted_customer_list):
            print(f"{{ 'first_name': '{customer.first_name}', 'last_name': '{customer.last_name}'}}", end='')
            if i < len(sorted_customer_list) - 1:
                print(",\n")
            else:
                print("\n")
        print("=========== End of Customer List ===========")

    def print_shopping_item_list(self, shopping_item_list: List[ShoppingItem]) -> None:
        print("=========== Shopping Item List ===========")
        sorted_shopping_item_list = sorted(shopping_item_list, key=lambda item: item.name)
        print("[")
        for i, item in enumerate(sorted_shopping_item_list):
            print(f"{{ 'name': '{item.name}', 'price': '{item.price}'}}", end='')
            if i < len(sorted_shopping_item_list) - 1:
                print(",\n")
            else:
                print("\n")
        print("=========== End of Shopping Item List ===========")
