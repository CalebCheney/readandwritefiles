
import csv

def main():
    infile = open('EmployeePay.csv', 'r')

    employee_pay = csv.reader(infile, delimiter=',')

    #skip
    next(employee_pay)

    for record in employee_pay:
        sal_bonus = float(record[4]) * int(record[3])
        print("ID: ",record[0], '\n', "First Name: ", record[1], '\n', "Last Name: ", record[2], '\n', "Salary: ", '$', format(float(record[3]), ',.2f'), '\n', 'Bonus: ', round(format(float(record[4]), '%'), 2),  '\n', "Total Pay: ", '$', format(sal_bonus, ',.2f'), sep = '')
        input()

main()

