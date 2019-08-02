import java.util.Scanner;
public class MoneyCounter {
    public static void main (String [] args) {
        Scanner computerII = new Scanner (System.in);
        System.out.println("Enter the amount of cents you have. : ");
        int cents = computerII.nextInt();
        int dollars = cents/100;
        cents = (cents%100);
        int quarters = cents/25;
        cents = (cents%25);
        int dimes = cents/10;
        cents = (cents%10);
        int nickles = cents/5;
        cents = (cents%5);
        int pennies = cents/1;
        System.out.printf("You have %s dollar(s), %s quarter(s), %s dime(s), %s nickle(s), %s pennie(s). ", dollars, quarters, dimes, nickles, pennies, cents);
    }
}