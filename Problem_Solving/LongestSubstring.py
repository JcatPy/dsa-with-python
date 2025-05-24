def lengthOfLongestSubstring(s):
    substring_list = []
    sub = ''

    for char in s:
        if char in sub:  # If duplicate found, store substring and reset
            substring_list.append(sub)
            sub = sub[sub.index(char) + 1:]  # Remove characters before the duplicate
        sub += char  # Add new character

    substring_list.append(sub)  # Add the last substring

    # Find the longest substring
    for i in substring_list:
        if len(i) > len(sub):
            sub = i
    return len(sub)
