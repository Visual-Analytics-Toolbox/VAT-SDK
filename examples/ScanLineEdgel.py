from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

class MaximumScan:
    def __init__(self, threshold):
        self.threshold = threshold
        self.value_max = threshold
        self.peakMax = 0
        self.maximum = False

    def add(self, point, value):
        
        if self.maximum:
            self.value_max = self.threshold
            self.maximum = False

        if value > self.value_max:
            self.value_max = value
            self.peakMax = point
        
        elif self.value_max > self.threshold and value < self.value_max:
            self.maximum = True
            return True

        return False

img = np.asarray(Image.open('test.png'))

first_channel = img[:,:,0]

class Edgel():
    def __init__(self,x,y,positive):
        self.x = x
        self.y = y
        self.positive = positive
    
    def __repr__(self):
        return f"{self.x} {self.y} {"positive" if self.positive else "negative"}"

edgels = []

for x in range(0,first_channel.shape[1],30):
    begin_found = False
    pos_scan = MaximumScan(20)
    neg_scan = MaximumScan(20)
    last_pixel_val = first_channel[first_channel.shape[0]-1,x]
    for y in range(first_channel.shape[0]-2,0,-1):
            
            if y <= 2:
                continue
            
            if y + 2 >= first_channel.shape[0]:
                continue 

            curr_pixel_val = first_channel[y,x]

            gradient = curr_pixel_val - last_pixel_val
            
            last_pixel_val = curr_pixel_val

            if pos_scan.add(y+1, gradient):
                peak_y = pos_scan.peakMax

                f_2 = first_channel[peak_y-2,x]
                f0  =  first_channel[peak_y,x]
                f2  =  first_channel[peak_y+2,x]
            
                if(f_2-f0 > pos_scan.value_max): 
                    peak_y -= 1
                if(f0 -f2 > pos_scan.value_max):
                    peak_y += 1

                begin_found = True
                edgels.append(Edgel(x,peak_y,True))
               
            if neg_scan.add(y+1, -gradient):
                peak_y = neg_scan.peakMax

                f_2 = first_channel[peak_y-2,x]
                f0  =  first_channel[peak_y,x]
                f2  =  first_channel[peak_y+2,x]
            
                if(f_2-f0 > neg_scan.value_max): 
                    peak_y -= 1
                if(f0 -f2 < neg_scan.value_max):
                    peak_y += 1

                if begin_found:
                    begin_found = False
                    edgels.append(Edgel(x,peak_y,False))

print(first_channel.shape)
print(edgels)

for edgel in edgels:
    plt.plot(edgel.x,edgel.y,marker='v',color="blue" if edgel.positive else "red")
imgplot = plt.imshow(first_channel)
plt.show()
