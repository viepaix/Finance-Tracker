"""Personal Finance Tracker:
Create a Python program that helps users track their personal finances. Users should be able to:

Add income and expense transactions with categories and amounts.
View a summary of their income, expenses, and net savings over time.
Generate reports, such as monthly or yearly financial statements, and visualize the data using
libraries like Matplotlib or Seaborn.
This project will involve data management, calculations, and possibly data visualization. 
It's a practical project that can help you improve your data handling and analysis skills."""

import sys
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December' ]

input_months = []


def income():
    print('~ Select in which category you want to add an income ~')
    print('- Montly')
    print('- Direct')
    print('- other')
    
    category_input = input("Category: ")
    
    if category_input == "Montly" or  category_input == "montly" or category_input == "1":
        
        month_input = input('For which month you want to add\n')
        if month_input in months:
            try: 
                amount_input = float(input(f'Amounth to add in "{month_input}": '))
                total = print(f"You added ${amount_input} in {month_input}")
                
                input_months.append({month_input : amount_input})

                return total
            except ValueError: print('Invalid amount')
        else: 
            print(f'Invalid month please enter any of this: {months}')
      
    elif category_input == "Direct" or category_input =="direct" or category_input == "2":
        month_input = input('For which month you want to add\n')
        direct_input = input('Specify from what is this input (e.g.: sell a book, clear a car, single thinks)\n')
        amount_input = input(f"Amount to add in {direct_input}: ")

        input_months.append({month_input : amount_input})

        total = print(f"You added {amount_input} from: {direct_input}")
        return total

    elif category_input == "Other" or category_input == "other" or category_input == "3":
        month_input = input('For which month you want to add\n')
        other_input = input('From where is this money (what ever which is not direct or montly)\n')
        amount_input = input(f'Amounth to add in "{other_input}": ')
        
        input_months.append({month_input : amount_input})
        
        total = print(f"You added {amount_input} from: {other_input}")
        return total
    else: print("Select a valid category")

def summary():
    summary_data = {}
    
    for month in months:
        total_income = 0
        for entry in input_months:
            if month in entry:
                total_income += float(entry[month])
        summary_data[month] = total_income
        
    

    print("Summary of income per month")
    for month, total in summary_data.items():
        print(f"{month}: ${total}")
        
    print("------------------------------------")

def report():
    
    if input_months == []:
        print('⟪ Nothing have been added ⟫')
    else: 
        report_print = print(f'You have added this: {input_months}')
        return report_print
    return None

def graphic():
    
    summary_data = {}
    
    for month in months:
            total_income = 0
            for entry in input_months:
                if month in entry:
                    total_income += float(entry[month])
            summary_data[month] = total_income
    
    for month, total in summary_data.items():
        x_data = month
        y_data = total
        
        
        plt.ylim(top=6000 ,bottom=0)
        
        plt.xlabel('Months')
        plt.ylabel('Total income')
        
        plt.bar(x_data, y_data)
    show_graphic = plt.show()
        
    return show_graphic

while True:
    print('[Personal Finance Tracker]')
    print('-What you want to do?')
    print("1. Add income")
    print("2. Generate report")
    print("3. See summary")
    print("4. Visualize the data")
    print("5. Exit")

    option = int(input("enter your option: "))
    print("------------------------------------")

    if option == 1:
        income()
        
    elif option == 2:
        report() 
        
    elif option == 3:
        summary()
        
    elif option == 4:
        graphic()
        
    elif option == 5:
        sys.exit()
        
    else: print('Error value')