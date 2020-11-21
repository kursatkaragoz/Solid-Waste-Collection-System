from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QInputDialog, QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot, QTime
from PyQt5.QtGui import QColor
import pandas as pd
from KatiAtikToplamaDesign import MyGUI   #Design Import
import random
from datetime import datetime, timedelta

class System:
    def __init__(self, name: None, totalTruckCount: int, totalPersonelCount: int, shiftCount: int):
        self.__name = name or 'GOP'
        self.__totalTruckCount = totalTruckCount
        self.__totalPersonelCount = totalPersonelCount
        self.__shiftCount = shiftCount
        self.__truckList = []
        self.__districtList = []
        self.__streetCountList = []

    def getName(self):
        return self.__name

    def getTotalTruckCount(self):
        return self.__totalTruckCount

    def getTotalPersonelCount(self):
        return self.__totalPersonelCount

    def getShiftCount(self):
        return self.__shiftCount

    def getDistrictList(self):
        return self.__districtList

    def getStreetCountList(self):
        return self.__streetCountList

    def getTruckList(self):
        return self.__truckList

    def setName(self, new_name):
        self.__name = new_name

    def setTotalTruckCount(self, new_count):
        self.__totalTruckCount = new_count

    def setTotalPersonelCount(self, new_count):
        self.__totalPersonelCount = new_count

    def setShiftCount(self, new_count):
        self.__shiftCount = new_count

    def setDistrictList(self, new_list):
        self.__districtList = new_list

    def setStreetCountList(self, new_list):
        self.__streetCountList = new_list

    def setTruckList(self, new_list):
        self.__truckList = new_list

    def calculateTime(self, time1, second):
        time1 = datetime.strptime(time1, '%H:%M:%S')
        result = time1 + timedelta(seconds=second)

        return str(result.time())

    def shiftStart(self, shift: object, shiftId):
        # print("{}. Vardiya Başladı, Saat: {}".format(shiftId, shift.getStartTime()))
        message = "{}. Vardiya Başladı, Saat: {}".format(shiftId, shift.getStartTime())
        return message

    def calculateCleaningTime(self, personelCount, weatherCondition):

        # Hava durumu (15-20) beklenen durumdur. Kat sayısı = 1
        #             (21-30) her konteyner için 10sn gecikme
        #             (31-40) her konteyner için 20sn gecikme
        #             (1,14) her konteyner için 10 sn gecikme
        #             (0,-10) her konteyner için 20 sn gecikme
        # ------------------------------------------------------------
        # 2+1 (1 söför) işçi varsa 1 konteyner %100 performans = 2dk
        # 3+1           işci varsa 1 konteyner %150 performans = 1.5 dk
        # 4+1           işçi varsa 1 konteyner %200 performans = 1dk
        if personelCount == 3:
            cleaningTime = 120   # sn
        if personelCount == 4:
            cleaningTime = 90    # sn
        else:
            cleaningTime = 60    # sn

        if (weatherCondition > 15) and (weatherCondition < 20):
            cleaningTime = cleaningTime
        if (weatherCondition > 21) and (weatherCondition < 30):
            cleaningTime += 10
        if (weatherCondition > 31) and (weatherCondition < 40):
            cleaningTime += 20
        if (weatherCondition > 1) and (weatherCondition < 14):
            cleaningTime += 10
        if (weatherCondition > -14) and (weatherCondition < 0):
            cleaningTime += 20

        return cleaningTime  # return seconds, sn

    def sendTheTruck(self, target: object, time: str, personelCount: int, shift: object):
        found = False
        for arac in self.__truckList: # dizi, array
            if arac.getState() == "pasif": # araç müsait
                found = True  #arac bulundu
                arac.setState('active')
                self.setTotalPersonelCount(self.getTotalPersonelCount() - personelCount)
             #  print("{} plakalı araç, {} bölgesinde ,{} saat'inde harekete başladı."
             #         .format(arac.getPlate(), target.getName(), time))
                message = "{} plakalı araç, {} bölgesinde ,{} saat'inde harekete başladı.".format(arac.getPlate(), target.getName(), time)

                break
        if found == False: # araç bulunamadı
             # print("Garajda Yeterli Araç Yok")
            message = "Garajda Yeterli Araç yok"

        return message, arac

    def streetDelay(self,transTime, traffic):
        # default sokağa geliş süresi 1dk,  %50 trafikde 1.5dk'da sokağa ulaşım sağlanır.
        # Sokağa geliş süresi * trafik yoğunluğu(0,100)
        transCost = transTime + (transTime * traffic / 100)    # integer veri döner
        transCost = timedelta(minutes=transCost) # TİME türünde veriye dönüştürür

        return transCost.seconds


