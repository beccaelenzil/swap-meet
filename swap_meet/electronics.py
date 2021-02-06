from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=None):
        super().__init__(condition, category='Electronics')

    def __str__(self):
        return "A gadget full of buttons and secrets."
