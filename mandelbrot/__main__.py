import matplotlib.pyplot as plt
import numpy as np
import sys


def get_iter(c: complex, thresh: int = 4, max_steps: int = 25) -> int:
    z = c
    i = 1
    while i < max_steps and (z * z.conjugate()).real < thresh:
        z = z * z + c
        i += 1
    return i


def plotter(n, thresh, pos, zoom, max_steps=25):
    zoom = zoom * n / 10
    while 2 * zoom >= n:
        print("Double n because 2*i > n")
        n *= 2

    mx = 2.48 / (n - 1)
    my = 2.26 / (n - 1)
    mapper = lambda x, y: (mx * x - 2, my * y - 1.13)
    img = np.full((n - int(zoom * 2), n - int(zoom * 2)), 255)

    for x in range(0, n - int(zoom * 2)):
        sys.stdout.write(f"\rPROGRESS: {round((x / (n - zoom * 2)) * 100)}%")
        sys.stdout.flush()
        for y in range(0, n - int(zoom * 2)):
            it = get_iter(complex(*mapper(x + pos[0] * n / 100 + int(zoom), y + pos[1] * n / 100 + int(zoom))),
                          thresh=thresh, max_steps=max_steps)
            img[y][x] = it

    return img


def main(n, pos, zoom):
    # n = 100000
    # pos = [0, -10]
    # zoom = 4.5

    print("Starting mandelbrot calculation....")
    img = plotter(n, thresh=4, max_steps=50, pos=pos, zoom=zoom)
    print("\nMandelbrot array calculated!\nStarting GUI implementation...")
    plt.imshow(img)
    plt.axis("off")
    plt.show()
    print("GUI ready!")


if __name__ == "__main__":
    print("starting StickyPiston-Development mandelbrot generator...")
    n = int(input("Enter resolution: "))
    pos = int(input("Enter x (int): ")), int(input("Enter y (int): "))
    zoom = float(input("Enter zoom (float): "))

    main(n, pos, zoom)
