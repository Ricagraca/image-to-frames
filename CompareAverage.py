import zope

from CompareAlgorithm import CompareAlgorithm


@zope.interface.implementer(CompareAlgorithm)
class CompareAverage:

    def calculate(self, x):
        r, g, b = 0, 0, 0
        for height in x:
            for width in height:
                r = r + width[0]
                g = g + width[1]
                b = b + width[2]

        assert (len(x) > 0) and len(x[0]) > 0
        number_of_pixels = len(x) * len(x[0])

        return (r / number_of_pixels), (g / number_of_pixels), (b / number_of_pixels)

    def similarity(self, x, y):
        xr, xg, xb = self.calculate(x)
        yr, yg, yb = self.calculate(y)

        magnitude = lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2

        vector = [xr - yr, xg - yg, xb - yb]
        return magnitude(vector)
