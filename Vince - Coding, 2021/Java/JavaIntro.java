import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class JavaIntro {
    public static void main (String[] args) {
        JFrame frame = new JFrame ("App");
        frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().setLayout(new BorderLayout());
        frame.setVisible (true);
        JLabel headlabel = new JLabel ("Age Data Collector");
        frame.add(headlabel, BorderLayout.NORTH);
        JLabel alabel = new JLabel ("What is your age?");
        frame.add(alabel, BorderLayout.WEST);
        JTextField atext = new JTextField (8);
        frame.add(atext, BorderLayout.CENTER);
        JButton abutton = new JButton ("Submit");
        frame.add(abutton, BorderLayout.EAST);
        frame.pack();
        frame.setLocationRelativeTo (null);
        frame.setVisible (true);
    }
}