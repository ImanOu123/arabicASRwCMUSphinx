#!/usr/bin/env python3
"""
Recognize a single utterance from a WAV file.

Supporting other file types is left as an exercise to the reader.
"""

# MIT license (c) 2022, see LICENSE for more information.
# Author: David Huggins-Daines <dhdaines@gmail.com>

from pocketsphinx import Decoder
import argparse
import wave

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("audio", help="Audio file to recognize")
args = parser.parse_args()
with wave.open(args.audio, "rb") as audio:
    decoder = Decoder(hmm="an4/model_parameters/an4.cd_cont_200", dict="an4/etc/an4.dic", lm="an4/etc/an4.lm", samprate=audio.getframerate())
    # decoder = Decoder(samprate=audio.getframerate()) # using default acoustic model/dictionary/language model
    decoder.start_utt()
    decoder.process_raw(audio.getfp().read(), full_utt=True)
    decoder.end_utt()
    print(decoder.hyp().hypstr)
