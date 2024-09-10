package Strategy.Arithmetic;

public class Subtraction implements Strategy{

    @Override
    public void execute(int a, int b){
        System.out.println(a-b);
    }
}
