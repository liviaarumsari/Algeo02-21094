import numpy as np
import math

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

    # dist = 0
    # for coef in diff:

    return math.sqrt(sum(pow(coef, 2) for coef in diff))


# Return path sorted by most similar
def getSimilarImagesPathSorted(
    unkownImageVector: np.matrix,
    mean: np.matrix,
    trainingImages: np.ndarray,
    trainingImagesPaths: list[str],
    eigenfaces: list[np.matrix],
) -> list[np.matrix]:
    # Calculate coefficient matrix (Omega) of unknown image
    newImageCoef = vectorOfCoefficients(eigenfaces, unkownImageVector - mean)

    distList = []
    for idx in range(len(eigenfaces)):
        # Calculate distance between unknown image and the-idx'th training image
        trainingImageVector = np.reshape(trainingImages[idx, :, 0], (65536, 1))
        dist = calculateEuclideanDist(
            newImageCoef, vectorOfCoefficients(eigenfaces, trainingImageVector - mean)
        )
        distList.append((dist, trainingImagesPaths[idx]))

    distListSorted = sorted(distList, key=lambda x: x[0])

    similarity = 1 - (distListSorted[0][0] / distListSorted[-1][0])

    return (
        [distTuple[1] for distTuple in distListSorted],
        similarity,
        distListSorted[0][0],
    )
