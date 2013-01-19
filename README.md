Thank you for making it this far. I hope this code provides value to you – by all means have at it. 

I detail the process on my blog, http://byzach.tumblr.com. In short, I recently realized first hand the lack of protection a password provides me. Upon making setting a good one, I got an email from the company that I registered with, which contained my password in plain text. I learned that this combination of words, numbers, and characters cannot and will not protect me against someone who wants to access my information.
There seems to be a compromise I made by creating passwords: I either used bad ones so I could remember them, or I made great ones but sat in my inbox looking for a password reset email with frequency. There should not be a compromise in security or performance. 
So I made this little website. The idea is to tie my identity to my phone and authenticate through text messages. Websites need to collect as little as a phone number, and the user needs to remember no secure details. The user will receive a text message containing three random words, which they type into their web browser. It's a total of three steps and there is nothing to forget or other software to sign into. It's secure – as long as you do have your phone – and simple to recreate. 

I wrote the whole backend on Python using the excellent Flask. Beyond that, it uses Twilio to send texts and Wordnik to generate random words. Both of them are easy to replace in the code, but they are also very easy to integrate and are very good services. To use each, you will need freely-obtainable API keys and replace them where appropriate within my code. This includes:

a randomly generated secret key, which allows Flask to securely sign data stored in the session – replace 'SECRET_KEY' in code,
a Twilio SID – replace 'TWILIO_SID' in code,
a Twilio authentication token – replace 'TWILIO_TOKEN' in code,
a Wordnik API key – labeled 'WORDNIK_API_KEY' within the Wordnik URL,
and a number from Twilio to send from that matches your account – replace 'TWILIO_SEND_NUMBER' in the message creation line.

All of the python code is in txt.py. I have tried to leave comments throughout without being overwhelming and all of the formatting has been tested. If you have any questions, the Github repo is at http://github.com/zchr/phonein and the Stackoverflow community has proved incredibly helpful with Flask.

Per Flask's directory organization, the folder 'templates' houses all of the html files. Flask lets you display python variables directly within the html – as well as write 'if' statements and the like. The css file – I kept it simple and linked all of the html files to one stylesheet – is within the 'static' folder. 

This project is under the MIT License. I wrote this for practice and for the sake of executing an idea of mine. I am happy to have gotten it this far, and I hope that the code inspires others to create alternate solutions to address the issue that is passwords. Best of luck and enjoy.

Zach, @zsch 
