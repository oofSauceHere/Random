# look its been a while since ive used python

import cv2 as cv

INTERVAL = 255/10
LARGE_SPECTRUM = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
SMALL_SPECTRUM = "@%#*+=-:. "

def calc_brightness(color):
    r = 0.2126*color[0]
    g = 0.7152*color[1]
    b = 0.0722*color[2]

    return r + g + b

def determine_char(brightness, spectrum):
    position = int(brightness//INTERVAL)
    if(position == 70 or position == 10):
        position -= 1
    
    return spectrum[position]

filename = input("filename: ")
img = cv.imread('asciifier/input/' + filename)
height, width, channels = img.shape

spectrum_size = input("spectrum size (10 or 70, invalid input results in 10): ")
spectrum = SMALL_SPECTRUM

if(spectrum_size == '70'):
    INTERVAL = 255/70
    spectrum = LARGE_SPECTRUM

with open('asciifier/output/art.txt', 'w') as f:
    for i in range(0, height):
        for j in range(0, width):
            f.write(str(determine_char(calc_brightness(img[i][j]), spectrum)) + ' ')
        f.write('\n')
    f.close()

print('done !!')