class Inventory:
    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.items = []
        self.remaining_capacity = self.capacity

    def add_item(self, item):
        if self.remaining_capacity > 0:
            self.items.append(item)
            self.remaining_capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        items = ", ".join(self.items)
        return f"Items: {items}.\nCapacity left: {self.remaining_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
