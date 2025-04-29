#Importing all necessary libraries and files to run the code
from pydub import AudioSegment
from playsound import playsound
import ffprobe
import numpy as np, wave, matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from Help import Helpme
from frequencyClass import FrequencyCalculator
import librosa

#Main Class definition
class GUI(tk.Tk):
    def __init__(self):
# Inheritance with the tkinter class
        super().__init__()
# Code playing the boot chime
        playsound('Mr Audio Jingle.mp3')
# All the tkinter attributes such as buttons and titles, this defines the program GUI
        self.title("Mr Audio")
        self.geometry('1024x380')
        self.titleLabel = tk.Label(self,text='Mr Audio.exe')
        self.titleLabel.pack()
        self.uploadLabel = tk.Label(self,text="Upload a file to enable the programs functionality")
        self.uploadLabel.place(x=1, y=10)
        self.volumeLabel = tk.Label(self,text="Volume Modulator")
        self.volumeLabel.place(x=190,y=240)
        self.pitchLabel = tk.Label(self,text="Pitch Modulator")
        self.pitchLabel.place(x=195,y=75)
        self.uploadButton = tk.Button(self, text='To upload file, click here',width=30,height=1, command=self.UploadAction)
        self.uploadButton.place(x=1, y=35)
        self.freqButton = tk.Button(self,text="Frequency",width=10,height=1,command=self.freqCalculator)
        self.freqButton.place(x=1,y=75)
        self.rateButton = tk.Button(self,text="Rate",width=10,height=1,command=self.rateCalculator)
        self.rateButton.place(x=1,y=100)
        self.bpmButton = tk.Button(self,text="BPM",width=10,height=1,command=self.calculateBPM)
        self.bpmButton.place(x=1,y=125)
        self.cropButton = tk.Button(self,text="Crop",width=10,height=1,command=self.cropSongFile)
        self.cropButton.place(x=1,y=150)
        self.outputLabel = tk.Label(self,text="↓ Outputs from program functions will appear here ↓")
        self.outputLabel.place(x=600,y=10)
        OutputTitle = tk.Label(self,text="↓ Metadata output from program will show below ↓")
        OutputTitle.place(x=600,y=80)
        self.pitchButton = tk.Button(self,text="Pitch",width=10,height=1,command=self.changePitch)
        self.pitchButton.place(x=1,y=175)
        self.metadataButton = tk.Button(self,text="Metadata",width=10,height=1,command=self.MetadataPrint)
        self.metadataButton.place(x=1,y=175)
        self.playButton = tk.Button(self,text="Play",width=10,height=1,command=self.PlayFile)
        self.playButton.place(x=710,y=265)
        self.exitButton = tk.Button(self,text="Exit Program",width=10,height=1,command=exit)
        self.exitButton.place(x=840,y=265)
        self.wait_visibility()
        self.entry = tk.Entry(self)
        self.entry.place(x=500,y=270)
        self.errorOutput = tk.Label(self,text="Errors from program:")
        self.errorOutput.place(x=650,y=300)
# Making the volume slider used to control the volume of the audio file
        self.Volumeslider = tk.Scale(
            self,
            from_=0,
            to=150,
            orient="horizontal",
            length=450,
            tickinterval = 10)
# Making the vertial slider used to change the pitch of the audio 
        self.Volumeslider.place(x=30, y=260)
        self.pitchSlider = tk.Scale(
            self,
            from_=2,
            to=-2,
            orient="vertical",
            length=150,
            tickinterval = 1)
        self.pitchSlider.place(x=130, y=80)
# Calls two functions to make the menu bar
        self.makeMenuBar()
        CodeWanted = self.UploadAction()

#Method to allow user to upload a file to the program
    def UploadAction(self,event=None):
        try:
# Global variable to allow the file to be accessed in any file or method\
            global CodeWanted
# Code used to open the file and document the part of the file identifier that is required to edit it
            UploadedFilename = filedialog.askopenfilename()
            UploadedFilename1 = UploadedFilename.split('/')
            lenUploaded = len(UploadedFilename1)
            CodeWanted = UploadedFilename1[lenUploaded-1]
