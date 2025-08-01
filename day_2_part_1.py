class Dimension:
    def __init__(self, length: int = 0, width: int = 0, height: int = 0):
        self.length: int = length
        self.width: int = width
        self.height: int = height

    def get_surface_area(self) -> int:
        return (
            (2 * self.length * self.width)
            + (2 * self.width * self.height)
            + (2 * self.height * self.length)
        )

    def get_smallest_side_area(self) -> int:
        return min(self.length*self.width, self.width*self.height, self.height*self.length)


with open('data/day_2_input.txt', 'r') as data_file:
    order_total: int = 0
    while True:
        line = data_file.readline()
        if not line:
            break
        current_dimension: Dimension = Dimension()

        dimensions = line.strip().split('x')
        current_dimension.length = int(dimensions[0])
        current_dimension.width = int(dimensions[1])
        current_dimension.height = int(dimensions[2])

        print(
            f"({current_dimension.length}, {current_dimension.width}, {current_dimension.height})"
        )
        order_total += (
            current_dimension.get_surface_area() + current_dimension.get_smallest_side_area()
        )
    print(order_total)