import Data

def expensesList():
    print 'Digite o nome do gasto'
    item = raw_input()
    print 'Digite o valor do gasto'
    price = float(raw_input())
    
    data = [{ 'item': item, 'price': price}]
    Data.inset(data)
