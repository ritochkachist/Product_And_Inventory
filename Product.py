# Product Class

class Product():
  # Initialization of variables or Constructor
  def __init__(self, productName, productID, productManufacturer, wholesaleCost, retailCost, quantityInInventory, reorderLevel, productDescription):
    self.productName = productName
    self.productID = productID
    self.productManufacturer = productManufacturer
    self.wholesaleCost = wholesaleCost
    self.retailCost = retailCost
    self.quantityInInventory = quantityInInventory
    self.reorderLevel = reorderLevel
    self.productDescription = productDescription

  # Get functions to return the value of an instance variable
  def getProductName(self):
    return self.productName

  def getProductID(self):
    return self.productID

  def getManufacturer(self):
    return self.manufacturer

  def getWholesaleCost(self):
    return self.wholesaleCost

  def getRetailCost(self):
    return self.retailCost

  def getQuantityInInventory(self):
    return self.quantityInInventory

  def getReorderLevel(self):
    return self.reorderLevel

  def getpProductDescription(self):
    return self.productDescription

  # Set functions to modify the value of an instance variable
  def setProductName(self, newName):
    self.productName = newName

  def setProductID(self, newID):
    self.productID = newID

  def setManufacturer(self, newManufacturer):
    self.manufacturer = newManufacturer

  def setWholesaleCost(self, newWholesaleCost):
    self.wholesaleCost = newWholesaleCost

  def setRetailCost(self, newRetailCost):
    self.retailCost = newRetailCost

  def setQuantityInInventory(self, newQuantityInInventory):
    self.quantityInInventory = newQuantityInInventory

  def setReorderLevel(self, newReorderLevel):
    self.reorderLevel = newReorderLevel

  def setProductDescription(self, newDescription):
    self.productDescription = newDescription

  # Reorder Warning checks the reorder level against the quantity in inventory and returns Boolean to indicate if the item needs to be reordered
  def reorderWarning(self):
    if self.quantityInInventory <= self.reorderLevel:
      return True
    else:
      return False

  # Inventory Value returns the value of the current products inventory by calculating Qty * wholesale cost
  def inventoryValue(self):
    value = self.quantityInInventory * self.wholesaleCost
    return value

  # Details return the basic details about a product such as product name and ID number
  def details(self):
    pd = "The product name: " + self.productName + "\nThe product ID: " + self.productID + "\nThe product manufacturer: " + self.productManufacturer + "\nThe whole sale cost: " + str(self.wholesaleCost) + "\nThe retail cost: " + str(self.retailCost) + "\nThe quantity in inventory: " + str(self.quantityInInventory) + "\nThe reorder level: " + str(self.reorderLevel) + "\nThe description of the product: " + self.productDescription
    return pd  
    