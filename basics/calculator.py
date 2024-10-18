"""
This is a simple calculator cli program made using click. See https://click.palletsprojects.com/en/8.1.x/

Author: https://github.com/ubaidrmn
Date: October 19, 2024
"""

import click

OPERATORS_OPERATIONS = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

@click.command()
@click.option('--op', help='The operation (add/sub/mul/div)', type=str)
@click.option('--operand-1', help='The first operand', type=int)
@click.option('--operand-2', help='The second operand', type=int)
def main(op, operand_1, operand_2):
    """Calculator that takes an arithmetic operation, two integer operands & then performs the operation."""
    _result = OPERATORS_OPERATIONS[op](operand_1, operand_2)
    print(_result)

if __name__ == '__main__':
    main()