class Shift:
    def __init__(self, startTime: str):
        self.__startTime = startTime

        # Çalışan kamyonların toplam çalışma saati
        self.__finishTruckTime = []
        # Kapasitesi dolmuş, boşaltıma gitmiş araçlar
        self.fullTruckList = []
        self.fullTruckTimeList = []

        # State Tablosu için kullanılacak değişkenler
        # vardiyada, her mahalleden toplanan çöp ağırlıkları

        self.startTimes = []
        self.truckNames = []
        self.districtNames = []
        self.streetNames = []
        self.collectedGarbages = []
        self.totalCollectedGarbages = []
        self.serviceTimes = []
        self.totalServiceTimes = []
        self.finishTimes = []
        self.personelCountList = []
        self.workedTruck = []
        self.delayTraffic = []
        self.containerCounts = []




    def getStartTime(self):
        return self.__startTime

    def getPersonelCount(self):
        return self.__ShiftpersonelCount

    def getFinishTruckTime(self):
        return self.__finishTruckTime

    def setStartTime(self, new_time):
        self.__startTime = new_time

    def setPersonelCount(self, new_count):
        self.__ShiftpersonelCount = new_count

    def setFinishTruckTime(self, new_time):
        self.__finishTruckTime = new_time


class District:
    def __init__(self, name: str, streetCount: int):
        self.__name = name
        self.__streetCount = streetCount
        self.__streetList = []
        self.currentTime = ""

    def getStreetList(self):
        return self.__streetList

    def setStreetList(self, streetList: None):
        self.__streetList = streetList or []

    def getName(self):
        return self.__name

    def getStreetCount(self):
        return self.__streetCount

    def setName(self, new_name):
        self.__name = new_name

    def setStreetCount(self, new_count):
        self.__streetCount = new_count

    def addStreet(self, street: object):
        self.__streetList.append(street)


class Street:
    def __init__(self, name: str, containerCount: int, transTime: int):
        self.__name = name
        self.__containerCount = containerCount
        self.__trans_time = transTime or 1
        self.__containerList = []

    def getName(self):
        return self.__name

    def getContainerCount(self):
        return self.__containerCount

    def getTransTime(self):
        return self.__trans_time

    def setName(self, new_name):
        self.__name = new_name

    def setContainerCount(self, new_count):
        self.__containerCount = new_count

    def setTransTime(self, new_time):
        self.__trans_time = new_time

    def getContainerList(self):
        return self.__containerList

    def addContainer(self, container: object):
        self.__containerList.append(container)


class Container:
    def __init__(self, containerId: str, containerWeight: float):
        self.__containerId = containerId
        self.__containerWeight = containerWeight

    def getContainerId(self):
        return self.__containerId

    def getContainerWeight(self):
        return self.__containerWeight

    def setContainerId(self, new_id):
        self.__containerId = new_id

    def setContainerWeight(self, new_weight):
        self.__containerWeight = new_weight



