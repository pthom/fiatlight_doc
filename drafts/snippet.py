import fiatlight as fl
from fiatlight.fiat_kits.fiat_image import ImageU8, ImageU8_GRAY
from enum import Enum
import cv2

"""
void cv::Canny(InputArray image,
    OutputArray edges,
    double      threshold1,
    double      threshold2,
    int      apertureSize = 3,
    bool      L2gradient = false
    );

Parameters
    image 8-bit input image.
    edges output edge map; single channels 8-bit image, which has the same size as image .
    threshold1: first threshold for the hysteresis procedure.
    threshold2: second threshold for the hysteresis procedure.
    apertureSize: aperture size for the Sobel operator (should be odd, between 3 and 7).
    L2gradient: a flag, indicating whether a more accurate norm should be used to calculate the gradient
"""


class CannyApertureSize(Enum):
    APERTURE_3 = 3
    APERTURE_5 = 5
    APERTURE_7 = 7


@fl.with_fiat_attributes(t_lower__range=(0, 10000), t_upper__range=(0, 10000))
def canny(
    image: ImageU8,
    t_lower: float,
    t_upper: float,
    aperture_size: CannyApertureSize = CannyApertureSize.APERTURE_3,
    l2_gradient: bool = False,
) -> ImageU8_GRAY:
    """
    :param image: Image: Input image to which Canny filter will be applied
    :param t_lower: T_lower: Lower threshold value in Hysteresis Thresholding
    :param t_upper: Upper threshold value in Hysteresis Thresholding
    :param aperture_size: Aperture size of the Sobel filter.
    :param l2_gradient   Boolean parameter used for more precision in calculating Edge Gradient.
    :return: a binary image with edges detected using Canny filter
    """
    r = cv2.Canny(image, t_lower, t_upper, apertureSize=aperture_size.value, L2gradient=l2_gradient)
    return r  # type: ignore
