def matrix_input():
    print(" ")
    print("===================================")
    print(" ")
    print("Matrix A:")
    a11 = int(input("Enter a\u2081\u2081: "))
    a12 = int(input("Enter a\u2081\u2082: "))
    a21 = int(input("Enter a\u2082\u2081: "))
    a22 = int(input("Enter a\u2082\u2082: "))
    print(" ")
    print("Matrix B:")
    b11 = int(input("Enter a\u2081\u2081: "))
    b12 = int(input("Enter a\u2081\u2082: "))
    b21 = int(input("Enter a\u2082\u2081: "))
    b22 = int(input("Enter a\u2082\u2082: "))
    print(" ")
    print("===================================")
    print(" ")
    return a11, a12, a21, a22, b11, b12, b21, b22

def matrix_represent():
    print("Matrix A:")
    print(" ")
    print(a11,"", a12), print(a21,"", a22)
    print(" ")
    print("Matrix B:")
    print(" ")
    print(b11,"", b12), print(b21,"", b22)
    print(" ")
    print("===================================")
    print(" ")
    return matrix_represent

def matrix_multiply():
    c11 = (a11*b11) + (a12*b21)
    c12 = (a11*b12) + (a12*b22)
    c21 = (a21*b11) + (a22*b21)
    c22 = (a21*b12) + (a22*b22)
    return c11, c12, c21, c22,

def matrix_result():
    print("Result A x B:")
    print(" ")    
    print(c11,"", c12), print(c21,"", c22)
    print(" ")
    print("===================================")
    print(" ")
    return matrix_result

def main():
    global a11, a12, a21, a22, b11, b12, b21, b22
    global c11, c12, c21, c22
    (a11, a12, a21, a22, b11, b12, b21, b22) = matrix_input()
    matrix_represent()
    (c11, c12, c21, c22) = matrix_multiply()
    matrix_result()