class Truck:
    def __init__(self, plate: str, capacity: float):
        self.__plate = plate
        self.__capacity = capacity
        self.__state = "pasif"

    def getPlate(self):
        return self.__plate

    def getCapacity(self):
        return self.__capacity

    def getState(self):
        return self.__state

    def setPlate(self, newPlate):
        self.__plate = newPlate

    def setCapacity(self, newCapacity):
        self.__capacity = newCapacity

    def setState(self, new_state):
        self.__state = new_state

    def collectGarbage(self, system:object, shift: object, truck: object, street: object, container: object, time):

        if container.getContainerWeight() <= self.getCapacity():
            self.setCapacity(self.getCapacity() - container.getContainerWeight())
            message = "{}' in {}. konteyner'i toplandı, Araç Kapasite: {} saat: {} ".format(street.getName(), int(container.getContainerId())+1,self.getCapacity(), time)
            return message, True
        else:
            # print("{} plakalı aracın kapasitesi doldu, {} saat'inde boşaltım için yola çıktı".format(truck.getPlate(), time))
            message = "{} plakalı aracın kapasitesi doldu, {} saat'inde boşaltım için yola çıktı".format(truck.getPlate(), time)
            shift.fullTruckList.append(truck)
            shift.fullTruckTimeList.append(time)
            _, arac = system.sendTheTruck(street, time, random.randint(3, 5), shift)
            return message, arac


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = MyGUI()
        self.gui.setupUi(self)
        self.gui.dataImportButton.triggered.connect(self.openFileNameDialog)
        #self.gui.actionNEW.triggered.connect(self.deneme)
        self.gui.startButton.clicked.connect(self.algorithmRun)
        self.gui.selectShiftCombo.currentIndexChanged.connect(self.selectedShiftDisplay)

        # Aşağıdaki Kodların tamamlı, işlemleri enter key ile tamamlayabilmek için (her entry'E enter özelliği veriliyor)
        self.gui.truckEntry.returnPressed.connect(self.algorithmRun)
        self.gui.personelEntry.returnPressed.connect(self.algorithmRun)
        self.gui.districtEntry.returnPressed.connect(self.algorithmRun)
        self.gui.streetEntry.returnPressed.connect(self.algorithmRun)
        self.gui.shiftEntry.returnPressed.connect(self.algorithmRun)
        self.gui.containerEntry.returnPressed.connect(self.algorithmRun)
        self.gui.weatherEntry.returnPressed.connect(self.algorithmRun)
        self.gui.trafficEntry.returnPressed.connect(self.algorithmRun)

    @pyqtSlot()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Verilerinin Kayıtlı Oldğu, Excel tablosunu Seç", "C:/Users/Kürşad/Desktop/pyqt5","All Files (*);;Xlsx Files (*.xlsx)", options=options)
        if '.xlsx' not in fileName:    #Eğer dosya adında .xlsx yok ise yanlış dosya seçilmiştir.
            print("Seçim yapılmadı")
        else:
            #Read Excel
            ReadDistrictData = pd.read_excel(fileName, sheet_name='Mahalleler')
            ReadTruckData = pd.read_excel(fileName, sheet_name='Kamyonlar')

            # transfer DataFrame
            self.districtData = pd.DataFrame(data=ReadDistrictData, columns=['Mahalle', 'Sokak Sayısı'])
            self.truckData = pd.DataFrame(data=ReadTruckData, columns=['Plaka', 'Kapasite'])


            truckCount = self.truckData.shape[0]
            districtCount = self.districtData.shape[0]

            #the information read is added to the GUI
            self.gui.truckEntry.setText(str(truckCount))                    # Kamyon Sayısı Entry'e yazdırıldı
            self.gui.truckEntry.setEnabled(False)                                   # Kamyon sayısının yazılı olduğu kutu değiştirilemez.
            self.gui.districtEntry.setText(str(districtCount))              # Mahalle Sayısı
            self.gui.districtEntry.setEnabled(False)                                # Mahalle sayısının olduğu kutu değiştirilemez
            self.gui.streetEntry.setText(str(self.districtData['Sokak Sayısı'].sum()))   # Sokak sayılarının toplamı(sum)
            self.gui.streetEntry.setEnabled(False)                                  # Sokak sayılarının olduğu kutu değiştirilemez
            self.gui.containerEntry.setEnabled(False)

            #silinecek bu kısım default değerler

            self.gui.weatherEntry.setText("15")
            self.gui.trafficEntry.setText("1")
            self.gui.personelEntry.setText("115")
            self.gui.shiftEntry.setText("1")


