class Item:
    def __init__(self, condition=None, category=''):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def longest_description(self):
        return "implemented in child"