# Margarita Chistiakova
# 12/2/2022
# Final Project! 

from Inventory import Inventory

myInventory = Inventory()

print("Welcome to the Inventory Program!")

choice = 0
while choice != 3:
  print("Please choose your option from the menu below:")
  print("1. Add a product to inventory")
  print("2. Edit an existing inventory item")
  print("3. Quit")
  choice = int(input())

  if choice == 1:
    print("Please enter the name of the product:")
    name = input()
    print("Please enter product ID")
    iD = input()
    print("Please enter product manufacturer")
    manufacturer = input()
    print("Please enter product wholesale cost")
    wholesaleCost = input()
    print("Please enter product retail cost")
    retailCost = input()
    print("Please enter product quantity in inventory")
    quantityInInventory = input()
    print("Please enter reorder level of the product")
    reorderLevel = input()
    print("Please enter description of the product")
    description = input()

    myInventory.addProductToInventory(name, iD, manufacturer, wholesaleCost, retailCost, quantityInInventory, reorderLevel, description)
    
    myInventory.allInventory()
    
  elif choice == 2:
    print("Please choose your options from the menu below:")
    print("1. Edit the name of a product")
    print("2. Edit product ID")
    print("3. Edit product manufacturer")
    print("4. Edit product wholesale cost")
    print("5. Edit product retail cost")
    print("6. Edit product quantity in inventory")
    print("7. Edit product reorder level")
    print("8. Edit description of the product")
    choice2 = int(input())
    if choice2 == 1:
      print("Please enter the ID of the product you wish to change: ")
      iD = input()
      print("Please enter the new name of the product: ")
      name = input()
      myInventory.modifyProductName(iD, name)

    elif choice2 == 2:
      print("Please enter the ID of the product you wish to change: ")
      iD = input()
      print("Please enter new ID")
      iD = input()
      myInventory.modifyProductID(iD, iD)

    elif choice2 == 3:
      print("Please enter the ID of the product you wish to change: ")
      iD = input()
      print("Plese enter a new manufacturer of the product")
      manufacturer = input()
      myInventory.modifyManufacturer(iD, manufacturer)

    elif choice2 == 4:
      print("Please enter the ID of the product you wish to change: ")
      iD = input()
      print("Please enter the new wholesale cost of the product")
      wholesaleCost = input()
      myInventory.modifyWholesaleCost(iD, wholesaleCost)

    elif choice2 == 5:
      print("Please enter the ID of the product you wish to change: ")
      iD = input()
      print("Please enter the retail cost of the product")
      retailCost = input()
      myInventory.modifyRetailCost(iD, retailCost)

    elif choice2 == 6:
      print("Please enter the ID of the product you wish to change: ")
      iD = input()
      print("Please enter a new quantity in inventory for this product ")
      quantityInInventory = input()
      myInventory.modifyDescription(iD, quantityInInventory)

    elif choice2 == 7:
      print("Please enter the ID of the product you wish to change: ")
      iD = input()
      print("Please enter the reorder level of the product: ")
      reorderLevel = input()
      myInventory.modifyReorderLevel(iD, reorderLevel)

    elif choice2 == 8:
      print("Please enter the ID of the product you wish to change: ")
      iD = input()
      print("Please enter the description of the product: ")
      description = input()
      myInventory.modifyDescription(iD, description)