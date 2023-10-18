



#include <stdio.h>
#include <math.h>

double binomialCoeff(int n, int k) {
    double result = 1.0;
    for (int i = 1; i <= k; i++) {
        result *= (double)(n - i + 1) / i;
    }
    return result;
}

int main() {
    int n = 5;        
    double p = 0.5;   
    int k = 3;        

    double binomial_pmf = binomialCoeff(n, k) * pow(p, k) * pow(1 - p, n - k);
    double mu = n * p;
    double sigma = sqrt(n * p * (1 - p));

    double normal_pdf = exp(-0.5 * pow((k - mu) / sigma, 2)) / (sigma * sqrt(2 * M_PI));
    double normal_ans1 = exp(-0.5 * pow((k - mu) / sigma, 2)) / (sigma * sqrt(2 * M_PI));

    printf("answer through normal dist: %lf\n", normal_ans1);
    printf("answer through binomial dist: %lf\n", binomial_pmf);

    return 0;
}

