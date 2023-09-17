#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(0));
    int c1=0;
    int c2=0;
    double pAB = (double)7/10;
    double pB = (double)17/20;
    for (int i=0; i<10000; i++) {
        if ((double)rand() / RAND_MAX < pAB)
            c1++;

        if ((double)rand() / RAND_MAX < pB)
            c2++;
    }
    printf("P(A|B)=%lf\n", (double)c1/c2);
    return 0;
}
