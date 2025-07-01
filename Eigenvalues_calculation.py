import math as math 
def eigenvalues_calculation(A):
    a=A[0][0]
    b=A[0][1]
    c=A[1][0]
    d=A[1][1]
    tr=a+d
    det=(a*d)-(c*b)
    D=(tr**2)-(4*det)
    lamda_1=((tr)+math.sqrt(D)) /2
    lamda_2=((tr)-math.sqrt(D)) /2
    
    eigenvalues=[lamda_1,lamda_2]

    return eigenvalues
# Example usage:
if __name__ == "__main__":
    A = [[4, 2], [1, 3]]
    eigenvalues = eigenvalues_calculation(A)
    print("Eigenvalues:", eigenvalues)