# Aşağıdaki Bölüm Tablolarda satır ve sütun oluşturur ardından excelden okuyup DataFramelere attığımız veriler bu tablolara yazılır.


            # Truck Data write in TruckTable
            rowCountTruckTable = truckCount
            columnCountTruckTable = self.truckData.shape[1]
            truckColumnsName = self.truckData.columns

            self.gui.truckTable.setRowCount(rowCountTruckTable)
            self.gui.truckTable.setColumnCount(columnCountTruckTable)
            self.gui.truckTable.setHorizontalHeaderLabels(truckColumnsName)

            for i in range(rowCountTruckTable):
                for j in range(columnCountTruckTable):
                    x = str(self.truckData.iloc[i, j])
                    self.gui.truckTable.setItem(i, j, QTableWidgetItem(x))


            # DistrictData Write in DistrictTable
            rowCountDistrictTable = districtCount  # self.districtData.shape[0]
            columnCountDistrictTable = self.districtData.shape[1]
            districtColumnsName = self.districtData.columns

            self.gui.districtTable.setRowCount(rowCountDistrictTable)
            self.gui.districtTable.setColumnCount(columnCountDistrictTable)
            self.gui.districtTable.setHorizontalHeaderLabels(districtColumnsName)

            for i in range(rowCountDistrictTable):
                for j in range(columnCountDistrictTable):
                    x = str(self.districtData.iloc[i, j])
                    self.gui.districtTable.setItem(i, j, QTableWidgetItem(x))


    @pyqtSlot()
    def algorithmRun(self):

        if(self.gui.personelEntry.text() == "" or self.gui.shiftEntry.text() == "" or self.gui.weatherEntry.text() == "" or self.gui.trafficEntry.text() == ""):
            QMessageBox.critical(self, "Missing Value", "Lütfen, İstenilen Parametreleri Eksiksiz Giriniz")

        else:
            # parameters types convert integer

            self.truckCount = int(self.gui.truckEntry.text())
            self.personelCount = int(self.gui.personelEntry.text())
            self.districtCount = int(self.gui.districtEntry.text())
            self.streetCount =  int(self.gui.streetEntry.text())
            self.shiftCount = int(self.gui.shiftEntry.text())
            self.weatherCondition = int(self.gui.weatherEntry.text())
            self.trafficRate = int(self.gui.trafficEntry.text())

            #Combobox'a shift sayısı kadar seçenek yüklüyoruz.
            self.gui.selectShiftCombo.addItem('Vardiya Seciniz')
            self.gui.selectShiftCombo.addItems(['Vardiya ' + str(i + 1) for i in range(self.shiftCount)])


            # Create Object (system, trucks, Shifts, Districts, Streets, Containers)

            trucks = [Truck(plate=self.truckData.Plaka[i], capacity=float(self.truckData.Kapasite[i])) for i in range(0,self.truckCount)]

            sistem = System("Gazi Osman Paşa", self.truckCount, self.personelCount, self.shiftCount)
            sistem.setTruckList(list(trucks))
            sistem.setDistrictList(self.districtData.Mahalle)              # self.districtData['Mahalle']
            sistem.setStreetCountList(self.districtData['Sokak Sayısı'])   #district.data.Sokak!!!!!Sayısı  (boşluk bırakılamaz o nedenle bu yöntemi uyguladık)



            # Tüm vardiyaların başlangıç saati varsayılan olarak 06:00 olarak alındı.
            self.vardiyalar = [Shift('06:00:00') for i in range(self.shiftCount)]

            # Mahalleler Oluşturuluyor
            mahalleler = [
            District(
                name = sistem.getDistrictList().__getitem__(i),
                streetCount = sistem.getStreetCountList().__getitem__(i)
            ) for i in range(len(sistem.getDistrictList()))
            ]

            # Her bir mahalleye ait sokak sayısı kadar sokak oluşturuluyor isimlendirme sokak(İ), i sürekli artar ==> sokak1, sokak2, sokak3.....
            # Her bir sokak oluşturulduğu anda, o sokağa ait random(1,2) (1 veya 2) konteyner oluşturuluyor
            # Her oluşturulan random konteyner için 40 ila 60 arası ağırlık oluşturuluyor.

            self.totalContainerCount = 0

            for i in range(len(mahalleler)):
                sokakSayisi = mahalleler.__getitem__(i).getStreetCount()
                for y in range(sokakSayisi):
                    name = "Sokak {}".format(y + 1)
                    containerCount = random.randint(1, 2)
                    self.totalContainerCount += containerCount   # Toplam konteyner sayısı, üretilen konteyner sayısı kadar arttırıldı.
                    transTime = 0.5
                    sokak = Street(name=name, containerCount=containerCount, transTime = transTime)
                    mahalleler.__getitem__(i).addStreet(sokak)

                    # Sokak bloğunun içinde iken container üretilip soağa yükleniyor.
                    for z in range(containerCount):
                        id = str(z)
                        weight = random.randint(50, 70)
                        container = Container(containerId=id, containerWeight=weight)
                        sokak.addContainer(container)

            # Toplam Konteyner sayısı arayüze yazılıyor
            self.gui.containerEntry.setEnabled(True)  # Kutu yazılabilir halde
            self.gui.containerEntry.setText(str(self.totalContainerCount))
            self.gui.containerEntry.setEnabled(False) # Kutu yazılamaz halde


    # Bu bölüme kadar nesneler oluşturuldu ve gerekli bilgileri dolduruldu.
    # Aşağıdaki bölümde asıl algoritmaız işleyecek.


            for i in range(self.shiftCount):
                serviceTimes = []
                invalid = False
                while invalid == False:
                    shiftStartTime= QInputDialog.getText(self,'Vardiya Saati','{}. Vardiya Baslanic Zamanini Giriniz örn(06:00):'.format(i+1))
                    if ':' in shiftStartTime.__getitem__(0):
                        invalid = True
                        vardiya = self.vardiyalar.__getitem__(i)
                        vardiya.setStartTime(str(shiftStartTime.__getitem__(0)) + ":00")
                        message = sistem.shiftStart(vardiya, i+1)
                        self.gui.outputList.addItem(" ")
                        self.gui.outputList.addItem(message)
                        self.gui.outputList.item(len(self.gui.outputList)-1).setForeground(QColor('red'))

                        for y in range(len(sistem.getDistrictList())):
                            mahalle = mahalleler.__getitem__(y)
                            mahalle.currentTime = vardiya.getStartTime()
                            personelCount = random.randint(3,5) # arac ile birlikte yollanacak personel sayısı (2+1),(3+1),(4+1)
                            message, arac = sistem.sendTheTruck(mahalle, mahalle.currentTime, personelCount, vardiya)
                            self.gui.outputList.addItem(message)
                            self.gui.outputList.item(len(self.gui.outputList) - 1).setForeground(QColor('blue'))

                            for st in mahalle.getStreetList():
                                vardiya.startTimes.append(mahalle.currentTime)
                                delay = sistem.streetDelay(st.getTransTime(), self.trafficRate) # return second
                                currentTime1 = sistem.calculateTime(mahalle.currentTime, delay) # hours + seconds
                                mahalle.currentTime = currentTime1
                                garbageWeight=0
                                for cnt in st.getContainerList():

                                    garbageWeight += int(cnt.getContainerWeight())
                                    cnt.setContainerWeight(random.randint(40,60))
                                    cleaningTime = sistem.calculateCleaningTime(personelCount, self.weatherCondition)# temizlik süresi hesaplandı
                                    currentTime = sistem.calculateTime(mahalle.currentTime, cleaningTime)# Güncel saat hesaplandı
                                    mahalle.currentTime = currentTime  # güncel saat işlendi.
                                    message, result = arac.collectGarbage(sistem, vardiya, arac, st, cnt, currentTime)
                                    self.gui.outputList.addItem(message)
                                    if result != True: arac = result

                                #Konteynerlar temizlendi, sistem durumuna yansıtmak için bilgiler işleniyor.

                                vardiya.delayTraffic.append(timedelta(seconds=delay))
                                vardiya.truckNames.append(arac.getPlate())
                                vardiya.districtNames.append(mahalle.getName())
                                vardiya.streetNames.append(st.getName())
                                vardiya.collectedGarbages.append(int(garbageWeight))
                                vardiya.totalCollectedGarbages.append(sum(vardiya.collectedGarbages))
                                vardiya.serviceTimes.append(timedelta(seconds=cleaningTime * len(st.getContainerList())))
                                serviceTimes.append(cleaningTime * len(st.getContainerList()))
                                vardiya.finishTimes.append(mahalle.currentTime)
                                vardiya.personelCountList.append(sistem.getTotalPersonelCount())
                                vardiya.containerCounts.append(len(st.getContainerList()))



                        uniqueDistrict = pd.unique(vardiya.districtNames)
                        totalTime=0
                        y=0
                        for i,value in enumerate(serviceTimes):
                            if uniqueDistrict[y] == vardiya.districtNames[i]:
                                totalTime=totalTime + value
                                newTotalTime = str(timedelta(minutes=totalTime/60))
                                vardiya.totalServiceTimes.append(newTotalTime)
                            else:
                                y += 1
                                totalTime = value
                                newTotalTime = str(timedelta(minutes=totalTime/60))
                                vardiya.totalServiceTimes.append(newTotalTime)



                        # Burada i'nci vardiya bitti. Kamyon sayısı,durumu, personel sayısı güncellenir.
                        for i in sistem.getTruckList():
                            i.setCapacity(10000)
                            i.setState("pasif")
                        sistem.setTotalPersonelCount(self.personelCount)
                        sistem.setTotalTruckCount(self.truckCount)

    @pyqtSlot()
    def deneme(self):

        print("tamam")

    @pyqtSlot()
    def selectedShiftDisplay(self):

        index = self.gui.selectShiftCombo.currentIndex()
        if index != 0:
            self.gui.stateTable.setRowCount(1)
            vardiya = self.vardiyalar.__getitem__(index-1)

            for i in range(len(vardiya.startTimes)):
                rowCount = self.gui.stateTable.rowCount()
                self.gui.stateTable.insertRow(rowCount)
                self.gui.stateTable.setItem(rowCount, 0, QTableWidgetItem(vardiya.startTimes[i]))
                self.gui.stateTable.setItem(rowCount, 1, QTableWidgetItem(str(vardiya.delayTraffic[i])))
                self.gui.stateTable.setItem(rowCount, 2, QTableWidgetItem(vardiya.truckNames[i]))
                self.gui.stateTable.setItem(rowCount, 3, QTableWidgetItem(vardiya.districtNames[i]))
                self.gui.stateTable.setItem(rowCount, 4, QTableWidgetItem(vardiya.streetNames[i]))
                self.gui.stateTable.setItem(rowCount, 5, QTableWidgetItem(str(vardiya.containerCounts[i])))
                self.gui.stateTable.setItem(rowCount, 6, QTableWidgetItem(str(vardiya.collectedGarbages[i])))
                self.gui.stateTable.setItem(rowCount, 7, QTableWidgetItem(str(vardiya.totalCollectedGarbages[i])))
                self.gui.stateTable.setItem(rowCount, 8, QTableWidgetItem(str(vardiya.personelCountList[i])))
                self.gui.stateTable.setItem(rowCount, 9, QTableWidgetItem(str(vardiya.serviceTimes[i])))
                self.gui.stateTable.setItem(rowCount, 10, QTableWidgetItem(str(vardiya.totalServiceTimes[i])))
                self.gui.stateTable.setItem(rowCount, 11, QTableWidgetItem(vardiya.finishTimes[i]))



app = QApplication([])
window = Main()
window.show()
app.exec_()