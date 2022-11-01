def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    if s[0]=="*":
        a=0
    if s[1]=="*":
        a=1
    if s[2]=="*":
        a=2
    if s[3]=="*":
        a=3
    if s[4]=="*":
        a=4
    return a
print(main("sal*m"))