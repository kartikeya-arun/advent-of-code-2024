# Part 1
with open('input.txt', 'r') as file:
    lines = file.readlines()
    ip = []
    ans = 0

    def isSafe(lis):
        monotonous = 0
        for i in range(1, len(lis)):
            diff = lis[i]-lis[i-1]
            # determine wether 1 <= diff(report[0],report[1]) <= 3
            if (abs(diff) < 1 or abs(diff) > 3):
                return False
            if monotonous == 0:
                # case1: when looking at second element:
                # determine if the array is increasing or decreasing
                if diff > 0:
                    monotonous = 1
                elif diff < 0:
                    monotonous = -1
            else:
                # case2: looking at any elenet after that:
                if ((monotonous > 0 and diff < 0) or (monotonous < 0 and diff > 0)):
                    # 1. Check if not monotonous
                    return False
        return True
    for line in lines:
        ip.append(list(map(int, line.strip().split(' '))))
    for report in ip:
        if isSafe(report):
            ans += 1
        else:
            for i in range(len(report)):
                if isSafe(report[:i]+report[i+1:]):
                    ans += 1
                    break
            continue
    print(ans)
