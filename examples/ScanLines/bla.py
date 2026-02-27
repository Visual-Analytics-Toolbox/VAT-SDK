from vaapi.client import Vaapi
import os
from PIL import Image
from kbm import process_image
import requests
import cv2
import numpy as np
brightness_threshold_top = 6*2
brightness_threshold_bottom= 6*4
scanline_count_top = 41
scanline_count_bottom = 31
pixel_border_y = 3
double_edgel_angle_threshold = 0.2
double_edgel_green_check = True
minEndPointGreenDensity = 0.3

dynamicThreshold = True
dynamicThresholdMin = 12
dynamicThresholdMax = 24

class MaximumScan:
    def __init__(self, threshold):
        self.threshold = threshold
        self.value_max = threshold
        
        # Instead of a reference to an external variable, 
        # we store the result right here inside the class.
        self.peak_location = 0 
        self.peak_found = False

    def add(self, location, value):
        # 1. Reset if we found a peak on the PREVIOUS step
        if self.peak_found:
            self.value_max = self.threshold
            self.peak_found = False

        # 2. Climbing up the hill (New highest point found)
        if value > self.value_max:
            self.value_max = value
            self.peak_location = location # Remember where we saw this max value
        
        # 3. Going down the hill (The previous step was the peak)
        elif self.value_max > self.threshold and value < self.value_max:
            self.peak_found = True
            return True # WE FOUND AN EDGE!

        return False


def scanForEdgels(start,end,img):
    endpointPosInImage = start
    
    step = 2

    #idk what happens here in c++ code...

    begin_found = False
    t_edge = brightness_threshold_bottom

    lastGreenPoint = start

    peak_point_max = start
    peak_point_min = start

    positive_scan = MaximumScan(t_edge)
    negative_scan = MaximumScan(t_edge)

def ScanLineEdgel(image):
    img = Image.open(image)

    step = img.width / scanline_count_bottom
    scanline_x = step /2

    borderY = img.height - pixel_border_y -1

    start = [int(scanline_x),int(borderY)]
    end = [int(scanline_x),img.height]

    for i in range(0,scanline_count_bottom):
        scanForEdgels(start,end,img)




if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )

    # response = client.image.list(log=155,camera="BOTTOM")
    # url = "https://logs.berlin-united.com/" + response.items[5].image_url
    # url = "https://logs.berlin-united.com/2024-07-15_RC24/2024-07-15_20-00-00_Berlin%20United_vs_SPQR%20Team_half1-test/extracted/2_16_Nao0017_240715-1830/log_bottom/0007849.png"
    # response = requests.get(url)
    # response.raise_for_status()  # Raise an error for bad status codes

    # image = np.asarray(bytearray(response.content), dtype="uint8")
    # image_cv = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # cv2.imwrite("test.png", image_cv)


    process_image("test.png",31,50)