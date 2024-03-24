import chess
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QBrush
from PySide6.QtCore import QPointF, QRectF, Qt, Signal
from chess_game.piece import Piece
from chess_game.constants import MARGIN, SQUARE_SIZE

class Chessboard(QGraphicsScene):
    fenUpdated = Signal(str)
    def __init__(self, board, parent = None):
        super().__init__(parent)
        self.board = board


    def render(self):
        self.clear()
        orientation = True

        for square, bitboard in enumerate(chess.BB_SQUARES):
            file = chess.square_file(square)
            rank = chess.square_rank(square)
            x = (file if orientation else 7 - file) * SQUARE_SIZE + MARGIN
            y = (7 - rank if orientation else rank) * SQUARE_SIZE + MARGIN
            square_color = Qt.GlobalColor.white if chess.BB_LIGHT_SQUARES & bitboard else Qt.GlobalColor.gray
            self.addRect(QRectF(x, y, SQUARE_SIZE, SQUARE_SIZE), brush=QBrush(square_color))

        # Render pieces on squares.
        for square in chess.SQUARES:
            file = chess.square_file(square)
            rank = chess.square_rank(square)
            x = (file if orientation else 7 - file) * SQUARE_SIZE + MARGIN
            y = (7 - rank if orientation else rank) * SQUARE_SIZE + MARGIN
            piece = self.board.piece_at(square)

            if piece is not None:
                piece_symbol = piece.symbol()
                color = "white" if piece_symbol.isupper() else "black"
                filename = f"{piece_symbol}-{color}.svg"
                item = Piece(self, self.board,filename, piece, square)
                item.setFlag(QGraphicsPixmapItem.GraphicsItemFlag.ItemIsMovable)
                item.setPos(QPointF(x, y))
                self.addItem(item)