from dataclasses import dataclass
from typing import Callable

def xor(a, b):
    return a ^ b

def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

@dataclass
class Gate:
    inputs: list[str]
    gate: Callable
    output: str

gate_to_function = {
    'XOR': xor,
    'AND': and_gate,
    'OR': or_gate,
}

wires = dict()
gates: list[Gate] = []

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line == '':
            break
        line = line.split(': ')
        wires[line[0]] = int(line[1])
    for line in f:
        line = line.strip()
        line = line.split()
        gates.append(Gate([line[0], line[2]], gate_to_function[line[1]], line[4]))

updated_wires = list(wires.keys())
while updated_wires:
    updated_wire = updated_wires.pop()
    for gate in gates:
        if updated_wire not in gate.inputs:
            continue
        if gate.output in wires:
            continue
        if not all([w in wires for w in gate.inputs]):
            continue
        wires[gate.output] = gate.gate(*[wires[o] for o in gate.inputs])
        updated_wires.append(gate.output)
    print(wires)

z_wires = [wires[z] for z in sorted([z_ for z_ in wires.keys() if z_.startswith('z')], reverse=True)]

result = 0
for z in z_wires:
    result <<= 1
    result += z
print(result)