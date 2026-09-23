from validator import Validator
numInput = Validator.Number
def show_menu():
     return"""============================
1.Show device properties
============================
"""

is_running = True
while is_running:
     print(show_menu(), end="")
     choise = numInput.integer_input_rangeot(1,error_message="Only integer allowed",print_message="> ", error_range_message="Only (0-1) allowed")
     match choise:
          case 0:
               is_running = False
          case 1:
               print("Hola",end="\n\n")