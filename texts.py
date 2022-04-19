import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# text = 'stand in tadasana feet parallel lift up the toes and spread them back down onto the mat inhale in and out through the nose lengthen through the fingertips and inhaling gazing up the thumbs and exhaling fold forward at the hips bend your knees here if you need to inhale lengthen through the spine to look up and exhaling forward bend the knees and step the right foot back into a long lunge drop the right knee release the toes coming into a long lunge position looking straight ahead breathing in and out through the nose find one spot to rest your eyes tuck the right toes under step the left back into a long plank draw the lower abdomen in and drop the knees chest and forehead down to the ground tuck the elbows in release the abdomen release the toes and inhale up to bhujangasana drawing the kneecaps up and exhaling forward tuck the toes under press the hips back towards the heels and lift up into adam asana down face dog spread the feet to hip width apart and start treading lightly through the feet just right and left a few times just to warm up the ankles and the knees and settle back down into down  dog inhale step the right foot forward in between the hands release the left knee release the toes and gaze straight ahead  tuck the left toes under step it forward and release the head down  and inhaling reverse the swan dive all the way back up to standing lengthening through the fingertips and exhaling the arms back down by your side and let's go again inhaling the arms up and exhaling forward inhaling lengthen up through the spine to look up and exhaling down and step the left leg back release the knee release the toes gazing forward inhale up to unjani asana pressing the palms of the hands together lengthening up through the fingertips as you exhale dropping into that left hip there exhaling the arms down by the front foot walking your hands back and flexing the front foot rest your eyes on your big toe  when you're ready bend your elbows and sink further deeper into the stretch  inhaling forward walk the hands forward tuck the back toes and step back into plank drop the knees chest and forehead down to the ground keeping the elbows in releasing the abdomen releasing the toes and inhaling up to bojangasana lifting up through the kneecaps exhaling down tuck the back toes press back towards the heels and lifting up to down face bring your feet hip width apart have the heels turned out slightly so they're parallel pressing through the hands and lifting through the sit bones as you exhale gently drawing that lower abdomen back towards the spine and inhaling stepping forward with the left leg releasing the toes and inhaling the arms up to anjani asana  as you inhale lengthening up through the fingertips and as you exhale dropping into that right hip  exhaling the hands down walking the hands back flexing the left toes towards you  lengthening through the crown of the head and then exhaling bending the elbows to come further into the stretch walking the hands forward tuck the back toes under and step forward into uttanasana and inhaling reversing the swan dive all the way back up to standing and exhaling back to tadasana and let's go again inhaling up exhaling forward inhaling lengthening the spine to look up and exhaling down  step the right leg back inhale the arms to anjunasana  if you'd like to take it a little bit deeper start to lift the sternum up to the ceiling and exhaling the arms down tucking the back toes under stepping into plank  and shifting your weight over to the outside of the right foot and extending the left arm towards the ceiling and if you're ready gazing up with the left thumb keep lifting up through that right side waist and keep breathing exhaling the hand back down and swapping over to the other side so coming onto the outside of the left foot extending the right arm up and when you're ready turning your gaze to look at your right thumb  and coming back to plank dropping the knees chest and forehead to the ground releasing the abdomen releasing the toes and inhaling up to bujangasana let's take a variation interlacing the fingers behind you drawing the hands away from the body and lengthening them away down towards your feet keep breathing and exhaling down tucking the toes under pressing the hips back lifting into adam and separating the feet to hip width apart  as you inhale lengthening up through the sit bones and exhaling pressing the chest towards the legs stepping the right foot in between the hands and inhaling up to anjani asana lifting the sternum coming into a slight upper body arch  and exhaling the hands down tuck the back toes under step it forth uttanasana allow the skull to hang forward and inhaling the arms all the way back up and exhaling to tadasana let's scoop down inhaling to ut bringing the arms alongside the ears and when you're ready bring your gaze up in between your hands drawing that lower abdomen in as you exhale bending a bit further down  and exhaling the arms down  and inhaling lengthening the spine to look up and coming back down bending the knees and jumping back to plank  exhaling down and chaturanga dandasana and inhaling up to ul up face dog and exhaling back rolling over the toes into down face dog bring the feet together side by side keeping them parallel and let's inhale the right leg up into three legged dog keep the right leg the right toes pointing down keeping the leg parallel keeping the shoulders square and bend the knee and bring that back down let's inhale the left leg up  pressing out through that left heel as you press away with the hands and bend that leg and bring it back down and come down onto your knees bring the big toes together and sit back on the heels into adam resting warrior lift back up into down dog bring the right knee forward the left knee forward sit to one side unfold the legs in front of you bringing them hip width apart uncurl the spine one vertebra at a time lengthen the legs out in front of you and coming into shavasana palms facing up  feet falling away from each other  then enjoy your rest'
text = 'stand in tadasana'
raw_text = text.lower()


# create mapping of unique chars to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_vocab = len(chars)
# print("Total Characters: ", n_chars)
# print("Total Vocab: ", n_vocab)

# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)
