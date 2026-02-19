"""
Advanced Calculator - Supports +, -, *, /, %, Mean, Median, Mode
"""

from statistics import mean, median, mode, multimode


def get_numbers(prompt="Enter numbers separated by spaces: "):
    while True:
        try:
            nums = list(map(float, input(prompt).split()))
            if not nums:
                print("  ⚠  Please enter at least one number.")
                continue
            return nums
        except ValueError:
            print("  ⚠  Invalid input. Use numbers only (e.g. 4 7 2.5 9).")


def get_two_numbers():
    while True:
        try:
            a = float(input("  Enter first number  : "))
            b = float(input("  Enter second number : "))
            return a, b
        except ValueError:
            print("  ⚠  Please enter valid numbers.")


def basic_operations():
    ops = {
        '1': ('+', lambda a, b: a + b),
        '2': ('-', lambda a, b: a - b),
        '3': ('*', lambda a, b: a * b),
        '4': ('/', lambda a, b: a / b if b != 0 else None),
        '5': ('%', lambda a, b: a % b if b != 0 else None),
    }
    print("\n  Operations: [1] Add  [2] Subtract  [3] Multiply  [4] Divide  [5] Modulo")
    choice = input("  Pick an operation (1-5): ").strip()
    if choice not in ops:
        print("  ⚠  Invalid choice.")
        return
    symbol, func = ops[choice]
    a, b = get_two_numbers()
    result = func(a, b)
    if result is None:
        print("  ⚠  Cannot divide by zero!")
    else:
        # Type-cast result to int if it's a whole number
        display = int(result) if result == int(result) else result
        print(f"\n  ✅  {a} {symbol} {b} = {display}")


def stats_operations():
    nums = get_numbers()
    int_nums = [int(n) if n == int(n) else n for n in nums]   # clean display

    calc_mean   = mean(nums)
    calc_median = median(nums)
    calc_modes  = multimode(nums)                              # handles multi-mode
    calc_avg    = sum(nums) / len(nums)                        # same as mean, shown explicitly

    def fmt(v):
        return int(v) if v == int(v) else round(v, 4)

    print(f"""
  ─────────────────────────────────
  Numbers : {int_nums}
  Count   : {len(nums)}
  Sum     : {fmt(sum(nums))}
  ─────────────────────────────────
  Mean    : {fmt(calc_mean)}
  Average : {fmt(calc_avg)}
  Median  : {fmt(calc_median)}
  Mode    : {[fmt(m) for m in calc_modes]}
  ─────────────────────────────────""")


def percentage_calc():
    while True:
        try:
            value = float(input("  Enter the value    : "))
            pct   = float(input("  Enter percentage % : "))
            result = (pct / 100) * value
            print(f"\n  ✅  {pct}% of {value} = {round(result, 4)}")
            break
        except ValueError:
            print("  ⚠  Please enter valid numbers.")


MENU = """
╔══════════════════════════════════════╗
║        🧮  ADVANCED CALCULATOR       ║
╠══════════════════════════════════════╣
║  [1]  Basic Operations  (+ - * / %)  ║
║  [2]  Statistics  (Mean/Median/Mode) ║
║  [3]  Percentage Calculator          ║
║  [0]  Exit                           ║
╚══════════════════════════════════════╝
"""

def main():
    while True:
        print(MENU)
        choice = input("  Your choice: ").strip()
        if   choice == '1': basic_operations()
        elif choice == '2': stats_operations()
        elif choice == '3': percentage_calc()
        elif choice == '0':
            print("\n  👋  Goodbye!\n")
            break
        else:
            print("  ⚠  Invalid option. Choose 0-3.")

if __name__ == "__main__":
    main()
