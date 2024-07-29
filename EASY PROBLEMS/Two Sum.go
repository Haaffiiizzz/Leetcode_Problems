func twoSum(nums []int, target int) []int {
	var result []int
	for i, n := range nums {
		for j := i + 1; j < len(nums); j++ {
			if n+nums[j] == target {
				result = []int{i, j}
				return result
			}
		}
	}
	return nil
}