# This line is used to create the audio file for use in the program, with the correct extensions
            song = AudioSegment.from_mp3(CodeWanted)
            return CodeWanted
        except:
            ErrorPrint = tk.Label(self,text="Inputted file is not an accepted file, please try again")
            ErrorPrint.place(x=650,y=330)
        
# Code to export the file (Menu bar, File, Export)   
    def ExportFile(self,CodeWanted):
        if len(CodeWanted)==0:
            CodeWanted = self.UploadAction()
# This line is used to create the audio file for use in the program, with the correct extensions
        sound = AudioSegment.from_file(CodeWanted)
        sound.export("Output.mp3", format="mp3") 

# Method used to calculate frequency. This method interacts with the Audio class in the other file
    def freqCalculator(self):
        dst = 'test.wav'
# This line is used to create the audio file for use in the program, with the correct extensions
        sound = AudioSegment.from_mp3(CodeWanted)
        sound.export(dst, format="wav")
# Opens the file using the wave library        
        wav_song = wave.open('test.wav','rb')
# Gets the current frame rate of the file
        sample_rate = wav_song.getframerate()
# Calls the  frequency calculator method in the other file linked to the program
        Calc = FrequencyCalculator(sample_rate,"R")
        Calc.maximumFreqCalculator()
        RateValue = tk.Label(self,text=f"Calculated Frequency: {Calc.freqGetter()}")
        RateValue.place(x=600,y=50)

# Public method which is used to calculate the rate from the sample resolution
    def rateCalculator(self):
        dst = 'test.wav'
# This line is used to create the audio file for use in the program, with the correct extensions
        sound = AudioSegment.from_mp3(CodeWanted)
        sound.export(dst, format="wav")
        wav_song = wave.open('test.wav','rb')
        sample_freq = wav_song.getframerate()
        RateValue = tk.Label(self,text=f"Calculated Sample Rate: {sample_freq}")
        RateValue.place(x=800,y=50)

# Public Method used to change the pitch of the audio file
    def changePitch(self):
# This line is used to create the audio file for use in the program, with the correct extensions
        sound = AudioSegment.from_file(CodeWanted, format=CodeWanted[-3:])
# Retrieves the value from the pitch slider in the tkinter interface
        octaves = self.pitchSlider.get()
# Calculating the sample rate using the original rate
        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
# Changes the pitch of the file and 'spawns' a new file in the place of it
        pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        pitch_sound = pitch_sound.set_frame_rate(44100)
# Exports the audio file as a .wav file
        pitch_sound.export(f"octave_{octaves}.wav", format="wav")

# Method used to crop the song file to the length specified by the user using the text entry box on the GUI
    def cropSongFile(self):
# This line is used to create the audio file for use in the program, with the correct extensions
        sound = AudioSegment.from_file(CodeWanted, format=CodeWanted[-3:])
# Deciding the length of the crop and converting the time to seconds - collects data from the entry of the tkinter interface
        try:
            cropLength = int(self.entry.get()) * 1000
            croppedLength = sound[:cropLength]
# Exports the cropped file as a mp3 file to the directory chosen by the user
            croppedLength.export("croppedFile.mp3", format="mp3")
        except:
            RateValue = tk.Label(self,text="This value is not valid to crop the file, please re-enter a value")
            RateValue.place(x=600,y=330)

# Public Method used to output some basic metadata to the user about the inputted file
    def MetadataPrint(self):
        dst = 'test.wav'
# This line is used to create the audio file for use in the program, with the correct extensions
        sound = AudioSegment.from_mp3(CodeWanted)
# Exports the inputted file as a wav file for use in the pydub library
        sound.export(dst, format="wav")
# Opens the audio file
        wav_file = AudioSegment.from_file(file="test.wav", format="wav")
# Creates all the data as tkinter items and places them into the GUI Interface
        RateValue = tk.Label(self,text=f"Rate: {wav_file.frame_rate}")
        RateValue.place(x=600,y=100)
        WidthValue = tk.Label(self,text=f"Width: {wav_file.sample_width}")
        WidthValue.place(x=600,y=120)
        MaxValue = tk.Label(self,text=f"Max: {wav_file.max}")
        MaxValue.place(x=600,y=140)
        LengthValue = tk.Label(self,text=f"Length: {len(wav_file)}")
        LengthValue.place(x=600,y=160)  

# Method to create a graph for the signal of the file
    def signalGraph(self):
