#Adrian Gomez
#20119988

def main():
    x=eval(input("Enter a five-digit integer number: "))
    A= x%10
    B= x//10
    C= B%10
    D= B//10
    E= D%10
    F= D//10
    G= F%10
    H= F//10
    print(H, G, E, C, A)
    print(A, C, E, G, H)
    print(H)
    print(G)
    print(E)
    print(C)
    print(A)
main()
