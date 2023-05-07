import requests
from bs4 import BeautifulSoup

site_url = 'https://liquipedia.net/dota2/Main_Page'


def get_match_cards():
    page = requests.get(url=site_url)
    soup = BeautifulSoup(page.text, "lxml")

    data = []
    match_cards = soup.find_all("table", class_="wikitable wikitable-striped infobox_matches_content")

    print("total cards:", len(match_cards))

    for i in range(0, 5):
        team_left = match_cards[i].find("td", class_="team-left").find("span", class_="team-template-text").text
        team_right = match_cards[i].find("td", class_="team-right").find("span", class_="team-template-text").text
        score = match_cards[i].find("td", class_="versus").find("div").text
        try:
            games_count = match_cards[i].find("td", class_="versus").find("abbr").text
        except:
            games_count = "Not known"

        tournament = match_cards[i].find("td", class_="match-filler").find("div").find("a")["title"]

        data.append({
            'team_left': team_left,
            'team_right': team_right,
            'score': score,
            'games_count': games_count,
            'tournament': tournament,
        })

    return data


def show_matches():
    matches = get_match_cards()
    result: str = ''

    for match in matches:
        result += f"""
{match.get('team_left')} {match.get('score')} {match.get('team_right')}
( {match.get('games_count')} ) {match.get('tournament')}
        """

    return result
