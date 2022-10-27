class Board:
        
    def __init__(self):
        
        self.cells = []
        self.ROWS, self.COLUMNS = 12, 12
        self.border_color = ((84, 84, 84))
        self.cell_color = ((239, 245, 203))
        self.cell_size = 60
        self.castle_color = ((53, 115, 109))