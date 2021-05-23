import operator
import speech_recognition as sr
print("Speech Recognition Current Version is : "+ sr.__version__)

r = sr.Recognizer()

# device_index = 1 -> Headset (OnePlus Bullets Wireless)
my_mic_device = sr.Microphone( device_index = 1)
with my_mic_device as source:
	print("Say what you want to calculate.[Like 3 plus 3]  -> ")

	#  below command reduces the noise
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source)
	my_string = r.recognize_google(audio)

try:
    print("Google Speech Recognition thinks you said - " + my_string)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Add Pocket Sphinx module
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(my_string))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

def know_the_operator(op):
	return{
	'+' : operator.add,
	'-' : operator.sub,
	'*' : operator.mul,
	'divided' : operator.__truediv__,
	'by' : operator.__truediv__,
	'mod' : operator.mod,
	'Mod' : operator.mod,
	'^' : operator.xor,

	}[op]

def expression_val(op1, oper, op2):
	op1, op2 = int(op1), int(op2)
	return know_the_operator(oper)(op1, op2)

print(expression_val(*(my_string.split())))
