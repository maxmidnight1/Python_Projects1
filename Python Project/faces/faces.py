# faces.py

def convert(input_str):
    """
    Convert emoticons in the input string to corresponding emoji.
    :param input_str: str
    :return: str
    """
    return input_str.replace(':)', '\U0001F642').replace(':(', '\U0001F641')

def main():
    """
    Prompt the user for input, convert the input string, and print the result.
    """
    user_input = input("Enter a string: ")
    converted_input = convert(user_input)
    print(converted_input)


main()
