"""
split_up.py
Author: Kevin Augustine

Take the input string and put commas between the individual characters.
"""

def split_up( original: str ) -> str:
    """
        Return a string where all the characters of the argument
        string are separated by commas.
    """
    result = ""
    x = 0
    for ch in original:
        if x == len(original) - 1:
            result = result + ch
        else:
            result = result + ch + ','
        x += 1
    return result


def main():
    arg = input( "Type something, then hit enter: " )
    print()
    print( split_up( arg ) )
    print()


if __name__ == "__main__":
    main()
