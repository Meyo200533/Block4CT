import random
myList = []
unique_List = []

def mainprogram():
    #build out while loop
    while True:
        print("hello,there! Let's work with lists!")
        print("please choose from the following options. type the number of the choice")
        choice = input ("""1. add to list,
2.add a bunch of numbers,
3.get an item at an index 
4.sort list 
5.random search 
6.linear search 
7.recursive Bianary search 
8.iterative Bianary search
9.print list
10. quit  """)
              if choice == "1":
                  addToList()
              elif choice == "2":
                  addBunch()
              elif choice == "3":
                  indexValues()
              elif choice == "4":
                  sortList(myList)
              elif choice =="5":
                  randomSearch():
              elif choice == "6":
                  linearSearch()
              elif choice == '7':
                binSearch- input("what number are you looking for?  ")
                reacursiveHinarySearch(unique_List, 0, len(unique_List)-1, int(binSearch)
              elif choice == "8":
                  binSearch - input("what number are you looking for?  ")
                  result = iterativeBinarySearch(unique_List, int(binSearch))
                  if result != -1:
                      print("your number is at index position {}".format(resulte))
                  else:
                      print("your number is not found in that, bud!")

            elif choice == "9":
                printLists()
            else:
                  break
def addToList():
    
    print ("Adding to list! Great choice!")
    mewItem = input("Type an interger here!  ")
    myList.append(int(newItem))
    #we need to think about errors!

def addABunch():
    print("We're gonna add a bunch of numbers to your list!")
    numToAdd = input("how many new intergers would you like to add?  ")
    numrange = input("And how high would you like those numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
        print("Your list is complete!")

def sortList(myList):
    #note that this is the first function we've built here that takes ARGUMENTS
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
        unique_list.sort()
        showMe = input("would you like to see the unique values in your list?  y/n")
        if showMe.lower() == "y":
             print(unique_list)
            
def indexValues():
    print("At what index position do you want to search?")
    indexpos = input("type an index position here:
    print(myList[int(indexpos)])
                    

def randomsearch():
    print("oH iM sO rAnDom!!!:)
    print("myList(random.randint(0, len(mylist)-1)])
    if len(unique_list[random.randint(0, len)uniqie_list)-1)])


def linearSearch():
    print("we're going to go thrugh this list one itme at a time!")
    searchvalue  = input ("what are you looking for?   ")
    for x in range(len(mylist)):
        if myList[x] == int(searchValue):
          print("your item is at index position{}".format(x))

def printLists():
    if len(unique_lsit) == 0:
        print(myList)
  else:
      whichOne = input("which list do you want to see, sorted or un-sorted ?  ")
      if whichOne.lower() == "sorted":
          print(unique_list)

def recursivebinarySearch(unique_List, low, High, x):
    if high >= low:
        mid = (high + low) //2
        if unique_list[mid] == x:
            print("your number is at index position{}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursivebinarysearch(unique_list, low, mid-1, x)
        elif:
            return recursviebinarysearch(unique_list, mid, +1, high, x)
    else:
        print("your number isn't here!")
          

def indexValues():
    print("At what index position do you want to search?")
    indexpos = input ("type an index  position here:
    print(myList(int(indexpos)])

def printlist():
    if len(unique_list) == 0:
        print(mylist)
    else:
        whichOne  = input ("which list do you want to see? sorted or un un-sorted")
        if which.lower() == "sorted":
            print(unique_list)               
    

if __name__ == "__main__":
    mainprogram()
    
