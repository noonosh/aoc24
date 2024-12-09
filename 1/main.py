from part2 import part2


def main():
    try:
        list1 = []  # List for first numbers
        list2 = []  # List for second numbers

        with open('1/input.txt', 'r') as file:
            for line in file:
                num1, num2 = map(int, line.strip().split())
                list1.append(num1)
                list2.append(num2)

        list1.sort()
        list2.sort()

        total_sum = 0

        for i in range(len(list1)):
            difference = abs(list1[i] - list2[i])
            total_sum += difference

        return total_sum

    except FileNotFoundError:
        print("Error: input.txt file not found")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    x = main()
    y = part2()
    print(x)
    print(y)
