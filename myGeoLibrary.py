import matplotlib.pyplot as plt

class baseMap():
    def __init__(self):
        self.projection = 'EPSG:26920' # NAD83 / UTM zone 20N
        self.baseImage = 'baseImage2.png'
        self.oxUTM = 200000
        self.oyUTM = 4700000
        self.widthUTM = 600000
        self.heightUTM = 600000
        self.prepareBasemap()

    def prepareBasemap(self):
        self.baseImageArray = plt.imread(self.baseImage)
        self.widthImage = self.baseImageArray.shape[0]
        self.heightImage = self.baseImageArray.shape[1]
        plt.imshow(self.baseImageArray)

class showBasemap(baseMap):
    def __init__(self):
        baseMap()
        plt.show()

class showUTM(baseMap):
    def __init__(self,xUTM=334000, yUTM=4970000):
        super().__init__()
        self.plotUTM(xUTM,yUTM)
        plt.show()

    def plotUTM(self,xUTM,yUTM):
        rxUTM = xUTM - self.oxUTM
        ryUTM = yUTM - self.oyUTM
        rxUTM = (rxUTM/self.widthUTM)*self.widthImage
        ryUTM = (1-(ryUTM/self.heightUTM))*self.heightImage
        plt.scatter(rxUTM,ryUTM)



