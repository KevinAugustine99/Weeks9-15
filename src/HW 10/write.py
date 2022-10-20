import random
def main():

    file1 = open("data7.txt","w") 
    for _ in range(25):
        file1.write(str(random.randint(1,100)))
        file1.write("\n")
    file1.close()

main()