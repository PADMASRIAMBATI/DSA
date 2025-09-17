# s = "abcdabehf"
# arr = []
# a = int(input("Size: "))


# hash = [0]*26
# for i in range(len(s)):
#     hash[ord(s[i])-ord('a')] += 1

# for j in range(a):
#     c = input()
#     arr.append(c)
#     j -= 1

# for c in arr:
#     print(hash[ord(c)-ord("a")])


s = "abc@--a[[ehf"
arr = []
a = int(input("Size: "))


hash = [0]*256
for i in range(len(s)):
    hash[ord(s[i])] += 1

for j in range(a):
    c = input()
    arr.append(c)
    j -= 1

for c in arr:
    print(hash[ord(c)])
