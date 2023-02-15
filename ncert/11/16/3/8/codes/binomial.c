#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// Generate a bernoulli sample
// p is the probability of success
int bernoulli(double p) { 
    double s = (double)rand()/RAND_MAX;
    return (s <= p)?1:0;
}

// Calculate factorial of small numbers
int fac(int n) {
    int ans = 1;
    for (int i = 1; i <= n; i++) ans *= i;
    return ans;
}

int main() {
    srand(time(NULL));
    int N = 10000000;   // Number of samples
    double p = 0.5;   // Probability of success
    int n = 3;          // Number of trials     
    int arr[n+1]; memset(arr, 0, sizeof(arr)); // Initialize pmf array
    for (int i = 0; i < N; i++) {
        int ans = 0;
        for (int j = 0; j < n; j++) ans += bernoulli(p);
        ++arr[ans];
    }
    // Verify with actual pmfs
    double tharr[n+1];
    for (int i = 0; i <= n; i++) { 
        tharr[i] = fac(n)/(fac(i)*fac(n-i))*pow(p,i)*pow(1-p,n-i);
    }
    printf("Theoretical pmfs:\n");
    for (int i = 0; i <= n; i++) printf("%lf ", tharr[i]);
    printf("\nEmpirical pmfs:\n");
    for (int i = 0; i <= n; i++) printf("%lf ", arr[i]/(1.0*N));
    return 0;
}
