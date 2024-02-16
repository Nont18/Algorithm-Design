#include <stdio.h>

void merge(int A[], int p, int q, int r) {
    int n1 = q - p + 1;
    int n2 = r - q;
    int L[n1], R[n2];

    // Copy data to temporary arrays L[] and R[]
    for (int i = 0; i < n1; i++) {
        L[i] = A[p + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = A[q + 1 + j];
    }

    // Merge the two arrays back into A[p..r]
    int i = 0, j = 0, k = p;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if there are any
    while (i < n1) {
        A[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if there are any
    while (j < n2) {
        A[k] = R[j];
        j++;
        k++;
    }
}

int mergesort(int A[],int p, int r){
    if(p==r){
        return 0;
    }
    int q = (p+r)/2;
    mergesort(A,p,q);
    mergesort(A,q+1,r);
    merge(A,p,q,r);

}




int main(){
    int A[] = {31,41,59,26,41,58};
    // = {37, 89, 14, 52, 71, 9, 66, 44, 28, 7, 50, 61, 83, 95, 19, 76,
    //  2, 68, 34, 56, 93, 11, 72, 30, 84, 5, 23, 78, 47, 64, 16, 98, 39, 57, 21,
    //  87, 13, 70, 45, 81, 8, 31, 74, 49, 26, 69, 92, 12, 59, 4, 41, 75, 27, 53,
    //  90, 20, 65, 3, 88, 18, 48, 79, 33, 60, 91, 22, 86, 10, 37, 55, 77, 35, 67,
    //  1, 58, 96, 17, 82, 29, 43, 63, 6, 80, 25, 51, 38, 73, 15, 94, 24, 62, 42,
    //  99, 32, 54, 40, 85, 46, 97, 36, 100};
    int p = 0;
    int r = (sizeof(A)/sizeof(A[0]))-1;
    mergesort(A,p,r);


// Print the sorted array
    printf("Sorted array: ");
    for (int i = 0; i <= r; i++) {
        printf("%d ", A[i]);
    }

    return 0;



}