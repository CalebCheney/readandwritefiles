def main():
#Variable Names
    name1 = "John Locke"
    name2 = "David Hume"
    name3 = "Edmund Bruke"
#File Writing
    outfile = open('philosophers.txt', 'w')

    outfile.write(name1 + '\n')
    outfile.write(name2 + '\n')
    outfile.write(name3 + '\n')
#Close File
    outfile.close()
#Appending Name
def add_my_name():
    outfile = open("philosophers.txt", "a")

    outfile.write("Caleb Cheney\n")

    outfile.close()

main()
add_my_name()