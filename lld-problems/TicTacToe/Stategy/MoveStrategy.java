package Stategy;

import models.Board;

public interface MoveStrategy {
    boolean isValidMove(Board board, int x, int y);
}
