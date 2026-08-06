// HLUM HTET AUNG (40841063)

package part2DiceGame;

public class RoundRecorder {
    private static String roundHistory = "";

    // Records details after each round
    public static void recordRound(int roundNum, int betAmount, int die1, int die2, int netEarnings) {
        String outcome = (netEarnings >= 0) ? "+£" + netEarnings : "-£" + Math.abs(netEarnings);
        roundHistory += "Round " + roundNum + " | Bet: £" + betAmount + 
                        " | Rolled: [" + die1 + ", " + die2 + "]" + 
                        " | Net: " + outcome + "\n";
    }

    // Retrieves all recorded rounds so far
    public static String getHistory() {
        return roundHistory;
    }

    // Resets history for a new game session
    public static void reset() {
        roundHistory = "";
    }
}