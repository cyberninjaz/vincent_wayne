import java.util.Random;
import java.util.Scanner;
public class BattleFight {
    static void battle (Fighter user, Fighter cpu) {
        Scanner sc = new Scanner (System.in);
        Random rng = new Random ();

        while (user.health > 0 && cpu.health > 0) {
            // print attack options
            System.out.println("It your turn to attack in the battle. Which weapon do you want to attack with, or which spell do you want to cast?");
            for (Attack a : user.attacks) {
                System.out.println(a.name);
            }

            // get input
            String userchoice = sc.nextLine();  // name of an attack
            
            // search through user.attacks, and find the attack that matches "choice"
            Attack usersAttack = null;
            for (Attack a : user.attacks) {
                if (userchoice.equals(a.name)) {
                    usersAttack = a;
                    break;
                }
            }

            //use the attack
            if (rng.nextDouble() < usersAttack.accuracy) {
                System.out.println("The attack is successful and hits.");
                int netDamage = usersAttack.damage - cpu.defense;
                if (netDamage <= 0)
                    System.out.println("They blacked the attack! No......!");
                else
                    cpu.health -= netDamage;

            }
            else
                System.out.println("The attack misses.");
            // Pick cpu attack
            int index = rng.nextInt (cpu.attacks.length);
            Attack cpuAttack = cpu.attacks[index];
            System.out.println(cpu.name + " uses her attack: " + cpuAttack.name);
            
            if (rng.nextDouble() < cpuAttack.accuracy) {
                System.out.println ("The attack is succesful and hits. Amandy's health is " + cpu.health +" ");
                user.health = user.health - cpuAttack.damage + user.defense;
                System.out.println("You have " + user.health + " HP left.");
            }
            else
                System.out.println("The attack misses.");
        }

    }


    public static void main(String[] args) {
        //Scanner sc = new Scanner(System.in);
        Fighter user = new Fighter();
        user.defense = 30;
        user.health = 100;
        user.strength = 1;
        user.name = "Evan";
        Attack punch = new Attack();
        punch.damage = 5;
        punch.accuracy = 0.60;
        punch.name = "Punch";
        Attack kick = new Attack();
        kick.damage = 7;
        kick.accuracy = 0.50;
        kick.name = "Kick";

        user.attacks = new Attack[] {punch, kick};
        
        Fighter cpu = new Fighter();
        cpu.defense = 50;
        cpu.health = 100;
        cpu.strength = 1;
        cpu.name = "Sensei";
        Attack slash = new Attack();
        slash.damage = 40;
        slash.accuracy = 0.80;
        slash.name = "slash";
        Attack pistol = new Attack();
        pistol.damage = 80;
        pistol.accuracy = 1.00;
        pistol.name = "pistol";

        cpu.attacks = new Attack[] {slash, pistol};
        battle(user,cpu);
    }
}
        