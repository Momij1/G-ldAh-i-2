# treasure_box = [
#     0, 1, 2,
#     3, 4, 5,
#     6, 7, 8
# ]

# treasure_box : 宝箱の位置を表す属性(0~8)

class Tile: 
    def __init__(self, id, shape, tb, player): 
        self.identification = id # 主キー(0~35)
        self.shape = shape # 地形(0 : 海, 1 : 陸)
        self.treasure_box = tb # 宝箱の位置(0~8)
        self.player = player # どちらのプレイヤーが置いたか(0 : player1, 1 : player2)
        self.adjacency = None # プレイヤー側(端)と隣接しているか(0~8)

    def __repr__(self):
        # __init__の情報をprintするためのコード
        s = self.shape
        return (
            f"Tile(id = {self.identification})\n"
            f"{s[0], s[1], s[2]}\n"
            f"{s[3], s[4], s[5]}\n"
            f"{s[6], s[7], s[8]}\n"
            f"treasure = {self.treasure_box}\n"
            f"player = {self.player}\n"
            f"adjencency = {self.adjacency}"
        )

class TileFactory:
    def __init__(self, tile_map):
        self._next_id = 0
        self.tile_map = tile_map
    
    def create(self, tile_type, treasure_box = None, player = None) :
        tile = Tile(
            id=self._next_id,
            shape=self.tile_map[tile_type].copy(),
            tb=treasure_box,
            player=player
        )
        self._next_id += 1
        
        return tile

class Board:
    size = 6
    
    def __init__(self):
        self.grid = [[None for i in range(self.size)] for j in range(self.size)]

    def __repr__(self):
        lines = []
        for row in self.grid:
            lines.append(
                " ".join("." if t is None else "T" for t in row)
            )
        return "\n".join(lines)

    def place_tile(self, row, col, tile):
        self.grid[row][col] = tile
        
    def get_tile(self, row, col):
        return self.grid[row][col]
    
    def is_inside(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size
    
    def is_edge(self, row, col):
        return row == 0 or row == self.size - 1 or col == 0 or col == self.size - 1

tile_map = {
    "island" : [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ],
    "straight" : [
        0, 0, 0,
        1, 1, 1,
        0, 0, 0
    ],
    "diagonal" : [
        0, 0, 0,
        1, 0, 0,
        1, 1, 0
    ], 
    "double_diagonal" : [
        0, 1, 1,
        1, 0, 0,
        1, 1, 0
    ],
    "t" : [
        0, 0, 0,
        1, 1, 1, 
        0, 1, 0
    ], 
    "cross" : [
        0, 1, 0,
        1, 1, 1, 
        0, 1, 0
    ]
}

tile_defs = [
    # tile名, 枚数, 宝箱の位置
    ("island", 1, 4),
    ("straight", 2, 4),
    ("diagonal", 4, 4),
    ("double_diagonal", 9, 4),
    ("t", 8, 4),
    ("t", 4, 1),
    ("cross", 8, 4)
]

tile_list = []

factory = TileFactory(tile_map)
board = Board()

for tile_type, count, treasure in tile_defs:
    for _ in range(count):
        tile_list.append(
            factory.create(
                tile_type=tile_type,
                treasure_box=treasure
            )
        )
    
tile = factory.create("straight", treasure_box=4, player=0)
board.place_tile(2, 3, tile)

print(board)