def main():
    #write your code below this line
    count = 0

    while True:
        number = int(input("Give a number:"))

        if number == 0:
            break
        
        count = count + 1

    print("Number of numbers:", count)

if __name__ == '__main__':
    main()
