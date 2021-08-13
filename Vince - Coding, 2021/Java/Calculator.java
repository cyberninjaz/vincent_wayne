import java.awt.*;
import java.awt.event.*;

import javax.lang.model.util.ElementScanner14;
import javax.swing.*;
//import javax.swing.border.Border;

public class Calculator {
    private static int score = 1;

    public static void main (String[] args) {
        JFrame frame = new JFrame ("Calculator 300");
        frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel p1 = new JPanel (new BorderLayout());
        JLabel top = new JLabel("     - Calculator 300 -     ");
        Font cal = new Font ("Arial", Font.ITALIC, 30);
        top.setFont (cal);
        top.setBackground (Color.BLUE);
        top.setForeground (Color.CYAN);
        top.setOpaque(true);
        top.setHorizontalAlignment(JLabel.CENTER);
        top.setBorder(BorderFactory.createEmptyBorder(7, 0, 7, 0));
        p1.add (top, BorderLayout.NORTH);

        JLabel visor = new JLabel ("");
        Font vis = new Font ("Arial", Font.PLAIN, 20);
        visor.setFont (vis);
        visor.setBackground (Color.WHITE);
        visor.setForeground (Color.BLACK);
        visor.setOpaque(true);
        visor.setHorizontalAlignment(JLabel.CENTER);
        visor.setBorder (BorderFactory.createLineBorder (Color.black));
        p1.add (visor, BorderLayout.CENTER);

        //JLabel spacerone = new JLabel ("");
        //spacerone.setBorder(BorderFactory.createEmptyBorder(30, 0, 0, 0));
        //p1.add (spacerone, BorderLayout.SOUTH);

        frame.add (p1, BorderLayout.NORTH);
        
        JPanel p2 = new JPanel (new GridLayout(4,3));
        Font gridpr = new Font ("Arial", Font.PLAIN, 11);

        for (String text : new String[] {"7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "Enter", "Clear"}) {
            JPanel wrapper = new JPanel(new BorderLayout());
            wrapper.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
            JButton btn = new JButton (text);
            btn.setFont (gridpr);
            wrapper.add(btn, BorderLayout.CENTER);
            p2.add (wrapper);
            if (text.equals("Enter"))
                btn.addActionListener (event -> {
                    String a = visor.getText();
                    
                    // 1. Locate the operator
                    int operadd = a.indexOf("+");
                    int opersub = a.indexOf("-");
                    int opermul = a.indexOf("*");
                    int operdiv = a.indexOf("/");
                    int location;
                    if (operadd != -1)
                        location = operadd;
                    else if (opersub != -1)
                        location = opersub;
                    else if (opermul != -1)
                        location = opermul;
                    else if (operdiv != -1)
                        location = operdiv;
                    else
                        return;  // can't finish because no operator

                    // 2. Extract numbers
                    String a1 = a.substring (0, location);
                    String a2 = a.substring (location + 1);
                
                    // 3. Parse numbers
                    double x1 = Double.parseDouble (a1);
                    double x2 = Double.parseDouble (a2);

                    // 4. Compute answer
                    double ans = Double.NaN;
                    if (location == (operadd))
                        ans = x1+x2;
                    else if (location == (opersub))
                        ans = x1-x2;
                    else if (location == (opermul))
                        ans = x1*x2;
                    else if (location == (operdiv))
                        ans = x1/x2;
                    // 5. dis[layt answer]
                    visor.setText(""+ ans);
                });
            else if (text.equals("Clear"))
                btn.addActionListener (event -> {
                    visor.setText("");
                });
            else
                btn.addActionListener(event -> {
                    JButton b = (JButton) event.getSource();
                    String t = b.getText();
                    visor.setText (visor.getText() + t);
                });
        }
        frame.add (p2, BorderLayout.CENTER);

        JPanel p3 = new JPanel (new GridLayout(2,3));

        for (String texttwo : new String[] {"Add +", "Subtract -", "Multiply *", "Divide %", "Decimal", "Backspace"}) {
            JPanel wrappertwo = new JPanel (new BorderLayout ());
            wrappertwo.setBorder(BorderFactory.createEmptyBorder (5,5,5,5));
            JButton btntwo = new JButton (texttwo);
            btntwo.setFont (gridpr);
            wrappertwo.add (btntwo, BorderLayout.CENTER);
            p3.add (wrappertwo);

            btntwo.addActionListener(event -> {
                JButton b = (JButton) event.getSource();
                String t = b.getText();
                if (score < 2) {
                    score = score + 1;
                    if (t.equals("Add +"))
                        visor.setText (visor.getText() + "+");
                    else if (t.equals("Subtract -"))
                        visor.setText (visor.getText() + "-");
                    else if (t.equals("Multiply *"))
                        visor.setText (visor.getText() + "*");
                    else if (t.equals("Divide %"))
                        visor.setText (visor.getText() + "/");
                }
                else if (t.equals("Decimal"))
                    visor.setText (visor.getText()+ ".");
                else if (t.equals("Backspace")) {
                    String hemi = visor.getText();
                    visor.setText(hemi.substring(0, hemi.length()-1));
                }
            });
        }

        // JButton grideight = new JButton ("8");
        // grideight.setFont (gridpr);
        // p2.add (grideight);
        frame.add (p3, BorderLayout.SOUTH);
        
        frame.setSize (400, 400);
        frame.setVisible (true);
        
    }
}
