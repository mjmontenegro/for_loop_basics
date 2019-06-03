def basic():
    for num in range(150):
        print(num)

def multOfFive():
    for num in range(5,1001,5):
        print(num)

def countingDojo():
    for num in range(1, 101):
        if not (num % 5):
            if not (num % 10):
                print("Coding Dojo")
            else:
                print("Coding")
        else:
            print(num)

def hugeSucker():
    sum = 0
    for num in range(1,500001,2):
        sum += num
    print(sum)

def countdown():
    for num in range(2018, 0, -4):
        print(num)

def flexCounter():
    lowNum = 2
    highNum = 9
    mult = 3
    for num in range(lowNum, highNum + 1):
        if not (num % mult):
            print(num)

