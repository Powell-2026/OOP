A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A>B>C:
    print("A is the greatest, C is the smallest")
elif A>C>B:
    print("A is the greatest, B is the smallest")
elif B>A>C:
    print("B is the greatest, C is the smallest")
elif B>C>A:
    print("B is the greatest, A is the smallest")
elif C>B>A:
    print("C is the greatest, A is the smallest")
elif C>A>B:
    print("C is the greatest, B is the smallest")
elif A==B>C:
    print("A and B are equal and both greater than C")
elif A==C>B:
    print("A and C are equal and both greater than B")
elif A==B<C:
    print("A and B are equal and both less than C")
elif A==C<B:
    print("A and C are equal and both less than B")
elif C==B>A:
    print("C and B are equal and both greater than A")
elif C==B<A:
    print("C and B are equal and both less than A")