#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <float.h>

void main()
{
	FILE *fp;
	int i, j, n=1000000;
	double temp, x, sum=0, sum_sq=0, mean, var;
	fp= fopen("Gaussian.dat", "w");
	for(i=0; i<n;i++)
	{
		temp= 0;
		for(j=0; j<12;j++)
		{
			temp= temp + (double)rand()/RAND_MAX;
		}
		x= temp-6;
		fprintf(fp,"%lf\n",x);
		//printf("%lf\t", x);
		sum=sum+x;
		sum_sq= sum_sq+ (x*x);
	}
	fclose(fp);
	mean= sum/n;
	var= (sum_sq/n)- (mean*mean);
	printf("\nThe mean and variance are: %lf\t %lf",mean, var );
}
	
