import numpy as np
import cv2
import matplotlib.pyplot as plt
import numpy.linalg as LA
import os
from qrMethod import *
import recognition


def normalizeImage(path):
    img_rgb = cv2.imread(path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    resized = cv2.resize(img_gray, (256, 256), interpolation=cv2.INTER_AREA)
    # Cek hasil image yang diresize
    # cv2.imshow("test image", resized)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    norm = np.zeros_like(resized.astype(float))
    minPx, maxPx = resized.min(), resized.max()
    num_img = resized.shape[0]

    for img in range(num_img):
        norm[img, ...] = (resized[img, ...] - float(minPx)) / float(maxPx - minPx)

    return np.reshape(norm, (256 * 256, 1))


def extractMatrices(directory):

    len = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            len += 1

    # result = np.empty((len, 256, 256))
    result = np.empty((len, 256 * 256, 1))

    idx = 0
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        # Test matrix hasil
        # temp = normalizeImage(path)
        # print(temp)
        # print(len(temp), "x", len(temp[0]))
        # tempMat = normalizeImage(path)
        # result.append(tempMat)
        result[idx] = normalizeImage(path)
        idx += 1

    return result


def meanOfMatrices(trainingMatrices):
    return np.mean(trainingMatrices, axis=0)


def differenceOfMatrix(trainingMatrix, mean):
    return np.subtract(trainingMatrix, mean)


def differenceList(trainingMatrices, mean):
    result = np.empty((len(trainingMatrices), len(trainingMatrices[0]), 1))
    for i in range(len(result)):
        result[i] = differenceOfMatrix(trainingMatrices[i], mean)
    return result


def unflattenMatrix(matrix):
    return np.reshape(matrix, (256, 256))


def concatMatrix(result):
    matrixConcat = np.empty((128, 128 * len(result)))
    for i in range(len(result)):
        if i == 0:
            matrixConcat = result[0]
        else:
            matrixConcat = np.concatenate((matrixConcat, result[i]), axis=1)
    return matrixConcat


def matrixCovariant(matrixConcat):
    transposeConcat = matrixConcat.transpose()
    matrixCovariant = np.dot(transposeConcat, matrixConcat)
    return matrixCovariant


def getEigenVector(matrixCovariant):
    for i in range(256):
        q, r = getQr(matrixCovariant)
        if i == 0:
            eigenVector = q
        else:
            eigenVector = np.dot(eigenVector, q)
        matrixCovariant = np.dot(r, q)
    print("==========Eigen value ===============")
    eigenValue = sorted(matrixCovariant.diagonal(), reverse=True)
    print(eigenValue)
    return eigenVector


# Variable names based on GeeksForGeeks tutorial
# Returns list of vectors (in a (NxN,1) matrix)
def calculateEigenfaces(
    A_matrix: np.matrix, eigenVectors: np.ndarray
) -> list[np.matrix]:
    eigenfaces = []
    for vi in eigenVectors:
        vi_mat = np.reshape(vi, (len(A_matrix[0]), 1))
        eigenfaces.append(np.matmul(A_matrix, vi_mat))

    return eigenfaces


def trainFromFolder(path):
    imageMatrices = extractMatrices(path)
    mean = meanOfMatrices(imageMatrices)
    normalizedMatrices = differenceList(imageMatrices, mean)

    augmentedMatrixOfImages = concatMatrix(normalizedMatrices)
    covariantL = matrixCovariant(augmentedMatrixOfImages)
    eigenVectors = getEigenVector(covariantL)

    print("finished training")

    return (
        calculateEigenfaces(augmentedMatrixOfImages, eigenVectors),
        mean,
        imageMatrices,
    )


# # TES FUNGSI
# ret = extractMatrices("test")
# print(ret.shape)
# print("Hasil Training Matrix dari Seluruh Gambar")
# # print(ret)
# # print(ret[0])
# # print(ret[0, 1])
# print("Rata-rata Training Matrix")
# mean = meanOfMatrices(ret)
# print(mean.shape)
# print(unflattenMatrix(mean).shape)
# # cv2.imshow("average_face", unflattenMatrix(mean))
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # print(mean)
# print("Selisih Tiap Training Matrix dengan Rata-rata")

# temp = differenceList(ret, mean)
# print(temp.shape)

# concat = concatMatrix(temp)
# print(concat.shape)
# covariant = matrixCovariant(concat)
# print(covariant.shape)
# # Eigenvecotrs dari matrix
# eigenVectors = getEigenVector(covariant)

# eigenfaces = calculateEigenfaces(concat, eigenVectors)

# # Test Recognition of Unknown image
# unknownVect = normalizeImage(
#     os.path.join(
#         os.path.dirname(os.path.dirname(__file__)),
#         os.path.join("unknown.jpg"),
#     )
# )
# mostSimilarImage = recognition.mostSimilarImage(unknownVect, mean, ret, eigenfaces)
# mostSimilarImage_matrix = np.reshape(mostSimilarImage, (256, 256))
# cv2.imshow("test", mostSimilarImage_matrix)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
