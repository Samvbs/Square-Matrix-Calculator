def matrix_input():
    print(" ")
    print("===================================")
    print(" ")
    print("Matrix A:")
    a11 = int(input("Enter a\u2081\u2081: "))
    a12 = int(input("Enter a\u2081\u2082: "))
    a13 = int(input("Enter a\u2081\u2083: "))
    a21 = int(input("Enter a\u2082\u2081: "))
    a22 = int(input("Enter a\u2082\u2082: "))
    a23 = int(input("Enter a\u2082\u2083: "))
    a31 = int(input("Enter a\u2083\u2081: "))
    a32 = int(input("Enter a\u2083\u2082: "))
    a33 = int(input("Enter a\u2083\u2083: "))
    print()
    print("Matrix B:")
    b11 = int(input("Enter a\u2081\u2081: "))
    b12 = int(input("Enter a\u2081\u2082: "))
    b13 = int(input("Enter a\u2081\u2083: "))
    b21 = int(input("Enter a\u2082\u2081: "))
    b22 = int(input("Enter a\u2082\u2082: "))
    b23 = int(input("Enter a\u2082\u2083: "))
    b31 = int(input("Enter a\u2083\u2081: "))
    b32 = int(input("Enter a\u2083\u2082: "))
    b33 = int(input("Enter a\u2083\u2083: "))
    print(" ")
    print("===================================")
    print(" ")
    return a11, a12, a13, a21, a22, a23, a31, a32, a33, b11, b12, b13, b21, b22, b23, b31, b32, b33

def matrix_represent():
    print("Matrix A:")
    print(" ")
    print(a11,"", a12,"", a13), print(a21,"", a22,"", a23), print(a31,"", a32,"", a33)
    print(" ")
    print("Matrix B:")
    print(" ")
    print(b11,"", b12,"", b13), print(b21,"", b22,"", b23), print(b31,"", b32,"", b33)
    print(" ")
    print("===================================")
    print(" ")
    return matrix_represent

def matrix_multiply():
    c11 = (a11*b11) + (a12*b21) + (a13*b31)
    c12 = (a11*b12) + (a12*b22) + (a13*b32)
    c13 = (a11*b13) + (a12*b23) + (a13*b33)
    c21 = (a21*b11) + (a22*b21) + (a23*b31)
    c22 = (a21*b12) + (a22*b22) + (a23*b32)
    c23 = (a21*b13) + (a22*b23) + (a23*b33)
    c31 = (a31*b11) + (a32*b21) + (a33*b31)
    c32 = (a31*b12) + (a32*b22) + (a33*b32)
    c33 = (a31*b13) + (a32*b23) + (a33*b33)
    return c11, c12, c13, c21, c22, c23, c31, c32, c33

def matrix_result():
    print("Result A x B:")
    print(" ")    
    print(c11,"", c12,"", c13), print(c21,"", c22,"", c23), print(c31,"", c32,"", c33)
    print(" ")
    print("===================================")
    print(" ")
    return matrix_result

def main():
    global a11, a12, a13, a21, a22, a23, a31, a32, a33
    global b11, b12, b13, b21, b22, b23, b31, b32, b33
    global c11, c12, c13, c21, c22, c23, c31, c32, c33
    (a11, a12, a13, a21, a22, a23, a31, a32, a33,
     b11, b12, b13, b21, b22, b23, b31, b32, b33) = matrix_input()
    matrix_represent()
    (c11, c12, c13, c21, c22, c23, c31, c32, c33) = matrix_multiply()
    matrix_result()