from collections import defaultdict
import os
import pandas as pd

classes_list = [
  ['full-AV', 'video-only','audio-only'],
  ['speech', 'song'],
  ['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised'],
  ['normal', 'strong'],
  ["Kids are talking by the door", "Dogs are sitting by the door"],
  ['1st repetition', '2nd repetition'],
  ["male", "female"],
]
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = defaultdict(list)
    for entry in listOfFile:
        file = os.listdir(dirName+'/'+entry)
        allFiles[entry]=file
                
    return allFiles
def load_RAVDESinfo(data_dir, list_classes, X=None, Y=None):
  """
  this function will return audio file PATH and labels seperately when data directory(`data_dir`) 
  and the class list(list_classes) are passed to it
  """
  audio_dataset = list()

  if not(X or Y):
    X = list()
    Y = list()
  actors = [dir for dir in os.listdir(data_dir) if dir.startswith('Actor_')]
  for dir in actors:
    act_dir = os.path.join(data_dir,dir)
    for wav in os.listdir(act_dir):
      # getting labels form the encoded file names
      label = [(int(i)-1) for i in wav.split('.')[0].split('-')]
      # converting gender labels to only 0 and 1
      label[-1] = 1 if label[-1]%2 else 0

      l_text = []

      # converting labels back to string
      for i in range(0, len(label)):
        l_text.append(list_classes[i][label[i]])
        

      X.append(os.path.join(act_dir, wav)) 
      Y.append(l_text)
  
  return X,Y
def getdata(video_folder:str):
  video_info=load_RAVDESinfo(video_folder,classes_list)
  label_headers = ['Audio_file', 'modality', 'vocal_channel', 'emotion', 'emotional_intensity', 'statement', 'repetition', 'gender']
  df_=defaultdict(list)
  df_[label_headers[0]]=video_info[0]
  for j,label in enumerate(label_headers[1:],0):
    df_[label]=[i[j] for i in video_info[1]]

  return pd.DataFrame(df_) 
