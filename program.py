# This function XORs all the elements of our array. Since x XOR 0 = x, we do
# not need to set a special case for 0.
def xor_all(array_):
    result = 0
    for i in range(len(array_)):
        result ^= array_[i]
    return result

# This function plays the best move by checking if by removing an element from
# the array causes xor_all to return 0. If it doesn't find any good move, it
# removes the first element in the array.
def remove_best(array_):
    for i in range(len(array_)):
        array_work = array_.copy()
        array_work.pop(i)
        if xor_all(array_work) == 0:
            continue
        else:
            array_.pop(i)
            return array
    array.pop(0)
    return array


test_cases = int(input())
for case in range(test_cases):
    array_length = int(input())
    array = list(map(lambda x: int(x), input().split()))
    turn = 1
    # Check if xor_all(array) is 0 at the beginning of a turn. If it's zero,
    # the player about to play his turn wins.
    while xor_all(array) != 0:
        array = remove_best(array)
        turn += 1
    # If the played turns are even, Watson wins, as Sherlock always plays the
    # first turn.
    if turn % 2 == 0:
        print("Watson")
    else:
        print("Sherlock")
