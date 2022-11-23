#include <stdio.h>
/*
Find the two numbers that sum up to 2020 and return their product
*/
int main() {
    int arr[200];

    const char* filename = "input/day01.txt";
    FILE* file = fopen (filename, "r");
    int n = 0;
    int i = 0;
    fscanf (file, "%d", &n);
    while (!feof (file)){
        printf("%d ", n);
        arr[i] = n;
        fscanf (file, "%d", &n);
        i = i + 1;
    }
    fclose (file);

    for (i=0; i < 200; i++){
        for (int j = i+1; j <200; j++){
            if (arr[i] + arr[j] == 2020){
                printf("\n%d * %d = %d\n", arr[i], arr[j], arr[i]*arr[j]);
            }
        }
    }

    for (i=0; i < 200; i++){
        for (int j = i+1; j <200; j++){
            for (int k = j+1; k <200; k++){
                if (arr[i] + arr[j] + arr[k] == 2020){
                    printf("\n%d * %d * %d = %d\n", arr[i], arr[j], arr[k], arr[i]*arr[j]*arr[k]);
                }
            }
        }
    }
    
}