class FrequencyCalculator:
    def __init__(self,inputVal,rateOrFreq):
        if rateOrFreq.upper() == "R":
                self.SampleRate = inputVal
        else:
                self.MaximumFreq  = inputVal

    def sampleRateCalculator(self):
        self.SampleRateCalc = self.MaximumFreq * 2
        #print(self.SampleRateCalc)
        return self.SampleRateCalc

    def maximumFreqCalculator(self):
        self.MaximumFreqCalc = self.SampleRate / 2
        #print(self.MaximumFreqCalc)
        return self.MaximumFreqCalc

    def freqGetter(self):
        return self.MaximumFreqCalc

    def rateGetter(self):
        return self.SampleRateCalc

