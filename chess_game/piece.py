import chess
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import QPointF, Qt
import os
from chess_game.constants import SQUARE_SIZE

class Piece(QGraphicsPixmapItem):
    def __init__(self, scene, board, svg_file, chess_piece,initial_square):
        super().__init__()
        self.scene = scene
        self.board = board
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.join(current_dir, os.pardir)
        base_dir = os.path.normpath(base_dir)
        assets_path = os.path.join(base_dir, 'assets', 'chess_pieces')
        svg_file_path = os.path.join(assets_path, svg_file)
        renderer = QSvgRenderer(svg_file_path)
        pixmap = QPixmap(SQUARE_SIZE,SQUARE_SIZE)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        self.setPixmap(pixmap)
        self.chess_piece = chess_piece
        # Store the initial square of the piece
        self.initial_square = initial_square
        # Track the current square of the piece
        self.current_square = initial_square
        self.original_pos = QPointF(initial_square % 8 * SQUARE_SIZE,
                                    initial_square // 8 * SQUARE_SIZE)
        self.setPos(self.original_pos)


    def generate_position_fen(self,board):
        fen_rows = []
        for rank in range(7, -1, -1):  # 7 to 0
            empty_count = 0
            fen_row = ""
            for file in range(8):  # 0 to 7
                piece = board.piece_at(chess.square(file, rank))
                if piece is None:
                    empty_count += 1
                else:
                    if empty_count > 0:
                        fen_row += str(empty_count)
                        empty_count = 0
                    fen_row += piece.symbol()
            # End of rank, append remaining empty square count
            if empty_count > 0:
                fen_row += str(empty_count)
            fen_rows.append(fen_row)
        return '/'.join(fen_rows)


    def generate_custom_fen(self, scene):
        # 8x8 board
        board_matrix = [["" for _ in range(8)] for _ in range(8)]
        # Fill the board matrix with the current pieces
        for item in scene.items():
            if isinstance(item, Piece):
                x, y = item.x() // SQUARE_SIZE, item.y() // SQUARE_SIZE
                # Convert graphical coordinates to chess board coordinates
                rank, file = 7 - int(y), int(x)
                piece_symbol = item.chess_piece.symbol()
                board_matrix[rank][file] = piece_symbol
        # Convert the board matrix to FEN notation
        fen_parts = []
        for rank in board_matrix:
            empty = 0
            fen_part = ""
            for square in rank:
                if square == "":
                    empty += 1
                else:
                    if empty > 0:
                        fen_part += str(empty)
                        empty = 0
                    fen_part += square
            if empty > 0:
                fen_part += str(empty)
            fen_parts.append(fen_part)
        # Reverse the ranks to get the correct order
        fen_position = "/".join(fen_parts[::-1])
        return fen_position

    def mousePressEvent(self, event):
        self.original_pos = self.pos()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        x = round(self.x() / SQUARE_SIZE) * SQUARE_SIZE
        y = round(self.y() / SQUARE_SIZE) * SQUARE_SIZE

        file = x // SQUARE_SIZE
        rank = 7 - (y // SQUARE_SIZE)
        square = chess.square(file, rank)
        target_piece = self.scene.board.piece_at(square)

        if target_piece is None or square == self.initial_square:
            self.setPos(QPointF(x, y))
            self.scene.board.push(chess.Move(self.current_square, square))
            self.current_square = square
        else:
            self.setPos(self.original_pos)


        # if we want to restrict the movement of the pieces only to inside the chessboard
        # if a piece is moved outside of the board then it is returned back to where it was
        """ if 0 <= x <= (7 * SQUARE_SIZE) and 0 <= y <= (7 * SQUARE_SIZE):
            file = x // SQUARE_SIZE
            rank = 7 - (y // SQUARE_SIZE)
            square = chess.square(file, rank)
            target_piece = self.scene.board.piece_at(square)

            if target_piece is None or square == self.initial_square:
                self.setPos(QPointF(x, y))
                self.scene.board.push(chess.Move(self.current_square, square))
                self.current_square = square
            else:
                self.setPos(self.original_pos)
        else:
            self.setPos(self.original_pos) """

        #fen_position_test = self.generate_position_fen(self.scene.board)
        #print("generated_fen_position", fen_position_test)
        fen_position = self.generate_custom_fen(self.scene)
        self.scene.fenUpdated.emit(fen_position)

