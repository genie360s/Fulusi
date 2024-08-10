## About Fulusi 📈

Fulusi is a project that aims to build financial awareness on the Tanzania Finance Market with focus on Bank Forex Exchange rates , Stock Markets ( Dar es Salaam Stock Market ), Government Mutual Funds ( UTT AMIS ), Watumishi Housing Fund , Government Bonds and Corporate Bonds. Ideally an information platform that provides live data , shows trend on the growth of foreign currencies , stocks and mutual funds to help Tanzanian citizens to invest.

## The Why 🤔💭?

According to the recent Tanzania CENSUS survey , 1% of Tanzanians invest in the stock market compared to 4% in Kenya , the rate is similar in other investment instruments including bonds , mutual funds and foreign exchanges. I believe with this platfom citizens can get live data and monitor how different instruments perform and invest. 

## The Roadmap 🛣️
- [x] Collecting Live Data
- [x] Building the UI and UX of the platform
- [x] Implementing User Authentication
- [x] visualizing data collected in table format
- [x] Design database to store all scrapped data
- [x] Design APIs to retrieve data from the database
- [x] Collecting and storing data in a database.
- [ ] Visualize growth across time (Will need collection for atleast 3 months) 
- [x] Able to compare forex prices in banks and suggest the cheapest bank to do exchange.
- [ ] Predict how the investment instruments will perform though machine learning models.
- [ ] Chatbot that will use both native language swahili and english to provide updates.

## How to get started 🚀!

## Prerequisites
- Python > 3.5
- pip latest version
- git 

### NB
- The project is built on Linux Kernel | Ubuntu OS ( 24.04 )

## Steps

1. Clone the repository
```bash
git clone https://github.com/genie360s/findailyupdates
```
2. Create a virtual environment
```bash
python3 -m venv .venv
```
3. Activate the virtual environment
```bash
source .venv/bin/activate
```
4. Install python packages from ```requirements.txt```
```bash
pip install -r requirements.txt
```
@todo: db setup
5. Create the user table
```bash
flask --app flaskr init-db
```
6. Run the Flask development server, with debug option
```bash
flask --app flaskr run --debug
```
7. Hooray 🚀 ! Now you are ready to start contributing.

> Created By: Alex Mkwizu @genie360s

