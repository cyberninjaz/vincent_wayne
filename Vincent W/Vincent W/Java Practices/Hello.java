import java.util.Scanner;
public class Hello {
    public static void main (String [] args) {
        Scanner computerII = new Scanner (System.in);
        System.out.println("Ask the computer what you want to print.");
        var answer = computerII.nextLine();
        System.out.println(answer);
    }
}
        