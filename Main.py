import Expenses
import Data

def menu():
    tab = ''
    while(tab != '0'):
        print '--- Enter 1 to add a new bill, 2 to calculate all the monthly spendings, 3 to list all the bills info and 0 to exit. ---'
        tab = raw_input()

        if(tab == '1'):
            Expenses.expensesList()

        elif(tab == '2'):
            Data.getValues()

        elif(tab == '3'):
            Data.listItens()

menu()