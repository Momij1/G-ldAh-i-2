import random

class Tile:
    def __init__(self, id, terrain, tb, player, edge):
        self.id = id # 主キー(0~35)
        self.terrain = terrain # 地形
        self.tb = tb # 宝箱の位置(0~8)
        self.player = player # どちらのplayerが置いたか(0, 1)
        self.edge = edge # player1, 2側の端と接触している部分

    def __repr__(self):
        return (
            f'''
            Tile(id={self.id}),\n 
            terrain={self.terrain},\n
            tb={self.tb},\n
            player={self.player},\n
            edge={self.edge}\n
            '''
        )
    
terrain_data = {
    # 名前 : (地形, 個数, 宝箱の位置)
    "island" : ([
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ], 1, 4),
    "straight" : ([
        0, 0, 0,
        1, 1, 1,
        0, 0, 0
    ], 2, 4), 
    "diagonal" : ([
        0, 0, 0,
        1, 0, 0,
        1, 1, 0
    ], 4, 4),
    "dpuble_diagonal" : ([
        0, 1, 1,
        1, 0, 1,
        1, 1, 0
    ], 9, 4),
    "t_tb_land" : ([
        0, 0, 0,
        1, 1, 1,
        0, 1, 0
    ], 8, 4),
    "t_tb_sea" : ([
        0, 0, 0,
        1, 1, 1,
        0, 1, 0
    ], 4, 1),
    "cross" : ([
        0, 1, 0,
        1, 1, 1,
        0, 1, 0
    ], 8, 4)
}

tile_list = []
tile_id = 0

# 疑似コード
for name, (terrain, count, tb) in terrain_data.items():
    for _ in range(count):
        tile = Tile(
            id = tile_id,
            terrain = terrain,
            tb = tb,
            player=None,
            edge = None
            )
        tile_id += 1
        tile_list.append(tile)

board = [[' ' for i in range(6)] for j in range(6)]

random.shuffle(tile_list)

cnt = 0

for col in range(6):
    for row in range(6):
        board[col][row] = tile_list[cnt]
        cnt += 1
        
print(board)

'''+
terrainのイメージ
0 : 海, 1 : 陸
terrain = [
    0, 0, 0,
    1, 1, 1,
    0, 0, 0
]

edgeのイメージ
edge = [0, 1, 2]([6, 7, 8])
'''