# Multimodal-Emotion-Recognition-on-RAVDESS-dataset
Emotion recognition is a topical area that is attracting the attention of many researchers, and which always poses a challenge, in view of the complexity of the data collected. In these notebooks, we have proposed an emotion recognition system on bimodal data for human emotions using the database RAVDESS. The system focuses on the classification of eight basic emotions (happiness, neutrality, calm, sadness, anger, fear, disgust and surprise). We start with
extract the face data, then the voice features, and after integrating them into the multimodal fusion approach, we implement several algorithms
for classification.

## Speech Emotion Recognition:
We will now describe the method of extracting the characteristics of the
speech from a set of audio data: For the recognition of emotions,
we used a deep neural network that was trained from scratch. All
of the SER system is presented in sections:
1. Voice signal data enters the signal pre-processing block. the
signal preprocessing cuts long data based on 3 seconds and
sets the short data to zero.
2. Data enters the feature extraction block after preprocessing. The feature extraction block converts the speech signal into a
spectrogram, then into a Mel scale.
3. Next comes the conversion to logarithmic scale, which is performed with the Librosa library [50].
4. Finally, the logarithmic spectrogram is converted into an image.

![alt text](https://github.com/RosRed/Multimodal-Emotion-Recognition-on-RAVDESS-dataset/blob/main/img/proc_audio.png)

## Facial Emotion Recognition:

##Results Fusion

