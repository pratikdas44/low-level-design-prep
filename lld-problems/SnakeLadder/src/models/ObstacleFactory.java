package models;

import java.util.List;

public class ObstacleFactory {
    public static void createSnakes(Board board, List<int []> snakes){
        for(int[] snake: snakes){
            board.addSnakes(snake[0], snake[1]);
        }
    }

    public static void createLadders(Board board, List<int []> ladders){
        for(int[] ladder: ladders){
            board.addLadders(ladder[0], ladder[1]);
        }
    }
}
