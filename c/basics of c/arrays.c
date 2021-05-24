#include <stdio.h>

int main() {
    // defines an array of 3 integers 
    int numbers[7];
    int average;

    // populate the array 
    numbers[0] = 10;
    numbers[1] = 20;
    numbers[2] = 30;
    numbers[3] = 40;
    numbers[4] = 50;
    numbers[5] = 60;
    numbers[6] = 70;

    // print the 7th number from the array, which has an index of 6
    printf("The 7th number in the array is %d\n", numbers[6]);
    // finds the average of the array
    average = (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6]) / 7;
    printf("The Average is %d\n",average);
  return 0;
}