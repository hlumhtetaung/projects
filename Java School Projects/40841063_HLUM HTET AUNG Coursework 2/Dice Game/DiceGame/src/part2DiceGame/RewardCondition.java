// HLUM HTET AUNG (40841063)

package part2DiceGame;

public class RewardCondition {
	// Called from BettingProgram to check reward condition
    public static int applyPayout(int die1, int die2, int bet_amount, int bank_balance) {
        if (Math.abs(die1 - die2) == 1) {
            bank_balance += (bet_amount * 2); 
        } else if (die1 == die2) {
            bank_balance += (bet_amount * 3); 
        }
        
        return bank_balance;
    }

    public static String getResultMessage(int die1, int die2) {
        if (Math.abs(die1 - die2) == 1) {
            return "Congrats! Your bet has doubled.";
        } else if (die1 == die2) {
            return "Congrats! Your bet has tripled.";
        } else {
            return "Sorry, you did not win this time.";
        }
    }
}