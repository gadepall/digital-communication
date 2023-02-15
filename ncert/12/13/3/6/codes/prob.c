#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Generate a bernoulli sample
// p is the probability of success
int bernoulli(double p) { 
    double s = (double)rand()/RAND_MAX;
    return (s <= p)?1:0;
}

int main() {
    srand(time(NULL));
    int N = 10000000;   // Number of samples
    double x = 1.0/3;   // Probability of choosing a single coin
    double y1 = 1, y2 = 3.0/4, y3 = 1.0/2;  // Bernoulli parameters
    int arr[3][2]; memset(arr, 0, sizeof(arr)); // Initialize the joint pmf array
    for (int i = 0; i < N; i++) { 
        double smpl = (double)rand()/RAND_MAX;
        if (smpl < x) ++arr[0][bernoulli(y1)];
        else if (smpl < 2*x) ++arr[1][bernoulli(y2)];
        else ++arr[2][bernoulli(y3)];
    }
    // Obtain probability that Y=1
    int y = 0;
    for (int i = 0; i < 3; i++) y += arr[i][1];
    // Print theoretical and empirical probabilities
    printf("Theoretical probability: %lf\nEmpirical probability: %lf\n", 4.0/9, (1.0*arr[0][1])/y);
}
