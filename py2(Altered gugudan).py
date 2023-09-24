# n단(n : 2 ~ 19) n is input.
# When n is even : result is always even, too.
# Thus n -> odd : result : odd, even taking turns.
# result -> odd -> result = result - 2n + 1

def gugu():
    print("Range of n : 2 ~ 20")
    n = int(input("Define n : "))
    if n % 2 == 0 : 
        for i in range(1, 10) : 
            result1 = n*i
            print(result1)
    if n % 2 != 0 :
        for j in range(1, 10) :
            if j % 2 == 1 :
                o_result2 = n*j  # original value
                a_result2 = n*j + 2*n + 1   # altered value
                print(n, " x ", j, " = ", o_result2, "->", a_result2,"(", n, "x", j, "+", "2", "*", n, "+", "1", ")")
            else : 
                result2 = n*j
                print(n, " x ", j, " = ", result2)
def repeatt():
    a = int(input("Decide the number of repetition : "))
    return a

def main():
    rpt = repeatt()
    while(rpt != 0) :
        gugu()
        rpt -=1
        print("\n")

main()
