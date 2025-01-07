import itertools
import sys

def generate_power_set(e):
    n = len(e)
    all_subsets = []
    for subset_size in range(n + 1):
        current_subsets = list(itertools.combinations(e, subset_size))
        all_subsets.extend(current_subsets)
    return all_subsets
def run_program():
    if len(sys.argv) < 2:
        print("Запуск python main1.py число число")
        sys.exit(1)

    e = list(map(int, sys.argv[1:]))
    subsets = generate_power_set(e)

    print("Список подмножеств для заданного множества:")
    for subset in subsets:
        formatted_output = f"({', '.join(map(str, subset))})"
        print(formatted_output)

if __name__ == "__main__":
    run_program()
