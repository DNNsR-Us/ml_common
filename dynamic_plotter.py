import matplotlib.pyplot as plt


class PltDynamicEpoch(object):
    def __init__(self):
        self.figNew=plt.figure(figsize=(8, 6))
        self.figNew.tight_layout()
        self.axNew1 = self.figNew.subplots(1,1)
        self.axNew1.grid(color='GRAY', linestyle='--', linewidth=.5)
        self.axNew1.set_xlabel('Epoch') ; self.axNew1.set_ylabel('Y')
#         self.axNew1.set_xlim(0,30) ; self.axNew1.set_ylim(0,30)
        self.axNew1.set_ylabel("Loss")
        self.axNew2 = self.axNew1.twinx()  # instantiate a second axes that shares the same x-axis
        self.axNew2.set_ylabel("Accuracy %", color='g')
        self.xdata = []
        self.yTrainLosses = []
        self.yTestLosses = []
        self.yAccuracy = []
#         pltDynamicEpoch(self.xdata, self.yTrainLosses, self.yTestLosses, self.yAccuracy, self.axNew1, self.axNew2,'b','r','g')
#         lines, labels = self.axNew1.get_legend_handles_labels()
#         lines2, labels2 =self.axNew2.get_legend_handles_labels()
#         self.axNew2.legend(lines + lines2, labels + labels2, loc='upper center',ncol=3)
    def addData(self,x, y1, y2, y3, color1, color2, color3):
        self.xdata.append(x)
        if(len(self.xdata)==2):
            lines, labels = self.axNew1.get_legend_handles_labels()
            lines2, labels2 =self.axNew2.get_legend_handles_labels()
            self.axNew2.legend(lines + lines2, labels + labels2, loc='upper center',ncol=3)
        self.yTrainLosses.append(y1)
        self.axNew1.plot(self.xdata, self.yTrainLosses, color1, marker='o',mec='BLACK',label='TrainLoss')
        self.yTestLosses.append(y2)
        self.axNew1.plot(self.xdata, self.yTestLosses, color2, marker='v',mec='BLACK',label='TestLoss')
        self.yAccuracy.append(y3)
        self.axNew2.plot(self.xdata, self.yAccuracy, color3, marker='^',mec='BLACK',label='Accuracy')
        self.figNew.canvas.draw()

class PltDynamicBatch(object):
    def __init__(self):
        self.figLossBatch=plt.figure(figsize=(8, 5))
        rows, cols = (30, 64) 
        xDataTrainBatch=[[]]
        xDataTestBatch=[[]]
        yTrainLossesBatch=[[]]
        yTestLossesBatch=[[]]
        self.axLossBatch = figLossBatch.subplots(1,1)
        self.axLossBatch.grid(color='GRAY', linestyle='--', linewidth=.5)
        self.axLossBatch.set_xlabel('Batch') ; axLossBatch.set_ylabel('Y')
        self.axLossBatch.set_xlim(0,len(carsDatasetTrainTrans)/64) ;axLossBatch.set_ylim(0,30)
        self.axLossBatch.set_ylabel("Loss")
        self.axLossBatch.autoscale(enable=True, axis='both', tight=None)
#         pltDynamicBatch(xDataTrainBatch[0],yTrainLossesBatch[0],str(0),axLossBatch,'o',"Train",'b')
#         pltDynamicBatch(xDataTestBatch[0],yTestLossesBatch[0],str(0),axLossBatch,'v',"Test",'r')
        lines, labels = axLossBatch.get_legend_handles_labels()
        self.xLossBatch.legend(lines, labels, loc='upper center',ncol=2)
    def addData(self, x, y1, batchNum,ax1, mark, lab,color1):
        ax1.plot(x, y1, color1, marker=mark,mec='BLACK',label=lab)        
        self.figLossBatch.canvas.draw()
