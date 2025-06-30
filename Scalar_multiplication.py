import numpy as np
def scalar_multiplication(matrix: list[list[float]], scalar: float) -> list[list[float]]:
   a=np.array(matrix)
   b=a.flatten()
   c=[]
   for i in b:
         c.append(i*scalar)
   d=np.array(c)
   shape=a.shape
   result=d.reshape(shape)
   return result.tolist()
# Example usage
print(scalar_multiplication([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))  # Output: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
print(scalar_multiplication([[1, 2], [3, 4]],   3))  # Output: [[3, 6], [9, 12]]
    
   