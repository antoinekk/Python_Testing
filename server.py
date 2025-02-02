import json
from flask import Flask,render_template,request,redirect,flash,url_for

def loadClubs():
    try:
        with open('../../clubs.json') as c:
            listOfClubs = json.load(c)['clubs']
            return listOfClubs
    except:
        with open('clubs.json') as c:
            listOfClubs = json.load(c)['clubs']
            return listOfClubs

def loadCompetitions():
    try:
        with open('../../competitions.json') as comps:
            listOfCompetitions = json.load(comps)['competitions']
            return listOfCompetitions
    except:
        with open('competitions.json') as c:
            listOfClubs = json.load(c)['competitions']
            return listOfClubs

clubs = loadClubs()
competitions = loadCompetitions()

def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = 'something_special'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        try:
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            return render_template('welcome.html',club=club,competitions=competitions)
        except:
            if request.form['email'] == "":
                flash("Field cannot be empty, please enter a valid email.")
            else:
                flash("This is not a valid email. Try again.")
            return render_template('index.html'), 403
    
    @app.route('/clubsPoints')
    def clubsPoints():
        all_clubs = sorted(clubs, key=lambda club: club['name'])
        return render_template('clubs.html', clubs=all_clubs)


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        foundClub = [c for c in clubs if c['name'] == club][0]

        try:

            foundCompetition = [c for c in competitions if c['name'] == competition][0]
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
        
        except IndexError:

            flash("Something went wrong. Please try again.")
            return render_template('welcome.html', club=club, competitions=competitions), 404


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]

        try:

            placesRequired = int(request.form['places'])

            if placesRequired > int(competition['numberOfPlaces']):
                flash("There are not enough places available.")
            
            elif placesRequired > int(club['points']):
                flash("You do not have enough points.")

            elif placesRequired > 12:
                flash("You cannot purchase more than 12 places.")
            
            else:
                competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
                club['points'] = int(club['points']) - placesRequired
                flash("Booking complete!")
                return render_template('welcome.html', club=club, competitions=competitions)

        except ValueError as message:
            flash(message)

        return render_template('welcome.html', club=club, competitions=competitions), 400
        
    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))
    
    return app