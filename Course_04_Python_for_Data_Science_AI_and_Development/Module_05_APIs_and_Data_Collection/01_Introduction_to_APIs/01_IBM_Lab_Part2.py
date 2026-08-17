# =============================================================================
# SECTION 3
# NBA API
# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 70)
print("SECTION 3 : NBA API")
print("=" * 70)

from nba_api.stats.static import teams

# -----------------------------------------------------------------------------
# Helper Function
# -----------------------------------------------------------------------------


def one_dict(list_dict):
    """
    Convert a list of dictionaries into
    a dictionary of lists.
    """

    keys = list_dict[0].keys()

    output = {key: [] for key in keys}

    for dictionary in list_dict:
        for key, value in dictionary.items():
            output[key].append(value)

    return output


# -----------------------------------------------------------------------------
# Retrieve NBA Teams
# -----------------------------------------------------------------------------

nba_teams = teams.get_teams()

print("\nFirst Three Teams\n")

for team in nba_teams[:3]:
    print(team)

# -----------------------------------------------------------------------------
# Convert to DataFrame
# -----------------------------------------------------------------------------

dict_nba_team = one_dict(nba_teams)

df_teams = pd.DataFrame(dict_nba_team)

print("\nNBA Teams DataFrame")

print(df_teams.head())

# -----------------------------------------------------------------------------
# Find Golden State Warriors
# -----------------------------------------------------------------------------

print("\nGolden State Warriors\n")

df_warriors = df_teams[df_teams["nickname"] == "Warriors"]

print(df_warriors)

# -----------------------------------------------------------------------------
# Warriors Team ID
# -----------------------------------------------------------------------------

id_warriors = df_warriors["id"].values[0]

print("\nWarriors Team ID")

print(id_warriors)

# =============================================================================
# SECTION 4
# Download Dataset
# =============================================================================

print("=" * 70)
print("SECTION 4 : Download Dataset")
print("=" * 70)

import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

file_name = "Golden_State.pkl"


def download_file(url, file_name):
    """
    Download file from URL.
    """

    try:

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        with open(file_name, "wb") as file:

            file.write(response.content)

        print("\nDownload Successful")

    except Exception as error:

        print("\nDownload Failed")

        print(error)


download_file(url, file_name)

# =============================================================================
# SECTION 5
# Read Pickle File
# =============================================================================

print("=" * 70)
print("SECTION 5 : Read Dataset")
print("=" * 70)

games = pd.read_pickle(file_name)

print(games.head())

# =============================================================================
# SECTION 6
# Home vs Away Games
# =============================================================================

print("=" * 70)
print("SECTION 6 : Home vs Away Analysis")
print("=" * 70)

games_home = games[games["MATCHUP"] == "GSW vs. TOR"]

games_away = games[games["MATCHUP"] == "GSW @ TOR"]

print("\nNumber of Home Games")

print(len(games_home))

print("\nNumber of Away Games")

print(len(games_away))

# =============================================================================
# SECTION 7
# Mean PLUS_MINUS
# =============================================================================

print("=" * 70)
print("SECTION 7 : PLUS_MINUS Analysis")
print("=" * 70)

print("\nAverage PLUS_MINUS (Home)")

print(games_home["PLUS_MINUS"].mean())

print("\nAverage PLUS_MINUS (Away)")

print(games_away["PLUS_MINUS"].mean())

# =============================================================================
# SECTION 8
# Plot
# =============================================================================

print("=" * 70)
print("SECTION 8 : Visualization")
print("=" * 70)

fig, ax = plt.subplots(figsize=(12, 5))

games_away.plot(x="GAME_DATE", y="PLUS_MINUS", ax=ax, label="Away")

games_home.plot(x="GAME_DATE", y="PLUS_MINUS", ax=ax, label="Home")

plt.title("Golden State Warriors vs Toronto Raptors")

plt.ylabel("PLUS_MINUS")

plt.xlabel("Game Date")

plt.grid(True)

plt.tight_layout()

plt.show()

# =============================================================================
# SECTION 9
# IBM Quiz
# =============================================================================

print("=" * 70)
print("SECTION 9 : IBM Quiz")
print("=" * 70)

print("\nAverage Points at Home")

print(games_home["PTS"].mean())

print("\nAverage Points Away")

print(games_away["PTS"].mean())

# =============================================================================
# END OF LAB
# =============================================================================

print("=" * 70)

print("LAB 01 COMPLETED SUCCESSFULLY")

print("=" * 70)
