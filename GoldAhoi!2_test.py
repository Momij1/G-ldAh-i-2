class Tile: 
    def __init__(self, id, nw, n, ne, w, center, e, sw, s, se, tb, player): 
        self.identification = id # 主キー的なやつ
        self.north_west = nw
        self.north = n
        self.north_east = ne
        self.west = w
        self.center = center
        self.east = e
        self.south_west = sw
        self.south = s
        self.south_east = se
        self.treasure_box = tb # 宝箱の位置
        self.player = player # どちらのプレイヤーが置いたか
        self.adjacency = None # プレイヤー側(端)と隣接しているか

    def __repr__(self):
        # __init__の情報をprintするためのコード
        return f"Tile(id={self.identification},\n{self.north_west, self.north, self.north_east}\n{self.west, self.center, self.east}\n{self.south_west, self.south, self.south_east}, \n{self.treasure_box}, \n{self.player}, \n{self.adjacency})\n"


tile_list = []

for i in range(1):
    tile_island = Tile(
                i, # id
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                None, # treasure_box
                None # player
            )
            # リストに追加
    tile_list.append(tile_island)

for i in range(1, 2 + 1):
    tile_straight = Tile(
                i, # id
                0, 0, 0,
                1, 1, 1,
                0, 0, 0,
                None, # treasure_box
                None # player
            )
            # リストに追加
    tile_list.append(tile_straight)

for i in range(3, 3 + 4):
    tile_diagonal = Tile(
                i, # id
                0, 0, 0,
                1, 0, 0,
                1, 1, 0,
                None, # treasure_box
                None # player
            )
            # リストに追加
    tile_list.append(tile_diagonal)

for i in range(7, 7 + 9):
    tile_double_diagonal = Tile(
                i, # id
                0, 1, 1,
                1, 0, 1,
                1, 1, 0,
                None, # treasure_box
                None # player
            )
            # リストに追加
    tile_list.append(tile_double_diagonal)
    
for i in range(16, 16 + 8):
    tile_t_tresure_land = Tile(
                i, # id
                0, 0, 0,
                1, 1, 1,
                0, 1, 0,
                None, # treasure_box
                None # player
            )
            # リストに追加
    tile_list.append(tile_t_tresure_land)    

for i in range(24, 24 + 4):
    tile_t_tresure_land = Tile(
                i, # id
                0, 0, 0,
                1, 1, 1,
                0, 1, 0,
                None, # treasure_box
                None # player
            )
            # リストに追加
    tile_list.append(tile_t_tresure_land)    

for i in range(28, 28 + 8):
    tile_cross = Tile(
                i, # id
                0, 1, 0,
                1, 1, 1,
                0, 1, 0,
                None, # treasure_box
                None # player
            )
            # リストに追加
    tile_list.append(tile_cross)    

print(tile_list)