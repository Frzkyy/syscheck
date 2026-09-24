class Validator:
     class Number:
          # ==================== INTEGER ====================
          #only integer
          @staticmethod
          def integer_input(print_message=None, error_message=None):
               while True:
                    try:
                         return int(input(print_message or ""))

                    except ValueError:
                         if error_message:
                              print(error_message)


          #integer with top limit (bottom =0)
          @staticmethod
          def integer_input_rangeot(top,print_message=None,error_message=None,error_range_message=None):
               while True:
                    number = Validator.Number.integer_input(print_message,error_message)

                    if 0 <= number <= top:
                         return number

                    if error_range_message:
                         print(error_range_message)


          #integer with custom range
          @staticmethod
          def integer_input_range(bottom,top, print_message=None,error_message=None,error_range_message=None):
               while True:
                    number = Validator.Number.integer_input(print_message,error_message)

                    if bottom <= number <= top:
                         return number

                    if error_range_message:
                         print(error_range_message)


          # ==================== FLOAT ====================
          #only float
          @staticmethod
          def float_input(print_message=None, error_message=None):
               while True:
                    try:
                         return float(input(print_message or ""))

                    except ValueError:
                         if error_message:
                              print(error_message)


          #float with top limit(bottom = 0)
          @staticmethod
          def float_input_rangeot(top,print_message=None,error_message=None,error_range_message=None):
               while True:
                    number = Validator.Number.float_input(print_message,error_message)

                    if 0 <= number <= top:
                         return number

                    if error_range_message:
                         print(error_range_message)


          #float with custom range
          @staticmethod
          def float_input_range(bottom,top,print_message=None,error_message=None,error_range_message=None):
               while True:
                    number = Validator.Number.float_input(print_message,error_message)

                    if bottom <= number <= top:
                         return number

                    if error_range_message:
                         print(error_range_message)

import platform
import os
def clearScreen():
     OS = platform.system()
     if OS == "linux":
          os.system("clear")

