package Calculator;

public class Number implements ArithmeticExp{
    int value;
    public Number(int value){
        this.value = value;
    }

    public int evaluate(){
        System.out.println("Value is " + value);
        return value;
    }
}
