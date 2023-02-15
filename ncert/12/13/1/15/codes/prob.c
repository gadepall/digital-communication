#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int N = 10000000;   // Number of samples
    int c = 2, d = 6;   // Total number of outcomes for coin and die
    int arr[6][8];      // Array counting probabilities
    memset(arr, 0, sizeof(arr));
    // Generate a random number N times
    // and tabulate the probabilities
    for (int i = 0; i < N; i++) { 
        int smpl = rand()%d;
        if (smpl%3 == 0) { 
            int toss = rand()%c;
            ++arr[smpl][toss];
        } else { 
            int roll = rand()%d;
            ++arr[smpl][roll+2];
        }
    }
    // Obtain marginal probabilities
    int t = 0;
    for (int i = 0; i < 8; i++) { 
        t += arr[2][i];
    }
    // Print theoretical and empirical probabilities
    printf("Theoretical probability: 0\nEmpirical probability: %lf\n", (1.0*arr[2][0])/t);
}
