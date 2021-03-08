import speech_recognition as spr

reader = spr.Recognizer()
def function_to_read_file(recognizer, audio_file):
    with audio_file as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_file_ = reader.record(source)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        try:
            response["transcription"] = recognizer.recognize_google(audio_file_)

        except spr.RequestError:

            response["success"] = False
            response["error"] = "Ooooopssss!! API Unavailable!"

        except spr.UnknownValueError:
            response["error"] = "unable to recognise"
        
        return response

    

#if __name__=="__main__":
 #   audio_ = input("Please enter the file name\n " )
  #  reader = spr.Recognizer()
   # audio = spr.AudioFile(audio_)

    #result = function_to_read_file(reader, audio)
    #print (result["transcription"])

def transcribing (filename):
    audio_ = filename
    #reader = spr.Recognizer()
    audio = spr.AudioFile(audio_)

    result = function_to_read_file(reader, audio)
    return result

if __name__ == "__main__":
    import sys
    transcribing(int(sys.argv[1]))

    



