import get_seam
import numpy as np
import seam_removal

# average func
def aveg(output_list, j):
    if j == 0:
        return (output_list[0]+output_list[1])/2
    else:
        return (output_list[j]+output_list[j-1])/2

#inserting columns
def col_insertion(img, change):
    img_new = img
    seam_global = []
    
    # removing columns in duplicate image and storing the seams
    for i in range(change):
        if i%10 == 0:
            print("Inserted %s columns"%(i))

        n, m, depth = img.shape
        seam = get_seam.get_seam_horizontal(img)
        
        seam_global.append(np.array(seam)+i)
       
        output = np.zeros((n, m-1, depth))
        for row in range(n):
            col = seam[row]
            output[row, :, 0] = np.delete(img[row, :, 0], col)
            output[row, :, 1] = np.delete(img[row, :, 1], col)
            output[row, :, 2] = np.delete(img[row, :, 2], col)

        img = output.astype(np.uint8)
    
    seam_global = np.array(seam_global).T
    n, m, depth = img_new.shape
    output = np.zeros((n, m+change, depth))

    # using the seams to insert new columns in the original image
    for row in range(n):
        output[row, :, 0][:m] = img_new[row, :, 0]
        output[row, :, 1][:m] = img_new[row, :, 1]
        output[row, :, 2][:m] = img_new[row, :, 2]

    for row, i in enumerate(seam_global):
        count = 0
        for j in i:
            output[row, :, 0] = np.insert(output[row, :, 0], j+count, aveg(output[row, :, 0], j))[:-1]
            output[row, :, 1] = np.insert(output[row, :, 1], j+count, aveg(output[row, :, 1], j))[:-1]
            output[row, :, 2] = np.insert(output[row, :, 2], j+count, aveg(output[row, :, 2], j))[:-1]
            count += 1

    return output.astype(np.uint8)

####################################

#inserting rows
def row_insertion(img, change):
    img_new = img.T
    seam_global = []
    
    # removing rows in duplicate image and storing the seams
    for i in range(change):
        if i%10 == 0:
            print("Inserted %s rows"%(i))

        img_t = img.T
        depth, n, m = img_t.shape
        seam = get_seam.get_seam_vertical(img)
        
        seam_global.append(np.array(seam)+i)
       
        output = np.zeros((depth, n, m-1))
        for row in range(n):
            col = seam[row]
            output[0, row, :] = np.delete(img_t[0, row, :], col)
            output[1, row, :] = np.delete(img_t[1, row, :], col)
            output[2, row, :] = np.delete(img_t[2, row, :], col)

        img = output.T.astype(np.uint8)

    seam_global = np.array(seam_global).T
    depth, n, m = img_new.shape
    output = np.zeros((depth, n, m+change))

    # using the seams to insert new rows in the original image

    for row in range(n):
        output[0, row, :][:m] = img_new[0, row, :]
        output[1, row, :][:m] = img_new[1, row, :]
        output[2, row, :][:m] = img_new[2, row, :]

    for row, i in enumerate(seam_global):
        count = 0
        for j in i:
            output[0, row, :] = np.insert(output[0, row, :], j+count, aveg(output[0, row, :], j))[:-1]
            output[1, row, :] = np.insert(output[1, row, :], j+count, aveg(output[1, row, :], j))[:-1]
            output[2, row, :] = np.insert(output[2, row, :], j+count, aveg(output[2, row, :], j))[:-1]
            count += 1

    return output.T.astype(np.uint8)
