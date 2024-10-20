from typing import Callable, Generator
import re


# find all decimal numbers in text like as valid income
def generator_numbers(text: str) -> Generator:
    pattern = re.compile(r"\s\d+\.\d+\s")
    result = re.findall(pattern, text)

    for item in result:
        yield float(item.strip())


# return total income
def sum_profit(text: str, func: Callable[[str], float]) -> float:
    sum = 0

    for amount in func(text):
        sum += amount

    return sum


def main():
    text = "The employee's total income consists of several parts: 1000.01 $ as basic income, supplemented by additional receipts of 27.45 $ and 324.00 $."
    total_income = sum_profit(text, generator_numbers)
    print(f"Total income: {total_income}")


if __name__ == "__main__":
    main()
