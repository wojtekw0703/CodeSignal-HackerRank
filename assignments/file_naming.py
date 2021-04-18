"""
Platform: CodeSignal

You are given an array of desired filenames in the order of their creation. 
Since two files cannot have equal names, the one which comes later will have an
addition to its name in a form of (k), where k is the smallest positive integer such 
that the obtained name is not used yet.

Return an array of names that will be given to the files.
"""


def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j = 1
            while names[i] + "(" + str(j) + ")" in names[:i]:
                j += 1
            names[i] += "(" + str(j) + ")"
    return names