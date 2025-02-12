#q1 Union of Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

#q2 Intersection of Sets
intersection_set = set1 & set2
print(intersection_set)

#q3 Difference of Sets
difference_set = set1 - set2
print(difference_set)

#q4 Check Subset
is_subset = set1.issubset(set2)
print(is_subset)

#q5 Check Element
check_element = 2 in set1
print(check_element)

#q6 Set Length
set_length = len(set1)
print(set_length)

#q7 Convert List to Set
lst = [1, 2, 2, 3, 4, 4, 5]
list_to_set = set(lst)
print(list_to_set)

#q8 Remove Element
set1.discard(2)
print(set1)

#q9 Clear Set
set1.clear()
print(set1)

#q10 Check if Set is Empty
is_empty_set = len(set1) == 0
print(is_empty_set)

#q11 Symmetric Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_diff = set1 ^ set2
print(symmetric_diff)

#q12 Add Element
set1.add(6)
print(set1)

#q13 Pop Element
popped_element = set1.pop() if set1 else None
print(popped_element)

#q14 Find Maximum
max_value = max(set2)
print(max_value)

#q15 Find Minimum
min_value = min(set2)
print(min_value)

#q16 Filter Even Numbers
set_numbers = {1, 2, 3, 4, 5, 6}
even_numbers = {x for x in set_numbers if x % 2 == 0}
print(even_numbers)

#q17 Filter Odd Numbers
odd_numbers = {x for x in set_numbers if x % 2 != 0}
print(odd_numbers)

#q18 Create a Set of a Range
range_set = set(range(1, 11))
print(range_set)

#q19 Merge and Deduplicate
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged_set = set(list1 + list2)
print(merged_set)

#q20 Check Disjoint Sets
disjoint_check = set1.isdisjoint(set2)
print(disjoint_check)

#q21 Remove Duplicates from a List
unique_list = list(set(lst))
print(unique_list)

#q22 Count Unique Elements
unique_count = len(set(lst))
print(unique_count)

#q23 Generate Random Set
import random
random_set = {random.randint(1, 100) for _ in range(5)}
print(random_set)
