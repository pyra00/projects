#Create a 2d List, store monthly sales
sales =[
    [1200,1500,1800],
    [2000,2100,2200],
    [1600,1700,1900]
]
print(sales)
#print one row
print(sales[0])
#print the first month sales from store one
print(sales[0][0])
#print the second months sales from store two
print(sales[1][1])

#loop thrpugh every store
for row in sales:
    print(row)
#loop through sales amounts
for row in sales:
    for amount in row:
        print(amount)
#print sales like a table
for row in sales:
    for amount in row:
        print(row, end='\t')
print()

#add a report heading
print('Monthly Sales Report')
for row in sales:
    for amount in row:
        print(f'${amount}', end= ' ')
    print()
#calculate grand total
grand_total=0
for row in sales:
    for amount in row:
        grand_total += amount
print('Grand Total = $', grand_total)
#Counter
count = 0
for row in sales:
    for amount in row:
        count+=1
    print('Count =', count)
#Find average
for row in sales:
    for amount in row: 
        grand_total+=amount
        count+=1
average = grand_total/count
print('Average = $',round(average,2))

# put it all tg
