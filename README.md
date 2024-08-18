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
- Python > 3.8 👉🏾[How to download and Install Python](https://www.python.org/downloads/)
- pip latest version 👉🏾[Installing Pip lates Version](https://pip.pypa.io/en/stable/installation/)
- git 👉🏾[Download Git](https://git-scm.com/downloads)
- IDE i.e 👉🏾[VS Code](https://code.visualstudio.com/download#)

### NB
- The project is built on Ubuntu OS ( 24.04 ), but can be run on Windows and MacOs

## Steps to get started on Ubuntu 24.04

1. Fork the repository 👉🏾 [Click here to Fork !](https://github.com/genie360s/Fulusi/fork)

2. Clone the forked repository to your machine.

```bash
git clone https://github.com/<github_username>/Fulusi
```

3. Navigate to the parent directory.

```bash
cd Fulusi
```

4. Create a virtual environment.

```bash
python3 -m venv .venv
```

5. Activate the virtual environment

```bash
source .venv/bin/activate
```

6. Install python packages from ```requirements.txt```

```bash
pip install -r requirements.txt
```

7. Install PostgreSQL 👉🏾 [How to Install PostgreSQL](https://www.postgresql.org/download/linux/ubuntu/)

8. Setting up PostgreSQL in Linux 👉🏾[Using PSQL in Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-22-04)

9. Create a new database 👉🏾[Creating a new database with PSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-22-04#step-4-creating-a-new-database)

10. Create the user table

```bash
flask --app flaskr init-db
```

11. Run the Flask development server, with debug option and port option

```bash
flask --app flaskr run --debug --port 8070
```

12. Navigate to the "/api/" directory

```bash
cd api
```

13. Run the API server

``` bash
python3 api.py
```

14. Hooray 🚀 ! Now the Project is ready and running

## How I contribute ?

Please read the [contribution guideline](/CONTRIBUTING.md)

> Created By: Alex Mkwizu @genie360s

