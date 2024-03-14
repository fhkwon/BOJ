a,b,c = map(int, input().split())
nums = [a,b,c]
nums_dict = {a: nums.count(a), b: nums.count(b), c: nums.count(c)}
cnt = max(list(nums_dict.values()))
max_num = [i for i, v in nums_dict.items() if v == cnt][0]

if cnt == 3:
    p = 10000 + a*1000
elif cnt == 2:
    p = 1000 + max_num * 100
else:
    p = max(nums)*100
    
print(p)