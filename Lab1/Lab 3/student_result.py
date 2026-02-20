# single line comment
"""
multiline comment // docstream
this is cli application to calculate student result
and possibly to export them to csv file
"""

#helper function
def prompt_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Empty input is not allowed. Try again.")

def clean_name(raw_name: str) -> str:
    return raw_name.strip().title()
def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if val < min_val:
            print(f"Value must be at least {min_val}. Try again.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}. Try again.")
            continue
        return val
def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if val < min_val:
            print(f"Value must be at least {min_val}. Try again.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}. Try again.")
            continue
        return val

def compute_total_and_percentage(marks: list[float]) -> tuple[float, float]:
    # total = sum(marks)
    total = 0.0
    for m in marks:
        total += m
    percentage = total / len(marks)
    return total, percentage

def grade_from_percentage(pct: float) -> str:
    if pct >= 90.0:
        return "A"
    elif pct >= 80.0:
        return "B"
    elif pct >= 70.0:
        return "C"
    elif pct >= 60.0:
        return "D"
    else:
        return "F"

        
#app functionalities implementation

def add_students(students: list[dict]) -> None:
    sid = 

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
    #list to contain students like key value pairs--id,name,credit of a students
   students: list[dict] = []

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
    


