import random
myList = []
unique_List = []

def mainprogram():
    #build out while loop
    while True:
        print("hello,there! Let's work with lists!")
        print("please choose from the following options. type a NUMBER ONLY ")
        choice = input ("""1. add to list<
1.add to list 
2.add a bunch of numbers 
3.Retun the value at an index position,
4.short list,
5.random choice
6.linear search,
7.Recursive search
8.print lsit,
9.find sun of numbers,
10.end program  """)
        if choice == "1":
            addtolist()
        elif choice == "2":
            addaBunch()
        elif choice == "3":
            indexValues()
        elif choice == "4":
            sortList(myList)
        elif chouce == "5":
            randomSearch()
        elif choice == "6":
            linearSearch()
        elif choice == "7":
            binsearch = input("What numbers are you looking for? ")
            reacursiveBianarySearch(unique_list, 0, len(unique_list)-1, int(binsearch))
        elif choice == "8":
            printList()
        elif choice == "9":
            numberSum()
        else:
            break
        except:
            print("An ERROR occurred")
            
def addtoList():
    newItem = input("Please type an integer!  ")
    myList.append(int(newitem))
    print(myList)

def addbunch():
    print("We're gonna add a bunch of numbers to your list!")
    numtoAdd = input("How many new intergers would you like to add?  ")
    numrange = input("And how high would you like those numbers to go?   ")
    for x in range (0, int(numtoadd)):
        myList.append(random.randint(0,int(numRange)))
        print("Your list is complete!")

def sortList(myList):
    for x in my list:
        if x not in unique_list:
            unique_list.append(x)
        unique_list.sort()
        showMe = input('Wanna see your new,  shorted list?  y/n")
        if showMe.lower() == "y":
             print(unique_list)

def numbernum():
    1st = []
    num = int(input("would you like to add up?  "))
    for x in range(num):
        numbers = int(input("Number  "))
        1st.append(numbers)
        print("The sum of your numbers are  ",sum(1st))
            
    
def randomsearch():
    print("We picked a random number for you!!!")
    print("myList(random.randint(0, len(mylist)-1)])


def linearSearch():
    print("we're going to go thrugh this list one itme at a time!")
    searchvalue  = input ("what are you looking for?   ")
          for x in range(len(mylist)):
          print("your item is at index position{}".format(x))

def recursiveBinarySearch(unique_List, low, High, x):
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

def iterativeBinary(unique_list, X):
    low = 0
    high 
        
          

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
    
