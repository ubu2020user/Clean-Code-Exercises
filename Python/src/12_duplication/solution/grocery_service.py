from typing import List, Any

from shopping_item import ShoppingItem
from customer import Customer


class GroceryService:
    def print_list(self, title: str, items: List[Any], sort_key: str, format_item: callable) -> None:
        print(f"=========== {title} ===========")
        sorted_items = sorted(items, key=lambda item: getattr(item, sort_key))
        print("[")
        for i, item in enumerate(sorted_items):
            print(format_item(item), end='')
            if i < len(sorted_items) - 1:
                print(",\n")
            else:
                print("\n")
        print(f"=========== End of {title} ===========")

    def print_customer_list(self, customer_list: List[Customer]) -> None:
        self.print_list(
            title="Customer List",
            items=customer_list,
            sort_key="last_name",
            format_item=lambda customer: f"{{ 'first_name': '{customer.first_name}', 'last_name': '{customer.last_name}'}}"
        )

    def print_shopping_item_list(self, shopping_item_list: List[ShoppingItem]) -> None:
        self.print_list(
            title="Shopping Item List",
            items=shopping_item_list,
            sort_key="name",
            format_item=lambda item: f"{{ 'name': '{item.name}', 'price': '{item.price}'}}"
        )
