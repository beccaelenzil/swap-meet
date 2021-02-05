from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=None):
        Item.__init__(self, category='Clothing')
        self.condition=condition

    def __str__(self):
        return "The finest clothing you could wear."