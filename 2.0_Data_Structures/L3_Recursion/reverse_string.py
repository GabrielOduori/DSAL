def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """
    
    # TODO: Write your recursive string reverser solution here
    if len(input)==0:
        return ""
    return ''.join(reversed(input))

    """
    Alternative solution
    first_char = input[0]
    the_rest = slice(1, None)
    sub_string = input[the_rest]
    reversed_substring = reverse_string(sub_string)
    return reversed_substring + first_char
    """



print(reverse_string('Gabriel'))
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")