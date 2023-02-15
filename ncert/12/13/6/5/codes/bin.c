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
    double p = 2.0/5;   // Probability of success
    int n = 6;          // Number of trials     
    int arr[n+1]; memset(arr, 0, sizeof(arr)); // Initialize pmf array
    for (int i = 0; i < N; i++) {
        int ans = 0;
        for (int j = 0; j < n; j++) ans += bernoulli(p);
        ++arr[ans];
    }
    for (int i = 0; i < n+1; i++) printf("%d ", arr[i]);
    printf("\n");
    // Answers
    double a1 = 0.004096;
    double a2 = 0.1792;
    double a3 = 0.995904;
    double a4 = 0.27648;
    // Answer 1
    printf("Answer 1\n");
    printf("Theoretical probability: %lf\nEmpirical probability: %lf\n", a1, (1.0*arr[6])/N);
    // Answer 2
    printf("Answer 2\n");
    printf("Theoretical probability: %lf\nEmpirical probability: %lf\n", a2, (1.0*arr[4]+arr[5]+arr[6])/N);
    // Answer 3
    printf("Answer 3\n");
    printf("Theoretical probability: %lf\nEmpirical probability: %lf\n", a3, 1.0 - (1.0*arr[6])/N);
    // Answer 4
    printf("Answer 4\n");
    printf("Theoretical probability: %lf\nEmpirical probability: %lf\n", a4, (1.0*arr[3])/N);
}
