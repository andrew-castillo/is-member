"""
is_member.py: Recursive implementation of is_member() on a set
              represented by a sorted list of integers
Authors: Andrew Castillo
Credits:
MVP Richelle Cabatic (consulted with on the binary search thing)

CIS 210 assignment 5, part 2, Fall 2016. 
"""
import argparse      # Used in main program to get PIN code from command line
from test_harness import testEQ  # Used in CIS 210 for test cases 

## Constants used by this program

def gen_set(set_file):
    """
    Function reads a text file and creates a sorted list of lines that
    are an element of the integers.
    
    args:
        set_file: file containing integers on each line

    returns:
        the_set: sorted list of all lines in set_file
    """
    the_set = []
    
    for line in set_file:
        line = line.strip()
        the_set.append(int(line))

    the_set.sort()
    
    return the_set

def is_member(set, number):
    """
    Function checks if the length of the set is 0, then if the number
    inputted matches set[-1].

    args:
        set: sorted list of int values to search through
        number: an integer value

    returns:
        boolean value, True if number is in the set, False otherwise.
    
    """
    if set[0] == number:
        return True
    if len(set) > 1:
        middle = len(set)//2 
        current_num = set[middle]

        if number == current_num:
            return True
        
        elif number > current_num:
            return is_member(set[middle:], number)#####leaving slice index empty creates an error?

        elif number < current_num:
            return is_member(set[:middle], number)
    return False



def run_tests():
    """
    This function runs a set of tests to help you debug your
    program as you develop it.
    """
    l = [-27, -12, -5, -1, 0, 2, 3, 6, 8, 10, 13, 25, 46, 99]
    print("**** TESTING --- Check membership of locally-defined set")
    print(l)
    testEQ("-99 is False", is_member(l, -99), False)
    testEQ("115 is False", is_member(l, 115), False)
    testEQ("-27 is True", is_member(l, -27), True)
    testEQ("99 is True", is_member(l, 99), True)
    testEQ("0 is True", is_member(l, 0), True)
    testEQ("-4 is False", is_member(l, -4), False)
    testEQ("14 is False", is_member(l, 14), False)
    print("*** End of provided test cases.  Add some of your own? ****")

def main():
    """
    Interaction if run from the command line.
    """
    parser = argparse.ArgumentParser(description="Recursive implementation of is_member()")
    parser.add_argument("set", type=argparse.FileType('r'),
                        help="A text file containing set elements, one per line.")
    parser.add_argument("number", type=int, help="number to check for membership")
    args = parser.parse_args()  # gets arguments from command line
    set_file = args.set
    number = args.number
    the_set = gen_set(set_file)
    if is_member(the_set, number):
        print(number, "is an element of the set")
    else:
        print(number, "is not an element of the set")

if __name__ == "__main__":
    #run_tests()
    main()
