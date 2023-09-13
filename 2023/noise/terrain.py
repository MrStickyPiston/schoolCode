import argparse
import random
import subprocess
import sys
import time
from gooey import Gooey

startTime = time.time()

"""Example configuaration: --shape 1000 1000 --scale 550 --persistence 0.45 --lacunarity 1.86"""

try:
    import noise
except ImportError:
    if sys.version_info.major != 3 or sys.version_info.minor != 11:
        print(f"Invalid version f{sys.version}. Please install noise module manually")
        exit(1)
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
        print(f"Generating terrain ({str(round((i / args.shape[0]) * 100, 1))}% Done)")
        for j in range(args.shape[1]):
            world[i][j] = args.noise(i / args.scale,
                                     j / args.scale,
                                     octaves=args.octaves,
                                     persistence=args.persistence,
                                     lacunarity=args.lacunarity,
                                     repeatx=args.shape[0],
                                     repeaty=args.shape[1],
                                     base=args.seed)

    print(f"Generating terrain (100% Done)")
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

    plotinfo = f"""
------------------- Terrain Info -------------------
time elapsed: {time.time() - startTime}
mode: {args.mode}
seed: {args.seed}
scale: {args.scale}
shape: {args.shape[0]}x{args.shape[1]}
octaves: {args.octaves}
persistence: {args.persistence}
lacunarity: {args.lacunarity}
----------------------------------------------------
"""

    print(f"\n{plotinfo}")

    if args.debug:
        ax.text2D(-0.1, 0.85, plotinfo, ha='left', va='top', transform=ax.transAxes)
    ax.set_axis_off()

    matplotlib.pyplot.grid(False)
    matplotlib.pyplot.show()


@Gooey(program_name='3D terrain generator')
def main():
    parser = argparse.ArgumentParser(prog='3D terrain generator',
                                     description='A program to generate 3D terrain with the use of noises.')

    parser.add_argument('--seed',
                        help="The base of the noise. (INT)",
                        dest="seed",
                        type=int,
                        default=random.randint(1000, 9999))

    parser.add_argument('--octaves',
                        help="The amount of octaves, that 'carve' the terrain. (INT)",
                        dest="octaves",
                        type=int,
                        default=5)

    parser.add_argument('--scale',
                        help="The scale of the generated terrain. (INT)",
                        dest="scale",
                        type=int,
                        default=1000)

    parser.add_argument('--shape',
                        help="The shape of the generated terrain. (INT INT)",
                        dest="shape",
                        nargs=2,
                        type=int,
                        default=[1000, 1000])

    parser.add_argument('--persistence',
                        help="The smoothness of the generated terrain (FLOAT)",
                        dest="persistence",
                        type=float,
                        default=0.5)

    parser.add_argument('--lacunarity',
                        help="The roughness of the generated terrain (FLOAT)",
                        dest="lacunarity",
                        type=float,
                        default=2)

    parser.add_argument('--mode',
                        help="The noise mode the terrain uses. (perlin|simplex)",
                        dest="mode",
                        choices=["perlin", "simplex"],
                        default="simplex")

    parser.add_argument('--debug',
                        help="Show debug info.",
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


if __name__ == "__main__":
    main()
