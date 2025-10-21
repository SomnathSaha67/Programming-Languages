#include <stdio.h>
#include <stdlib.h>
int main(void) {
    char operator;
    printf("Enter operator (+, -, *, /): ");
    if (scanf(" %c", &operator) != 1) return 1;
    int n;
    printf("Enter number of operands: ");
    if (scanf("%d", &n) != 1) return 1;
    if (n <= 0) {
        printf("Number of operands must be >= 1\n");
    }
    if (operator == '+') {
        double total = 0.0;
        for (int i = 0; i < n; ++i) {
            double val;
            printf("Enter operand %d: ", i + 1);
            if (scanf("%lf", &val) != 1) return 1;
            total += val;
        }
        printf("%g\n", total);
    } else if (operator == '-') {
        double result;
        printf("Enter operand 1: ");
        if (scanf("%lf", &result) != 1) return 1;
        for (int i = 2; i <= n; ++i) {
            double val;
            printf("Enter operand %d: ", i);
            if (scanf("%lf", &val) != 1) return 1;
            result -= val;
        }
        printf("%g\n", result);
    } else if (operator == '*') {
        double result = 1.0;
        for (int i = 0; i < n; ++i) {
            double val;
            printf("Enter operand %d: ", i + 1);
            if (scanf("%lf", &val) != 1) return 1;
            result *= val;
        }
        printf("%g\n", result);
    } else if (operator == '/') {
        double result;
        printf("Enter operand 1: ");
        if (scanf("%lf", &result) != 1) return 1;
        for (int i = 2; i <= n; ++i) {
            double denom;
            printf("Enter operand %d: ", i);
            if (scanf("%lf", &denom) != 1) return 1;
            if (denom == 0.0) {
                printf("Division by zero.\n");
            }
            result /= denom;
        }
        printf("%g\n", result);
    } else {
        printf("Invalid operator!\n");
    }
    return 0;
}