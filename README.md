# Machine Learning app for Fraud Login Detection
*Authors : Marin BOUTHEMY*

This application written with Pygame aims to detect incoherent behavior during the user logging to a website.
Based on the statistics related to user's taste and machine learning trained algorithm, it outputs a probability if 
the user trying to logging is a hacker (bot, fraud...) or not.

This application was developped for a hackathon challenge organized by Société Générale and HSBC in France in 2018.

It won the third prize corresponding to a 3000€ cash prize, you can find the results video
 [here](https://www.youtube.com/watch?v=bmnIbri1EqQ).


## Requirements
The library has some requirements :
 - Python 3
 - Numpy
 - Pandas
 - networkX

To install all this requirement you can use the following:

```
pip install requirements.txt
```

## Utilisation

To run it for the sign up of the user (first connection):

```
python hacking_premiere_connexion.py
```

Then, you can activate it for the user sign in (second connection):

```
python hacking_seconde_connexion.py
```