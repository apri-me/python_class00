
def remove_repetition(li):
    return list(set(li))

# def remove_repetition2(li):
#     remove_indices = set()
#     for i in range(len(li) - 1):
#         for j in range(i + 1, len(li)):
#             if li[i] == li[j]:
#                 remove_indices.add(j)
#     print(remove_indices)
#     for i in remove_indices:
#         li.pop(i)
#     return li


print(remove_repetition([1,1,1,1]))