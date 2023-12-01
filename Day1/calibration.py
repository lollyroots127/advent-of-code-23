def partone():
    with open('Day1/input.txt', 'r') as file:
        sum = 0
        for line in file.readlines():
            nums = []
            for i in line:
                if i.isdigit():
                    nums.append(i)
            value = nums[0] + nums[-1]
            sum += int(value)
        print(sum)

def parttwo():
    with open('Day1/input.txt', 'r') as file:
        sum = 0
        numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        for line in file.readlines():
            nums = []
            remaining_chars = ''
            for char in line:
                if char.isdigit():
                    nums.append(char)
                    remaining_chars = ''
                else:
                    remaining_chars += char
                    for num in numbers.keys():
                        if remaining_chars.find(num) != -1:
                            nums.append(numbers[num])
                            remaining_chars = char            
            value = nums[0] + nums[-1]
            print("Value: " + value)
            sum += int(value)
        print(sum)

parttwo()
            
