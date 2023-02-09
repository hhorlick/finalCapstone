###########Shoe inventory manager###########


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

       
    def get_cost(self): #return cost of shoe 
        cost = self.cost
        return cost
    
    def get_code(self): #return code of shoe 
        code = self.code
        return code

    def get_country(self): #return country of shoe 
        country = self.country
        return country 

    def get_product(self): # return name of shoe 
        product = self.product
        return product

    def get_quantity(self): #return quantity of shoe
        quantity = self.quantity
        quantity = int(quantity)
        return quantity
    
    def change_quantity(self,new_quantity): #change quantity of shoe
        self.quantity =(int(self.quantity.strip()) + new_quantity)

    def __str__(self): #print out details of shoe
        print (f"""
        Product  = {self.product}
        Country  = {self.country}
        Code     = {self.code}
        Cost     = £{self.cost}
        Quantity = {self.quantity}
        """)

#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============
'''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def read_shoes_data():
    file = None
    try:
        f = open('inventory.txt','r')
        lines = f.readlines()[1:]
        f.close()
        for line in lines:
            item = line.split(",")
            country = item[0]
            code = item[1]
            product = item [2]
            cost = item [3]
            quantity = item [4].strip()
            new_shoe_name = "Shoe" + str(len(shoe_list))
            new_shoe_name = Shoe(country, code, product, cost, quantity) # Create new object 
            shoe_list.append(new_shoe_name) #add new object to shoe list 

    except FileNotFoundError as error: #Error message for no file 
            print("The file that you are trying to open does not exist")
            print(error)
    finally:
            if file is not None:
                file.close()

#function for writing data held in shoe list to file 
def write_shoes_data():
    f=open('inventory.txt','a')
    f.write("Country,Code,Product,Cost,Quantity\n")
    i=0
    while i <len(shoe_list):
        f.write(str(shoe_list[i].get_country()) + "," + str(shoe_list[i].get_code()) + "," + str(shoe_list[i].get_product()) + "," + str(shoe_list[i].get_cost()) + "," + str(shoe_list[i].get_quantity()))
        f.write("\n")
        i+=1
    f.close()
   
 
def capture_shoes():

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input ("What Country does the shoe come from?") 
    code = input ("What is the code for this ")
    while len(code) != 8 or code[0:3] != "SKU": #Check that it is a real code 
        code = input("That is an invalid code. Please enter it again")
    product = input ("What is the product called?")
    while True: # ensure input is a number 
            try: 
                cost = float (input("What is the cost of the product? \n"))
                break
            except Exception:
                print (f"Oops! that is not a vaild number")
    while True: # ensure input is a number 
            try: 
                quantity = int (input("What is the Quantity of the product? \n"))
                break
            except Exception:
                print (f"Oops! Answer must be a whole number")
    new_shoe_name = "Shoe" + str(len(shoe_list))
    new_shoe_name = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe_name)
    print ("New shoe added. Details below")
    print (shoe_list[0].__str__())

def view_all():

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for item in shoe_list:
        item.__str__()

def re_stock():

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    quantity_dic = {} #create empty dictionary
    item_index = 0
    for item in shoe_list:
        item_quantity =int(item.get_quantity())
        quantity_dic [item_index] = item_quantity # populate empty dictionary 
        item_index +=1
    sorted_quantity_list = sorted(quantity_dic.items(), key=lambda x:x[1]) # sort dictionary into ascending
    sorted_quantity_dic = dict(sorted_quantity_list)
    temp = min(sorted_quantity_dic.values())
    lowest_item = [key for key in sorted_quantity_dic if sorted_quantity_dic[key] == temp]
    print ("The following item has the lowest stock")
    shoe_list[lowest_item[0]].__str__() #shows lowest stock item 
    re_stock_amount = int(input("What quantity of this shoe would you like to order?"))
    shoe_list[lowest_item[0]].change_quantity(re_stock_amount)
    print (f"{re_stock_amount} have been added. The new stock amount is shown below")
    shoe_list[lowest_item[0]].__str__() #shows shoe with updated stock info
    write_shoes_data() # writes new information to file


def search_shoe(code_input):
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''
    code_list = []
    i=0
    while i < len(shoe_list): # generate list of all the codes 
        code_list.append(shoe_list[i].get_code())
        i+=1
    
    try :
        code_list.index(code_input) # find index position of code 
        code_index = code_list.index(code_input)
        shoe_list[code_index].__str__()
    
    except ValueError :
        print ("Code doesn't exist")
        code_input = ("Please enter another code")
    
    
    
   

def value_per_item():
    ''' 
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    total_value_list = []
    i=0
    while i < len(shoe_list):
        shoe_value =float(shoe_list[i].get_cost()) * float(shoe_list[i].get_quantity()) 
        total_value_list.append(shoe_value)
        print (shoe_list[i].get_product() + " Total value = £" + str(shoe_value))
        i+=1
    
    

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    quantity_dic = {}
    item_index = 0
    for item in shoe_list:
        item_quantity =int(item.get_quantity())
        quantity_dic [item_index] = item_quantity # generate dictionary with quantities 
        item_index +=1
    sorted_quantity_list = sorted(quantity_dic.items(), key=lambda x:x[1]) # Sort the dictionary into descending order 
    sorted_quantity_dic = dict(sorted_quantity_list)
    temp = max(sorted_quantity_dic.values())
    highest_item = [key for key in sorted_quantity_dic if sorted_quantity_dic[key] == temp] #get highest item 
    print ("The following item has the highest stock")
    shoe_list[highest_item[0]].__str__()


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main():
    read_shoes_data()
    while True:
        user_input = input("""
        What action would you like to take?
        cs -- Capture new shoe data 
        va -- View all shoes
        rs -- ReStock shoes
        ss -- Search shoes
        gv -- Get value of stock
        hq -- Get shoe with highest quantity
        ex -- Exit\n""").lower()

        if user_input == "cs":
            capture_shoes()
        
        elif user_input == "va":
            view_all()
        
        elif user_input == "rs":
            re_stock()
        
        elif user_input == "ss":
            code_input = (input("Please enter the code for a shoe"))
            search_shoe(code_input)
        
        elif user_input == "gv":
            value_per_item()
        
        elif user_input == "hq":
            highest_qty()


        elif user_input == "ex":
            print ("Goodbye")
            break
        
        else:
            user_input = ("that is not a valid input. Please try again")

main()
