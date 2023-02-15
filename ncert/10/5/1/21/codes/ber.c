#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int N = 10000000;    // Number of samples
    int t = 144;        // Total number of pens
    int d = 20;         // Number of defective pens
    int ctr = 0;        // Number of successful trials
    double p = 1.0 - (1.0*d)/t;   // Probability of success
    // Generate a random number N times
    // and count the number of successes.
    for (int i = 0; i < N; i++) { 
        int smpl = rand()%t;
        if (smpl >= d) ++ctr;
    }
    // Print theoretical and empirical probabilities
    printf("Theoretical probability: %lf\nEmpirical probability: %lf\n", p, (1.0*ctr)/N);
}
