'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''


def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0] 
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix



strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
strs2 = ["dog","racecar","car"]
print(longestCommonPrefix(strs2))