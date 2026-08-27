from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_student=None
    best_score=-1
    for stu in scores:
        name,score=stu
        if score>best_score:
            best_student=name
        best_score=max(score,best_score)
    return best_student



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
