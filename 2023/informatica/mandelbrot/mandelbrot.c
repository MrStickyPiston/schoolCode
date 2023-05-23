#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char* argv[]);
int get_iter(double x, double y, int maxiter);

int main(int argc, char* argv[]) {
  if (argc != 8) {
    printf("Invalid args. Example args:\n%s -2 1 -1.1 1.1 50 1028 mandelbrot.ppm\n", argv[0]);
    return 1;
  }

  const double xmin = atof(argv[1]);
  const double xmax = atof(argv[2]);
  const double ymin = atof(argv[3]);
  const double ymax = atof(argv[4]);

  const uint16_t maxiter = (unsigned short) atoi(argv[5]);

  const int xres = atoi(argv[6]);
  const int yres = (xres * (ymax - ymin)) / (xmax - xmin);

  const char * filename = argv[7];

  FILE * file = fopen(filename, "wb");
  //char * comment = "# Mandelbrot set";

  fprintf(file,
    "P6\n# Mandelbrot, xmin=%lf, xmax=%lf, ymin=%lf, ymax=%lf, maxiter=%d\n%d\n%d\n%d\n",
    xmin, xmax, ymin, ymax, maxiter, xres, yres, (maxiter < 256 ? 256 : maxiter));

  const double dx = (xmax - xmin) / xres;
  const double dy = (ymax - ymin) / yres;
  
  if (xres < 10) {
    printf("Too small xres: %d.\nAborting the generation...\n", xres);
    return 1;
  } else if (yres < 10) {
    printf("Too small yres: %d.\nAborting the generation...\n", yres);
    return 1;
  }

  double x, y;
  double u, v;
  int i, j, iterations;
  for (j = 0; j < yres; j++) {
    y = ymax - j * dy;
    for (i = 0; i < xres; i++) {
      x = xmin + i * dx;
      iterations = get_iter(x, y, maxiter);

      if (iterations >= maxiter) {
        const unsigned char black[] = {
          0,
          0,
          0,
          0,
          0,
          0
        };
        fwrite(black, 6, 1, file);
      } else {
        const unsigned char color[] = {
          iterations >> 8,
          iterations & 255,
          iterations >> 8,
          iterations & 255,
          iterations >> 8,
          iterations & 255,
        };
        fwrite(color, 6, 1, file);
      };
    }
  }
  fclose(file);
  return 0;
}

int get_iter(double x, double y, int maxiter) {
  double u = 0.0;
  double v = 0.0;
  double u2 = 0.0;
  double v2 = 0.0;

  int i;

  for (i = 1; i < maxiter && (u2 + v2 < 4.0); i++) {
    v = 2 * u * v + y;
    u = u2 - v2 + x;
    u2 = u * u;
    v2 = v * v;
  };
  return i;
}