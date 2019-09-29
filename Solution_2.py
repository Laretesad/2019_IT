import matplotlib.pyplot as plt
import numpy as np
import math

sigum = int(input())
windows_size = int(input())
def get_core(windows_size, signum):
    core = np.zeros((windows_size, windows_size))
    mean = windows_size // 2
    for x in range(windows_size):
        for y in range(windows_size):
            core[x][y] = math.exp( (-0.5 * (x - mean) / signum) ** 2.0 + ((y - mean) /signum) ** 2.0) / (2 * math.pi * signum * signum)
    core /= core.sum()
    return core
def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return
def filter(img, window_size):
    img2 = np.zeros_like(img)
    core = get_core(window_size)
    p = window_size//2
    for k in range(img.shape[2]):
        for i in range(p, img.shape[0]-p):
            for j in range(p, img.shape[1]-p):
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                imgend[i,j,k] = (core*window).sum()
    return imgend
def main():
    img = plt.imread("img.png")[:, :, :3]
    add_noise(img)
    img2 = filter(img)
    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()
if __name__ == "__main__":
    main()
