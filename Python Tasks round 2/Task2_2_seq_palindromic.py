def longest_palindromic_subsequence_lcs(s: str) -> tuple[int, str]:
    n = len(s)
    rev_s = s[::-1]
    table = [[0] * (n + 1) for _ in range(n + 1)]

  
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev_s[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    
    i, j = n, n
    lps = []

    while i > 0 and j > 0:
        if s[i - 1] == rev_s[j - 1]:
            lps.append(s[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return table[n][n], ''.join(reversed(lps))



print(longest_palindromic_subsequence_lcs('BADSFABSD'))