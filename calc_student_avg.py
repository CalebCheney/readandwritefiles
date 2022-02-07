import csv

def main():
    infile = open('Student_Scores.csv', 'r')
    outfile = open('student_avg.csv', 'w')

    #define file object
    student_file = csv.reader(infile, delimiter = ',')

    #skip headers
    next(student_file)

    #write headers
    outfile.write('Name' + ',' + 'AvgScore' + '\n')

    for record in student_file:
        name = record[0]
        test1 = record[1]
        test2 = record[2]
        test3 = record[3]
        avg = round((int(record[1]) + int(record[2]) + int(record[3])) / 3, 2) 
        outfile.write(name + ',' + str(avg) + '\n')

    outfile.close()
    infile.close()

main()