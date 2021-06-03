#include <stdio.h>

int main() {
  int a = 3; // basic number
  float b = 4.5; // numbers with fractions
  double c = 5.25; // Double is more precise than float 
  float sum;

  sum = c + b + a; // addition
  sum = c - b - a; // subtraction
  sum = c * b * a; // multiplication
  sum = c / b / a; // division

  printf("The sum of a, b, and c is %f.\n", sum);
  return 0;
}