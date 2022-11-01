def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a=0
    if len(s) >n:
        a=s[n]
    else:
        a=False

    return a
print(main("salom",4))
