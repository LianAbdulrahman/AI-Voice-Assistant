from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine
import cohere

# API key injection
co = cohere.Client('api key here')

#text to audio setting
engine = SystemEngine()
stream = TextToAudioStream(engine)

#this to turn speech to text
def process_text(text):
    print(f"entered text: {text}")

    # generate response from chere
    response = co.chat(
        message=text,
        model="command",
        temperature=0.3
    )


    answer = response.text
    print(f"Answer: {answer}")

    # play response in audio
    stream.feed(answer)
    stream.play_async()


if __name__ == '__main__':
    print("Wait until it says 'speak now'")


    recorder = AudioToTextRecorder()

    while True:
        # record and process speech
        recorder.text(process_text)
