import string
import collections


def caesar(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_undercase)
    lower = collections.deque(string.ascii_undercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = "".join(list(upper))
    lower = "".join(list(lower))

    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(
        string.maketrans(string.ascii_lowercase, upper))


our_string = "This is too easy"

for i in range(len(string.ascii_uppercase)):
    print(i, "|", caesar(our_string, i))
