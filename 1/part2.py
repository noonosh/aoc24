
def part2():
    try:
        list1 = []
        list2 = []

        with open('1/input.txt', 'r') as file:
            for line in file:
                num1, num2 = map(int, line.strip().split())
                list1.append(num1)
                list2.append(num2)

        freq_dict = {}
        for num in list2:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        total_sum = 0
        for num in list1:
            frequency = freq_dict.get(num, 0)
            total_sum += num * frequency

        return total_sum

    except FileNotFoundError:
        print("Error: input.txt file not found")
    except Exception as e:
        print(f"An error occurred: {e}")
