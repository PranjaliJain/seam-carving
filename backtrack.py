import numpy as np
import cv2
import get_min_path
import energy

#vertical seam, horizontal change
# backtracking dp's path to obtain seam
def horizontal_back(mat, index_min):
    n,m = mat.shape
    seam = [index_min]
    prev = index_min

    for i in range(n-2, -1, -1):
        min_val = min(mat[i][prev-1:prev+2]) if prev != 0 else min(mat[i][:2])
        for j, w in enumerate(mat[i]):
            if w == min_val:
                if prev-2 < j < prev+2:
                    seam.append(j)
                    break
        prev = j
    return seam[::-1]

#horizontal seam, vertical change
# backtracking dp's path to obtain seam
def vertical_back(mat, index_min):
    n,m = mat.shape
    seam = [index_min]
    prev = index_min

    for i in range(m-2, -1, -1):
        min_val = min(mat[prev-1:prev+2, i]) if prev != 0 else min(mat[:2, i])

        for j, w in enumerate(mat[:, i]):
            if w == min_val:
                if prev-2 < j < prev+2:
                    seam.append(j)
                    break
        prev = j
    return seam[::-1]