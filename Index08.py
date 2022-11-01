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
        a=s[0]
    if s[1]=="*":
        a=s[1]
    if s[2]=="*":
        a=s[2]
    if s[3]=="*":
        a=s[3]
    if s[4]=="*":
        a=s[4] 
    return a
        