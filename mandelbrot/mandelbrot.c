#include <stdio.h>
#include <complex.h>

enum {size = 10000};
int set[size*2][size*2];

int mandelbrot(complex double c, int thresh, int max_steps){
    
    complex double z = c;
    int iterations = 1;

    while (iterations < max_steps &&  creal(z*conj(z)) < thresh){
        z = z * z + c;
        iterations += 1;
    }
    return iterations;
}

int main(){
    complex double c;

    double mx = 2.48 / (size - 1);
    double my = 2.26 / (size - 1);
    

    for (int x = -size; x<size; x++){
        
        for (int y = -size; y<size; y++){
            
            c = mx * x - 1 + my * y * I ;
            int iterations = mandelbrot(c, 4, 50);
            if (iterations != 50){
                //printf("%d at %f + %f\n", iterations, creal(c), cimag(c));
            }
            //printf("%f + %f\n", creal(c), cimag(c));

            set[x+size][y+size] = iterations;
        }
    }

    for(int i = 0; i < size*2; i++) {
        for(int j = 0; j < size*2; j++) {
            if (set[i][j] != 50){
                printf("*", set[i][j]);
            } else {
                printf(" ");
            }
        }
    printf("\n");
    } 
}
