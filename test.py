import numpy as np
import cv2


def _read_surf(file_path):
    rawdata = np.loadtxt(file_path)
    print('raw,', rawdata, rawdata.shape, len(rawdata.shape))

    if len(rawdata.shape) == 2:
        output = np.zeros((2, rawdata.shape[0], 2))
        for i in range(rawdata.shape[0]):
            output[0, i, 0] = rawdata[i, 0]
            output[0, i, 1] = rawdata[i, 1]
            output[1, i, 0] = rawdata[i, 2]
            output[1, i, 1] = rawdata[i, 3]

        return np.expand_dims(output, axis=0)
    else:
        return np.zeros((1, 2, 0, 2))


if __name__ == '__main__':
    surf = _read_surf('/Users/plusub/PycharmProjects/coupe.DVSG/images/stable/1/features/1_1.feature')
    print('surf,', surf, surf.shape)
