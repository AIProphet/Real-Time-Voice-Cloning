
## Mel-filterbank parameters
mel_window_length = 25  # In milliseconds
mel_window_step = 10    # In milliseconds
mel_n_channels = 40

# Number of spectrogram frames in a partial utterance
partial_utterance_length = 160  

sampling_rate = 16000

## Voice Activation Detection parameters
# Window size of the VAD. Must be either 10, 20 or 30 milliseconds.
# This sets the granularity of the VAD. Should not need to be changed.
vad_window_length = 30  # In milliseconds
# Number of frames to average together when performing the moving average smoothing.
# The larger this value, the larger the VAD variations must be to not get smoothed out. 
vad_moving_average_width = 8
# Maximum number of consecutive silent frames a segment can have.
vad_max_silence_length = 6

## Model parameters
model_hidden_size = 128
model_embedding_size = 256
model_num_layers = 3

