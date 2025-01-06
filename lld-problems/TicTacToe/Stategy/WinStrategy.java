package Stategy;

import models.Board;

public interface WinStrategy {
    boolean checkWin(Board board, char symbol);
}

