# not so great but works for this input

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

gates2 = [dict() for _ in range(46)]

# find carry
for gate in gates:
    if 'x00' in gate.inputs and gate.gate == and_gate:
        gate
        break

wrong = []

for i in range(1, 46):
    for gate in gates:
        if f'x{i:02}' in gate.inputs and gate.gate == xor:
            gates2[i]['input_xor_output'] = gate.output

        if f'x{i:02}' in gate.inputs and gate.gate == and_gate:
            gates2[i]['input_and_output'] = gate.output

        # check z connection
        if f'z{i:02}' == gate.output:
            if gate.gate != xor and i != 45:
                wrong.append(gate.output)
                break
            gates2[i]['output_xor_inputs'] = gate.inputs

# check xor output connected to xor inputs
for g in gates2[:-1]:
    if 'output_xor_inputs' in g:
        inputs = g['output_xor_inputs']
        if g['input_xor_output'] not in inputs:
            wrong.append(g['input_xor_output'])

# check wrong connection to xor inputs
for gate in gates:
    if gate.gate == xor:
        if gate.output[0] != 'z' and gate.inputs[0][0] not in ['x', 'y']:
            wrong.append(gate.output)

# check and input wrongly from and outputs
for gate in gates:
    if gate.gate == and_gate:
        for in_ in gate.inputs:
            for g in gates:
                if in_ == g.output and g.gate == and_gate and g.inputs[0] not in ['x00', 'y00']:
                    wrong.append(g.output)
print(wrong)

wrong.sort()

print(','.join(wrong))
