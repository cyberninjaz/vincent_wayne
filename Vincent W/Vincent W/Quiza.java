import java.util.Scanner;
public class Quiz {
    public static void main (String [] args) {
        Scanner sc = new Scanner (System.in);
        int score = 0;
        System.out.println("Welcome to the Quiz of knowledge. There are 10 questions. Remember to try your best, and the computer will give you your grade. If you fail the test, you will be enforced to try it again. Once you finish the proctor.");
        System.out.println("Question 1, what are the first 9 digits of pi? : ");
        String a = sc.nextLine();
        if (a.equals("3.14159265")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 2, what is the chemical used in the theory of schrödinger's cat? : ");
        String b = sc.nextLine();
        if (b.equals("hydrocyanic acid")) {
            System.out.println("Correct");
            score = score+1;
        } 
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 3, what were the four major battles in World War I? : ");
        String c = sc.nextLine();
        if (c.equals("Ypres, Somme, Verdun, and Argonne")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 4, what are the two isotopes of hydrogen that begin nuclear fusion? : ");
        String d = sc.nextLine();
        if (d.equals("deuterium and tritium")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 5, how does a capsule at high speed in a circular orbit around earth, return to the earth vertically? : ");
        String e = sc.nextLine();
        if (e.equals("Using speed, switch into an ellipical orbit, then a parabolic orbit, an then at a direct 45 degree angle downward. Then, catch air using a parachute, and land safely.")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 6, what is the fuel for most rockets that pass the Earth's atmosphere? : ");
        String f = sc.nextLine();
        if (f.equals("liquid hydrogen")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 7, what theory is faster than the speed of light, and can be used to replace binary in computers? : ");
        String g = sc.nextLine();
        if (g.equals("quantum entanglement")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("What do an overdoseage of mega vitamins cause? : ");
        String h = sc.nextLine();
        if (h.equals("It creates antioxidation which stops your oxidation, which is carsenigenic.")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 8, If a plane shot off of the ground at and exact 45 degree angle, what would that create? : ");
        String i = sc.nextLine();
        if (i.equals("a g-force that will stop gravity for a few seconds")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 9, what is the radioactive particle that alters DNA? : ");
        String j = sc.nextLine();
        if (j.equals("beta particles")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        System.out.println("Question 10, what kind of charge does a neutron have? : ");
        String k = sc.nextLine();
        if (k.equals("it doesen't have a charge")) {
            System.out.println("Correct");
            score = score+1;
        }
        else {
            System.out.println("Incorrect");
            score = score+0;
        }
        if
    }
}
