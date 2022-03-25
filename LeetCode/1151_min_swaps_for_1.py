# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

# data = [1,0,1,0,1,0,0,1,1,0,1]
# data = [1,0,1,0,1,0,1,1,,0,1]
def minSwaps(self, data: List[int]) -> int:
        zeros = min_zeros = 0

        ones = sum(data)
        if ones == 1 : return 0

        slider = len(data) - ones-1

        for i in range(slider):
            zeros = data[i:ones+i].count(0)
            if zeros < min_zeros : return zeros
            min_zeros = zeros

        return min_zeros

ones = 6
len(data) = 11
slider = 6

for i in range(slider):
    zeros = data[i:ones+i].count(0)
    i = 0, data[0:6], zeros = 3,
    i = 1, data[1:7], zeros = 4
    i = 2, data[2:8], zeros = 3
    i = 3, data[3:9], zeros = 3
    i = 4, data[4:10], zeros = 3
    i = 5, data[5:11], zeros = 3
