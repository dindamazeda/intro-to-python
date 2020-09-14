products1 = {'keks', 'banane', 'brasno', 'kafa', 'mleko'}
products2 = {'kafa', 'sok', 'brasno', 'koka-kola', 'pecivo', 'hleb', 'testenine'}

products_intersection = products1.intersection(products2)
print(products_intersection)


products_diff = products2.difference(products1)
print(products_diff)


products_union = products1.union(products2)
print(products_union)


symmetric_diff = products2.symmetric_difference(products1)
print(symmetric_diff)

print(products1)
print(products2)