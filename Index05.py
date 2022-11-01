def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    if 0<=s[0] and s[0]<=9:
        a=1
    if 0<=s[1] and s[1]<=9:
        a=2
    if 0<=s[2] and s[2]<=9:
        a=3
    if 0<=s[3] and s[3]<=9:
        a=4
    if 0<=s[4] and s[4]<=9:
        a=5
    return a