#sorting will be a bottleneck of O nlogn
#use a hashSET not hashMAP

def containsduplicates(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
print(containsduplicates([1,2,3,4,4]))