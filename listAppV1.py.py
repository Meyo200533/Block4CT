import random
myList = []
unique_List = []

def mainprogram():
    #build out while loop
    while True:
        print("hello,there! Let's work with lists!")
        print("please choose from the following options. type the number of the 
        choice = input ("""1. add to list<
2.Retun a vlue in a lsit,
3.add a bunch of numbers 
4.random search
5. linear search
6. print list
7.
8.quit  """)
              if choice == "1":
                  addtoList()
              elif choice =="2":
                  indexvalues()
              elif choice =="3":
                  randomsearch()
              elif choice =="4":
                  randomSearch()
              elif choice =="5":
                  linearsearch():
              elif choice == "6":
                  sortList(mylist)
            elif choice == '7':
                printlist()
                  
              else:
                  break
def addtoList():
    print ("adding to list! great choice!")
    mewItem = input("type an interger here!  ")
    myList.append(int(newItem))
    #we need to think about errors!

def addbunch():
    print("we are gonna add a bunch of numbers to your list!")
    numtoadd = input("how many new intergers would you like to add?  ")
    numrange = input(" and how high would you like those numbers to go?   ")
    for x in range (0, int(numtoadd)):
        print("your list is complete!")

def sortList(myList):
    #"myList" is the ARGUMANT this function takes.
    for x in range:
        if x not in unique_list:
            unique_list.append(x)
        unique_list.sort()
        showMe = input('wanna see your new,  shorted list?  y/n")
        if showMe.lower() =="y":
             print(unique_list)

def randomsearch():
    print("oH iM sO rAnDom!!!:)
    print("myList(random.randint(0, len(mylist)-1)])


def linearSearch():
    print("we're going to go thrugh this list one itme at a time!")
    searchvalue  = input ("what are you looking for?   ")
          for x in range(len(mylist)):
          print("your item is at index position{}".format(x))

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
    
