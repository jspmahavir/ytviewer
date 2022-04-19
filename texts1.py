import nltk
# nltk.download()

text = "Computers don't speak English. So, we've to learn C, C++, ,C#, Java, Python and the like! Yay!"

# from nltk.tokenize import sent_tokenize
# sentences = sent_tokenize(text)
# print(len(sentences), 'sentences:\n')
# for s in sentences:
#     print(s)

from nltk.tokenize import word_tokenize
words = word_tokenize(text)

# nltk.download('stopwords')
print(words)

# from nltk.corpus import stopwords
# stop_words = set(stopwords.words('english'))
# tokens = [w for w in tokens if not w in stop_words]
# print(tokens)

# from nltk.stem.porter import PorterStemmer
# porter = PorterStemmer()
# stems = []
# for t in tokens:    
#     stems.append(porter.stem(t))
# print(stems)

# pos_tagged_text = nltk.pos_tag(words)
# print(pos_tagged_text)

# for pos_tag_word in pos_tagged_text:
#     print(pos_tag_word[0], ":")
#     nltk.help.upenn_tagset(pos_tag_word[1])


# @app.route('/videocommnet', methods=['POST'])
#     def videocommnet():
#         print("videocommnet")
#         # videoContent = request.json["transcript"]
#         # videoContent = "stand in tadasana feet parallel lift up the toes and spread them back down onto the mat inhale in and out through the nose lengthen through the fingertips and inhaling gazing up the thumbs and exhaling fold forward at the hips bend your knees here if you need to inhale lengthen through the spine to look up and exhaling forward bend the knees and step the right foot back into a long lunge drop the right knee release the toes coming into a long lunge position looking straight ahead breathing in and out through the nose find one spot to rest your eyes tuck the right toes under step the left back into a long plank draw the lower abdomen in and drop the knees chest and forehead down to the ground tuck the elbows in release the abdomen release the toes and inhale up to bhujangasana drawing the kneecaps up and exhaling forward tuck the toes under press the hips back towards the heels and lift up into adam asana down face dog spread the feet to hip width apart and start treading lightly through the feet just right and left a few times just to warm up the ankles and the knees and settle back down into down  dog inhale step the right foot forward in between the hands release the left knee release the toes and gaze straight ahead  tuck the left toes under step it forward and release the head down  and inhaling reverse the swan dive all the way back up to standing lengthening through the fingertips and exhaling the arms back down by your side and let's go again inhaling the arms up and exhaling forward inhaling lengthen up through the spine to look up and exhaling down and step the left leg back release the knee release the toes gazing forward inhale up to unjani asana pressing the palms of the hands together lengthening up through the fingertips as you exhale dropping into that left hip there exhaling the arms down by the front foot walking your hands back and flexing the front foot rest your eyes on your big toe  when you're ready bend your elbows and sink further deeper into the stretch  inhaling forward walk the hands forward tuck the back toes and step back into plank drop the knees chest and forehead down to the ground keeping the elbows in releasing the abdomen releasing the toes and inhaling up to bojangasana lifting up through the kneecaps exhaling down tuck the back toes press back towards the heels and lifting up to down face bring your feet hip width apart have the heels turned out slightly so they're parallel pressing through the hands and lifting through the sit bones as you exhale gently drawing that lower abdomen back towards the spine and inhaling stepping forward with the left leg releasing the toes and inhaling the arms up to anjani asana  as you inhale lengthening up through the fingertips and as you exhale dropping into that right hip  exhaling the hands down walking the hands back flexing the left toes towards you  lengthening through the crown of the head and then exhaling bending the elbows to come further into the stretch walking the hands forward tuck the back toes under and step forward into uttanasana and inhaling reversing the swan dive all the way back up to standing and exhaling back to tadasana and let's go again inhaling up exhaling forward inhaling lengthening the spine to look up and exhaling down  step the right leg back inhale the arms to anjunasana  if you'd like to take it a little bit deeper start to lift the sternum up to the ceiling and exhaling the arms down tucking the back toes under stepping into plank  and shifting your weight over to the outside of the right foot and extending the left arm towards the ceiling and if you're ready gazing up with the left thumb keep lifting up through that right side waist and keep breathing exhaling the hand back down and swapping over to the other side so coming onto the outside of the left foot extending the right arm up and when you're ready turning your gaze to look at your right thumb  and coming back to plank dropping the knees chest and forehead to the ground releasing the abdomen releasing the toes and inhaling up to bujangasana let's take a variation interlacing the fingers behind you drawing the hands away from the body and lengthening them away down towards your feet keep breathing and exhaling down tucking the toes under pressing the hips back lifting into adam and separating the feet to hip width apart  as you inhale lengthening up through the sit bones and exhaling pressing the chest towards the legs stepping the right foot in between the hands and inhaling up to anjani asana lifting the sternum coming into a slight upper body arch  and exhaling the hands down tuck the back toes under step it forth uttanasana allow the skull to hang forward and inhaling the arms all the way back up and exhaling to tadasana let's scoop down inhaling to ut bringing the arms alongside the ears and when you're ready bring your gaze up in between your hands drawing that lower abdomen in as you exhale bending a bit further down  and exhaling the arms down  and inhaling lengthening the spine to look up and coming back down bending the knees and jumping back to plank  exhaling down and chaturanga dandasana and inhaling up to ul up face dog and exhaling back rolling over the toes into down face dog bring the feet together side by side keeping them parallel and let's inhale the right leg up into three legged dog keep the right leg the right toes pointing down keeping the leg parallel keeping the shoulders square and bend the knee and bring that back down let's inhale the left leg up  pressing out through that left heel as you press away with the hands and bend that leg and bring it back down and come down onto your knees bring the big toes together and sit back on the heels into adam resting warrior lift back up into down dog bring the right knee forward the left knee forward sit to one side unfold the legs in front of you bringing them hip width apart uncurl the spine one vertebra at a time lengthen the legs out in front of you and coming into shavasana palms facing up  feet falling away from each other  then enjoy your rest "
#         videoContent = "tadasana"
#         # copyai_url = 'https://www.copy.ai/tools/instagram-caption-generator'
#         # copyai_url = 'https://app.copy.ai/projects/2046419?tool=InstagramCaptions&tab=results'
#         simplified_url = 'https://app.simplified.co/login'
#         options = webdriver.ChromeOptions()
#         options.add_argument('--no-sandbox')
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
#         driver.get(simplified_url)

