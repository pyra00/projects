sales =[
    [1200,1500,1800],
    [2000,2100,2200],
    [1600,1700,1900]
]
grand_total=0
count=0
print('Monthly Sales Report')
for row in sales:
    for amount in row:
        print(f"${amount}", end="\t")
grand_total+=amount
count+=1
average = grand_total/count
print('\nGrand Total = $', grand_total)
print('Average Monthly Sales = $', round(average, 2))