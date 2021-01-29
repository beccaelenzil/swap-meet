class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try: 
            self.inventory.remove(item)
        except:
            return False
        return item

    def get_by_category(self, category):
        filtered_list = []
        for item in self.inventory:
            if item.category == category:
                filtered_list.append(item)
        return filtered_list

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        # get first item   
        my_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]

        #swap
        self.inventory = self.inventory[1:]
        other_vendor.inventory = other_vendor.inventory[1:]

        self.inventory.append(other_first_item)
        other_vendor.inventory.append(my_first_item)

        return True

