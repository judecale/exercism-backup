def equilateral(sides):
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    if sides[0] != sides[1] or sides[0] != sides[2] or sides[1] != sides[2]:
        return False


def scalene(sides):
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    
    if a != b and a != c and b != c:
        return True
    if a == b or a == c or b == c:
        return False
