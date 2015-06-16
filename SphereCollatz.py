#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    if (i > j) :
        temp = i
        i = j
        j = temp

    max_cycle_len = 1
    for n in range (i, j+1) :
        c = 1
        my_val = n
        while n > 1 :
            if (n % 2) == 0 :
                n = (n // 2)
            else :
                n = n + (n << 1) + 1
            c += 1

        assert c > 0

        if (c > max_cycle_len) :
            max_cycle_len = c

    return max_cycle_len

# --------------------
# collatz_eval_cache
# --------------------
def collatz_eval_cache (i, j):
    assert i > 0
    assert j > 0

    array = []
    for k in range (0, 1000000):
        array.append(0)

    if (i > j) :
        temp = i
        i = j
        j = temp

    max_cycle_len = 1

    for n in range (i, j+1) :
        c = 1
        index = n

        while n > 1 :
            if (n % 2) == 0 :
                n = (n // 2)
            else :
                n = n + (n << 1) + 1

            if (n <= 1000000 and array[n] != 0) :
                c += array[n]
                break;
            c +=1

        assert c > 0
        array[index] = c

        if (c > max_cycle_len) :
            max_cycle_len = c

    return max_cycle_len


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        #v    = collatz_eval(i, j)
        v = collatz_eval_cache(i, j)
        collatz_print(w, i, j, v)

#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""
