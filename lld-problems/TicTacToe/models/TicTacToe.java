package models;

import Players.Player;
import Players.PlayerFactory;
import Stategy.DefaultMoveStrategy;
import Stategy.DefaultWinStrategy;
import Stategy.MoveStrategy;
import Stategy.WinStrategy;

import java.util.Scanner;
import java.util.Stack;

public class TicTacToe {
    private Board board;
    private Player player1;
    private Player player2;
    private Player currentPlayer;
    private MoveStrategy moveStrategy;
    private WinStrategy winStrategy;
    private Stack<Comamnd> history;  // Corrected typo here

    public TicTacToe(){
        GameController gameController = GameController.getInstance();
        board = new Board(3);
        player1 = PlayerFactory.createPlayer('X');
        player2 = PlayerFactory.createPlayer('O');
        currentPlayer = player1;
        moveStrategy = new DefaultMoveStrategy();
        winStrategy = new DefaultWinStrategy();
        board.addObserver(player1);
        board.addObserver(player2);
        history = new Stack<>();
    }

    public void playGame(){
        Scanner scanner = new Scanner(System.in);
        while(true){
            System.out.println("Player " + currentPlayer);  // Fixed print statement here
            System.out.println("Enter row 0, 1, or 2:");
            int x = scanner.nextInt();
            System.out.println("Enter column 0, 1, or 2:");
            int y = scanner.nextInt();

            if(moveStrategy.isValidMove(board, x, y)){
                makeMove(x, y, currentPlayer.getSymbol());
                System.out.println("Do you want to undo? Yes/No");
                String isUndo = scanner.next();

                if(isUndo.equalsIgnoreCase("Yes")){  // Fixed string comparison
                    undoMove();
                    System.out.println("Make move again");
                    continue;
                }

                if(winStrategy.checkWin(board, currentPlayer.getSymbol())){
                    System.out.println("Player " + currentPlayer.getSymbol() + " wins!");
                    break;
                }

                if(isDraw()){
                    System.out.println("Game draw");
                    break;
                }
                switchPlayer();
            }else{
                System.out.println("Invalid move! Try again");
            }
        }
        scanner.close();
    }

    public void switchPlayer(){
        currentPlayer = (currentPlayer == player1) ? player2 : player1;
    }

    public boolean isDraw(){
        for(int i = 0; i < board.getSize(); i++){
            for(int j = 0; j < board.getSize(); j++){
                if(board.getcell(i, j) == '\0') {
                    return false;
                }
            }
        }
        return true;
    }

    public void makeMove(int x, int y, char symbol){
        Comamnd move = new MoveCommand(x, y, board, symbol);  // Corrected class name here
        history.add(move);
        move.execute();
    }

    public void undoMove(){
        Comamnd lastMove = history.pop();  // Corrected class name here
        lastMove.undo();
    }

    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        game.playGame();
    }
}
