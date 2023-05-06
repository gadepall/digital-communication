def main():
    a = float(input('Enter probability of A :'))
    b = float(input('Enter probability of B :'))

    P_A_and_B = a*b
    P_A_andNot_B = a*(1-b)
    P_A_or_B = a + b - a*b
    P_neither_A_nor_B = 1 - (a + b - a*b)

    print('P(A and B) = ',P_A_and_B)
    print('P(A and not B) = ',P_A_andNot_B)
    print('P(A or B) = ',P_A_or_B)
    print('P(neither A nor B) = ',P_neither_A_nor_B)

if __name__=='__main__':
    main()




