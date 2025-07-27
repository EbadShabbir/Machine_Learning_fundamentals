import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    M1=np.array(matrix)
    try:
        inverse1=np.linalg.inv(M1)
        inverse=inverse1.tolist()
    except np.linalg.LinAlgError:
        return None
        

	return inverse
