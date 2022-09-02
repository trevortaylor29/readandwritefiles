import csv

def main():

    infile = open('steps.csv', 'r')
    outfile = open('avg_steps.csv', 'w')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    avg_dict = {i: 0 for i in range(1, 13)}
    count_dict = {i: 0 for i in range(1, 13)}
   
    month_arr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for row in csvfile:
        avg_dict[int(row[0])] += int(row[1])
        count_dict[int(row[0])] += 1
    
    outfile.write('Month, Avg\n')
    for record in avg_dict:
        avg_dict[record] = round(avg_dict[record] / count_dict[record], 2)
        outfile.write(str(month_arr[record - 1]) + ', ' + str(avg_dict[record]) + '\n')

   
    outfile.close()
    

   
main()