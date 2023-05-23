def solution(A,B):
    zip_list = list(zip(sorted(A, reverse=True), sorted(B)))
    return sum([c[0]*c[1] for c in zip_list])