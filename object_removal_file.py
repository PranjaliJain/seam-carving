import numpy as np
import cv2
import energy
import seam_removal
import seam_insertion

def add_mask_to_energy(img, up_row, down_row, left_col, right_col):
    # Energy for each pixel 
    mat = energy.pixel_energy(img)
    mat = mat.astype(np.float64)
    
    # Masking the energy matrix
    mask_shape = mat[up_row:down_row,left_col:right_col].shape
    mat[up_row:down_row,left_col:right_col] = np.ones(mask_shape)*(-3000)
    return mat

def seam_detect(mat):
    backtrack = np.zeros(mat.shape, dtype=np.uint16)
    n,m = mat.shape

    dp = np.zeros(mat.shape)
    dp[0] = mat[0]
    
    #Finding minimum path
    for i in range(1, n):
        for j in range(m):
            if j == 0:
                idx = np.argmin(dp[i - 1, j:j + 2])
                tip = 0
            else:
                idx = np.argmin(dp[i - 1, j - 1:j + 2])
                tip = 1

            min_ = dp[i - 1, idx + j - tip]
            backtrack[i, j] = idx + j - tip

            dp[i, j] = mat[i,j] + min_

    #Backtracking
    seam = []
    arrow = np.argmin(dp[-1])

    for i in range(n-1, -1, -1):
        seam.append(arrow)
        arrow = backtrack[i, arrow]

    seam.reverse()
    return seam

def remove_seam_image(img, seam):
    #removing seam line from image
    n, m, depth = img.shape
    output = np.zeros((n, m-1, depth))
    for row in range(n):
        col = seam[row]
        output[row, :, 0] = np.delete(img[row, :, 0], col)
        output[row, :, 1] = np.delete(img[row, :, 1], col)
        output[row, :, 2] = np.delete(img[row, :, 2], col)
    return output.astype(np.uint8)

def remove_seam_mat(mat, seam):
    #removing seam line from energy matrix
    n, m = mat.shape
    output = np.zeros((n, m-1))
    for row in range(n):
        col = seam[row]
        output[row, :] = np.delete(mat[row, :], col)
    return output
##########################################################
##########################################################    
##########################################################
def removal_run(img, up_row, down_row, left_col, right_col):
    #Removing seams until object disappears
    mat = add_mask_to_energy(img, up_row, down_row, left_col, right_col)
    count = 0
    while mat.min() == -3000:
        count += 1 
        if count%10 == 0:
            print("Removing object - %s"%(count))
        seam = seam_detect(mat)
        img = remove_seam_image(img, seam)
        mat = remove_seam_mat(mat, seam)
    return img

def insertion_run(img, img_new):
    #Inserting new columns until image size is back to original
    change = img.shape[1] - img_new.shape[1]
    return seam_insertion.col_insertion(img_new, change)







