package models;

import Players.Player;

import java.util.ArrayList;
import java.util.List;

public class Board {

    private int size;
    private char [][] board;
    private List<Player> playerList = new ArrayList<>();

    public Board(int size){
        this.size = size;
        board = new char[size][size];
    }

    public void addObserver(Player player){
        playerList.add(player);
    }

    public void notifyObservers(){
        for(Player player : playerList){
            player.update(this);
        }
    }

    public void updateBoard(int x, int y, char symbol){
        board[x][y] = symbol;
        notifyObservers();
    }

    public void undoMove(int x, int y){
        board[x][y] = '\0';
        notifyObservers();
    }

    public char getcell(int x, int y){
        return board[x][y];
    }

    public int getSize(){
        return this.size;
    }
}
