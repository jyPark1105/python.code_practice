def inputt():
    a = int(input("first value : "))
    b = int(input("second value : "))
    s = [a, b]
    return s

def GCD(num1, num2):
    if num1 > num2 : num = num1
    elif num1 < num2 : num = num2
    else : return num1 # num1 = num2
    while num > 0 :
        if num1 % num == 0 and num2 % num == 0 : break
        else : num -= 1
    return num

def main():
    st = inputt()
    print (GCD(st[0], st[1]))
    return 0

main()