# Opens the audio file
        dst = 'test.wav'
# This line is used to create the audio file for use in the program, with the correct extensions
        sound = AudioSegment.from_mp3(CodeWanted)
        sound.export(dst, format="wav")
# Opens the file using the wave library        
        wav_obj = wave.open('test.wav','rb')
# Uses the wave module to get a framerate and calculate the number of frames
        sample_freq = wav_obj.getframerate()
        n_samples = wav_obj.getnframes()
        time = n_samples/sample_freq
# Retrieving number of channels from wave library
        n_channels = wav_obj.getnchannels()
        signal_wave = wav_obj.readframes(n_samples)
        signal_array = np.frombuffer(signal_wave,dtype=np.int16)
# Using two arrays to store signals for the right and left channels of the audio
        r_channel = signal_array[1::2]
        l_channel = signal_array[0::2]
        times = np.linspace(0, n_samples/sample_freq, num=n_samples)
# Using matplotlib to plot the graphs for both the channels
        plt.figure(figsize=(15,5))
        plt.plot(times,l_channel)
        plt.title('L Channel')
        plt.ylabel('Signal Value')
        plt.xlabel('Time (s)')
        plt.xlim(0, time)
        plt.show()
        plt.figure(figsize=(15,5))
        plt.plot(times,r_channel)
        plt.title('R Channel')
        plt.ylabel('Signal Value')
        plt.xlabel('Time (s)')
        plt.xlim(0, time)
        plt.show()

# Module that uses similar functions to the above library, except to make a frequency graph
    def frequencyGraph(self):
# Opens the audio file using wave library
        dst = 'test.wav'
# This line is used to create the audio file for use in the program, with the correct extensions
        sound = AudioSegment.from_mp3(CodeWanted)
        sound.export(dst, format="wav")
# Opens the file using the wave library        
        wav_obj = wave.open('test.wav','rb')
# Uses a part of the library to get the frame rate and number of frames, then works out the time
        sample_freq = wav_obj.getframerate()
        n_samples = wav_obj.getnframes()
        time = n_samples/sample_freq
        n_channels = wav_obj.getnchannels()
        signal_wave = wav_obj.readframes(n_samples)
        signal_array = np.frombuffer(signal_wave,dtype=np.int16)
# Plots the graphs using matplotlib and arrays to show signal
        r_channel = signal_array[1::2]
        l_channel = signal_array[0::2]
        times = np.linspace(0, n_samples/sample_freq, num=n_samples)
        plt.figure(figsize=(15, 5))
        plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
        plt.title('Left Channel')
        plt.ylabel('Frequency (Hz)')
        plt.xlabel('Time (s)')
        plt.xlim(0, time)
        plt.colorbar()
        plt.show()
        plt.figure(figsize=(15, 5))
        plt.specgram(r_channel, Fs=sample_freq, vmin=-20, vmax=50)
        plt.title('Right Channel')
        plt.ylabel('Frequency (Hz)')
        plt.xlabel('Time (s)')
        plt.xlim(0, time)
        plt.colorbar()
        plt.show()

# Module to open the new window for the prorgam
    def openNewWindow(self):
# Creates a new Tkinter space with dimensions 1024 pixels by 100 pixels
        root2 = tk.Tk()
        root2.geometry("1024x100")
        label = tk.Label(text="Mr Audio", background="#ffffff")
        label.pack()
        uploadButton = tk.Button(root2, text='To upload file, click here',width=30,height=1, command=self.UploadAction)
        uploadButton.pack(side="left", padx=1, pady=1)
        entry1 = tk.Entry(root2) 
        Text(root2, height=5, width=10)
        self.makeMenuBar()

# The following two modules are used to change the volume of the audio file and export them to a new wav file
    def VolumeChanger10(self):
        if CodeWanted[-3:] == 'wav':
            file = AudioSegment.from_wav(CodeWanted)
            file = file - 10
            file.export("ChangedVolume-10.wav", "wav")
        elif CodeWanted[-3:] == 'mp3':
            file = AudioSegment.from_mp3(CodeWanted)
            file = file - 10
            file.export("ChangedVolume-10.mp3", "mp3")
        else:
            print('Invalid File Extension')
            
    def VolumeChangerCustom(self):
        changeVal =self.Volumeslider.get()
        if CodeWanted[-3:] == 'wav':
            file = AudioSegment.from_wav(CodeWanted)
            file = file - int(changeVal)
            file.export("ChangedVolumeCustom.wav", "wav")
        elif CodeWanted[-3:] == 'mp3':
            file = AudioSegment.from_mp3(CodeWanted)
            file = file - int(changeVal)
            file.export("ChangedVolumeCustom.mp3", "mp3")
        else:
            print('Invalid File Extension')

