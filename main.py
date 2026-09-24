from tools import Validator
import sysinfo
from tools import clearScreen
numInput = Validator.Number
def show_menu():
     return"""============================
1.Show device properties
0.Exit
============================
"""

def main():
     is_running = True
     while is_running:
          clearScreen()
          print(show_menu(), end="")
          choise = numInput.integer_input_rangeot(1,error_message="Only integer allowed",print_message="> ", error_range_message="Only (0-1) allowed")
          match choise:
               case 0:
                    break;
               case 1:
                    clearScreen()
                    sysinfo.get_info()
                    input("Press enter to continue")

if __name__ == "__main__":
     main()