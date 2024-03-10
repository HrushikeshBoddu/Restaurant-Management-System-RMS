# Importing necessary libraries
from tkinter import Tk
from tkcalendar import Calendar


class RMS:
    # Class attributes for the menu and customer tracking
    menu = {'chicken biryani': 120, 'mutton biryani': 160, 'egg biryani': 100}
    Noof_Customer = 0
    CustomerInfo = {}

    def __init__(self):
        # Taking customer details and handling input errors
        name = input("Enter your Name: ")
        while True:
            try:
                contact = int(input("Enter your Phone Number: "))
                break
            except:
                print('Enter the number, but you entered a character.')
        while True:
            try:
                persons = int(input("Number of Persons for feast: "))
                break
            except:
                print('Enter the number, but you entered a character.')
        while True:
            try:
                TableNumber = int(input('Enter Table Number: '))
                break
            except:
                print('Enter the number, but you entered a character.')

        # Date selection using tkinter Calendar widget
        print("Select Your Date:")
        root = Tk()
        root.geometry("200x200")
        cal = Calendar(root, selectmode='day', year=2023, month=11)
        cal.pack(pady=20)
        root.mainloop()
        date = cal.get_date()

        # Additional reservation details
        time = input("What time You Would like to Feast: (Lunch/Dinner) ")
        print()
        self.BillItems()  # Calls the method to calculate the bill based on selected items

        # Displaying the booking details
        print("****************** Booking Details **********************")
        print("Name: ", name)
        print("Contact: ", contact)
        print("Feast Date: ", date)
        print("Time Slot: ", time)
        print("Number of Persons: ", persons)
        print('Total items: ', self.NoOfItems)
        print('Total bill: ', self.total)

        # Updating the class attributes for customer tracking
        RMS.CustomerInfo[TableNumber] = [name, persons, contact]
        RMS.Noof_Customer += 1

    @classmethod
    def ShowCustomerInfo(cls):
        # Class method to print sorted customer information
        for keys, values in sorted(cls.CustomerInfo.items()):
            print(keys, ":", values)

    def ShowMenu(self):
        # Instance method to show the menu
        for key, value in self.menu.items():
            print(key, ':', value)

    def AddItemsMenu(self):
        # Allows adding items to the menu
        def AddingItems(Dish_Name, Dish_Price):
            self.menu[Dish_Name] = Dish_Price

        while True:
            self.Dish_Name = input("Enter Dish Name: ").lower()
            if self.Dish_Name == "done":
                print('Completed Adding Dishes Into Menu')
                break
            else:
                self.Dish_Price = int(input(f'Enter price of the {self.Dish_Name}: '))
                AddingItems(self.Dish_Name, self.Dish_Price)

    def BillItems(self):
        # Calculates the total bill based on selected items
        self.total = 0
        self.NoOfItems = 0
        self.ShowMenu()
        while True:
            self.AddingDish = input('Enter Dish Name: ').strip().lower()
            if self.AddingDish == "done":
                print('Great choice')
                break
            elif self.AddingDish not in self.menu:
                print(f'Sorry, {self.AddingDish} is out of stock')
            else:
                self.total += self.menu[self.AddingDish]
                self.NoOfItems += 1

    @classmethod
    def RemoveItemMenu(cls):
        # Allows removing items to the menu
        while True:
            cls.Remove_Item = input('Enter Item You Want To Remove From Menu: ')
            if cls.Remove_Item == 'done':
                print('Completed removing')
                break
            elif cls.Remove_Item in cls.menu:
                cls.menu.pop(cls.Remove_Item)
                print(f'{cls.Remove_Item} successfully removed from menu')
            else:
                print(f'{cls.Remove_Item} not in menu')
