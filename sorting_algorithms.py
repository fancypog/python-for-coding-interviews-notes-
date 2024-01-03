
# =============================================================================
# Selection sort
# =============================================================================

# 1. Find the minimun value (check the entire list)
# 2. Place the min_val to index 0

l1 = [5, 15, 1, 45, 0, 6]
def selection_sort(l1):
    for i in range(len(l1)):
        min_val = min(l1[i:])
        min_ind = l1.index(min_val)
        l1[i], l1[min_ind] = l1[min_ind], l1[i]# Swap in python
    return l1
selection_sort(l1)
