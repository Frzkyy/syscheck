class Validator:
     class Number:

          #only integer
          @staticmethod
          def integer_input(print_message=None,error_message=None):
               is_running = True
               while is_running:
                    try:
                         if print_message:
                              number = int(input(print_message))
                         else:
                              number = int(input(""))
                         return number
                    except ValueError:
                         if error_message:
                              print(error_message, end="")
                              input()

          #integer with range (minimum = 0)
          @staticmethod
          def integer_input_range(end,print_message=None,error_message=None,error_range_message=None):
               is_running = True
               while is_running:
                    try:
                         if print_message:
                              number = int(input(print_message))
                         else:
                              number = int(input())

                         if number > end or number < 0:
                              if error_range_message:
                                   print(error_range_message)
                              continue
                         
                         return number
                    except ValueError:
                         if error_message:
                              print(error_message, end="")
                              input()

          @staticmethod
          def float_input(print_message=None,error_message=None):
               is_running = True
               while is_running:
                    try:
                         if print_message:
                              number = float(input(print_message))
                         else:
                              number = float(input())
                         return number
                    except ValueError:
                         if error_message:
                              print(error_message, end="")
                              input()
                    