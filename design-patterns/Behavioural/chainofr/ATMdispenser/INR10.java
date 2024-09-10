package ATMdispenser;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane;

public class INR10 implements ChainDispenser {
    private ChainDispenser chainDispenser;
    
    @Override
    public void setnextChain(ChainDispenser chainDispenser){
        this.chainDispenser = chainDispenser;
    }

    @Override
    public void dispense(Currency cur){
        if(cur.getAmount() >= 10){
            int num = cur.getAmount() / 10;
            int remainder = cur.getAmount() % 10;
            System.out.println("Dispensing " + num + " 10 INR notes");
            if(remainder != 0){
                this.chainDispenser.dispense(new Currency(remainder));
            }
        }
        else{
            this.chainDispenser.dispense(cur);
        }
    }
}
