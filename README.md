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
For facial emotion recognition, we first extracted the images from the
videos at 30 frames per second, choosing 20 frames from each video (increase
the number or use all the images will make the process more expensive in terms of
calculation), converting them into 720*720 square images from their original size
of 1280*720, then detecting the face using the Dlib library ,
resizing to 48*48, and finally converting them to grayscale.
We used the **LRCN approach**, which combines the CNN and LSTM layers into one
single model. In our case, we used the pre-trained CNN model "Emotion" in
using the weights of the facial expression model, which is implemented in the library
DeepFace.
## Fusion
We merge the information learned from the two modalities via late fusion.
To do this, we retrieved the last fully-connected layers of the two models,
concatenated the feature sets of each modality, then formed a model of
classification.

![alt text](https://github.com/RosRed/Multimodal-Emotion-Recognition-on-RAVDESS-dataset/blob/main/img/late_fusion.png)

1. **model 1**: Considers the facial emotion recognition model.
2. **model 2**: Considers the speech emotion recognition model.

We concatenated the later layers of each model before the SoftMax layer. 
The shape of the vector is 1400 (1000 for speech, 400 for face).
We compared the performance of logistic regression with and without PCA, network
of neurons (NN), SVM.
We implemented the logistic regression algorithm and the SVM using the
sklearn library , for regularization parameter we use Optuna
for hyperparameter optimization.
