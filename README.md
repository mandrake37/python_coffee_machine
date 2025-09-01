# Coffee Machine Program Requirements

1. **Prompt User**  
   - The machine should prompt:  
     ```
     What would you like? (espresso/latte/cappuccino):
     ```
   - Check the user’s input to decide the next action.  
   - After each action is completed (e.g., drink dispensed), the prompt should appear again to serve the next customer.

2. **Turn Off the Machine**  
   - Entering `off` will turn off the coffee machine.  
   - This command is reserved for maintainers and should stop the program execution.

3. **Print Report**  
   - Entering `report` will generate a resource report showing current values, e.g.:  
     ```
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: $2.5
     ```

4. **Check Resource Sufficiency**  
   - When a drink is chosen, check if there are enough resources to make it.  
   - Example:  
     - Latte requires 200ml water, but only 100ml remains →  
       ```
       Sorry there is not enough water.
       ```
   - The same logic applies for milk or coffee.

5. **Process Coins**  
   - If resources are sufficient, prompt the user to insert coins.  
   - Coin values:  
     - Quarters = $0.25  
     - Dimes = $0.10  
     - Nickels = $0.05  
     - Pennies = $0.01  
   - Example calculation:  
     1 quarter + 2 dimes + 1 nickel + 2 pennies =  
     `0.25 + (0.10 × 2) + 0.05 + (0.01 × 2) = $0.52`

6. **Check Transaction Success**  
   - Verify if the user inserted enough money:  
     - Example: Latte costs $2.50, user inserted $0.52 →  
       ```
       Sorry that's not enough money. Money refunded.
       ```
   - If enough money is inserted:  
     - Add the cost of the drink to machine profits.  
     - Update `report` accordingly.  
   - If too much money is inserted:  
     - Provide change, rounded to 2 decimal places.  
       Example:  
       ```
       Here is $2.45 in change.
       ```

7. **Make Coffee**  
   - If the transaction is successful and resources are available:  
     - Deduct the required ingredients from machine resources.  
   - Example:  
     - **Before purchasing a latte:**  
       ```
       Water: 300ml
       Milk: 200ml
       Coffee: 100g
       Money: $0
       ```
     - **After purchasing a latte:**  
       ```
       Water: 100ml
       Milk: 50ml
       Coffee: 76g
       Money: $2.5
       ```
   - Confirm delivery to the user:  
     ```
     Here is your latte ☕️. Enjoy!
     ```
