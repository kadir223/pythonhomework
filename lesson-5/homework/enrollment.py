import statistics
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students=[uni[1] for uni in universities]
    tution=[uni[2] for uni in universities]
    return students, tution
def mean(value):
    return sum(value) / len(value)
def median(value):
    return statistics.median(value)
students, tution = enrollment_stats(universities)
def universities_stats(universities):
    print("******************************")
    print(f"Total students: {sum(students):,}")
    print(f"Total tuition: {sum(tution):,}")
    print("")
    print(f"Student mean: {mean(students):,.2f}")
    print(f"Student median: {median(students):,.2f}")
    print("")
    print(f"Tuition mean: {mean(tution):,.2f}")
    print(f"Tuition median: {median(tution):,.2f}")
    print("******************************")
universities_stats(universities)