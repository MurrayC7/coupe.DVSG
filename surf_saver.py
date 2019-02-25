import cv2
import numpy as np
import sys
import os

path = sys.path[0] + os.sep


def feature_extract(images_folder, draw_folder):
    featureSum = 0
    print(images_folder)
    filenames = [f for f in os.listdir(images_folder) if not f.startswith('.')]
    for filename in filenames:
        if 'ppm' in filename:
            filepath = images_folder + filename
            drawpath = draw_folder + filename
        else:
            continue
        img = cv2.imread(filepath)
        filename = filepath.split(os.sep)[-1].split('.')[0]
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # set Hessian threshold
        detector = cv2.xfeatures2d.SURF_create(2000)
        # find keypoints and descriptors directly
        kps, des = detector.detectAndCompute(gray, None)
        img = cv2.drawKeypoints(image=img, outImage=img, keypoints=kps, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
                                , color=(255, 0, 0))
        feature_name = images_folder + 'features%s%s.feature' % (os.sep, filename)
        # try:
        np.savetxt(feature_name, des, fmt='%.5e')  # 保存特征向量
        print(feature_name)
            # feature = np.loadtxt(feature_folder + filename)#加载特征向量
            # cv2.imwrite(drawpath, img)#保存绘制了SURF特征的图片

        # except:
        #     print('not saved!')
        #     continue
        featureSum += len(kps)
    print("featureSum: ", featureSum)


if __name__ == '__main__':
    images_folder = path + 'images/unstable/1' + os.sep
    draw_folder = path + 'results/unstable/1' + os.sep + 'drawImages' + os.sep
    feature_extract(images_folder, draw_folder)
