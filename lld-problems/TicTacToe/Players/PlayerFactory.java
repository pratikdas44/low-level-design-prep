package Players;

public class PlayerFactory {
    public static Player createPlayer(char symbol){
        return new HumanPlayer(symbol);
    }
}
