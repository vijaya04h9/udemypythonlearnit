# help(print)

# print.__doc__

# def find_longest(word1, word2, word3):
#     return max(len(word1), len(word2), len(word3))

# result = find_longest("short", "longer", "longest")
# print(result)

# result = find_longest = ("python", "is", "awesome" )
# print(result)

# color = min("purple", "blue", "white")
# print(color)
# color = max("purple", "blue", "white")
# print(color)

# color = min("Purple", "blue", "white")
# print(color)
# color = max("Purple", "blue", "white")
# print(color)

def find_longest(words):
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return min(longest_words)

word_list = ["short", "longer", "longest", "longesz"]
result = find_longest(word_list)
print(result)