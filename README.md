# UVSim
UVSim is a software-simulator to help Computer Science students learn machine language and computer architecture.

BasicML machine language programs can be executed using UVSim.

## Memory
All information is handled in terms of words. A word is a signed 4 digit number, ie. +1234 or -4321. UVSim has a 100-word memory. Memory locations range from 00..99. The BasicML program must be loaded into main memory starting at location 00 before execution.

## BasicML Instructions

| Opcode     | Operation | Description |
| ----------- | ----------- |----------- |
| 10 | Read | Read a word from the keyboard into a specific location in memory. |
| 11 | Write | Write a word from a specific location in memory to screen. |
| 20 | Load |Load a word from a specific location in memory into the accumulator. |
| 21 | Store |Store a word from the accumulator into a specific location in memory. |
| 30 | Add |Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator). |
| 31 | Subtract | Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator). |
| 32 | Divide | Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator). |
| 33 | Multiply | multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator). |
| 40 | Branch | Branch to a specific location in memory. |
| 41 | BranchNeg | Branch to a specific location in memory if the accumulator is negative. |
| 42 | BranchZero | Branch to a specific location in memory if the accumulator is zero. |
| 43 | Halt | Pause the program |

All BasicML operations are +. The last two digits of the of the BasicML instruction are the operand which represent the address of the memory location containing the word to which the operation applies.
Example: +1007 would be the READ Opcode which would read a word from the keyboard and store it in memory location 07.

## How to Run this Program Locally
1. Run UVSim by running `python3 main.py`
2. Once the prompt appears, begin entering the BasicML program word by word (word = signed 4 digit number).
3. Enter `-99999` when finished entering the BasicML program.
4. UVSim will then execute the BasicML program.


## How to Test
- All test files are prepended with 'test'.
- Install mock: `pip install mock`.
- Run a test file as follows `python3 test_math_ops.py`.
