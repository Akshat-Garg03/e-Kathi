print("\n" * 5)                  
                 
import os 
from datetime import datetime 
import random
from datetime import date
import mysql.connector as mc


x = random.randint(0,1000)
u_id=str(x)


today = date.today()
current_datetime = datetime.now()

mydb = mc.connect(host="localhost", user="root", password="admin")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists ekathi")
mycursor.execute("use ekathi")

list_foods = []                    
               
navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 

def def_default():
    global list_foods, list_foods, list_item_order
    list_item_order = [0] * 100                    
def_default()                                      
                                                   

def def_main():
    while True:
        print("*" * 31 + "e-Kathi" + "*" * 34 + "\n")
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     
              "\t(O) ORDER\n"                              
              "\t(R) REPORT\n"
              "\t(P) PAYMENT\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'O'):                                          
                print("\n" * 5)                                        
                def_order_menu()                                          
                break                                                     
            elif (input_1 == 'R'):                                        
                print("\n" * 5)                                        
                def_report()                                              
                break                                                     
            elif (input_1 == 'P'):                                        
                print("\n" * 5)                                         
                def_payment()                                             
                break                                                     
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")     
        else:                                                                                     
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")        

def def_order_menu():                                                                               
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(F) FOODS AND DRINKS\n"            
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'F'):  
                print("\n" * 5)
                def_food_drink_order()
                break
            elif (input_1 == 'M'):
                print("\n" * 5)
                def_main() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_full_file_reader():                                                                        
    file_foods = open('files'+navigator_symbol+'list_foods.fsd') 
    for i in file_foods: 
        list_foods.append(str(i.strip())) 
    file_foods.close()

    file_drinks = open('files'+navigator_symbol+'list_drinks.fsd') 
    for i in file_drinks:
        list_foods.append(str(i.strip()))
    file_drinks.close()



    i = 0
    while i <= 91: 
        if 'Rs' in list_foods[i]:
            list_foods[i] = str(list_foods[i][:list_foods[i].index('Rs') - 1]) + ' ' * (46 - (list_foods[i].index('Rs') - 1)) + str(list_foods[i][list_foods[i].index('Rs'):])
            
        i += 1
def_full_file_reader()

def def_food_drink_order():
    while True:

            print("*" * 52 + "ORDER FOODS & DRINKS" + "*" * 52)
            print(" |NO| |FOOD NAME|                                  |PRICE|  |  |NO| |DRINK NAME|                                 |PRICE|")

            i = 0
            while i < len(list_foods) - 46:
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  | " + " " + "| "
                drink = "(" + str(47 + i) + ")" + " " + str(list_foods[i+46])
                print(food, drink)
                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

            input_1 = input("Please Select Your Food Item: ").upper()
            if (input_1 == 'M'):
                print("\n" * 5)
                def_main() 
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") 
                break
            if (input_1 == 'P'):
                print("\n" * 5)
                def_payment() 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1])) 
                     except:
                        pass

                     input_2 = input("How Many You Want to Order?: ").upper() 
                     if int(input_2) > 0:
                        list_item_order[int(input_1) - 1] += int(input_2) 
                        print("\n" * 5)
                        print("Successfully Ordered!")
                        def_food_drink_order() 
                        break
                     else:
                        print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def def_report():
    while True:
        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
        file_report = open('files'+navigator_symbol+'report.fsd', 'r').read() 
        print(file_report)
        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'M'):
            print("\n" * 5)
            def_main() 
            break
        elif (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") 
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_payment():
    while True:
        print("*" * 38 + "PAYMENT" + "*" * 39 + "\n") 
        total_price = 0 
        o_id = str(today.strftime("%d%m")) + u_id
        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(current_datetime)[:19] + "" + " " * 17 + "Order ID:-  " + o_id + "\n" + " " * 17 + "-" * 35 
        i = 0
        while i < len(list_item_order): 
            if(list_item_order[i] != 0):
                if (i >= 0):
                    report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i]) 
                    order_det= str(list_foods[i]) + "  x  " + str(list_item_order[i])               #order details
                    print(" " * 17 + order_det) 
                    price = (list_foods[i].split('Rs ')[1])
                    if(price[len(price) - 1] == '.'):
                        price = price.split('.')[0]
                    total_price += int(price) * list_item_order[i]  
            i += 1
        total= str(round(total_price, 2))
        print("-"*84)                                      #total bill  
        print(" " * 17 + "TOTAL PRICES:"+" "*33 + "Rs " +" "+ total)
        print("-"*84)
        print("\n")

        print("\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'P'):
            print("\n" * 10)

            o_id = str(today.strftime("%d%m")) + u_id 
            c_name = input("Enter your name: ")
            c_add= input("Enter your room no.: ")
            c_phone = input("Enter your phone number: ")
            date_time = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")

            sql_insert = "insert into order_details values"\
            "(""'" + o_id + "','" + c_name + "','" + c_add + "','" + str(c_phone) + "','" + str(total) + "','"+ str(date_time) +"')"
            mycursor.execute(sql_insert)
            mydb.commit()
            del_choice=input("Do you want food delivery to your hostel room...(y/n):\n")
            if del_choice=='y':
                print("Your Order will be delieverd in 15-20 minutes and your order id is",o_id)
            else:
                print("Your order has been placed sucessfully. Please collect your order in 15-20 minutes\n Your order id is",o_id,"\n THANK YOU FOR EATING WITH US")
            file_report = open('files'+navigator_symbol+'report.fsd', 'a') 
            file_report.write(report_new)
            file_report.close()
            def_default() 
        elif (input_1 == 'M'):
            print("\n" * 10)
            def_main() 
            break
        elif (input_1 == 'R'):
            print("\n" * 10)
            def_report() 
            break
        elif ('E' in input_1) or ('e' in input_1):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
def_main() 
