
import csv

count = 0

customers = open('customers.csv','r')
outfile = open('customer_country.csv','w')

customer_file = csv.reader(customers, delimiter=',')

#to skip line header
next(customer_file)

outfile.write("FirstName" +','+ "LastName" +','+ "Country" + '\n')


for record in customer_file:
    first_name = record[1]
    last_name = record[2]
    country = record[4]
    count += 1
    outfile.write(first_name + ',' + last_name + ',' + country + '\n')

outfile.close()
customers.close()
print("Total Numbers of Customers:", count)



    

