// circle.c: Prints the areas of circles.
// Use circulatearea.c for the math

#include <stdio.h>

double circularArea(double r);

int main()
{
    double radius = 1.0, area = 0.0;
    printf("\n");
    printf("    Area of circles\n\n");
    printf("    Radius          Area\n"
           "----------------------------\n"
    );
    area = circularArea(radius);
    printf("%10.1f      %10.2f\n",radius,area);
    
    radius = 5.0;
    area = circularArea(radius);
    printf("%10.1f      %10.2f\n", radius, area);
    return 0;
}

// The function circularArea() calculates the area of circle
// Parameter: The radius of the circle
// Return value: The area of the circle
double circularArea(double r)
{
    const double pi = 3.1415926536; // Pi is a constant
    return pi * r * r;
}


