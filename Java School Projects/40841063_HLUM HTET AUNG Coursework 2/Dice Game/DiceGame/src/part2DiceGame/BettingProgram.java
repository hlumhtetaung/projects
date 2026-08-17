// HLUM HTET AUNG (40841063)

package part2DiceGame;

import javax.swing.JOptionPane;

public class BettingProgram { // called from DiceGame for betting program
	public static void betprogram(int bank_balance, int bet_amount, int round_count, int maxRound) {
		// Ask user if they are sure to play dice poker
		int play_choice = JOptionPane.showConfirmDialog(null, "Do you want to play dice poker?", 
				"Select Yes or No", JOptionPane.YES_NO_OPTION);
		if (play_choice == JOptionPane.YES_OPTION) {
			
			System.out.println("Dice Game Console Log\n===================================");
			String username = JOptionPane.showInputDialog("Enter username");
			if (username == null || username.trim().isEmpty()) {
				username = "Jimmy (Default)";
			}
			
			// User name entry
			System.out.println("Username: " + username);
			JOptionPane.showMessageDialog(null, "Hello, " + username + "\nYou have £" + bank_balance
					+ " in your bank account.");
			System.out.println("Hello, " + username + "\nYou have £" + bank_balance + " in your bank account.");
			
			/* 
			 * This do while loop is the main block that checks if the program will end or not.
			 * In this do while loop's while condition is the condition that checks if the game is over and
			 * what condition caused the program to end.
			 * */
			do {
			    
			    
			    // Prompt until a valid bet is entered
				/* 
				 * Here the while loop is used to ask users valid bet amount so that
				 * the amount users entered is valid integer and is within the range of 1 to 4 GBP.
				 * */
			    while (true) {
			    	String input = JOptionPane.showInputDialog("Enter bet amount (£1 to £4):");
			    	
			    	// Cancel button exit
			    	if (input == null) {
			            System.exit(0);
			        }
			    	
			    	// ADVANCED FEATURE 1: variable bet amount, Exception check on valid integer
			    	try {
			    	    bet_amount = Integer.parseInt(input);
			    	} catch (NumberFormatException e) {
			    	    JOptionPane.showMessageDialog(null, "Please enter a valid number.");
			    	    continue; // Restart the input loop
			    	}
			        
			        // If condition for valid bank balance
			        if (bet_amount < 1 || bet_amount > 4) {
			            JOptionPane.showMessageDialog(null, "Bet amount must be between £1 and £4.");
			        } else if (bet_amount > bank_balance) {
			            JOptionPane.showMessageDialog(null, "The bet amount is higher than your bank balance. Bank balance: " 
			            								+ bank_balance);
			        } else {
			            break;
			        }
			    }
			    
			    // Deduct bet from bank balance
			    bank_balance -= bet_amount;
			    JOptionPane.showMessageDialog(null, "Bet accepted! Bet amount: " + bet_amount +
			    "\nRemaining bank balance: " + bank_balance);
			    System.out.println("Bet amount is " + bet_amount + " and remaining bank balance is " + bank_balance);
			    
			    round_count++;
			    // Storing returning results from dice program in local variables
			    /*
			     * This code block is the function call from DiceRolling.
			     * As the dice rolling class return an array with the random dice rolls, according to the die count, the code block
			     * here assign those results from the list into die1 and die2 variables. If there is third die, we can assign it to
			     * die3 variable as the list will have 3 indices.
			     * */
			    int[] diceresults = DiceRolling.diceprogram();
			    int die1 = diceresults[0];
			    int die2 = diceresults[1];
			    JOptionPane.showMessageDialog(null, "Die 1: " + die1 + "\nDie 2: " + die2);
			    System.out.println("Die 1 rolled " + die1 + " and Die 2 rolled " + die2);
			    
			    // Assigning return value from an object into a variable
			    int newBalance = RewardCondition.applyPayout(die1, die2, bet_amount, bank_balance);
	            int netEarnings = newBalance - bank_balance;
	            bank_balance = newBalance;
			    String rewardmsg = RewardCondition.getResultMessage(die1, die2) + "\nBank balance: £" + bank_balance;
	
			    JOptionPane.showMessageDialog(null, rewardmsg);
			    
			    // Record results to display on final board
			    RoundRecorder.recordRound(round_count - 1, bet_amount, die1, die2, netEarnings);
			    
			} while (bank_balance > 0 && round_count <= maxRound);
			
			// Game ending condition
			if (bank_balance == 0) {
				JOptionPane.showMessageDialog(null, "Game Over: You ran out of money!");
				System.out.println("Game Over: You ran out of money!");
			} else if (round_count > 5) {
				JOptionPane.showMessageDialog(null, "Game Over: You completed 5 bets!");
				System.out.println("Game Over: You completed " + maxRound+ " bets!");
			}
			
			// See final bank balance in other currencies
			/*
			 * Currency changer here will pop up after the game has ended. This allow users to see their final remaining balance
			 * after the betting game in different currencies. The options include GBP (default), USD, EURO, and MMK (Myanmar Kyats).
			 * The class CurrencyChanger mainly handle the conversions and this code block make use of currency changer class's methods.
			 * */
			int choice = JOptionPane.showConfirmDialog(null, "Do you want to see your remaining bank balance in other currency?", 
					"Currency Selection", JOptionPane.YES_NO_OPTION);
			if (choice == JOptionPane.YES_OPTION) {
				// Bank Balance Currency Converter
				String[] currencies = {"GBP", "USD", "EUR", "MMK"};
	
				String currency = (String) JOptionPane.showInputDialog(
				        null,
				        "Choose your currency:",
				        "Currency Selection",
				        JOptionPane.QUESTION_MESSAGE,
				        null,
				        currencies,
				        currencies[0]
				);
	
				if (currency == null) {
				    currency = "GBP";
				}
	
				String symbol = CurrencyChanger.getSymbol(currency);
				
				JOptionPane.showMessageDialog(null, "Your bank balance in " + symbol + ": " + 
						CurrencyChanger.convert(bank_balance, currency));
			}
				
			
			// Output final result board to both Console and JOptionPane
		    ResultBoard.displayFinalResults(bank_balance);
		        
		    // ADVANCED FEATURE 2: displaying score board
		    ScoreBoard.board(username, bank_balance);
		} else {
			DiceGame.game();
		}
		
	}
}
