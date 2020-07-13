import get_seam
import numpy as np
#removing 1 column, i.e. removing one vertical seam --- Horizontal change
def col_removal(img):
    n, m, depth = img.shape
    seam = get_seam.get_seam_horizontal(img)

    output = np.zeros((n, m-1, depth))
    for row in range(n):
        col = seam[row]
        output[row, :, 0] = np.delete(img[row, :, 0], col)
        output[row, :, 1] = np.delete(img[row, :, 1], col)
        output[row, :, 2] = np.delete(img[row, :, 2], col)
    return output.astype(np.uint8)

#removing 1 row, i.e. removing one horizontal seam --- Vertical change
def row_removal(img):

    seam = get_seam.get_seam_vertical(img)
    depth, n, m = img.T.shape

    output = np.zeros((depth, n, m-1))
    for row in range(n):
        col = seam[row]
        output[0, row, :] = np.delete(img.T[0, row, :], col)
        output[1, row, :] = np.delete(img.T[1, row, :], col)
        output[2, row, :] = np.delete(img.T[2, row, :], col)
    return output.T.astype(np.uint8)
