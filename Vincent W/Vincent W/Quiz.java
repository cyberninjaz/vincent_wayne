import java.util.Scanner;
public class Quiz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = 0;
        
        Question q1 = new Question();
        q1.question = "Question 1, what are the first 9 digits of pi? :";
        q1.answer = "3.14159265";
        
        Question q2 = new Question();
        q2.question = "Question 2, what is the chemical used in the theory of schrödinger's cat? : ";
        q2.answer = "hydrocyanic acid";
        
        Question q3 = new Question();
        q3.question = "Question 3, what were the four major battles in World War I? : ";
        q3.answer = "Ypres, Somme, Verdun, and Argonne";
        
        Question q4 = new Question();
        q4.question = "Question 4, what are the two isotopes of hydrogen that begin nuclear fusion? : ";
        q4.answer = "deuterium and tritium";
        
        Question q5 = new Question();
        q5.question = "Question 5, how does a capsule at high speed in a circular orbit around earth, return to the earth vertically? : ";
        q5.answer = "Turn from a circular orbit, then a parabolic orbit, and the approach the ground at a 45 degree angle and activate parachutes.";
        
        Question q6 = new Question();
        q6.question = "Question 6, what is the fuel for most rockets that pass the Earth's atmosphere? : ";
        q6.answer = "liquid hydrogen";

        Question q7 = new Question();
        q7.question = "Question 7, what theory is faster than the speed of light, and can be used to replace binary in computers? : ";
        q7.answer = "quantum theory";

        Question q8 = new Question();
        q8.question = "Question 8, If a plane shot off of the ground at and exact 45 degree angle, what would that create? : ";
        q8.answer = "a g-force";
        
        Question q9 = new Question();
        q9.question = "Question 9, what is the radioactive particle that alters DNA? : ";
        q9.answer = "beta particles";
        
        Question q10 = new Question();
        q10.question = "Question 10, what occurs when you have an overdoseage of megavitamins? : ";
        q10.answer = "antioxidation";

        Question[] qList = { q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 };
        for (Question q : qList)
            if (q.askAndCheck (sc) == true)
                score++;
        
        System.out.println("You got " + score +  " out of 10 questions correct.");
        if (score <= 5)
            System.out.println("You got an F. You fail the test. Try to study harder to achieve a greater score. 😭");
        else if (score == 6)
            System.out.println("You got a D. You are at a horrible start. Study harder to achieve a greater score. 😢");
        else if (score == 7)
            System.out.println("You got a C. Get smarter to achieve a passable and more efficent score. 😔");
        else if (score == 8)
            System.out.println("You got a B. Your'e very close to an A but still need more effort. 🙁");
        else if (score == 9)
            System.out.println("You got an A-. Your not the best, but your'e pretty good. Study a bit harder to get more smart. 😐");
        else if (score == 10)
            System.out.println("Congratulations! You scored and A+! You won and beat the quiz! 😄");
    }
}


