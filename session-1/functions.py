# Simple python function

from typing import Any, List

def add_num(a, b):
    result = a + b
    print(result)
    return result

# Parameters
# Arguments
# Return Statements
# Function Outputs
# Function/variable name definition

# The if __name__ == "__main__": block ensures that the example code is only executed when the script is run directly, not when it is imported as a module.
if __name__ == "__main__":
    add_num(1,2)
























# Python function with type hints

def text_align(text: str, align: bool=False, remarks: Any= '') -> str:
    if align:
        result =  f" {text} ".center(50, "-")
    else:
        result =  f"{text}\n" + '-' * len(text)
    
    print(result)
    return result
    
text_align("anup", True, '')
text_align("anup", True, '')
# text_align("anup", "left")
text_align("a", "right", '')

# Code documentation
# Static type checking
# Default Arguments
# f-strings
# keyword-arguments and defualt argumnet