import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("ipl_matches.csv")
players = pd.read_csv("ipl_player_stats.csv")

print("IPL Matches")
print(matches.head())

print("\nTotal Matches:", len(matches))

print("\nMatch Columns:")
print(matches.columns.tolist())

print("\nPlayer Statistics")
print(players.head())

print("\nPlayer Columns:")
print(players.columns.tolist())

print("\nMissing Values:")
print(matches.isnull().sum())

if "winner" in matches.columns:
    print("\nTop Teams by Wins")
    print(matches["winner"].value_counts().head(10))

if "runs" in players.columns and "player" in players.columns:
    top_players = players.groupby("player")["runs"].sum()
    top_players = top_players.sort_values(ascending=False).head(10)

    print("\nTop 10 Run Scorers")
    print(top_players)

    top_players.plot(kind="bar")
    plt.title("Top 10 Run Scorers")
    plt.xlabel("Player")
    plt.ylabel("Runs")
    plt.tight_layout()
    plt.show()

print("\nIPL Analysis Completed!")
if "season" in matches.columns:
    print("\nMatches by Season")
    print(matches["season"].value_counts().sort_index())

if "toss_decision" in matches.columns:
    print("\nToss Decisions")
    print(matches["toss_decision"].value_counts())

if "toss_winner" in matches.columns and "winner" in matches.columns:
    toss_match_wins = (
        matches["toss_winner"] == matches["winner"]
    ).sum()

    print("\nToss Winner Also Won Match:", toss_match_wins)

if "venue" in matches.columns:
    print("\nTop 5 Venues")
    print(matches["venue"].value_counts().head(5))
with open("ipl_summary.txt", "w") as file:
    file.write("IPL Sports Data Analysis\n")
    file.write("========================\n")
    file.write(f"Total Matches: {len(matches)}\n")

    if "winner" in matches.columns:
        file.write("\nTeam Wins:\n")
        file.write(matches["winner"].value_counts().to_string())

print("\nSummary saved successfully!")