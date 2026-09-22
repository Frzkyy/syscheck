from validator import Validator
numer = Validator.Number.integer_input_range(50,error_message="Bodoh Anjing",print_message=": ")
print(numer)