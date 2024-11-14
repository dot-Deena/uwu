import speech_recognition as sr
import pyttsx3
import pyaudio

r = sr.Recognizer()
while (True):
         try:
             with sr.Microphone() as mic:
                     r.adjust_for_ambient_noise(mic, duration=2)
   
                     print("say something")
                     audio = r.listen(mic)
       
                     text = r.recognize_sphinx(audio)
                     print(f"what u said: {text}")
                     
         except sr.UnknownValueError:
            print("not working")

         if (text.lower()=="stop"):
               print("exiting")
               break

print("program terminated")
        
        

        
        

    