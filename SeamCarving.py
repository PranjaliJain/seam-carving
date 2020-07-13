import seam_removal
import seam_insertion
import object_removal_file

# For changing the size of the image
def perform_change(img, new_size): 
	orig_row, orig_col, depth = img.shape
	new_row, new_col = new_size
	img_new = img
############################################
	row_change = orig_row - new_row
	if row_change == 0:
		print("No change in rows")
	elif row_change < 0:
		img_new = seam_insertion.row_insertion(img_new, -row_change)
			
	else:
		for i in range(1, row_change+1):
			img_new = seam_removal.row_removal(img_new)
			if i%10 == 0:
				print("Removed %s rows"%(i)) 
############################################
	col_change = orig_col - new_col
	if col_change == 0:
		print("No change in columns")
	elif col_change < 0:
		img_new = seam_insertion.col_insertion(img_new, -col_change)
	else:
		for i in range(1, col_change+1):
			img_new = seam_removal.col_removal(img_new)
			if i%10 == 0:
				print("Removed %s columns"%(i))

	return img_new

################################################################
################################################################
################################################################
################################################################
################################################################
# For removing an object from the image
def object_removal(img, masking_box):
	up_row, down_row, left_col, right_col = masking_box
	reduced_img = object_removal_file.removal_run(img, up_row, down_row, left_col, right_col)
	print('\nObject removed successfully\n')
	enlarged_img = object_removal_file.insertion_run(img, reduced_img)
	print('\nImage restored successfully\n')
	return enlarged_img