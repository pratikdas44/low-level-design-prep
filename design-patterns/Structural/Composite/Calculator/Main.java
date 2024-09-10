package Calculator;

public class Main {
    public static void main(String[] args) {
        ArithmeticExp two = new Number(2);
        ArithmeticExp one = new Number(1);
        ArithmeticExp seven = new Number(7);
        ArithmeticExp addexp = new Expression(one, two, Operation.ADD);
        ArithmeticExp twoexp = new Expression(addexp, seven, Operation.MULTIPLY);
        System.out.println(twoexp.evaluate());
    }
}
