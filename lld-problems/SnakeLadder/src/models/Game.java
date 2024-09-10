package models;

import java.util.ArrayList;
import java.util.List;

public class Game {
    private List<Player> players;
    private int currentPlayerIndex;

    public Game(){
        this.players = new ArrayList<>();
        this.currentPlayerIndex = 0;
    }

    public List<Player> getPlayers() {
        return players;
    }

    public void setPlayers(List<Player> players) {
        this.players = players;
    }

    public int getCurrentPlayerIndex() {
        return currentPlayerIndex;
    }

    public Player getCurrentPlayers(){
        return players.get(currentPlayerIndex);
    }

    public void setCurrentPlayerIndex(int currentPlayerIndex) {
        this.currentPlayerIndex = currentPlayerIndex;
    }

    public void notifyPlayers(String message){
        for(Player player: players){
            player.update(message);
        }
    }

    public void addPlayer(Player player){
        players.add(player);
    }

    public void nextTurn(){
        currentPlayerIndex = ( currentPlayerIndex + 1) % players.size();
    }
}
