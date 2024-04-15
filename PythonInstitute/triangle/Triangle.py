class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__vertice3 = vertice3

    def perimeter(self):
        v1_v2 = self.__vertice1.distance_from_point(self.__vertice2)
        v2_v3 = self.__vertice2.distance_from_point(self.__vertice3)
        v3_v1 = self.__vertice3.distance_from_point(self.__vertice1)

        return v1_v2 + v2_v3 + v3_v1
