# Placement Training

**40 standalone Python programs for foundational coding practice.**

A collection of beginner-friendly exercises covering conditional statements, loops, number properties, and digit manipulation. Each program accepts terminal input and runs independently, making it easy to practise one problem at a time.

## At a glance

| Item | Details |
| --- | --- |
| Language | Python 3 |
| Programs | 40 |
| Dependencies | No third-party packages |
| Interface | Interactive terminal input and output |
| Organisation | One problem per file, all files at the repository root |

## Getting started

### Requirements

- Python 3 installed and available in your terminal.
- VS Code or another code editor.
- Git, if you choose to clone the repository.

### Download the repository

Clone it with Git:

```bash
git clone https://github.com/Shameen-Khan/Placement-Training-.git
cd Placement-Training-
```

Alternatively, select **Code → Download ZIP** on GitHub and extract the archive.

### Run a program in VS Code

1. Select **File → Open Folder** and open the cloned or extracted repository folder.
2. Select **Terminal → New Terminal**.
3. Run the file you want to practise:

   ```bash
   python 01_check_even_or_odd.py
   ```

4. Enter the requested value in the terminal and press **Enter**.

If your system uses `python3`, replace `python` with `python3`. On Windows, you can also use `py` when the Python launcher is installed.

## Program index

Select any program below to view its source code. The categories organise this index; the files themselves are stored directly at the repository root.

### Conditions and comparisons

| No. | Program |
| --- | --- |
| 01 | [Check even or odd](01_check_even_or_odd.py) |
| 02 | [Check positive negative or zero](02_check_positive_negative_or_zero.py) |
| 03 | [Largest of 2 numbers](03_largest_of_2_numbers.py) |
| 04 | [Largest of 3 numbers](04_largest_of_3_numbers.py) |
| 05 | [Smallest of 3 numbers](05_smallest_of_3_numbers.py) |
| 06 | [Check divisibility by 5](06_check_divisibility_by_5.py) |
| 07 | [Check divisibility by 5 and 11](07_check_divisibility_by_5_and_11.py) |
| 08 | [Check leap year](08_check_leap_year.py) |

### Number properties

| No. | Program |
| --- | --- |
| 09 | [Check prime number](09_check_prime_number.py) |
| 10 | [Check perfect number](10_check_perfect_number.py) |
| 11 | [Check armstrong number](11_check_armstrong_number.py) |
| 12 | [Check palindrome number](12_check_palindrome_number.py) |
| 13 | [Check strong number](13_check_strong_number.py) |
| 14 | [Check automorphic number](14_check_automorphic_number.py) |
| 15 | [Check neon number](15_check_neon_number.py) |

### Digit operations

| No. | Program |
| --- | --- |
| 16 | [Find last digit](16_find_last_digit.py) |
| 17 | [Find first digit](17_find_first_digit.py) |
| 18 | [Count number of digits](18_count_number_of_digits.py) |
| 19 | [Sum of digits](19_sum_of_digits.py) |
| 20 | [Product of digits](20_product_of_digits.py) |
| 21 | [Reverse a number](21_reverse_a_number.py) |
| 22 | [Count even digits](22_count_even_digits.py) |
| 23 | [Count odd digits](23_count_odd_digits.py) |
| 24 | [Sum of even digits](24_sum_of_even_digits.py) |
| 25 | [Sum of odd digits](25_sum_of_odd_digits.py) |
| 26 | [Find largest digit](26_find_largest_digit.py) |
| 27 | [Find smallest digit](27_find_smallest_digit.py) |
| 28 | [Count occurrence of a digit](28_count_occurrence_of_a_digit.py) |
| 29 | [Check whether number contains 0](29_check_whether_number_contains_0.py) |
| 30 | [Remove last digit](30_remove_last_digit.py) |

### Loops and sequences

| No. | Program |
| --- | --- |
| 31 | [Print 1 to n](31_print_1_to_n.py) |
| 32 | [Print n to 1](32_print_n_to_1.py) |
| 33 | [Print even numbers from 1 to n](33_print_even_numbers_from_1_to_n.py) |
| 34 | [Print odd numbers from 1 to n](34_print_odd_numbers_from_1_to_n.py) |
| 35 | [Sum of 1 to n](35_sum_of_1_to_n.py) |
| 36 | [Sum of even numbers up to n](36_sum_of_even_numbers_up_to_n.py) |
| 37 | [Sum of odd numbers up to n](37_sum_of_odd_numbers_up_to_n.py) |
| 38 | [Factorial of n](38_factorial_of_n.py) |
| 39 | [Multiplication table](39_multiplication_table.py) |
| 40 | [Count multiples of 3 from 1 to n](40_count_multiples_of_3_from_1_to_n.py) |

## Example runs

### Even or odd

```text
Enter an integer: 8
Even
```

### Prime number

```text
Enter an integer: 29
Prime number
```

### Sum of digits

```text
Enter an integer: 1234
Sum of digits: 10
```

### Factorial

```text
Enter a non-negative integer N: 5
Factorial: 120
```

## Number properties explained

| Property | Rule | Example |
| --- | --- | --- |
| Prime | An integer greater than 1 with exactly two positive divisors | 7: divisors are 1 and 7 |
| Perfect | Equals the sum of its positive proper divisors | 28 = 1 + 2 + 4 + 7 + 14 |
| Armstrong | Equals the sum of its digits, each raised to the number of digits | 153 = 1³ + 5³ + 3³ |
| Palindrome | Reads the same forwards and backwards | 121 |
| Strong | Equals the sum of the factorials of its digits | 145 = 1! + 4! + 5! |
| Automorphic | Its square ends with the original number | 25² = 625 |
| Neon | Equals the sum of the digits of its square | 9² = 81; 8 + 1 = 9 |

## Input conventions and edge cases

- **Integer input:** Enter whole numbers. Non-integer text and decimal input are not handled and will raise a `ValueError`.
- **Digit operations:** The minus sign is ignored. Zero is treated as one digit, so its digit count is 1 and its digit product is 0.
- **Reversing and truncating:** Reversing a number and removing its last digit preserve its sign. Leading zeros are not retained; reversing `1200` produces `21`.
- **Palindromes:** Negative integers are not treated as palindromes.
- **Special-number checks:** Armstrong, strong, automorphic, and neon programs require non-negative integers. Perfect numbers are positive; prime numbers start at 2.
- **Leap years:** The program applies Gregorian rules to positive years: divisible by 400, or divisible by 4 but not by 100.
- **Ranges:** Printing sequences requires a positive N. Summation, factorial, and counting multiples accept N = 0.
- **Factorial:** 0! = 1. Negative inputs are rejected.
- **Multiplication table:** Prints multipliers from 1 through 10.

## Practice approach

1. Read the problem and write your own solution before opening the source.
2. Predict the result for a sample input, then run the program.
3. Try boundary cases such as zero, one, repeated digits, equal values, and negative numbers where supported.
4. Explain the conditions and loops in your own words.
5. Extend the solution with input validation or a reusable function.

These exercises focus on basic Python and arithmetic logic. They are a starting point for placement preparation; broader practice should also include arrays, strings, data structures, algorithms, and complexity analysis.
