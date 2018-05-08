from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://127.0.0.1:27017')
db=client.gastos
collection = db.meusGastos

my_expenses = []

def inset(data):
    print(data)
    insert = db.meusGastos.insert(data)
    pprint(insert)
    print '--- Dado cadastrado com succeso! ---' 

def getValues():
    for obj in collection.find():
        price = obj['price']
        my_expenses.append(price)

    dataSum(my_expenses)

def listItens():
    for obj in collection.find():
        item = obj['item']
        price = obj['price']
        print'Nome: %s, Custo: %s' % \
        (item,price)


def dataSum(prices):
    result = sum(prices)

    print 'Gasto mensais de: %s' % \
    (result)
    


        

