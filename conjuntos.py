A = set([x for x in range(7, 31)])
B = set([2, 5, 7, 9, 15, 22, 33])
C = set([x for x in range(3, 30) if x % 3 == 1])

# (A ∩ C) ∪ (A⨁B)
result1 = (A.intersection(C)).union(A.symmetric_difference(B))
print("Resultado de la operación (A ∩ C) ∪ (A⨁B):", result1)

# ((A ∪ C)⨁B) ∩ (A − C)
result2 = ((A.union(C)).symmetric_difference(B)).intersection(A.difference(C))
print("Resultado de la operación ((A ∪ C)⨁B) ∩ (A − C):", result2)

# ((A ∪ B) − (A ∩ C)) ∩ (A ∪ B ∪ C)
result3 = ((A.union(B)).difference(A.intersection(C))).intersection(A.union(B).union(C))
print("Resultado de la operación ((A ∪ B) − (A ∩ C)) ∩ (A ∪ B ∪ C):", result3)