def insertion_sort(arr):
    """Sort a list in ascending order using insertion sort (in place)."""
    # The first element is already considered sorted.
    for i in range(1, len(arr)):
        key = arr[i]          # Element to insert into the sorted prefix
        j = i - 1

        # Shift larger elements one position to the right.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Put key in its correct position.
        arr[j + 1] = key

    return arr


def main():
    try:
        n = int(input("Enter number of elements: "))
        if n < 0:
            print("Please enter a non-negative number.")
            return

        if n == 0:
            arr = []
        else:
            arr = list(map(int, input(f"Enter {n} integers separated by spaces: ").split()))
            if len(arr) != n:
                print(f"Expected {n} integers, but received {len(arr)}.")
                return

        print("Sorted array:", *insertion_sort(arr))
    except ValueError:
        print("Invalid input. Enter integers only.")


if __name__ == "__main__":
    main()
