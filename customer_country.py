import csv
def main():

    infile = open('customers.csv', 'r')
    outfile = open('customer_country.csv', 'w')

    csvfile = csv.reader(infile, delimiter=',')
    

    rowcount = 0

    for record in csvfile:
        outfile.write(record[1] + ' ' + record[2] + ',' + ' ' + record[4])
        
        outfile.write('\n')
    
            
        

    outfile.close()
        

main()
