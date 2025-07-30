import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
np.random.seed(1)
cake = np.random.randint(20,50,size=7)
cookie = np.random.randint(30,60,size=7)
brownie = np.random.randint(10,30,size=7)
muffin = np.random.randint(5,25,size=7)
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
data = {
    'Cake':cake,
    'Cookie':cookie,
    'Brownie':brownie,
    'Muffin':muffin

}
df = pd.DataFrame(data,index=days)
print(df)
Total_sales = df.sum()
print("Total sales this week")
print(Total_sales)
# Total_sales.plot(Kind="bar", color="orange")
# plt.title("weeekly sales per item")
# plt.ylabel("Total Items Sold")
# plt.xlabel("Bakery Items")
# plt.grid(axis="y")
# plt.show
items = Total_sales.index
values=Total_sales.values
plt.bar(items,values,color='orange')
plt.title("weeekly sales per item")
plt.ylabel("Total Items Sold")
plt.xlabel("Bakery Items")
plt.grid(axis="y")
plt.show()
