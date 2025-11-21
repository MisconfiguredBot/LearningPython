def UserInput():

  print("Enter Your First Number:")
  FirstNumber = input()

  print("Enter Your Operator:")
  Operator = input()

  print("Enter Your Second Number:")
  SecondNumber = input()

  return FirstNumber, Operator, SecondNumber

def math(FirstNumber, Operator, SecondNumber):
  FirstNumber = float(FirstNumber)
  SecondNumber = float(SecondNumber)
  
  if Operator == '+':
    print("Equals =", FirstNumber + SecondNumber)

  elif Operator == '-':
    print("Equals =", FirstNumber - SecondNumber)

  elif Operator == '*':
    print("Equals =", FirstNumber * SecondNumber)

  elif Operator == '/':
    print("Equals =", FirstNumber / SecondNumber)
 
a, op, b = UserInput()
math(a, op, b)