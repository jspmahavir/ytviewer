import fetch from 'node-fetch'
import { initialize } from '@phonal-technologies/drafterai-js'

// Init an API with apikey and fetch provider
const accessKey = "prod_bCvHE131/126.v4eDMFgmDRrqaPBhFDa9jdYj"
const drafterApi = initialize(accessKey, { fetch })
const text = "however that\'s the way it goes but here\'s my next question because you said again you you\'ve been stacking on music and  what keeps you or what allows you to continue oh my god to make music good question i hate music i want to eliminate one of your answers don\'t tell me that it\'s for the love because this  ain\'t lovable anymore man it\'s not you know we always in the trenches you more so than us but we always making our music and doing our  right right i don\'t like music anymore right but i\'ve had this talent this ten thousand hours that i gotta use so that\'s why when we freestyle on him all my  is funny or being witty or something i\'m not spitting a real verse i\'m not taking it seriously so you shouldn\'t either yeah but if every now and then we\'ll be like i\'m about to just kill her freeze no i never said don\'t yes i never say that before yeah because we know what we\'re doing exactly we know what we\'re doing but my point is so please please help me to understand what allows you to continue to chug this musical boat on down this  time continue actually it i mean not just now corny that\'s part of that that\'s part of the answer technically it has to be that it has to be the love you ain\'t doing that there\'s levels to it i got this strong ass love hate relationship with music too you got to like isn\'t it a  it\'s so hard to be a fan it is um it\'s so hard not to try to look for and look through the smoke and mirrors these  provide um but for me i i ain\'t gonna lie too i have my times where i think about quitting this  sometimes cause it should get rough it do it\'s not for the week i mean it\'s not for the uh yeah not for the week no it\'s not you know what i\'m saying um but at first it was you being a rapper\'s rapper you too y\'all know at first it was to drop your nuts and show them but that\'s how that what y\'all talking about is the love that has lasted till now yeah i don\'t have it no more right look at look at how y\'all are smiling as we remember these moments it\'s because you when you think about it you go just like you\'re in the middle of you know is an abusive relationship now i see why some women don\'t leave i know right as soon as you\'re getting ready to go and walk out you remember when that  those cheddar bay biscuits i think the more you have your your heart in whatever your art is particularly it\'s gonna you\'re gonna have that strong love-hate relationship you know what i mean i think i don\'t sometimes you want to beat the  ass and sometimes you want to  the  out of them same same energy yeah hey man you just put it in another hole don\'t be around me be upstairs somewhere and let me have my man cave you know what i mean but that was my motivation then now it\'s more so i\'ll hear something that inspires me and even my approach to music is different now because i talk about a lot of different  and so i feel like a lot of the things that i choose to say and some of the subjects i choose to expound on i say them the way i would expect or i would love to hear someone i  with express and say these things to me so that\'s what keeps me moving so you\'re basically making you\'re making the music in the void that you\'re that is missing so you\'re making the music you want to hear yeah even when we were again in the heyday approach the way we approach rap same thing these  can\'t spit like this let me show them the same  it\'s funny that he says that i lit and i never do this i\'m not one of those hey listen to me rap i never send you a clip of me rapping and i sent you a clip of me rapping and i said listen to this and this is how i like for people to rap i\'m not saying it because it\'s specifically me like if someone else rap and i broke down how i like the rhyme pattern to sound and everything and yeah the the the uh the multiple syllable rhymes at the end and i was like this is how like a  rap and then he say the exact same thing he\'s like i remember someone like how i would like to hear about  rap even if it wasn\'t me but that\'s that music nerd  that allows us to keep coming back it\'s like you know like entendres and  like this is that\'s what i love an entendre some people might not even know what the  that is but that\'s a staple if you\'re making like the wraps the way i make them like punch liney type of exciting rap entondres is your friend we have no right right we have no right to even ask him that question when we rap more than he do this is very true but no but here\'s why i could ask the question it\'s for the love is why we do it no it\'s just sadly yes it is sadly for me it\'s almost like it\'s almost like like you know you the one that got away and you kind of want to remind her what she missing it\'s like cuz you love her that\'s right though because it\'s like look listen why would you give a  i\'m not even taking you serious but look what i could do if i did but that is why you do it but i don\'t think that so i guess that\'s the other energy of the love because you know love and hate is very close together so it might be that yeah that\'s the love hate party i hate  music every time i rap on this show like it\'s like i i hate it too much to write bars and give you my own yeah but i love it too much"
// Payload to exeute
const payload = {
  "workflowId": 83,
  "context": {
    "videoUrl": "https://www.youtube.com/watch?v=6eRkpd8LZQ0",
    "vidTranscript": text
  }
}

// Execute request could be async/await
;(async () => {
  const [queuedExecution] = await drafterApi.workflowExecutions.create(payload)
  console.log('queuedExecution', queuedExecution)

  const intervalId = setInterval(async () => {
    const [execution] = await drafterApi.workflowExecutions.find(
      { $limit: 10, '$sort[id]': -1, datagroup: queuedExecution.datagroup },
      { all: true }
    )

    if (['completed', 'failed'].includes(execution.status)) {
      clearInterval(intervalId)
    }

    console.log('execution', execution)
  }, 3000)
})()

