# Inventory Class

from Product import Product

class Inventory():
  def __init__(self):
    self.inventory = []

  def addProductToInventory(self, productName, productID, productManufacturer, wholesaleCost, retailCost, quantityInInventory, reorderLevel, description):
    ###In the line below, I am sending values to the function, I should not send self!
    newProduct = Product(productName, productID, productManufacturer, wholesaleCost, retailCost, quantityInInventory, reorderLevel, description)
    
    self.inventory.append(newProduct)

  def sellProduct(self, quantityInInventory, productID):
    for item in self.inventory:
      if productID == item.getproductID():
        item.setQuantityInInventory(quantityInInventory)

  def currentInventory(self, productID):
    for item in self.inventory:
      if productID == item.getproductID():
        return Product.inventoryValue() 

  def getNameofProduct(self, idNumber):
    for item in self.inventory:  
      if idNumber == item.getProductID():
        return item.getProductName()

  def getIDofProduct(self, idNumber):
    for item in self.inventory:
      if idNumber == item.getIDofProduct():
        return item.getIDofProduct()

  def getManufacturer(self, idNumber):
    for item in self.inventory:
      if idNumber == item.getManufacturer():
        return item.getManufacturer()

  def getWholesaleCostofProduct(self, idNumber):
    for item in self.inventory:
      if idNumber == item.getWholesaleCostofProduct():
        return item.getwWholesaleCostofProduct()

  def getRetailCostofProduct(self, idNumber):
    for item in self.inventory:
      if idNumber == item.getRetailCostofProduct():
        return item.getRetailCostofProduct()

  def getQuantityInInventoryofProduct(self, idNumber):
    for item in self.inventory:
      if idNumber == item.getQuantityInInventoryofProduct():
        return item.getQuantityInInventory()

  def getReorderLevelofProduct(self, idNumber):
    for item in self.inventory:
      if idNumber == item.getReorderLevelofProduct():
        return item.getReorderLevelofProduct

  def getDescriptionofProduct(self, idNumber):
    for item in self.inventory:
      if idNumber == item.getDescriptionofProduct():
        return item.getDescriptionofProduct()
        
  # goes through the list and sends the details of each product to an output file called inventory.txt
  def allInventory(self):
    target = open("inventory.txt", "w")
    for item in self.inventory:
      target.write(item.details())
      target.write("\n")
    target.close()

  # goes through the list calling the Reorder Warning function for each Product
  def reorderList(self):
    target = open("reorderlist.txt", "w")
    for item in self.inventory:
      if item.reorderWarning == True:
        target.write(item.details())
        target.write("\n")
    target.close()
        
  # returns boolean that indicates if an item is in the inventory
  def isAnItem(self, productID):
    for item in self.inventory:
      if productID == self.getProductID():
        return True
    return False

  # relay functions
  def modifyProductName(self, productID, newName):
    for item in self.inventory:
      if(productID == item.getProductID()):
        item.setProductName(newName)

  def modifyProductID(self, productID, newID):
    for item in self.inventory:
      if(productID == item.getProductID()):
        item.setProductName(newID)

  def modifyManufacturer(self, productID, newManufacturer):
    for item in self.inventory:
      if(productID == item.getProductID()):
        item.setProductName(newManufacturer)

  def modifyWholesaleCost(self, productID, newPrice):
    for item in self.inventory:
      if(productID == self.getProductID()):
        item.setProductName(newPrice)

  def modifyRetailCost(self, productID, newPrice):
    for item in self.inventory:
      if(productID == item.getProductID()):
        item.setRetailCost(newPrice)

  def modifyQuantityInInventory(self, productID, newQuantityInInventory):
    for item in self.inventory:
      if(productID == item.getProductID()):
        item.setProductName(newQuantityInInventory)

  def modifyReorderLevel(self,productID, newReorderLevel):
    for item in self.inventory:
      if(productID == item.getProductID()):
        item.setProductName(newReorderLevel)

  def modifyDescription(self, productID, name):
    for item in self.inventory:
      if(productID == item.getProductID()):
        return item.getProductName()