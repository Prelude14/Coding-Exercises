def my_coin_change(coins: list[int], amount: int):
   """
   Given an int array of coins that are different amounts, and an int amount total, returns the fewest number of coins from the array that       will equal that total amount, otherwise returns -1 if that is not possible.
   
   ************* NOTE: coins can be used an infinite amount of times. ***************
   
   Dont need to explain the math after, tho it would be nice.
   """
   amounts_list = [float('inf')] * (amount+1) #create list of minimum coins needed to make the amount equal to the index
   amounts_list[0] = 0 #can't make amount of 0, so set to 0

   #need to calculate each minimim coins needed for each amount i
   for i in range(1, amount+1):
      #try every coin to figure out which is the minimum needed for amount i
      for coin in coins:
         #as long as coin is NOT GREATER than amount i, AND i MINUS this coin's value is NOT infinity, we can use that coin
         if coin <= i and amounts_list[i-coin] != float('inf'):

            #if using this coin, need to set minimum coins to reach amount i to minimum between the current minimum and the minimum coins to             reach the left over amount from using this coin, in otherwords amounts_list[i-coin], since we should have already calculated                 that by the time we get to i == amount
            amounts_list[i] = min(amounts_list[i], amounts_list[i-coin] + 1) #update the minimum coins needed for amount i

   #check min_coins isn't infinity still, then we found the min coins needed to reach amount and can return it, otherwise return -1
   if amounts_list[amount] != float('inf'):
      return amounts_list[amount]
   else:
      return -1

def main():
  print("=" * 50)
  print("COIN CHANGE EXERCISE")
  print("=" * 50)

  coins = [1, 2, 5]
  amounts = [11, 15, 23, 30, 63]

  print(f"\nAvailable coins: {coins}")
  print("-" * 50)

  print("\n1. MINIMUM COINS NEEDED:")
  print("-" * 30)
  for amount in amounts:
      result = my_coin_change(coins, amount)
      print(f"   Amount ${amount:3d}: {result} coins")

  second_coins = [2]
  second_amounts = [3, 15, 23, 30, 63]

  print(f"\nAvailable coins: {second_coins}")
  print("-" * 50)

  print("\n1. MINIMUM COINS NEEDED:")
  print("-" * 30)
  for second_amount in second_amounts:
    second_result = my_coin_change(second_coins, second_amount)
    print(f"   Amount ${second_amount:3d}: {second_result} coins")


if __name__ == "__main__":
  main()