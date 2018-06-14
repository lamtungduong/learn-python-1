def getNumberFromInput(name):
  title = "Please enter "+name+" number: "
  while(True):
    try:
      data = float(raw_input(title))
    except ValueError:
      title = "It's not number, Please type again: "
      continue
    else:
      break
  return data
def sum(number1, number2):
  return number1 + number2

def main():
  print "====== Hello World ======"
  print "Program: Sum Of Two Numbers"
  number1 = getNumberFromInput("first")
  number2 = getNumberFromInput("second")
  result = sum(number1, number2)
  print "Result %s + %s =  %s" % (number1, number2, result)

main()