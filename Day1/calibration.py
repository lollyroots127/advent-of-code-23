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
    