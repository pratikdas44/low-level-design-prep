package Stategy;

import models.Board;

public class DefaultMoveStrategy implements MoveStrategy{
    @Override
    public boolean isValidMove(Board board, int x, int y){
        return board.getcell(x,y) == '\0';
    }
}
