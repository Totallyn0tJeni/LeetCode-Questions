class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        i = 0
        
        while i < length:
            if flowerbed[i] == 0:
                next_ = flowerbed[i + 1] if i < length - 1 else 0
                
                if next_ == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
                if n == 0:
                    return True
            else:
                i += 2
        
        return n <= 0

# Test cases
solution = Solution()

# Test Case 1
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(solution.canPlaceFlowers(flowerbed1, n1))  # Output: True

# Test Case 2
flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(solution.canPlaceFlowers(flowerbed2, n2))  # Output: False

# Test Case 3
flowerbed3 = [0, 0, 1, 0, 0]
n3 = 1
print(solution.canPlaceFlowers(flowerbed3, n3))  # Output: True

# Test Case 4
flowerbed4 = [0, 0, 1, 0, 0]
n4 = 2
print(solution.canPlaceFlowers(flowerbed4, n4))  # Output: False

# Test Case 5
flowerbed5 = [1, 0, 0, 0, 0, 1]
n5 = 2
print(solution.canPlaceFlowers(flowerbed5, n5))  # Output: False

# Test Case 6
flowerbed6 = [1, 0, 0, 0, 0, 1]
n6 = 1
print(solution.canPlaceFlowers(flowerbed6, n6))  # Output: False

# Test Case 7
flowerbed7 = [0, 0, 0, 0, 0, 0]
n7 = 3
print(solution.canPlaceFlowers(flowerbed7, n7))  # Output: True
