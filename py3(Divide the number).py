def sett():
    c = int(input("Define the start point : "))
    d = int(input("Define the end point : "))
    s = [c, d]
    return s

def dividee(a, b):
    num = a
    while num >= a and num <= b :
        if num % 2 != 0 and num % 3 != 0 :
            print(num)
            num += 1
            continue
        elif num % 2 != 0 or num % 3 != 0 :
            print(num)
            num += 1
        else : num += 1

def main():
    st = sett()
    dividee(st[0], st[1])

main()
