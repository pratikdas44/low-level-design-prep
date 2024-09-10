package ATMdispenser;

import java.util.Scanner;

public class ATMDispense {
    public ChainDispenser c1;
    public ATMDispense(){
        this.c1 = new INR50Dispense();
        ChainDispenser c2 = new INR20();
        ChainDispenser c3 = new INR10();

        c1.setnextChain(c2);
        c2.setnextChain(c3);
    }

    public static void main(String[] args) {
        Currency cur = new Currency(280);
        ATMDispense atmDispense = new ATMDispense();
        while (true) {
			int amount = 0;
			System.out.println("Enter amount to dispense");
			Scanner input = new Scanner(System.in);
			amount = input.nextInt();
			if (amount % 10 != 0) {
				System.out.println("Amount should be in multiple of 10s.");
				return;
			}
			// process the request
			atmDispense.c1.dispense(new Currency(amount));
		}
    }

}
