from enum import Enum

TYPE_ID_OPERATOR = 6
TYPE_ID_LITERAL_VALUE = 4

with open("input.in") as file:
    bits = bin(int(file.read().strip(), 16))[2:].zfill(8)

class Packet:
    def __init__(self, version, type_id) -> None:
        self.version, self.type_id = version, type_id

def get_version_and_type_id(bits):
    return (int(bits[0:3], 2), int(bits[3:6], 2))

initial_packet = Packet(*get_version_and_type_id(bits))

pass