from os import environ, path
from pocketsphinx import Decoder
from sphinxbase import *


print('a')

model_dir = '/home/wmlab/CMU_try/zh_broadcastnews_ptm256_8000/'
# lm_dir = '/home/wmlab/CMU_try/CMUsphinx-Demo-master/0506.lm'
# dict_dir = '/home/wmlab/CMU_try/CMUsphinx-Demo-master/0506.dic'
lm_dir = '/home/wmlab/CMU_try/try_python/usable_version/0506.lm'
dict_dir = '/home/wmlab/CMU_try/try_python/usable_version/0506.dic'
wav_file = '/home/wmlab/CMU_try/testing_audio/testing003.wav'

speech_rec = Decoder(hmm = model_dir, lm=lm_dir, dict=dict_dir)
wavFile = file(wav_file, 'rb')
wavFile.seek(44)
speech_rec.decode_raw(wavFile)
result = speech_rec.get_hyp()
print(result[0])