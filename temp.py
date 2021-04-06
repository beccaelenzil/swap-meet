class Currency:
    def __init__(self, value, unit="dollar"):
        self.value = value
        self.unit = unit
    
    def converter(self, other_unit):
        pass

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else: 
            return False

    def str(self):
        return f"{self.value} {self.unit}s"


five = Currency(5)
one = Currency(1)

print(one < five)
print(str(five))


# class Item:
#     def __init__(self, condition=None, category=''):
#         self.category = category
#         self.condition = condition

# class Clothing(Item):
#     def __init__(self, condition=None, category='clothing'):
#         super().__init__(category=category)
#         # self.category = category
#         # self.condition = condition
#         #pass
    


# shirt = Clothing(condition=5)
# print(shirt.condition)
# print(shirt.category)
    

