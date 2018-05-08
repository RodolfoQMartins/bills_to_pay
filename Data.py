from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://127.0.0.1:27017')
db=client.bills
collection = db.myBills

my_expenses = []

def inset(data):
    print(data)
    insert = collection.insert(data)
    pprint(insert)
    print '--- Data registered successfully! ---' 

def getValues():
    for obj in collection.find():
        price = obj['price']
        my_expenses.append(price)

    dataSum(my_expenses)

def listItens():
    for obj in collection.find():
        item = obj['item']
        price = obj['price']
        print'Name: %s, Price: %s' % \
        (item,price)


def dataSum(prices):
    result = sum(prices)

    print 'Month bills: %s' % \
    (result)
    


        

