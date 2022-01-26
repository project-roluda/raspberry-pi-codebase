import pyaudio 
import numpy as np
import librosa
import wave
from src.config import config_obj

def sample_audio(record_duration=1):

    audio_obj = pyaudio.PyAudio()

    for i in range(audio_obj.get_device_count()):
        print(i, audio_obj.get_device_info_by_index(i).get("name"))

    form_1 = pyaudio.paInt16
    chans = 1
    sampling_rate = 44100  
    chunk = 4096
    record_duration = record_duration
    device_index = 2    

    return_dict = {}
    
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

    print(type(frames))
    
    # archived, but keeping here just in case
    return_dict["channel"] = chans 
    return_dict["sample_width"] = audio.get_sample_size(form_1)
    return_dict["frame_rate"] = sampling_rate
    return_dict["frames"] = frames

    # saving file...
    wav_output_filename = "src/audio_sample.wav"
    wavefile = wave.open(wav_output_filename, "wb")
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(sampling_rate)
    wavefile.writeframes(b"".join(frames))
    wavefile.close()

    # calculate avg coefficients
    sound, sr = librosa.load(wav_output_filename)
    initial_coeff = librosa.feature.mfcc(y=sound, sr=sr, n_mfcc=100)
    avg_initial_coeff = np.mean(initial_coeff, axis=1)

    config_obj.audio_return_dict = return_dict
    config_obj.avg_initial_coeff = avg_initial_coeff
