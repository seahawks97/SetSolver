import Set
import Tile


def main():
    print("https://www.setgame.com/set/puzzle")
    my_set = Set.Set()
    my_set.add_tile_data("squiggle", "purple", 2, "solid")
    my_set.add_tile_data("oval", "green", 1, "solid")
    my_set.add_tile_data("diamond", "red", 3, "solid")
    my_set.add_tile_data("diamond", "purple", 1, "solid")
    my_set.add_tile_data("oval", "red", 1, "empty")
    my_set.add_tile_data("diamond", "red", 2, "empty")
    my_set.add_tile_data("oval", "red", 1, "solid")
    my_set.add_tile_data("oval", "purple", 3, "solid")
    my_set.add_tile_data("diamond", "purple", 3, "solid")
    my_set.add_tile_data("squiggle", "green", 1, "stripe")
    my_set.add_tile_data("squiggle", "purple", 3, "solid")
    my_set.add_tile_data("squiggle", "purple", 1, "solid")

    print(my_set)

    my_set.solve()


if __name__ == "__main__":
    main()
