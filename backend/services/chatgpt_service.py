import os
import openai

def generate_text():
    article = """
    Premier League referee David Coote has been suspended after a video allegedly showing him making derogatory comments about Liverpool and the club's former manager Jurgen Klopp was circulated on social media.
    Refereeing body PGMOL says the suspension comes into force with immediate effect and is pending a full investigation.
    The video, widely shared on social media, has not been verified by the BBC. It is unclear when it was filmed or its authenticity.
    Coote, 42, refereed Liverpool's 2-0 win against Aston Villa on Saturday. He is one of the Premier League’s most-experienced officials and has been refereeing matches in the top flight since 2018.
    The video being shared appears to refer to a Premier League match that Coote officiated between Liverpool and Burnley in July 2020, which finished 1-1.
    Klopp criticised Coote after the match, saying the referee failed to give fouls for challenges made on Liverpool's players.
    Referees are required to inform PGMOL of the club they support.
    Coote, from Nottingham, is registered as a Notts County fan and is therefore unable to officiate County or Nottingham Forest matches.
    PGMOL says it will not be making further comment on the case until its investigation is completed.
    What happened against Burnley?
    With their first Premier League title secured, Liverpool's aims in July 2020 had switched to becoming the first club to win every single home game during the course of the season.
    The Reds were on a 24-match winning run at Anfield, which had given them a 25-point lead over Pep Guardiola's Manchester City.
    In addition, Klopp's side were hoping to become the second team to amass 100 points during a 38-game Premier League season, matching Manchester City's achievement in the 2017-18 campaign.
    Andrew Robertson gave Liverpool the lead against the Clarets before Jay Rodriguez equalised to give the visitors a share of the spoils.
    At full-time, Klopp appeared to argue with Coote and his officials on the pitch.
    "The referee let lots of challenges go so it was clear that if the ball comes into the box it was dangerous. They did what they are good at and I respect that," said Klopp after the match.
    "We were angry with the referee but we have to criticise ourselves first for not finishing the game."
    Liverpool lost their next fixture against Arsenal, which ended their hopes of reaching 100 points.
    """
    openai.api_key = ''
    message = [{"role": "user", "content": "Give me a summary of this article in style of a radio show with two presenters called Adam and Amy having a conversation:" + article}]

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message
    ) 
    reply = chat.choices[0].message.content
    return formatText(reply)

def formatText(gen_text):
    text = gen_text.split("\n\n")
    formatText = []
    for t in text:
        formatText.append(t.rsplit(":", 1)[1].lstrip())
    return formatText


print(generate_text())