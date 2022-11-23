#include <stdio.h>
#include <math.h>

int fibonacci(int k);
void show_confidence_interval(float p, int n);
struct ConfidenceInterval get_confidence_interval(float p, int n);

struct ConfidenceInterval{
    float left;
    float right;
};

int main() {
   printf("Hello, World!\n");

    int a = 5;
    int b = 3;
    int c = a + b;

    printf("%d + %d = %d \n", a, b, c);

    char letter = 'W';
    printf("%c\n", letter);


    // if statements

    float n = 2.4;
    int k = 2;
    if (a > b){
        printf("%f is greater than %d.\n", n, k);
    }
    else{
        printf("%d is greater than %f.\n", k, n);
    }
    
    a = 1;
    b = 1;
    int fibo = 0;

    int i = 2;
    k = 8;
    // while loop
    while (i < k){
        fibo = a + b;
        a = b;
        b = fibo;
        i = i + 1;
    }

    printf("The %d-th fibonacci number is %d.\n", k, fibo);

    int start = 1;
    int end = 10;
    int sum = 0;
    // for loops
    for (int j = start; j <= end; j++){
        sum += j;
    }
    printf("The sum from %d to %d is %d.\n", start, end, sum);


    // calling function

    k = 10;
    fibo = fibonacci(k);
    printf("The %d-th fibonacci number is %d.\n", k, fibo);

    k = 12;
    printf("The %d-th fibonacci number is %d.\n", k, fibonacci(k));

    show_confidence_interval(0.2, 100);

    // structs
    struct ConfidenceInterval ci = get_confidence_interval(0.2, 100);
    printf("Confidence Interval using structs (%f, %f)", ci.left, ci.right);

    // parsing input file

   return 0;
}


int fibonacci(int k){
    int a = 1;
    int b = 1;
    int fibo = 0;

    int i = 2;
    // while loop
    while (i < k){
        fibo = a + b;
        a = b;
        b = fibo;
        i = i + 1;
    }
    return fibo;
}

void show_confidence_interval(float p, int n){
    float ci = 1.96 * sqrt(p * (1-p)/n);
    printf("Confidence interval of bernoulli variable with p=%f and n=%d is (%f, %f)\n", p, n, p-ci, p+ci);
}

struct ConfidenceInterval get_confidence_interval(float p, int n){
    float ci_half_length = 1.96 * sqrt(p * (1-p)/n);
    
    struct ConfidenceInterval ci;
    ci.left = p - ci_half_length;
    ci.right = p + ci_half_length;
    return ci;
}