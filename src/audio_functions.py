import pyaudio
import wave

import datetime

def sample_audio():

    audio_obj = pyaudio.PyAudio()

    for i in range(audio_obj.get_device_count()):
        print(i, audio_obj.get_device_info_by_index(i).get("name"))

    form_1 = pyaudio.paInt16
    chans = 1
    sampling_rate = 44100  
    chunk = 4096
    record_duration = 5
    device_index = 2    # TODO: check device index corresponds to correct value
    # wav_output_filename = f"static/audio_resutls/sample-{str(datetime.datetime.now())}.wav"
    wav_output_filename = "audio_sample.wav"
    
    audio = pyaudio.PyAudio()
    
    stream = audio.open(format = form_1, rate = sampling_rate, channels=chans,
                        input_device_index = device_index, input=True,
                        frames_per_buffer = chunk)
    
    frames = []
    
    for i in range(0, int((sampling_rate/chunk)*record_duration)):
        data = stream.read(chunk)
        frames.append(data)
        
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    wavefile = wave.open(wav_output_filename, "wb")
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(sampling_rate)
    wavefile.writeframes(b"".join(frames))
    wavefile.close()

    print("file saved!")

if __name__ == "__main__()":
    sample_audio()
    
sample_audio()