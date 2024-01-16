import SpaceTimeComplex



def looper2(n):
    for x in range(n[0]):
        print(x)

def testone(n):
    for x in range(len(n[0])):
        for y in range(len(n[0])):
            two = y
            one = x

def looper(n):
    today = n[0]
    stringer = n[1]
    for x in range(today):
        print(x)
    
    for y in stringer:
        print(y)

def logfunc(n):
    for x in range(0,len(n[0]),20):
        print(x)


def binary_search(n):
  array = n[0]
  target = n[1]
  low = 0
  high = len(array) - 1
  while low <= high:
    mid = (low + high) // 2 # integer division
    element = array[mid]
    if element == target:
      return mid
    elif element < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

real = SpaceTimeComplex.RealTime() # Create the class
#x.realTimeComplex(stmt="looper(10)",value=10)

testSet = real.generateTestSet(amount=100,type=0) #generate a test set

testSet1 = { # Test set example structure
            0: [4,"stnr=gwege"],
            1: [12,"sagsdgg"],
            2: [3,"esfsfsseafesfsefsef"]
            }

real.complexGuess(binary_search,testSet) #guess the complexity of a function. Returns the guess and a plot


