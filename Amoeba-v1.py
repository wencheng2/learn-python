# Import modules
from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Reading the image
image =cv2.imread ('Snap-4-1-Airyscan Processing-01.jpg')
image =cv2.cvtColor (image, cv2.COLOR_BGR2RGB)

plt.imshow(image)

def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color

def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    return modified_img


def color_analysis(img):
    clf = KMeans(n_clusters = 25)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    
    sum=0
    for value in counts.values():
        sum=sum+value
        #print(sum)
 
    percentage = []
    for value in counts.values(): 
        percentage.append(value/sum*100)
        #print(percentage)
    
    plt.figure(figsize = (12, 8))
    plt.ylabel('Color Percentage %')
    plt.xlabel('Color Index')
    plt.bar(hex_colors, percentage, color=hex_colors)
    
    #plt.bar(hex_colors, counts.values(), color=hex_colors)

    #plt.pie(percentage, labels= hex_colors, colors = hex_colors)   

    #plt.figure(figsize = (12, 8))
    #plt.pie(counts.values(), color_labels = hex_colors, colors = hex_colors)
    #plt.savefig("color_analysis_report.png")
    plt.show()


modified_image = prep_image(image)
color_analysis(modified_image)