import SpaceTimeComplex


def looper2(n):
    for x in range(n[0]):
        print(x)

def testone(n):
    for x in range(len(n)):
        for y in range(len(n)):
            for z in range(len(n)):
              two = y
              one = x
              three = z

def looper(n):
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

testSet = real.generateTestSet() #generate a test set

testSet1 = [[4,"stnr=gwege"], [12,"sagsdgg"], [3,"esfsfsseafesfsefsef"]] # format of array. 2d array with each test set inside

real.complexGuess(testone,testSet) #guess the complexity of a function. Returns the guess and a plot


