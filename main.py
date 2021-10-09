import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

'''calculate the local binary result and return the list'''
def cal_local_binary(img, i, j):
    result_list = []
    for y in range(i-1, i+2):
        for x in range(j-1, j+2):
            if y == i and x == j:
                continue
            result_list.append(0) if img[y][x] <= img[i][j] else result_list.append(1)
    return result_list

if __name__ == "__main__":
    # read file; top_left is (0, 0)
    img = cv2.imread("img.png",cv2.IMREAD_GRAYSCALE)

    # parameters
    height, width = img.shape
    new_img = np.zeros((height-1, width-1), dtype=np.uint8)

    # start calculating LBP process
    for i in range (1, height-1):
        for j in range (1, width-1):
            result_list = cal_local_binary(img, i, j)
            
            new_img[i-1][j-1] = math.pow(2, 7)*result_list[0]+\
                                math.pow(2, 6)*result_list[1]+\
                                math.pow(2, 5)*result_list[2]+\
                                math.pow(2, 4)*result_list[3]+\
                                math.pow(2, 3)*result_list[4]+\
                                math.pow(2, 2)*result_list[5]+\
                                math.pow(2, 1)*result_list[6]+\
                                math.pow(2, 0)*result_list[7]

    hist = cv2.calcHist([new_img], [0], None, [256], [0, 256])

    # show imgs
    cv2.imshow('image1', img)
    cv2.imshow('image2', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # show histogram feature
    plt.figure("Histogram")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    # write file
    cv2.imwrite('result.png', new_img)