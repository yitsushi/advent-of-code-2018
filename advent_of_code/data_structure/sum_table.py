class SumTable:
    __storage = None
    __sum = None

    def __init__(self, width, height):
        self.__storage = [[0] * width for _ in range(0, height)]
        self.__sum = [[0] * width for _ in range(0, height)]
        self.__storage[0][0] = 10

    def from_array(arr):
        c = SumTable(len(arr[0]), len(arr))
        [c.set_row(i, arr[i]) for i in range(0, len(arr))]
        return c

    def set_row(self, y, value):
        self.__storage[y] = value

    def calculate(self):
        for y in range(0, len(self.__storage)):
            for x in range(0, len(self.__storage[y])):
                left = self.__sum[y][x-1] if x > 0 else 0
                top = self.__sum[y-1][x] if y > 0 else 0
                dup = self.__sum[y-1][x-1] if x > 0 and y > 0 else 0
                self.__sum[y][x] = self.__storage[y][x] + left + top - dup

    def sum_array(self):
        return self.__sum

    def array(self):
        return self.__storage

    def value_at(self, x, y):
        return self.__sum[y][x]

    def area(self, top_left, bottom_right):
        a = self.value_at(top_left[0] - 1, top_left[1] - 1) if top_left[1] > 0 and top_left[0] > 0 else 0
        b = self.value_at(bottom_right[0], top_left[1] - 1) if top_left[1] > 0 else 0
        c = self.value_at(top_left[0] - 1, bottom_right[1]) if top_left[0] > 0 else 0
        d = self.value_at(*bottom_right)

        return d - b - c + a
