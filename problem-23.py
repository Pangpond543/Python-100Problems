def create_dictionary(tuple1: tuple[int, ...], tuple2: tuple[str, ...]) -> dict[int, str]:
    dict = {}
    for i in range(len(tuple1)):
        dict[tuple1[i]] = tuple2[i]
    return dict

print(create_dictionary((1, 2, 3, 4), ("ant", "cat", "dog", "cow")))

#--------------------------------------------------------------

def create_dictionary_2(tuple1: tuple[int, ...], tuple2: tuple[str, ...]) -> dict[int, str]:
    dict = {}
    for i, j in zip(tuple1, tuple2):
        dict[i] = j
    return dict

print(create_dictionary_2((1, 2, 3, 4), ("ant", "cat", "dog", "cow")))