#TempConvert.py
#Name:Erick Andres
#Date: 2/7/2026
#Assignment: Lab 3
#Purpose:To convert temperature from fahrenheit to celcius and display the result


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter temperature in Fahrenheit: "))

  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = (tempF-32) * 5/9
  tempC = round(tempC, 1)

  #Output converted temperature.

  print(tempF, "is", tempC, "degrees Celsius.")
if __name__ == '__main__':
  main()
