def display_mainmenu():
    print ("main menu")
    print("enter some num separated by commas")


def get_user_input():
    print ("get user input")
    inputstr = input()
    print ("raw input=",inputstr)
    #split inputstr into segment of strings using comma as splliter 
    splitlist = inputstr.split(",")
    print ("after split input=" , splitlist)
    #next step is to convert each short string in the list into float
    floatlist = [] #define an empty list of float numbers
    for x in splitlist:
        floatnum = float(x) #convert string to float
        floatlist.append(floatnum)#Add the float number to the float list
    
    print ("floatlist=",floatlist)
    return floatlist

def calc_avg():
    print ("calc average")

def find_min_max():
    print ("get min max")

def sort_temp():
    print ("sort temp")

def calc_median_temp():
    print ("calc median")

def main():
  display_mainmenu()
  floatlist = get_user_input()

    
if __name__ =="__main__":
    main()