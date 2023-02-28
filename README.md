# PoolballScript
Script to allocate points for Pool Ball Team guesses

## How to Use
1. Create an `answers.csv` file that holds all of the answers for each player's matching Pool Ball Team. The file should look something like below:
```
Timestamp,Your Name,Alex Wiggins,Oscar,Kara,Chlud,...
2/27/2023 18:56,Answers,Boomers,Track Stars,Chlud Luck,Chlud Luck,...
```
2. Download the Google Form responses from the High Tide folder in the team drive and rename it as `responses.csv`. Save it in this directory.
3. Run `python main.py` or `python3 main.py`.
4. This should print all of the responses for each guesser in your terminal.
5. It should also save the list of scores to a file called `finalscores.txt`, which is saved in descending order so you can get the top 3 or 5 scorers quickly.