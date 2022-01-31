def main():
#Opening File
    infile = open("philosophers.txt", "r")
#Reading file to variable
   # file_contents = infile.read()
#reading line by line with right strip method
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')
#display
    #print(file_contents)
    print(line1)
    print(line2)
    print(line3)

main()

