data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def count_elements(elements):
    sum = 0
    if isinstance(elements, int):
        return elements
    if isinstance(elements, str):
        return len(elements)
    if isinstance(elements, dict):
        elements = list(elements.items())
    for i in elements:
        sum = sum + count_elements(i)
    return sum
a = count_elements(data_structure)
print(a)
