import numpy as np
import math

# Generate vector of coefficients (omega in GFG)
# Reference: https://www.youtube.com/watch?v=61NuFlK5VdU
def calculateWeigths(
    eigenfaces: list[np.matrix], normalizedVector: np.matrix
) -> np.matrix:
    weights = np.zeros((len(eigenfaces), 1))
    for k in range(len(eigenfaces)):
        weights[k, 0] = np.matmul(eigenfaces[k].T, normalizedVector)

    return weights


def calculateFaceSpaceProj(eigenfaces: list[np.matrix], weights: np.matrix):
    eigenfaces_mat = np.hstack(eigenfaces)
    return np.matmul(eigenfaces_mat, weights)


# Calculate euclidean distance
def calculateEuclideanDist(A: np.matrix, B: np.matrix) -> float:
    diff = A - B
    diff = diff.flatten()

    return math.sqrt(sum(pow(coef, 2) for coef in diff))


def consineSimilarity(A: np.matrix, B: np.matrix) -> float:
    A = A.flatten()
    B = B.flatten()
    dotProduct = np.dot(A, B)
    ANorm = math.sqrt(sum(pow(el, 2) for el in A))
    BNorm = math.sqrt(sum(pow(el, 2) for el in B))

    return dotProduct / (ANorm * BNorm)


# Return path sorted by most similar
def getSimilarImagesPathSorted(
    unkownImageVector: np.matrix,
    mean: np.matrix,
    trainingImages: np.ndarray,
    trainingImagesPaths: list[str],
    eigenfaces: list[np.matrix],
) -> list[np.matrix]:
    # Calculate coefficient matrix (Omega) of unknown image
    newImageWeight = calculateWeigths(eigenfaces, unkownImageVector - mean)
    newImageProj = calculateFaceSpaceProj(eigenfaces, newImageWeight)

    distList = []
    for idx in range(len(eigenfaces)):
        # Calculate distance between unknown image and the-idx'th training image
        trainingImageVector = np.reshape(trainingImages[idx, :, 0], (65536, 1))
        trainingImageWeight = calculateWeigths(eigenfaces, trainingImageVector - mean)
        dist = calculateEuclideanDist(newImageWeight, trainingImageWeight)
        distList.append((dist, trainingImagesPaths[idx], trainingImageWeight))

    distListSorted = sorted(distList, key=lambda x: x[0])

    cosSim = consineSimilarity(newImageWeight, distListSorted[0][2])

    similarity = (cosSim + 1) / 2

    similarityThreshold = 0.5 * distListSorted[-1][0]

    return (
        [distTuple[1] for distTuple in distListSorted],
        calculateEuclideanDist(unkownImageVector - mean, newImageProj),
        similarity,
        similarityThreshold,
        distListSorted[0][0],
    )
