def arithmetic_arranger(problems, show_answers=False):
    top_numbers = []
    bottom_numbers = []
    eq_lines = []
    answers = []

    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for problem in problems:
            split_parts = problem.split()
            first_arg = split_parts[0]
            operator = split_parts[1]
            second_arg = split_parts[2]
            max_length = max(len(first_arg), len(second_arg))

            if operator not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."

            if len(first_arg) > 4 or len(second_arg) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            try:
                answer = str(eval(problem))
            except:
                return 'Error: Numbers must only contain digits.'

            top_numbers.append(first_arg.rjust(max_length + 2))
            bottom_numbers.append(operator + ' ' + second_arg.rjust(max_length))
            eq_lines.append('-' * (max_length + 2))

            if len(first_arg) < len(second_arg) and operator == '-':
                answers.append(' ' + answer.rjust(max_length))
            else:
                answers.append('' + answer.rjust(max_length + 2))

    arranged_numbers = ''
    arranged_numbers += '    '.join(top_numbers) + '\n' + '    '.join(bottom_numbers) + '\n' + '    '.join(eq_lines)
    
    if show_answers:
        arranged_numbers += '\n' + '    '.join(answers)

    return arranged_numbers

print(arithmetic_arranger(["3 + 855", "988 + 40"], True))