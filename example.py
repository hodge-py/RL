import SpaceTimeComplex


def looper2(n):
    for x in range(n):
        print(x)

def testone(n):
    for x in range(len(n)):
        for y in range(len(n)):
            for z in range(len(n)):
              two = y
              one = x
              three = z

def looper(today,stringer):
    for x in range(today):
        print(x)
    
    for y in stringer:
        print(y)



def logfunc(n):
    for x in range(0,len(n[0]),20):
        print(x) 


def binary_search(array,target):
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

testSet = real.generateTestSet(size2=100) #generate a test set

testSet1 = [[4,"stnr=gwege"], [12,"sagsdgg"], [3,"esfsfsseafesfsefsef"], [45,"stnrefgseege"], [17,"sagwetjtwfwe"], [34,"esfsfssem"],[41,"stn"], [53,"sakhhksdgg"], [24,"esjfjkkfsefsef"], [70,"stnwete"], [7,"sagwefwewsdfsdffwe"] ] 
# format of array. 2d array with each test set inside. You can make your own or just generate one with generateTestSet()

#real.complexGuess(testone,testSet) #guess the complexity of a function. Returns the guess and a plot

ratio = real.bestWorst(testone,testSet)


