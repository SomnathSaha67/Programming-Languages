#include <stdio.h>
#include <math.h>   
void main() {
    float radius, area;
    const float PI = 3.14159;
    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);
    area = PI * pow(radius, 2);
    printf("The area of the circle with radius %.2f is %.2f\n", radius, area);
}