import energy
import backtrack
import get_min_path

#vertical seam, horizontal change
def get_seam_horizontal(img):
    mat = energy.pixel_energy(img)
    index_min = get_min_path.horizontal(mat)

    seam = backtrack.horizontal_back(mat, index_min)
    return seam

#horizontal seam, vertical change
def get_seam_vertical(img):
    mat = energy.pixel_energy(img)
    index_min = get_min_path.vertical(mat)

    seam = backtrack.vertical_back(mat, index_min)
    return seam

