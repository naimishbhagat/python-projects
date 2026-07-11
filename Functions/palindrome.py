#paap, racecar, radar, madam
def check_palindrome(word):
    l = len(word) 
    for i in range(l):
        if word[i] !=word[l - i - 1]:
            return False
    return True

word ="sdds"

if check_palindrome(word):
    print("This sting is a palindrome")
else:
    print("This sting is not a palindrome")