# This library uses the python libary of librosa to load the audio file and calculate a BPM for the file and output it to the user
# The output is made into a tkinter label to output to the user
    def calculateBPM(self):
        soundFile = librosa.load(CodeWanted)
        waveform,sampleRate = soundFile
        tempoReading, frames = librosa.beat.beat_track(y=waveform,sr=sampleRate)
        bpm_label = tk.Label(self,text = "Tempo: {:.2f} BPM".format(tempoReading))
        bpm_label.place(x=600,y=30)

# A short module that is used for the play audio file function, it uses the playsound library to play the audio file
    def PlayFile(self):
        playsound(CodeWanted)

# This method is used to create a new tkinter window that has the dimenstions 1024x100.
# It then outputs the help menu that is defined in the help class in the subfile of the program
    def helpMenu(self):
        root2 = tk.Tk()
        root2.geometry("1024x100")
        label = tk.Label(root2,text="Mr Audio", background="#ffffff")
        label.pack()
        test = Helpme()
        helpMenu = tk.Label(root2,text=test.helpMenu())
        helpMenu.pack()

# This method is very similar to the above module and is used to open a new tkinter window and output the about menu to the user
    def aboutThisProgram(self):
        root2 = tk.Tk()
        root2.geometry("1024x100")
        help = Helpme()
        label = tk.Label(root2,text="Mr Audio", background="#ffffff")
        label.pack()
        aboutMenu = tk.Label(root2,text=help.aboutThisProgram())
        aboutMenu.pack()

# This method is used alongside the tkinter interface to create and manage the menu bar at the top, defining what each button does and the text on the button        
    def makeMenuBar(self):
        menubar = Menu(self)
# Defining one subsection of the menu
        filemenu = Menu(menubar, tearoff=0)
# Defining One of the menu items and its command linked to it
        filemenu.add_command(label="New", command=self.openNewWindow)
        filemenu.add_command(label="Open", command=self.UploadAction)
        filemenu.add_command(label="Export", command=lambda:self.ExportFile(CodeWanted))
        filemenu.add_command(label="Play", command=self.PlayFile)
# Adds a separator to the menu ( A Blank line ---------- )
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
# Adds and enables the menubar section called File
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Pitch", command=self.changePitch)
        editmenu.add_command(label="Crop", command=self.cropSongFile)
        editmenu.add_separator()
        editmenu.add_command(label="Volume -10db", command=self.VolumeChanger10)
        editmenu.add_command(label="Volume Changer Custom", command=self.VolumeChangerCustom)
        menubar.add_cascade(label="Edit",menu=editmenu)

        infomenu = Menu(menubar,tearoff=0)
        infomenu.add_command(label="BPM Calculator", command=self.calculateBPM)
        infomenu.add_command(label="Metadata Output", command=self.MetadataPrint)
        menubar.add_cascade(label="Info",menu=infomenu)

        freqmenu = Menu(menubar, tearoff=0)
        freqmenu.add_command(label="Frequency Calculate", command=self.freqCalculator)
        freqmenu.add_command(label="Rate Calculate", command=self.rateCalculator)
        menubar.add_cascade(label="Freqency/Rate Calculator", menu=freqmenu)
    
        windowmenu = Menu(menubar, tearoff=0)
        windowmenu.add_command(label="New", command=self.openNewWindow)
        windowmenu.add_command(label="Signal Graph Plotter", command=self.signalGraph)
        windowmenu.add_command(label="Frequency Graph Plotter", command=self.frequencyGraph)
        menubar.add_cascade(label="Window", menu=windowmenu)
    
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.helpMenu)
        helpmenu.add_command(label="About...", command=self.aboutThisProgram)
        menubar.add_cascade(label="Help", menu=helpmenu)

# Creates the menubar object in the tkinter interface
        self.config(menu=menubar)
