import java.util.Scanner;
public class Calculator {
    public static void main (String [] args) {
        Scanner computerII = new Scanner (System.in);
        System.out.println("Enter two numbers.");
        int computerIII = computerII.nextInt();
        int computerIV = computerII.nextInt();
        System.out.println(computerIII+computerIV);
        System.out.println(computerIII-computerIV);
        System.out.println(computerIII*computerIV);
        System.out.println(computerIII/computerIV);
        System.out.println(computerIII%computerIV);
    }
}