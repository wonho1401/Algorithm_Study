def solution(nums):
    len_nums = len(nums) // 2
    nums = set(nums)
    if len(nums) <= len_nums:
        return len(nums)
    else:
        return len_nums