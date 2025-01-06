package Stategy;

import models.Board;

public class DefaultWinStrategy implements WinStrategy{
    @Override
    public boolean checkWin(Board board, char symbol) {
        int size = board.getSize();
        for (int i = 0; i < size; i++) {
            if (checkRow(board, symbol, i) || checkColumn(board, symbol, i)) {
                return true;
            }
        }

        return checkDiagnoal(board, symbol) || checkAntidiagnoal(board, symbol);
    }

    private boolean checkRow(Board board, char symbol, int row){
        for(int i=0;i<board.getSize();i++){
            if(board.getcell(row,i) != symbol){
                return false;
            }
        }
        return true;
    }

    private boolean checkColumn(Board board, char symbol, int col){
        for(int i=0;i<board.getSize();i++){
            if(board.getcell(i,col)!= symbol){
                return false;
            }
        }
        return true;
    }

    private boolean checkDiagnoal(Board board, char symbol){
        for(int i=0;i<board.getSize();i++){
            if(board.getcell(i,i) != symbol){
                return false;
            }
        }
        return true;
    }

    private boolean checkAntidiagnoal(Board board, char symbol){
        int size = board.getSize();
        for(int i=0;i<size;i++){
            if(board.getcell(i,size-i-1) != symbol){
                return false;
            }
        }
        return true;
    }
}
