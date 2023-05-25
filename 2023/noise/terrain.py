import argparse
import os
import random
import subprocess
import sys
import time

startTime = time.time()

"""Example configuaration: --shape 1000 1000 --scale 550 --persistence 0.45"""

try:
    import noise
except ImportError:
    if sys.maxsize > 2 ** 32:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "wheels/noise-1.2.3-cp311-cp311-win_amd64.whl"])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "wheels/noise-1.2.3-cp311-cp311-win32.whl"])
    import noise

try:
    import numpy as np
    import matplotlib.pyplot
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import numpy as np
    import matplotlib.pyplot


class Args:
    def __init__(self,
                 seed=random.randint(1000, 9999),
                 octaves=5, scale=1000,
                 shape=[1000, 1000],
                 persistence=0.5,
                 lacunarity=2,
                 mode="simplex",
                 debug=False):
        self.seed = seed
        self.octaves = octaves
        self.scale = scale
        self.shape = shape
        self.persistence = persistence
        self.lacunarity = lacunarity

        self.mode = mode
        if self.mode == "perlin":
            self.noise = noise.pnoise2
        else:
            self.noise = noise.snoise2

        self.debug = debug


def generate(args):
    world = np.zeros(args.shape)
    for i in range(args.shape[0]):
        sys.stdout.write(f"\rGenerating terrain ({str(round((i / args.shape[0]) * 100, 1))}% Done)")
        sys.stdout.flush()
        for j in range(args.shape[1]):
            world[i][j] = args.noise(i / args.scale,
                                     j / args.scale,
                                     octaves=args.octaves,
                                     persistence=args.persistence,
                                     lacunarity=args.lacunarity,
                                     repeatx=args.shape[0],
                                     repeaty=args.shape[1],
                                     base=args.seed)

    sys.stdout.write(f"\rGenerating terrain (100% Done)")
    return world


def render(args, world):
    lin_x = np.linspace(0, 1, args.shape[0], endpoint=False)
    lin_y = np.linspace(0, 1, args.shape[1], endpoint=False)
    x, y = np.meshgrid(lin_x, lin_y)

    matplotlib.rcParams['toolbar'] = 'None'

    fig = matplotlib.pyplot.figure(f"3D terrain generator (seed: {args.seed})")
    fig.subplots_adjust(top=1.1, bottom=-.1)

    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(x, y, world, cmap='terrain')

    plotinfo = f"""Terrain Info
time elapsed: {time.time() - startTime}
mode: {args.mode}
seed: {args.seed}
scale: {args.scale}
shape: {args.shape[0]}x{args.shape[1]}
octaves: {args.octaves}
persistence: {args.persistence}
lacunarity: {args.lacunarity}"""

    print(f"\n{plotinfo}")

    if args.debug:
        ax.text2D(-0.1, 0.85, plotinfo, ha='left', va='top', transform=ax.transAxes)
    ax.set_axis_off()

    matplotlib.pyplot.grid(False)
    matplotlib.pyplot.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__),
                                     description='A program to generate 3D terrain with the use of noises.')

    parser.add_argument('--seed', '-s',
                        dest="seed",
                        type=int,
                        default=random.randint(1000, 9999))

    parser.add_argument('--octaves',
                        dest="octaves",
                        type=int,
                        default=5)

    parser.add_argument('--scale',
                        dest="scale",
                        type=int,
                        default=1000)

    parser.add_argument('--shape',
                        dest="shape",
                        nargs=2,
                        type=int,
                        default=[1000, 1000])

    parser.add_argument('--persistence',
                        dest="persistence",
                        type=float,
                        default=0.5)

    parser.add_argument('--lacunarity',
                        dest="lacunarity",
                        type=float,
                        default=2)

    parser.add_argument('--mode',
                        dest="mode",
                        choices=["perlin", "simplex"],
                        default="simplex")

    parser.add_argument('--debug',
                        dest="debug",
                        action='store_true')

    args = parser.parse_args()

    if args.mode == "perlin":
        args.noise = noise.pnoise2
    else:
        args.noise = noise.snoise2

    sys.stdout.write(f"Using seed {args.seed}")
    sys.stdout.write("\n")
    sys.stdout.flush()

    render(args, generate(args))
