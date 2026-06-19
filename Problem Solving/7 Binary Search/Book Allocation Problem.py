print('-----Brute Force-----')
books = [25,46,28,49,24]
students = 4

if students > len(books):
    print('-1')
def fun(books,pages):
    stu = 1
    student_pages = 0
    for i in range(len(books)):
        if books[i] + student_pages <= pages:
            student_pages += books[i]
        else:
            stu += 1
            student_pages = books[i]
    return stu
low = max(books)
high = sum(books)
for pages in range(low,high+1):
    count_student = fun(books,pages)
    if count_student == students:
        print(pages)
        break

print('-----Optimal Approach-----')
books = [25,46,28,49,24]
students = 4
if students > len(books):
    print('-1')
def fun(books,pages):
    stu = 1
    student_pages = 0
    for i in range(len(books)):
        if books[i]+student_pages <= pages:
            student_pages += books[i]
        else:
            stu += 1
            student_pages = books[i]
    return stu
low = max(books)
high = sum(books)
while low <= high:
    mid = (low+high)//2
    count_student = fun(books,mid)
    if count_student <= students:
        ans = mid
        high = mid - 1
    else:
        low = mid +1 
print(ans)