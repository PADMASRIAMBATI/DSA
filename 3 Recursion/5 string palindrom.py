# def palindrom(name,i):
#     n = len(name)
#     if i >= n//2:
#         return True
#     if name[i] != name[n-i-1]:
#         return False
#     return palindrom(name,i+1)
    
# name = "madam"
# print(palindrom(name,0))

# def palindrom1(self,name):
#     def help(i,n):
#         if i >= n//2:
#             return True
#         if name[i] != name[n-i-1]:
#             return False 
#         return help(i+1,n)
#     n=len(name)
#     return self.help(0,n)
# name = "newen"
# print(palindrom1(name))

def isPalindrome(s):
    s1 = ''.join(i for i in s if i.isalnum()).lower()
    def help(i,n):
        if i >= n//2:
            return True
        if s1[i] != s1[n-i-1]:
            return False
        return help(i+1,n)
    n=len(s1)
    return help(0,n)
s = '0P'
print(isPalindrome(s))