// HLUM HTET AUNG (40841063)

package part2DiceGame;

import javax.swing.JOptionPane;

public class ResultBoard {

    // Call this ONCE at the end of the game to print the board
    public static void displayFinalResults(int finalBankBalance) {
        String summary = "\nGAME RESULTS\n==============================================\n" 
                       + RoundRecorder.getHistory()
                       + "=============================================="
                       + "\nFinal Remaining Bank Balance: £" + finalBankBalance;

        // Print to Console
        System.out.println(summary);

        // Print to JOptionPane
        JOptionPane.showMessageDialog(null, summary, "Final Scoreboard", JOptionPane.INFORMATION_MESSAGE);
    }
}