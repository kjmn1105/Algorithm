while True:
    string = input()
    if string == ".":
        break

    string = "".join([c for c in string if c in "()[]"])
    while ("()" in string) or ("[]" in string):
        string = string.replace("()", "").replace("[]", "")

    print("no" if string else "yes")