def horspool(needle, haystack):
    m = len(needle)
    n = len(haystack)
    for window_size in range(n-m+1):
        for i in range(m):
            if needle[i] != haystack[window_size+i]:
                break
            if i == m-1:
                return window_size
    return -1

needle = "jeevika"
haystack = "hello there jeevika"
print(horspool(needle, haystack))