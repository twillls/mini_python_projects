def convert_to_snake_case(pascal_or_camel_cased_string):
    ###### Long form, for loop iteration #######
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #       converted_character = '_' + char.lower()
    #       snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string

    ###### USING LIST COMPREHSION ######
    # Inside square brackets, you can describe the value you want included in 
    # the list based on a given condition.
    # In this case, we are saying "append '_' + char.lower() to the list if 
    # char is in uppercase"
    # which will convert the capital letters to lower and concatenate '_' 
    # before the newly lower-cased character
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        # When starting a list comprehension with an if statement like this, 
        # you must add an else clause to the expression.
        # The expression would now be interpreted as:
        # "Append '_' + char.lower() to the list if char is in uppercase,
        # append char as is otherwise"
        # This covers both upper and lowercase characters in the input string
        else char
        # The final piece is the input string itself. The list comprehension
        # needs to know about the object it will iterate upon.
        # In this case, we will iterate all characters of the string.
        for char in pascal_or_camel_cased_string
    ]

    # Join the list elements into a string and strip off underscores from
    # beginning or end using a shorter alternative to above
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

if __name__ == '__main__':
    main()