from skimage.measure import compare_ssim as ssim
import numpy as np

def compare_images(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    SSIM = ssim(imageA, imageB)
    return err,SSIM