#         yourEmail = driver.find_element(By.XPATH,'//*[@id ="field-1"]')
#         yourEmail.send_keys("mahavir.ashapura@gmail.com")
#         yourPass = driver.find_element(By.XPATH,'//*[@id ="field-2"]')
#         yourPass.send_keys("Mahavir@123")

#         goButton = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/form/div[4]/button')
#         goButton.click()

#         sleep(5)
#         driver.maximize_window()

#         sleep(1)
#         # AIwriter = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[1]/div/div[2]/nav/ul/li[3]/div/span[2]')
#         # AIwriter.click()

#         sleep(1)

#         # AIWriterDetail = driver.find_element(By.XPATH,'//*[@id="left-tabs-ai--tabpanel-0"]/div/div[2]/div/div[1]/div/div/div/button')
#         # AIWriterDetail.click()

#         documentLink = 'https://app.simplified.co/ai/document/29bd1039-bef2-46dc-81f3-b900ff582cf1'
#         driver.get(documentLink)

#         sleep(2)
#         docContent = driver.find_element(By.XPATH,'//*[@id="scrolling-bounds"]/div[1]/div/div[1]')
#         docContent.clear()
#         docContent.click()
#         docContent.send_keys(videoContent)

#         # docContent1 = driver.find_element(By.XPATH, "//div[@class='ql-editor']")
#         # docContent1.send_keys(videoContent)

#         topic = driver.find_element(By.XPATH,'//input[@name="title"]')
#         tValue  = topic.getAttribute("value")
#         print(tValue)

#         topic.clear()
#         topic.send_keys(Keys.BACKSPACE)
#         topic.send_keys(Keys.chord(Keys.CONTROL,"a",Keys.DELETE))
#         topic.send_keys(videoContent)
        
#         # sleep(5)
#         # generateBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[2]/div/form/button')
#         # generateBtn.click()


#         sleep(5)
        
#         comments = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[2]/div')

#         print(comments)
        
#         for comment in comments:
#             print(comment)

#         # inputOne = driver.find_element(By.XPATH,'//*[@id ="input-one"]')
#         # inputOne.send_keys(videoContent)

#         # inputTwo = driver.find_element(By.XPATH,'//*[@id ="input-two"]')
#         # inputTwo.send_keys(videoContent)
        
#         # createButton = driver.find_element(By.XPATH,'//*[@id ="create-copy-button"]')
#         # createButton.click()
        

#         sleep(100)
        
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         return jsonify(headers)