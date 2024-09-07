actual_cost= float(input("Please Enter The Actuall Product Amount:"))
sale_amount= float(input("Please Enter the Sale Amount:"))

if(sale_amount > actual_cost):
    amount= sale_amount - actual_cost
    print("Total Profit = {0}".format(amount) )
    
else:
    print("No Profit!!!")

    

