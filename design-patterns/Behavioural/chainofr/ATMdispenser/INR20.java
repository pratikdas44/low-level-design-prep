package ATMdispenser;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane;

public class INR20 implements ChainDispenser {
    private ChainDispenser chainDispenser;
    
    @Override
    public void setnextChain(ChainDispenser chainDispenser){
        this.chainDispenser = chainDispenser;
    }

    @Override
    public void dispense(Currency cur){
        if(cur.getAmount() >= 20){
            int num = cur.getAmount() / 20;
            int remainder = cur.getAmount() % 20;
            System.out.println("Dispensing " + num + " 20 INR notes");
            if(remainder != 0){
                this.chainDispenser.dispense(new Currency(remainder));
            }
        }
        else{
            this.chainDispenser.dispense(cur);
        }
    }
}
