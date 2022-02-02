import Tile


class Set:
    def __init__(self):
        self.tiles = []
        self.counter = 0
        self.solved = []

    def __str__(self):
        out = "#\tShape\tColor\tCount\tFill\n" + "-"*36 + "\n"
        for i in range(len(self.tiles)):
            out += str(i+1) + "\t" + str(self.tiles[i]) + "\n"
        return out

    def _get_tiles(self):
        return self.tiles

    def _get_counter(self):
        return self.counter

    def _set_tiles(self, tiles):
        self.tiles = tiles

    def _set_counter(self, counter):
        self.counter = self

    def _increase_counter(self):
        self.counter += 1

    def _decrease_counter(self):
        self.counter -= 1

    def add_tile(self, tile):
        self.tiles.append(tile)
        self._increase_counter()

    def add_tile_data(self, shape, color, count, fill):
        t = Tile.Tile(shape, color, count, fill)
        self.tiles.append(t)
        self._increase_counter()

    def remove_tile(self, index):
        del self.tiles[index]
        self._decrease_counter()

    def remove_shapes(self, shape):
        for tile in self.tiles:
            if tile.shape == shape:
                self.tiles.remove(tile)

    def remove_colors(self, color):
        for tile in self.tiles:
            if tile.shape == color:
                self.tiles.remove(tile)

    def remove_count(self, count):
        for tile in self.tiles:
            if tile.shape == count:
                self.tiles.remove(tile)

    def remove_fill(self, fill):
        for tile in self.tiles:
            if tile.shape == fill:
                self.tiles.remove(tile)

    def _choose_tiles(self):
        # TODO
        # look at 3 different ones
        return [0, 1, 2]  # the indices of tiles to choose from

    def _is_valid(self, set, trait):
        # TODO
        for tile in set:
            if trait == 0:
                continue
            if trait == 1:
                continue
            if trait == 2:
                continue
            if trait == 3:
                continue

    def _solve_set(self):
        # TODO
        potential_set = self._choose_tiles()

        # shape, color, count, fill
        # 1 -> either all 3 are the same, or all 3 are different
        # 0 -> 2 are the same, but 1 is different
        # all 1s -> it's a set!
        viability = [0, 0, 0, 0]

        for i in range(4):
            if self._is_valid(potential_set, i):
                viability[i] = 1

        return 1

        # as soon as a false is returned, a negative can be set, otherwise continue
        # if all (same/diff, same/diff, same/diff, same/diff), it's a set

    def solve(self):
        pass
