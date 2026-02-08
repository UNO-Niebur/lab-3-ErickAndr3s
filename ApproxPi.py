#ApproxPi.py
#Name:Erick Andres
#Date:2/7/2026
#Assignment:Lab 3
#Purpose:Approximate π using a mathematical series and measure execution time.
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal precision (up to 10)
  precision = int(input("Enter the number of decimal places for pi (1-10): "))

  start = time.time()

  #calculate pi using the approximation technique
  approxPi = 4.0
  sign= -1 
  denom = 3

  #Loop until the level of percision is reached
  while round(approxPi, precision) != round(realPi, precision):
    approxPi += sign * 4 / denom
    sign *= -1
    denom += 2

  #print(approxPi)
  end = time.time()
  elapsedTime = end - start

  print(f"Approximated pi: {round(approxPi, precision)}")
  print(f"Real pi: {round(realPi, precision)}")
  print(f"Time elapsed:  {elapsedTime:.6f} seconds")


if __name__ == '__main__':
  main()
