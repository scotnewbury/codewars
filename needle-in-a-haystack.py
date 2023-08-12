def find_needle(haystack):
    # your code here
    position = 0
    for loop in haystack:
        if (haystack[position] == "needle"):
            return ("found the needle at position: " + str(position))
        position += 1
test_array = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
find_needle (test_array)