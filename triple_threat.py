"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Name - Month Year
"""

import random

def main() -> None:
    cost_to_play = 2
    base_prize = 10

    sim_days = int(input("How many days to simulate? "))

    print("Games Played,Total Collected,Total Paid Out,Profit")

    for i in range(sim_days):

        plays_per_day = random.randint(1000, 5000)

        prize = 0
        games_played = 0
        money_collected = 0

        for i in range(plays_per_day):

            games_played += 1
            money_collected += cost_to_play

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)


            if dice1 == dice2 and dice2 == dice3 and dice3 == dice1:
                if dice1 < 6:
                    prize += base_prize * dice1
                elif dice1 == 6:
                    prize += base_prize * 10

        print(f"{games_played},{money_collected},{prize},{money_collected-prize}")

if __name__ == "__main__":
    main()