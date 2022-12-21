from collections import namedtuple
from copy import copy

DataPoint = namedtuple("DataPoint", "position value")


def get_encrypted_input(path, decryption_key=1):
    with open(path) as file:
        lines = file.readlines()
    i = iter(range(len(lines)))
    encrypted_input = list(map(lambda l: DataPoint(next(i), int(l.replace('\n', '')) * decryption_key), lines))
    return encrypted_input


def mix_encrypted_input(encrypted_input, current_mix):
    message_length = len(encrypted_input)
    for data_point in encrypted_input:
        initial_index = current_mix.index(data_point)
        final_index = (initial_index + data_point.value) % (message_length - 1)
        del current_mix[initial_index]
        current_mix.insert(final_index, data_point)
    return current_mix


def compute_grove_coordinates(path, decryption_key=1, runs=1):
    encrypted_input = get_encrypted_input(path, decryption_key)
    deciphered_output = copy(encrypted_input)
    for _ in range(runs):
        deciphered_output = mix_encrypted_input(encrypted_input, deciphered_output)
    zero_index = deciphered_output.index([point for point in deciphered_output if point.value == 0][0])
    return sum([deciphered_output[(zero_index + i) % len(deciphered_output)].value for i in [1000, 2000, 3000]])
