from linked_list import LinkedList
from merge_sort import merge_sort
class Poly():
    def __init__(self, coefficient, degree):
        self.coefficient = coefficient
        self.degree = degree
    
    def get_value(self):
        return self.degree

    def __str__(self):
        return '({}*X^{})'.format(self.coefficient, self.degree)

class PolynomialOperation():
    def multiply(self, poly1, poly2):
        if not poly1 or len(poly1) == 0 or not poly2 or len(poly2) == 0:
            return None
        poly = LinkedList()
        for p1 in poly1:
            for p2 in poly2:
                poly.add_to_last(Poly(p1.coefficient * p2.coefficient, p1.degree + p2.degree))
        degree_map = {}
        for p in poly:
            if p.degree not in degree_map:
                degree_map[p.degree] = []
            degree_map[p.degree].append(p)
        poly_result = LinkedList()
        for _, v in degree_map.items():
            poly_result.add_to_last(Poly(sum(p.coefficient for p in v), v[0].degree))
        return poly_result

    def add(self, poly1, poly2):
        if not poly1 and not poly2:
            return None
        if poly1 and len(poly1) == 0:
            return poly2
        if poly2 and len(poly2) == 0:
            return poly1

        sorted_poly1 = merge_sort(poly1, f = lambda e : e.degree)
        sorted_poly2 = merge_sort(poly2, f = lambda e : e.degree)

        i = 0
        j = 0
        p1 = None
        p2 = None
        poly3 = LinkedList()
        while True:
            if i == len(sorted_poly1) or j == len(sorted_poly2):
                break
            p1 = sorted_poly1[i]
            p2 = sorted_poly2[j]
            if p1.degree == p2.degree:
                poly3.add_to_last(Poly(p1.coefficient + p2.coefficient, p1.degree))
                i += 1
                j += 1
            elif p1.degree < p2.degree:
                poly3.add_to_last(p1)
                i += 1
            else:
                poly3.add_to_last(p2)
                j += 1
        while i < len(sorted_poly1):
            poly3.add_to_last(sorted_poly1[i])
            i += 1
        while j < len(sorted_poly2):
            poly3.add_to_last(sorted_poly2[j])
            j += 1
        return poly3

    def exponentiation(self, poly, p):
        if not poly or len(poly) == 0:
            return poly
        result = LinkedList()

        if p == 0:
            result.add_to_last(Poly(1, 0))
            return result
        if p == 1:
            return poly

        if p == 2:
            return self.multiply(poly, poly)

        is_even = p % 2 == 0
        if is_even:
            return self.exponentiation(self.multiply(poly, poly), p // 2)
        else:
            return self.multiply(poly, self.exponentiation(self.multiply(poly, poly), p // 2))


def main():
    poly1 = LinkedList()
    poly2 = LinkedList()
    poly1.add_to_last(Poly(5, 10))
    poly1.add_to_last(Poly(4, 6))
    poly2.add_to_last(Poly(2, 1))
    poly2.add_to_last(Poly(3, 5))
    op = PolynomialOperation()
    result = op.multiply(poly1, poly2)
    print("multiply result--------------------")
    print('+'.join(map(str, result)))
    print("add      result--------------------")
    result = op.add(poly1, poly2)
    print('+'.join(map(str, result)))
    print("exp      result--------------------")
    result = op.exponentiation(poly1, 3)
    print('+'.join(map(str, result)))
    result = op.exponentiation(poly1, 2)
    print('+'.join(map(str, result)))

if __name__ == '__main__':
    main()

        