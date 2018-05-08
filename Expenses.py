import Data

def expensesList():
    print 'Enter the bill name:'
    item = raw_input()
    print 'Enter the value of that bill:'
    price = float(raw_input())
    
    data = [{ 'item': item, 'price': price}]
    Data.inset(data)
