package Calculator;

public class Expression implements ArithmeticExp{
    ArithmeticExp leftexp;
    ArithmeticExp rightexp;
    Operation operation;

    public Expression(ArithmeticExp leftexp, ArithmeticExp rightexp, Operation operation){
        this.leftexp = leftexp;
        this.rightexp = rightexp;
        this.operation = operation;
    }

    @Override
    public int evaluate(){
        int value = 0;
        switch (operation){
            case ADD:
                value = leftexp.evaluate() + rightexp.evaluate();
                break;

            case SUBTRACT:
                value = leftexp.evaluate() - rightexp.evaluate();
                break;

            case MULTIPLY:
                value = leftexp.evaluate() * rightexp.evaluate();
                break;

            case DIVIDE:
                value = leftexp.evaluate() / rightexp.evaluate();
                break;

        }

        System.out.println("Expression value is " + value);
        return value;
    }
}
