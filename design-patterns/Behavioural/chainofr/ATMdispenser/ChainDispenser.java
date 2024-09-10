package ATMdispenser;

public interface ChainDispenser {
    public void setnextChain(ChainDispenser chainDispenser);
    public void dispense(Currency cur);
}
