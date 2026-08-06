// HLUM HTET AUNG (40841063)

package part2DiceGame;

import java.util.Arrays;
import javax.swing.JOptionPane;

public class ScoreBoard {

    // Call this ONCE at game over
    public static void board(String username, int bank_balance) {
        // 1. Array of [Name, Balance] including 10 dummy players + active player
        String[][] players = {
            {"Ian", "30"}, {"Charlie", "25"}, {"Emma", "18"},
            {"Grace", "15"}, {"Alice", "12"}, {"Jack", "10"},
            {"Frank", "8"}, {"Bob", "4"}, {"Hannah", "2"}, {"David", "0"},
            {username, String.valueOf(bank_balance)}
        };

        // 2. Sort by balance directly from Highest to Lowest
        Arrays.sort(players, (a, b) -> Integer.parseInt(b[1]) - Integer.parseInt(a[1]));

        // 3. Build text string
        String output = "\n\nGAME SUMMARY\n"
                      + "Player: " + username + "\n"
                      + "----------------------------------------------\n"
                      + RoundRecorder.getHistory() + "\n"
                      + "================ TOP RANKINGS ================\n";

        for (int i = 0; i < players.length; i++) {
            String name = players[i][0];
            String bal = players[i][1];
            String marker = name.equals(username) ? " <-- YOU" : "";
            
            output += "#" + (i + 1) + " " + name + " : £" + bal + marker + "\n";
        }

        output += "==============================================";

        // 4. Output to Console and JOptionPane
        System.out.println(output);
        JOptionPane.showMessageDialog(null, output, "Leaderboard", JOptionPane.INFORMATION_MESSAGE);

        // Reset history for next game run
        RoundRecorder.reset();
    }
}