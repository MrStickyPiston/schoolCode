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

if "--seed" in sys.argv:
    try:
        seed = int(sys.argv[sys.argv.index("--seed") + 1])
    except IndexError:
        sys.stdout.write(f"Invalid seed")
        sys.stdout.flush()
        sys.exit(1)

    except ValueError:
        sys.stdout.write(f"Invalid seed")
        sys.stdout.flush()
        sys.exit(1)
else:
    seed = int(random.random() * 10000)

if "--scale" in sys.argv:
    try:
        scale = int(sys.argv[sys.argv.index("--scale") + 1])
    except IndexError:
        sys.stdout.write(f"Invalid scale")
        sys.stdout.flush()
        sys.exit(1)

    except ValueError:
        sys.stdout.write(f"Invalid scale")
        sys.stdout.flush()
        sys.exit(1)
else:
    scale = 1000

if "--shape" in sys.argv:
    try:
        shape = (int(sys.argv[sys.argv.index("--shape") + 1]), int(sys.argv[sys.argv.index("--shape") + 2]))
    except IndexError:
        sys.stdout.write(f"Invalid shape")
        sys.stdout.flush()
        sys.exit(1)

    except ValueError:
        sys.stdout.write(f"Invalid shape")
        sys.stdout.flush()
        sys.exit(1)
else:
    shape = (int(scale), int(scale))

if "--octaves" in sys.argv:
    try:
        octaves = int(sys.argv[sys.argv.index("--octaves") + 1])
    except IndexError:
        sys.stdout.write(f"Invalid octaves")
        sys.stdout.flush()
        sys.exit(1)

    except ValueError:
        sys.stdout.write(f"Invalid octaves")
        sys.stdout.flush()
        sys.exit(1)
else:
    octaves = 6

if "--persistence" in sys.argv:
    try:
        persistence = float(sys.argv[sys.argv.index("--persistence") + 1])
    except IndexError:
        sys.stdout.write(f"Invalid persistence")
        sys.stdout.flush()
        sys.exit(1)

    except ValueError:
        sys.stdout.write(f"Invalid persistence")
        sys.stdout.flush()
        sys.exit(1)
else:
    persistence = 0.5

if "--lacunarity" in sys.argv:
    try:
        lacunarity = float(sys.argv[sys.argv.index("--lacunarity") + 1])
    except IndexError:
        sys.stdout.write(f"Invalid lacunarity")
        sys.stdout.flush()
        sys.exit(1)

    except ValueError:
        sys.stdout.write(f"Invalid lacunarity")
        sys.stdout.flush()
        sys.exit(1)
else:
    lacunarity = 2.0

if "--debug" in sys.argv:
    debug = True
else:
    debug = False

sys.stdout.write(f"Using seed {seed}")
sys.stdout.write("\n")
sys.stdout.flush()

world = np.zeros(shape)
for i in range(shape[0]):
    sys.stdout.write(f"\rGenerating map ({str(round((i / shape[0]) * 100, 1))}% Done)")
    sys.stdout.flush()
    for j in range(shape[1]):
        world[i][j] = noise.snoise2(i / scale,
                                    j / scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=shape[0],
                                    repeaty=shape[1],
                                    base=seed)
    sys.stdout.write(f"\rGenerating map (100% Done)")

lin_x = np.linspace(0, 1, shape[0], endpoint=False)
lin_y = np.linspace(0, 1, shape[1], endpoint=False)
x, y = np.meshgrid(lin_x, lin_y)

matplotlib.rcParams['toolbar'] = 'None'

fig = matplotlib.pyplot.figure(f"3D terrain generator (seed: {seed})")
fig.subplots_adjust(top=1.1, bottom=-.1)

ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, world, cmap='terrain')

plotinfo = f"""Terrain Info
time elapsed: {time.time() - startTime}
seed: {seed}
scale: {scale}
shape: {shape[0]}x{shape[1]}
octaves: {octaves}
persistence: {persistence}
lacunarity: {lacunarity}"""

print(f"\n{plotinfo}")

if debug:
    ax.text2D(-.25, 1, plotinfo, ha='left', va='top', transform=ax.transAxes)
ax.set_axis_off()

matplotlib.pyplot.grid(False)
matplotlib.pyplot.show()
