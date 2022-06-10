""""

No Repeats Please
Return the number of total permutations of the provided string that don't have repeated consecutive letters.
Assume that all characters in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa),
 but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.

"""

import itertools

def permAlone(string) -> int:
    # Create a list of all permutations of the string.
    permutations = list(itertools.permutations(list(string)))
    permutations = [''.join(permutation) for permutation in permutations]
    copy_list_permutations = permutations.copy()
    #loop through all permutations
    for permutation in permutations:
        last_letter = ""
        for letter in permutation:
            #if last_letter is the same as letter
            if last_letter == letter:
                copy_list_permutations.remove(permutation)
                break
            else:
                last_letter=letter

    #print(copy_list_permutations)
    return len(copy_list_permutations)


s = "aab"
len_permutations = permAlone(s)
print("number of permutations", len_permutations)