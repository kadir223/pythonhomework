#q1 Count Occurrences
tpl = (1, 2, 3, 4, 2, 2, 5)
element = 2
count = tpl.count(element)
print(count)

#q2 Max Element
max_value = max(tpl)
print(max_value)

#q3 Min Element
min_value = min(tpl)
print(min_value)

#q4 Check Element
exists = element in tpl
print(exists)

#q5 First Element
first = tpl[0] if tpl else None
print(first)

#q6 Last Element
last = tpl[-1] if tpl else None
print(last)

#q7 Tuple Length
length = len(tpl)
print(length)

#q8 Slice Tuple
sliced = tpl[:3]
print(sliced)

#q9 Concatenate Tuples
tpl2 = (6, 7, 8)
concatenated = tpl + tpl2
print(concatenated)

#q10 Check if Tuple is Empty
is_empty = len(tpl) == 0
print(is_empty)

#q11 Get All Indices of Element
indices = [i for i, x in enumerate(tpl) if x == element]
print(indices)

#q12 Find Second Largest
unique_sorted = sorted(set(tpl))
second_largest = unique_sorted[-2] if len(unique_sorted) > 1 else None
print(second_largest)

#q13 Find Second Smallest
second_smallest = unique_sorted[1] if len(unique_sorted) > 1 else None
print(second_smallest)

#q14 Create a Single Element Tuple
single_element_tuple = (element,)
print(single_element_tuple)

#q15 Convert List to Tuple
lst = [1, 2, 3, 4, 5]
tuple_from_list = tuple(lst)
print(tuple_from_list)

#q16 Check if Tuple is Sorted
is_sorted = tpl == tuple(sorted(tpl))
print(is_sorted)

#q17 Find Maximum of Subtuple
max_subtuple = max(tpl[1:4])
print(max_subtuple)

#q18 Find Minimum of Subtuple
min_subtuple = min(tpl[1:4])
print(min_subtuple)

#q19 Remove Element by Value
new_tpl = tuple(x for x in tpl if x != element)
print(new_tpl)

#q20 Create Nested Tuple
chunk_size = 2
nested_tuple = tuple(tpl[i:i+chunk_size] for i in range(0, len(tpl), chunk_size))
print(nested_tuple)

#q21 Repeat Elements
n = 2
repeated = tuple(x for x in tpl for _ in range(n))
print(repeated)

#q22 Create Range Tuple
range_tuple = tuple(range(1, 11))
print(range_tuple)

#q23 Reverse Tuple
reversed_tuple = tpl[::-1]
print(reversed_tuple)

#q24 Check Palindrome
is_palindrome = tpl == tpl[::-1]
print(is_palindrome)

#q25 Get Unique Elements
unique_ordered = []
for x in tpl:
    if x not in unique_ordered:
        unique_ordered.append(x)
unique_tuple = tuple(unique_ordered)
print(unique_tuple)
