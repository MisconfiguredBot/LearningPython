def UserInput():

  print("Enter Your First Number:")
  firstNum = input()

  print("Enter Your Operator:")
  Operator = input()

  print("Enter Your Second Number:")
  secondNum = input()

  return firstNum, Operator, secondNum

def math(firstNum, Operator, secondNum):
  firstNum = float(firstNum)
  secondNum = float(secondNum)
  
  if Operator == '+':
    return firstNum + secondNum

  elif Operator == '-':
    return firstNum - secondNum

  elif Operator == '*':
    return firstNum * secondNum

  elif Operator == '/':
    return firstNum / secondNum
 
result = None 

while True:
  if result is None:
    a, op, b = UserInput()

  else:
    print("Previous result =", result)
    a = result
    op = input("Enter Operator: ")
    b = input("Enter Next Number: ")

  result = math(a, op, b)
  print("Equals =", result)

  again = input("Do another? (y/n): ")
  if again.lower() != "y":
    break
  
print("Cyah!")

 
a, op, b = UserInput()
math(a, op, b)