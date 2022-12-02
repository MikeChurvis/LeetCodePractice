from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        deduped_list_tail_position = 0

        for num in nums:
            if nums[deduped_list_tail_position] == num:
                continue

            deduped_list_tail_position += 1
            nums[deduped_list_tail_position] = num

        return deduped_list_tail_position + 1