def doubleNumber(x):
    x2 = x * 2
    return(x2)

def main():
    number = int(input("What number do you want doubled? "))
    answer = doubleNumber(number)
    print(answer)

main()