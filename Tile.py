class Tile:
    def __init__(self, shape, color, count, fill):
        self.shape = shape
        self.color = color
        self.count = count
        self.fill = fill

    def __str__(self):
        shape = str(self._get_shape())
        color = str(self._get_color())
        count = str(self._get_count())
        fill = str(self._get_fill())
        return f"{shape}\t{color}\t{count}\t{fill}"

    def _set_shape(self, shape):
        self.shape = shape

    def _set_color(self, color):
        self.color = color

    def _set_count(self, count):
        self.count = count

    def _set_fill(self, fill):
        self.fill = fill

    def _get_shape(self):
        return self.shape

    def _get_color(self):
        return self.color

    def _get_count(self):
        return self.count

    def _get_fill(self):
        return self.fill
