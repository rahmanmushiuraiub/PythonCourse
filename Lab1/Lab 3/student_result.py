# single line comment
"""
multiline comment // docstream
this is cli application to calculate student result
and possibly to export them to csv file
"""

#user interface
# cli menu printing function(function= reusable codeblocks)

def print_menu() -> None:   #def=define,dynamically,statically,strongly,weakly typing,None=null data type
    print(" === student result CLI === ") #at end by default caerriage return add
    print(" 1) Add student + compute results ")
    print(" 2) View student and result summary ")
    print(" 3) Search student by id ")
    print(" 4) Delete student by id ")
    print(" 5) Export result to CSV file ")
    print(" 6) Exit ")

#main function -- do not start run code from here
def main() -> None:

    while True:  #boolean capital letter
         print_menu()
         #variable to store choice
         choice = input("enter ur choice(1-6): ").strip()
          # python does not have switch case but match is available
         match choice:
            case "1":
                print("adding student")
            case "2":
                print ("viewing student and result summary..")
            case "3":
                print("searching student")
            case "4":
                print("delete")
            case "6":
                print("exiting application")
                break
            case _: #default case
                print("inavlid choice")
 

if __name__ == "__main__": #elseif=elif in python, __magic function(dander function) 
    main()
    


