package ATMdispenser;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane;

public class INR50Dispense implements ChainDispenser {
    private ChainDispenser chainDispenser;
    
    @Override
    public void setnextChain(ChainDispenser chainDispenser){
        this.chainDispenser = chainDispenser;
    }

    @Override
    public void dispense(Currency cur){
        if(cur.getAmount() >= 50){
            int num = cur.getAmount() / 50;
            int remainder = cur.getAmount() % 50;
            System.out.println("Dispensing " + num + " 50 INR notes");
            if(remainder != 0){
                this.chainDispenser.dispense(new Currency(remainder));
            }
        }
        else{
            this.chainDispenser.dispense(cur);
        }
    }

}
