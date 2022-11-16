import numpy as np

# Generate vector of coefficients (omega in GFG)
# Reference: https://www.youtube.com/watch?v=61NuFlK5VdU
def vectorOfCoefficients(
    eigenfaces: list[np.matrix], normalizedVector: np.matrix
) -> np.matrix:
    omega = np.zeros((len(eigenfaces), 1))
    for k in range(len(eigenfaces)):
        omega[k, 0] = np.matmul(eigenfaces[k].T, normalizedVector)

    return omega


# Calculate euclidean distance
# (no need to get square root as we're only
# trying to find the minimum anyway)
def calculateEuclideanDist(coefsNew: np.matrix, coefsTrain: np.matrix) -> float:
    diff = coefsNew - coefsTrain
    diff = diff.flatten()
    return sum(pow(coef, 2) for coef in diff)


# Return most similiar training image
def mostSimilarImage(
    unkownImageVector: np.matrix,
    mean: np.matrix,
    trainingImages: np.ndarray,
    eigenfaces: list[np.matrix],
) -> np.ndarray:
    # Calculate coefficient matrix (Omega) of unknown image
    newImageCoef = vectorOfCoefficients(eigenfaces, unkownImageVector - mean)

    minDist = None
    idxMinDist = 0
    for idx in range(len(eigenfaces)):
        # Calculate distance between unknown image and the-idx'th training image
        dist = calculateEuclideanDist(
            newImageCoef, vectorOfCoefficients(eigenfaces, trainingImages[idx, :, 0])
        )

        # Keep track of training image with least distance
        if minDist == None or dist < minDist:
            minDist = dist
            idxMinDist = idx

    return trainingImages[idxMinDist, :, 0]
