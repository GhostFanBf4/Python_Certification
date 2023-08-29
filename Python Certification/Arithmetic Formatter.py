def arithmetic_arranger(problems,boolean=False):
    
    first_operand_string = ''
    second_operand_string= ''
    result_string = ''
    lines = ''
  # first error
    if len(problems) > 5:
        return "Error: Too many problems."
  
    for problem in problems:
        splited = problem.split(" ")
        first_operand = splited[0]
        operator = splited[1]
        second_operand = splited[2]

    #third error
        try:
            first_operand = int(first_operand)
            second_operand = int(second_operand)
        except:
            return "Error: Numbers must only contain digits."
    
    # second error
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
    
    # fourth error
        if first_operand >= 10000 or second_operand >= 10000:
            return "Error: Numbers cannot be more than four digits."
        
        
        result = 0
        if boolean == True:
            if operator == '+':
                result = (first_operand + second_operand)
            else:
                result = (first_operand - second_operand)

        length = max(len(str(first_operand)), len(str(second_operand))) + 2
        top = str(first_operand).rjust(length)
        bottom = operator + str(second_operand).rjust(length - 1)
        line = ''
        res = str(result).rjust(length)
        for s in range(length):
            line += '-'
        
        if problem != problems[-1]:
            first_operand_string += top + '    '
            second_operand_string += bottom + '    '
            lines += line + '    '
            result_string += res + '    '
        else:
            first_operand_string += top
            second_operand_string += bottom 
            lines += line
            result_string += res

    first_operand_string.rstrip()
    second_operand_string.rstrip()
    lines.rstrip()

    if boolean:
        result_string.rstrip()
        arranged_problems = first_operand_string + '\n' + second_operand_string + '\n' + lines + '\n' + result_string
    else:
        arranged_problems = first_operand_string + '\n' + second_operand_string + '\n' + lines

    return arranged_problems

    

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))
print(arithmetic_arranger(["1a + 2b","32 + 698","32 + 698","32 + 698","32 + 698","32 + 698",]))
print(arithmetic_arranger(["1a + 2b"]))
print(arithmetic_arranger(["1001 + 30000"],True))
