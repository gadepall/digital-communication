#include <stdio.h>
#include <math.h>

// Function to calculate the entropy of a random variable X
double entropy(double x[], int n) {
    double ent = 0.0;
    for (int i = 0; i < n; i++) {
        if (x[i] > 0) {
            ent -= x[i] * log2(x[i]);
        }
    }
    return ent;
}

int main() {
 
    double X[] = {1.0 / 4.0, 1.0 / 2.0, 1.0 / 4.0}; 

    int K = sizeof(X) / sizeof(X[0]); 


    double HX = entropy(X, K);

   
    double H2X = entropy(X, K); 
    double HX2 = entropy(X, K); 
    double H2PowX = entropy(X, K); 

    // Update the distribution for X^2
    double X2[K];
    for (int i = 0; i < K; i++) {
        X2[i] = X[i] * X[i];
    }
    double HX2_updated = entropy(X2, K);

    // Check the statements
    printf("H(X) <= log2(K) bits: %s\n", HX <= log2(K) ? "True" : "False");
    printf("H(X) <= H(2X): %s\n", HX <= H2X ? "True" : "False");
    printf("H(X) <= H(X^2): %s\n", HX <= HX2_updated ? "True" : "False");
    printf("H(X) <= H(2^X): %s\n", HX <= H2PowX ? "True" : "False");

    return 0;
}

