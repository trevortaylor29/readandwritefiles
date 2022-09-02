import csv

def main():
    infile = open('EmployeePay.csv', 'r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for record in csvfile:
        print('ID: ' + record[0])
        print('First Name: ' + record[1])
        print('Last Name: ' + record[2])
        bonus = (float(record[3]) * float(record[4]))
        total_pay = bonus + float(record[3])
        print('Total Pay: ' + '$' + str(total_pay), sep='')
        input()

main()

