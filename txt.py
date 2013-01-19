from flask import Flask, session, request, url_for, render_template, redirect
from twilio.rest import TwilioRestClient 
import twilio.twiml
from wordnik import *
import time, json, urllib2

app = Flask(__name__)
app.secret_key = SECRET_KEY

#twilio auth
ACCOUNT_SID = TWILIO_SID
AUTH_TOKEN = TWILIO_TOKEN
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

global ar #the variable which will have the random words

@app.route('/', methods=['GET', 'POST'])
def home():
	#create an array to send with three random words from wordnik
	ar = []
	while len(ar) < 3:
		url = 'http://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&minDictionaryCount=10&maxLength=6&minLength=3&api_key=WORDNIK_API_KEY'
		rtrn = urllib2.urlopen(url)
		src = json.load(rtrn)
		ar.append(src['word'])
	

	if request.method == 'POST':
		try:
			message = client.sms.messages.create(to='+1'+request.form['number-form'], from_="TWILIO_SEND_NUMBER",
	                                     body=ar[0]+" "+ar[1]+" "+ar[2])
			session['words'] = ar[0]+" "+ar[1]+" "+ar[2]
			session['number_temp'] = '+1'+request.form['number-form'] #temporary number to store locally, which will help to track the progress of authentication.
			return redirect(url_for('auth'))
		except Exception as e: #if the sms could not be sent, display that there was an error.
			return render_template('index.html', note=True)	
	return render_template('index.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
	#first make sure that they are not already signed in
	if 'number_signed_in' in session:
		return redirect(url_for('home'))

	if request.method == 'POST':
		if request.form['veri-form'] == session['words']:
			session.pop('words', None) #get rid of words from session
			session['number_signed_in'] = session['number_temp']#declare logged in
			session.pop('number_temp', None) #get rid of temp from session

			return redirect(url_for('result'))
	return render_template('auth.html')	
@app.route('/result')
def result():
	return render_template('confirm.html')

@app.route('/logout')
def logout():
	session.pop('number_signed_in', None) #get rid of signed_in from session
	return redirect(url_for('home'))			

if __name__ == '__main__':
	app.run()		