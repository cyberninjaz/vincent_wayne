import java.util.Scanner;

class Question {
    String question;
    String answer;

    boolean askAndCheck (Scanner sc) {
        System.out.println(question);
        String a = sc.nextLine();
        if (a.equals (answer)) {
            System.out.println("Correct");
            return true;
        } else {
            return false;
        }
    }
}