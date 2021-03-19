import random
myList = []

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
7.quit  """)
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
              elif choice == "5":
                  print (myList)
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

def randomsearch():
    print("oH iM sO rAnDom!!!:)
    print("myList(random.randint(0, len(mylist)-1)])

def linearSearch():
    print("we're going to go thrugh this list one itme at a time!"0
    searchvalue  = input ("what are you looking for?   ")
          for x in range(len(mylist)):
          print("your item is at index position{}".format(x))
          

def indexValues():
    print("At what index position do you want to search?")
    indexpos = input ("type an index  position here:
    print(myList(int(indexpos)])

if __name__ == "__main__":
    mainprogram()
    
