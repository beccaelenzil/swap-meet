class Vendor:
    def __init__(self, name="vendor1",inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        
        self.name = name

ruthie = Vendor(inventory=["book1", "book2"])
print("ruthie's name", ruthie.name)

glenda = Vendor(inventory=["book1", "book2"])
print("glenda's inventory", glenda.inventory)
print("glenda's name", glenda.name)

glenda.name = "Glenda"

print("glenda's name", glenda.name)
print("ruthie's name", ruthie.name)