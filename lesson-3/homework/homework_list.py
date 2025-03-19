#q1 Count Occurrences
lst = [1, 2, 3, 4, 2, 2, 5]
element = 2
count = lst.count(element)
print(count)

#q2 Sum of Elements
total = sum(lst)
print(total)a

#q3 Max Element
max_value = max(lst)
print(max_value)

#q4 Min Element
min_value = min(lst)
print(min_value)

#q5 Check Element
exists = element in lst
print(exists)

#q6 First Element
first = lst[0] if lst else None
print(first)

#q7 Last Element
last = lst[-1] if lst else None
print(last)

#q8 Slice List
sliced = lst[:3]
print(sliced)

#q9 Reverse List
reversed_lst = lst[::-1]
print(reversed_lst)

#q10 Sort List
sorted_lst = sorted(lst)
print(sorted_lst)

#q11 Remove Duplicates
unique_lst = list(set(lst))
print(unique_lst)

#q12 Insert Element
lst.insert(2, 99)
print(lst)

#q13 Index of Element
index = lst.index(element) if element in lst else -1
print(index)

#q14 Check for Empty List
is_empty = len(lst) == 0
print(is_empty)

#q15 Count Even Numbers
even_count = len([x for x in lst if x % 2 == 0])
print(even_count)

#q16 Count Odd Numbers
odd_count = len([x for x in lst if x % 2 != 0])
print(odd_count)

#q17 Concatenate Lists
lst2 = [6, 7, 8]
concatenated = lst + lst2
print(concatenated)

#q18 Find Sublist
sublist = [2, 3]
sublist_exists = any(lst[i:i+len(sublist)] == sublist for i in range(len(lst) - len(sublist) + 1))
print(sublist_exists)

#q19 Replace Element
if element in lst:
    lst[lst.index(element)] = 100
print(lst)

#q20 Find Second Largest
unique_sorted = sorted(set(lst))
second_largest = unique_sorted[-2] if len(unique_sorted) > 1 else None
print(second_largest)

#q21 Find Second Smallest
second_smallest = unique_sorted[1] if len(unique_sorted) > 1 else None
print(second_smallest)

#q22 Filter Even Numbers
even_numbers = [x for x in lst if x % 2 == 0]
print(even_numbers)

#q23 Filter Odd Numbers
odd_numbers = [x for x in lst if x % 2 != 0]
print(odd_numbers)

#q24 List Length
length = len(lst)
print(length)

#q25 Create a Copy
copy_lst = lst[:]
print(copy_lst)

#q26 Get Middle Element
n = len(lst)
middle = lst[n//2-1:n//2+1] if n % 2 == 0 else lst[n//2]
print(middle)

#q27 Find Maximum of Sublist
max_sublist = max(lst[1:4])
print(max_sublist)

#q28 Find Minimum of Sublist
min_sublist = min(lst[1:4])
print(min_sublist)

#q29 Remove Element by Index
index_to_remove = 2
if 0 <= index_to_remove < len(lst):
    lst.pop(index_to_remove)
print(lst)

#q30 Check if List is Sorted
is_sorted = lst == sorted(lst)
print(is_sorted)

#q31 Repeat Elements
n = 2
repeated = [x for x in lst for _ in range(n)]
print(repeated)

#q32 Merge and Sort
merged_sorted = sorted(lst + lst2)
print(merged_sorted)

#q33 Find All Indices
indices = [i for i, x in enumerate(lst) if x == element]
print(indices)

#q34 Rotate List
rotation = 2
rotated = lst[-rotation:] + lst[:-rotation]
print(rotated)

#q35 Create Range List
range_lst = list(range(1, 11))
print(range_lst)

#q36 Sum of Positive Numbers
sum_positive = sum(x for x in lst if x > 0)
print(sum_positive)

#q37 Sum of Negative Numbers
sum_negative = sum(x for x in lst if x < 0)
print(sum_negative)

#q38 Check Palindrome
is_palindrome = lst == lst[::-1]
print(is_palindrome)

#q39 Create Nested List
chunk_size = 2
nested_list = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
print(nested_list)

#q40 Get Unique Elements in Order
unique_ordered = []
for x in lst:
    if x not in unique_ordered:
        unique_ordered.append(x)
print(unique_ordered)
