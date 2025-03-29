class basicCalculator:
    def calculate(self, input_string: str) -> int:

        digits = "0123456789"
        stack = []
        result = 0
        temp_value = 0
        sign = 1
        
        for character in input_string:
            if character in digits:
                # this mathematical formula accounts for numbers that are
                # longer than one character or out of the single digits
                # for the "8" in "6+7+8"
                # the formula would be temp_value = (0 * 10) + int(8) = 0 + 8
                # temp_value = 8
                # if the input was "6+7+11", where we now focus on 11
                # the formula becomes temp_value = (0 * 10) + int(1) = 0 + 1
                # temp_value = 1
                # then the next character would be the second 1 in 11
                # so the formula is now temp_value = (1 * 10) + int(1) = 10 + 1
                # temp_value = 11
                
                temp_value = (temp_value * 10) + int(character)
            elif character in ['+','-']:
                # here the character is checked to be either for
                # subtraction or addition
                # since all of these operations are additions
                # the sign determines whether the temp_value being added
                # is negative or positive
                
                # the signed temp_value is added to the result
                result += sign * temp_value

                # the signed temp_value gets reset
                temp_value = 0
                if character == '+':
                    sign = 1
                elif  character == '-':
                    sign = -1
            
            elif character == "(":
                # here we detect an open paranthesis
                # if so, we store the preliminary result and sign in a stack
                # so that those variables may be made available
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            
            elif character == ")":
                # here we detect a closing paranthesis
                # if so, the stored values from the stack are accessed
                # and added back to the result
                result += temp_value * sign
                result *= stack.pop()
                result += stack.pop()
                temp_value = 0
            
        return result + (temp_value * sign)


# Here are the test cases for testing the calculator
string_test_cases = [ 
    "-5+6+2-4+3+2-(8-1)",
    "(1 + 1)-1",
    "(2 - 3)+8 - (4+5) + 3",
    "(1+4)-(4)+(-3)-4",
    "(7-9)-(3-5)+18",
    "20-78-42+54+61",
    "(32-9)-9-12+(30+27)",
    "6+7+8+9",
    "6+7+8+9",
    "6+7+11",
    "67-(-((89+23)+106)+24+25)-36"
]


calculator = basicCalculator()

for test_case in string_test_cases:
    results = calculator.calculate(test_case)
    
    print("The input string is", test_case)
    print("The solution is", results, "\n")
