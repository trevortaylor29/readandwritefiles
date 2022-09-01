def main():
    infile = open('clients.txt', 'r')
    num = 0

    for line in infile:
        num += 1
        print(num, '. ', line.rstrip('\n'), sep='')

main()