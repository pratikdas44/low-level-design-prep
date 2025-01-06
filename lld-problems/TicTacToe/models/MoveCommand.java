package models;
import Players.Player;
public class MoveCommand implements Comamnd{
    private int row;
    private int col;
    private Board board;
    private char symbol;

    public MoveCommand(int row, int col, Board board, char symbol){
        this.row = row;
        this.col = col;
        this.board = board;
        this.symbol = symbol;
    }

    @Override
    public void execute(){
        board.updateBoard(row, col, symbol);
    }

    @Override
    public void undo(){
        board.undoMove(row, col);
    }
}
