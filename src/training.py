import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


def normalizeImage(path):
    img_rgb = cv2.imread(path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    resized = cv2.resize(img_gray, (128, 128), interpolation = cv2.INTER_AREA)
    # Cek hasil image yang diresize
    # cv2.imshow("test image", resized)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    norm = np.zeros_like(resized.astype(float))
    minPx, maxPx = resized.min(), resized.max()
    num_img = resized.shape[0]

    for img in range(num_img):
        norm[img, ...] = (resized[img, ...] - float(minPx)) / float(maxPx - minPx)
    
    return norm

def extractMatrices(directory):

    len = 0
    for filename in os.listdir(directory):
        f = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(directory, filename))
        if os.path.isfile(f):
            len += 1

    result = np.empty((len, 128, 128))

    idx = 0
    for filename in os.listdir(directory):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(directory, filename))
        # Test matrix hasil
        # temp = normalizeImage(path)
        # print(temp)
        # print(len(temp), "x", len(temp[0]))
        # tempMat = normalizeImage(path)
        # result.append(tempMat)
        result[idx] = normalizeImage(path)
        idx+=1
    
    return result

def meanOfMatrices(trainingMatrices):
    return np.mean(trainingMatrices, axis=0)

def differenceOfMatrix(trainingMatrix, mean):
    return np.subtract(trainingMatrix, mean)

def differenceList(trainingMatrices, mean):
    result = np.empty((len(trainingMatrices), len(trainingMatrices[0]), len(trainingMatrices[0])))
    for i in range (len(result)):
        result[i] = differenceOfMatrix(trainingMatrices[i], mean)
    return result

# TES FUNGSI
ret = extractMatrices('test')
print("Hasil Training Matrix dari Seluruh Gambar")
print(ret)
# print(ret[0])
# print(ret[0, 1])
print("Rata-rata Training Matrix")
mean = meanOfMatrices(ret)
print(mean)
print("Selisih Tiap Training Matrix dengan Rata-rata")
print(differenceList(ret, mean))




