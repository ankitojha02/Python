# WAP to print twinkle twinkle little star poem using print() function.
# print(''' Twinkle, twinkle, little star,How I wonder what you are!Up above the world so high,Like a diamond in the sky.
#       ''')

# Text to speech conversion using pyttsx3 library
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I am a Python programmer")
engine.runAndWait()
