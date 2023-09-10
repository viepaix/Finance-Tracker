"""Personal Finance Tracker:
Create a Python program that helps users track their personal finances. Users should be able to:

Add income and expense transactions with categories and amounts.
View a summary of their income, expenses, and net savings over time.
Generate reports, such as monthly or yearly financial statements, and visualize the data using
libraries like Matplotlib or Seaborn.
This project will involve data management, calculations, and possibly data visualization. 
It's a practical project that can help you improve your data handling and analysis skills."""
from datetime import date



months = ['January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December' ]

def income():
    print('~ Select in which category you want to add an income ~')
    print('- Montly')
    print('- Direct')
    print('- other')
    
    category_input = input("Category: ")
    
    if category_input == "Montly" or  category_input == "montly" or category_input == "1":
        
        month_input = input('For which month you want to add\n')
        if month_input in months:
            amounth_input = input(f'Amounth to add in "{month_input}": ')
            total = print(f"You added ${amounth_input} in {month_input}")
            print(total)
        else: 
            print(f'Invalid month please enter any of this: {months}')
      
    if category_input == "Direct" or category_input =="direct" or category_input == "2":
        direct_input = input('Specify from what is this input (e.g.: sell a book, clear a car, single thinks)\n')
        amounth_input = input(f"Amounth to add in {direct_input}: ")

        total = print(f"You added {amounth_input} from: {direct_input}")
        print(total)

    if category_input == "Other" or category_input == "other" or category_input == "3":
        other_input = input('For which month you want to add (what ever which is not direct or montly)\n')
        amounth_input = input(f'Amounth to add in "{other_input}": ')
        
        total = print(f"You added {amounth_input} from: {other_input}")
        print(total)
    else: print("Select a valid category")

print('[Personal Finance Tracker]')
print('-What you want to do?')
print("1. Add income")
print("2. Generate report")
print("3. See summary")
print("4. Visualize the data (not working)")

option = int(input("enter your option: "))
print("------------------------------------")

if option == 1:
    income()