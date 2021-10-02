from re import search
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from datetime import date,timedelta,datetime
import os.path
from os import path


class mywidget(Widget):

    if not path.exists('password.txt'):
        f=open('password.txt','w') 
        f.write('{}')
        f.close()
    
    FontOptions=('fontname1','fontname2','fontname3','fontname4','fontname5','fontname6','fontname7','fontname8','fontname9','fontname10','fontname11','fontname12.otf')
    
    main_font=FontOptions[10]
    
    ColorOptions=((153/255,0,0,1),(255/255,0,0,1),(204/255,0,1,1),(102/255,0,102/255,1),(102/255,0/255,204/255,1),(0,0,0,1),(179/255,134/255,0,1),(26/255,51/255,0,1),(255/255,85/255,0,1),(0/255,102/255,153/255,1),(255/255,77/255,210/255,1),(82/255,122/255,122/255,1))
    
    textColor=ColorOptions[3]
    
    ColorOptionsName=('Brown','Red','VioletPink','GreyishBlack','VioletBlue','Black','BlackishYellow','DarkGreen','Orange','BlueishGreen','LightPink','Grey')
    
    FontOptionsName=('Courgette','Alegreya','Satisfy','Bitter','OleoScript','Caveat', 'DancingScript','Grimalda','Quintessential', 'JosefinSans','Rancho','Sofia')
    
    fontsize="30sp"

    latestDate=""
    
    def __init__(self): 
        super(mywidget,self).__init__()
        

        self.i=Button(text='i',font_size="30sp",background_color=(51/255,204/255,255/255,1),size=(45,45),pos=(2,554),italic=True,bold=True,font_name=self.FontOptions[2])
        self.i.bind(on_press=self.info)
        self.add_widget(self.i)

        self.welcome=Label(text ='''         !!! WELCOME !!!

        Enter Your UserName''',font_size ="50sp",font_name=self.FontOptions[2],
        size_hint =(1, .5),
        pos =(305, 448))
        self.add_widget(self.welcome)
        self.name=TextInput(font_size ="30sp",font_name=self.FontOptions[4],foreground_color=(0/255,0,102/255,1),
        size =(200, 70),
        pos =(300,330))
        self.add_widget(self.name)

        self.enterPass=Label(text ='''Enter Your Password''',font_size ="50sp",font_name=self.FontOptions[2],
        size_hint =(1, .5),
        pos =(350, 250))
        self.add_widget(self.enterPass)
        self.password=TextInput(font_size ="30sp",font_name=self.FontOptions[4],foreground_color=(0/255,0,102/255,1),
        size =(200, 70),
        pos =(300,200))
        self.add_widget(self.password)

        self.enter=Button(text="ENTER",font_size ="20sp",background_color =(51/255, 1, 51/255, 1),font_name=self.FontOptions[2],
        size =(75,35),
        pos =(365, 100))
        self.enter.bind(on_press=self.Check)
        self.add_widget(self.enter)

        self.create=Button(text="New Diary? Click here !",font_size ="25sp",background_color =(0, 0, 1, 1),font_name=self.FontOptions[2],
        size =(250,30),
        pos =(280, 40))
        self.create.bind(on_press=self.Create)
        self.add_widget(self.create)
    
    def backUse(self,instance):
        self.remove_widget(self.use)
        self.remove_widget(self.backArr)

    def info(self,instance):
        
        self.backArr=Button(text='<-- BACK',font_size="90sp",background_color=(255/255,51/255,133/255,1),size=(800,120),pos=(0,490),bold=True,font_name=self.FontOptions[4])
        self.backArr.bind(on_press=self.backUse)
        self.add_widget(self.backArr)      

        self.use=TextInput(text='''   "i" Button - HOW TO USE !

                                  1) DIARY LOGIN PAGE-
          To open your Diary, you need to enter your name with password.
          If you are a new user, then click on "New Diary? Click here!" option to 
          create a new Diary with username and password.
          (Note: Password once created can't be changed.)

          After creating new Diary, you will be redirected to the password
          homepage again. 
          Enter new username and password to open your Diary.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
                                   2) MyDiary HOMEPAGE-
          In this page , you will find two options to explore -
          a- Write my Diary
          b- Read my Diary 
          
          For Adding a new entry in the Diary or editing any previous entry in the 
          Diary, click on "Write my Diary" Button.
          For Reading your previous Diary entries, click on "Read my Diary" Button.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            3)Here Lets see how to operate read and write pages separately.
            "HOME" Button can be used to go to My Diary HomePage.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                       "WRITE MY DIARY"

                > In this page, you can see a blank page TextBox and a date search option and 
                two buttons- "SAVE" and "HOME".

                > When you want to Add a new entry to your Diary, so just enter the 
                date(for which you are making the entry) in the given dateBox at the
                top and type the content of the entry in the given big Entry TextBox
                and after completion of the entry ,click on the "SAVE" Button to save
                it in your Diary.

                > When you want to Edit a old entry in your Diary, so just enter the 
                date(for which you are making the entry) in the given dateBox at the
                top and search for that entry by clicking on the search button (below
                the dateBox) and then edit the content of the entry in the Entry 
                TextBox and after completion of the entry ,click on the "SAVE" Button
                to save it in your Diary.

                > You can also change the features of the text that you are entering by
                clicking on the "Set" Button (present at top right).
                You can change the following features, according to your choice-
                I)Font 
                II)Font Color 
                III)Font Size 

                > Whenever you choose some new features and save your entry, so, when you'll
                read it, that entry will be displayed with the same features that you 
                choose.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                          "READ MY DIARY"
                
                ~ In this page, you can see a TextBox (with the latest entry or edit, you
                made), a date search option , a font resizer option and three 
                buttons - "PREVIOUS" , "NEXT" and "HOME".

                ~ When you search a date in the searchbox, the full diary entry content 
                will be displayed with its date in one corner.
                For seeing next or previous entries from this date, you can click on
                "NEXT" Button for seeing any immediate entries made after that date & 
                "PREVIOUS" Button for seeing any immediate entries made before that
                date

                ~ You can use the font resizer option to change the font of the diary entry,
                according to your choice, by entering the desired size and clicking on 
                "OK" Button.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                          PLEASE READ FROM THE TOP !
                                                                        ~ THANKYOU ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''',font_size ="15sp",
        size =(750, 500),
        pos =(25,3),font_name=self.FontOptions[3],readonly=True,foreground_color=self.ColorOptions[3])
        self.add_widget(self.use)

    def remove1(self):
        self.remove_widget(self.welcome)
        self.remove_widget(self.password)
        self.remove_widget(self.name)
        self.remove_widget(self.enter)
        self.remove_widget(self.enterPass)
        self.remove_widget(self.create)

    def Check(self,instance):
        self.remove1()
        with open('password.txt','r') as f:
            self.b=eval(f.read())
            f.close()    
        if self.name.text in self.b.keys() and str(self.b[self.name.text].keys())[12:-3]==self.password.text :
            self.homePage()
            with open('password.txt', 'r') as f:
                    self.a = eval(f.read())
                    self.latestDate=self.a[self.name.text][self.password.text]
                    f.close()
        else:
            self.__init__()
    
    def homePage(self):
        self.myDiary=Label(text =f'''MY DIARY''',font_size ="100sp",font_name=self.FontOptions[0],color=(self.ColorOptions[6]),
            size_hint =(1, .7),bold=True,
            pos =(350, 400))
        self.add_widget(self.myDiary)
            
        self.write=Button(text="Write my Diary",font_size ="25sp",font_name=self.FontOptions[2],background_color =(255/255, 51/255, 255/255, 1),
            size =(200,100),
            pos =(160, 200))
        self.write.bind(on_press=self.writeDetail)
        self.add_widget(self.write)

        self.read=Button(text="Read my Diary",font_size ="25sp",font_name=self.FontOptions[2],background_color =(51/255, 100/255, 255/255, 1),
            size =(200,100),
            pos =(450, 200))
        self.read.bind(on_press=self.readDetail)
        self.add_widget(self.read)

    def Create(self,instance):
        self.remove1()
        self.welcome=Label(text ="Enter Your UserName",font_size ="50sp",font_name=self.FontOptions[2],
        size_hint =(1, .5),
        pos =(350, 400))
        self.add_widget(self.welcome)
        self.name=TextInput(font_size ="30sp",font_name=self.FontOptions[4],foreground_color=(0/255,0,102/255,1),
        size =(200, 70),
        pos =(300,340))
        self.add_widget(self.name)
        
        self.enterPass=Label(text ='''Create Password''',font_size ="50sp",font_name=self.FontOptions[2],
        size_hint =(1, .5),
        pos =(350, 250))
        self.add_widget(self.enterPass)
        self.password=TextInput(font_size ="30sp",font_name=self.FontOptions[4],foreground_color=(0/255,0,102/255,1),
        size =(200, 70),
        pos =(300,200))
        self.add_widget(self.password)

        self.enter=Button(text="ENTER",font_size ="20sp",background_color =(51/255, 1, 51/255, 1),font_name=self.FontOptions[2],
        size =(75,35),
        pos =(413, 80))
        self.enter.bind(on_press=self.enterS1)
        self.add_widget(self.enter)

        self.back=Button(text="BACK",font_size ="20sp",background_color =(51/255, 1, 51/255, 1),font_name=self.FontOptions[2],
        size =(75,35),
        pos =(313, 80))
        self.back.bind(on_press=self.enterS2)
        self.add_widget(self.back)

    def enterS2(self,instance):
        self.remove_widget(self.back)
        self.remove1()
        self.__init__()

    def enterS1(self,instance):
        with open('password.txt', 'r') as f:
                    self.a = eval(f.read())
                    f.close()
        if self.name.text[0:]!=" "*len(self.name.text) and self.password.text[0:]!=" "*len(self.password.text):
            if self.name.text not in self.a.keys():
                self.remove1()
                self.a[self.name.text]={self.password.text:self.latestDate}
                with open('password.txt','w') as f:
                    f.write(str(self.a))
                    f.close()
                fh=open(f'{self.name.text}content.txt','w')
                fh.write("{}")
                fh.close()
                self.remove_widget(self.back)
                self.__init__()

    def remove2(self):
        self.remove_widget(self.myDiary)
        self.remove_widget(self.write)
        self.remove_widget(self.read)

    def nextClick(self,instance):
        try:
            (len(self.dateBox.text))==10 and int(self.dateBox.text[6:10]) and int(self.dateBox.text[0:2]) and int(self.dateBox.text[3:5])
            self.e=self.dateBox.text[6:10]+"-"+self.dateBox.text[3:5]+"-"+self.dateBox.text[0:2]
            self.e=datetime.strptime(self.e, "%Y-%m-%d")
            with open(f'{self.name.text}content.txt', 'r') as f:
                self.c = eval(f.read())
                if(len(self.c))!=0:
                    b=tuple(self.c)
                    if int(str(self.c[self.dateBox.text])[2:3])==len(b):
                        pass
                    else:
                        self.remove_widget(self.noteBox)
                        self.remove_widget(self.dateBox)
                        self.nextindex=int(str(self.c[self.dateBox.text])[2:3])+1
                        for i in range(0,len(b)):
                            
                            self.itsColor=self.c[b[i]][str(self.c[b[i]])[2:3]][f"{str(self.c[b[i]][str(self.c[b[i]].keys())[12:-3]].keys())[12:-3]}"][str(self.c[b[i]][str(self.c[b[i]])[2:3]][f"{str(self.c[b[i]][str(self.c[b[i]].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]]
                            self.itsFont=str(self.c[b[i]][str(self.c[b[i]])[2:3]][f"{str(self.c[b[i]][str(self.c[b[i]].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]
                            
                            if int(str(self.c[b[i]])[2:3])==self.nextindex:
                                self.noteBox=TextInput(text=f"{str(self.c[b[i]][str(self.c[b[i]].keys())[12:-3]].keys())[12:-3]}",font_size =self.fontsize,background_color=(204/255,1,1,1),font_name=self.itsFont,foreground_color=self.itsColor,
                                size =(750, 400),readonly=True,
                                pos =(25,67))
                                self.add_widget(self.noteBox)    
                                
                                self.dateBox=TextInput(text=b[i],font_size ="25sp",background_color=(51/255,204/255,204/255,1),font_name=self.FontOptions[4],foreground_color=(102/255,51/255,0/255,1),
                                size =(140, 40),readonly=True,
                                pos =(25,470))
                                self.add_widget(self.dateBox)    
                                break
        except ValueError:
            pass

    def previousClick(self,instance):
        try:
            (len(self.dateBox.text))==10 and int(self.dateBox.text[6:10]) and int(self.dateBox.text[0:2]) and int(self.dateBox.text[3:5])
            self.e=self.dateBox.text[6:10]+"-"+self.dateBox.text[3:5]+"-"+self.dateBox.text[0:2]
            self.e=datetime.strptime(self.e, "%Y-%m-%d")
            with open(f'{self.name.text}content.txt', 'r') as f:
                self.c = eval(f.read())
                if(len(self.c))!=0:
                    b=tuple(self.c)
                    if int(str(self.c[self.dateBox.text])[2:3])==1:
                        pass
                    else:
                        self.remove_widget(self.noteBox)
                        self.remove_widget(self.dateBox)
                        self.nextindex=int(str(self.c[self.dateBox.text])[2:3])-1
                        for i in range(0,len(b)):
                        
                            self.itsColor=self.c[b[i]][str(self.c[b[i]])[2:3]][f"{str(self.c[b[i]][str(self.c[b[i]].keys())[12:-3]].keys())[12:-3]}"][str(self.c[b[i]][str(self.c[b[i]])[2:3]][f"{str(self.c[b[i]][str(self.c[b[i]].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]]
                            self.itsFont=str(self.c[b[i]][str(self.c[b[i]])[2:3]][f"{str(self.c[b[i]][str(self.c[b[i]].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]
                        
                            if int(str(self.c[b[i]])[2:3])==self.nextindex:
                                self.noteBox=TextInput(text=f"{str(self.c[b[i]][str(self.c[b[i]].keys())[12:-3]].keys())[12:-3]}",font_size =self.fontsize,background_color=(204/255,1,1,1),font_name=self.itsFont,foreground_color=self.itsColor,
                                size =(750, 400),readonly=True,
                                pos =(25,67))
                                self.add_widget(self.noteBox)    
                                
                                self.dateBox=TextInput(text=b[i],font_size ="25sp",background_color=(51/255,204/255,204/255,1),font_name=self.FontOptions[4],foreground_color=(102/255,51/255,0/255,1),
                                size =(140, 40),readonly=True,
                                pos =(25,470))
                                self.add_widget(self.dateBox)    
                                break
        except ValueError:
            pass

    def writeDetail(self,instance):
        self.remove2()
        self.home=Button(text="HOME",font_size ="25sp",background_color =(1, 1, 0, 1),font_name=self.FontOptions[0],
            size =(160,60),
            pos =(40, 8))
        self.home.bind(on_press=self.homeTask2)
        self.add_widget(self.home)

        self.enterText=Label(text ='''Enter Text''',font_size ="35sp",bold=True,underline=True,font_name=self.FontOptions[4],
        size_hint =(1, .5),
        pos =(350, 435))
        self.add_widget(self.enterText)

        self.writeBox=TextInput(font_size =self.fontsize,background_color=(1,1,153/255,1),font_name=self.main_font,foreground_color=self.textColor,
        size =(750, 400),
        pos =(25,67))
        self.add_widget(self.writeBox)

        self.settings1=Button(text='Set',font_size="30sp",background_color=(51/255,204/255,255/255,1),size=(45,45),pos=(753,553),italic=True,bold=True,font_name=self.FontOptions[2])
        self.settings1.bind(on_press=self.Set1)
        self.add_widget(self.settings1)

        self.saveB=Button(text="SAVE",font_size ="25sp",background_color =(153/255,153/255,255/255,1),font_name=self.FontOptions[0],
            size =(160,60),
            pos =(600, 8))
        self.saveB.bind(on_press=self.saveTask)
        self.add_widget(self.saveB)

        self.search1=Button(text ='''Search (DD-MM-YYYY)''',font_size ="15sp",bold=True,
        size=(170, 30),background_color=(0,153/255,0,1),
        pos =(315, 520))
        self.search1.bind(on_press=self.show1)
        self.add_widget(self.search1)

        self.searchBar1=TextInput(font_size ="35sp",background_color=(1,1,1,1),font_name=self.FontOptions[4],
        size =(200, 50),
        pos =(300,550))
        self.add_widget(self.searchBar1)

    def readDetail(self,instance):
        self.remove2()
        self.next=Button(text="NEXT -->",font_size ="25sp",background_color =(0, 1, 0, 1),font_name=self.FontOptions[0],
            size =(160,60),
            pos =(598, 8))
        self.next.bind(on_press=self.nextClick)
        self.add_widget(self.next)

        self.previous=Button(text="<-- PREVIOUS",font_size ="25sp",background_color =(1, 153/255, 1, 1),font_name=self.FontOptions[0],
            size =(160,60),
            pos =(400, 8))
        self.previous.bind(on_press=self.previousClick)
        self.add_widget(self.previous)

        self.home=Button(text="HOME",font_size ="25sp",background_color =(1, 1, 0, 1),font_name=self.FontOptions[0],
            size =(160,60),
            pos =(40, 8))
        self.home.bind(on_press=self.homeTask1)
        self.add_widget(self.home)
        
        self.fontsizeText=TextInput(text=self.fontsize[:],pos=(636,470),font_size="25sp",size=(140,40),background_color=(51/255,204/255,204/255,1))
        self.add_widget(self.fontsizeText)
        self.fontsizer=Button(text='OK',font_size="30sp",background_color=(51/255,204/255,255/255,1),size=(54,40),pos=(723,470),italic=True,bold=True,font_name=self.FontOptions[2])
        self.fontsizer.bind(on_press=self.Set2)
        self.add_widget(self.fontsizer)
        self.FontLabel=Label(text="Font Size",font_size="30sp",color=(1,1,1,1),font_name=self.FontOptions[9],pos=(660,475),underline=True)
        self.add_widget(self.FontLabel)
        
        self.search2=Button(text ='''Search (DD-MM-YYYY)''',font_size ="15sp",bold=True,
        size=(170, 30),background_color=(0,153/255,0,1),
        pos =(315, 520))
        self.search2.bind(on_press=self.show2)
        self.add_widget(self.search2)

        self.searchBar2=TextInput(font_size ="35sp",background_color=(1,1,1,1),font_name=self.FontOptions[4],
        size =(200, 50),
        pos =(300,550))
        self.add_widget(self.searchBar2)

        with open(f'{self.name.text}content.txt', 'r') as f:
            self.c = eval(f.read())
            
        if self.latestDate in self.c.keys():
            b=self.latestDate
            self.itsColor=self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"][str(self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]]
            self.itsFont=str(self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]
            
            self.noteBox=TextInput(text=f"{str(self.c[self.latestDate][str(self.c[self.latestDate].keys())[12:-3]].keys())[12:-3]}",font_size =self.fontsize,background_color=(1,1,153/255,1),font_name=self.itsFont,foreground_color=self.itsColor,
            size =(750, 400),readonly=True,
            pos =(25,67))
            self.add_widget(self.noteBox)
        else: 
            self.noteBox=TextInput(text="",font_size =self.fontsize,background_color=(1,1,153/255,1),font_name=self.main_font,foreground_color=self.textColor,
            size =(750, 400),readonly=True,
            pos =(25,67))
            self.add_widget(self.noteBox)

        self.dateBox=TextInput(text=self.latestDate,font_size ="25sp",background_color=(51/255,204/255,204/255,1),font_name=self.FontOptions[4],foreground_color=(102/255,51/255,0/255,1),
        size =(140, 40),readonly=True,
        pos =(25,470))
        self.add_widget(self.dateBox)
        self.DateLabel=Label(text="Date",font_size="30sp",color=(1,1,1,1),font_name=self.FontOptions[9],pos=(38,475),underline=True)
        self.add_widget(self.DateLabel)

    def Set1(self,instance):
        self.ok1=Button(text='OK',font_size="90sp",background_color=(255/255,51/255,133/255,1),size=(800,120),pos=(0,490),bold=True,font_name=self.FontOptions[4])
        self.ok1.bind(on_press=self.exit1)
        self.add_widget(self.ok1)      

        self.config1=TextInput(font_size ="20sp",
        size =(760, 500),
        pos =(20,3),font_name=self.FontOptions[2],readonly=True)
        self.add_widget(self.config1)

        self.setLabel1=Label(text='Settings',pos=(360,400),font_size="60sp",color=(255/255,51/255,133/255,1),font_name=self.FontOptions[2],underline=True)
        self.add_widget(self.setLabel1)

        self.setLabel2=Label(text='Font',pos=(130,350),font_size="30sp",color=(102/255,0/255,102/255,1),font_name=self.FontOptions[4],underline=True)
        self.add_widget(self.setLabel2)
        self.fontText=TextInput(pos=(145,350),font_size="19sp",size=(70,30))
        self.add_widget(self.fontText)

        self.setLabel3=Label(text='Font Color',pos=(360,350),font_size="30sp",color=(102/255,0/255,102/255,1),font_name=self.FontOptions[4],underline=True)
        self.add_widget(self.setLabel3)
        self.fontcolorText=TextInput(pos=(375,350),font_size="19sp",size=(70,30))
        self.add_widget(self.fontcolorText)

        self.setLabel4=Label(text='Font Size',pos=(590,350),font_size="30sp",color=(102/255,0/255,102/255,1),font_name=self.FontOptions[4],underline=True)
        self.add_widget(self.setLabel4)
        self.fontsizeText=TextInput(text=self.fontsize[0:-2],pos=(605,350),font_size="19sp",size=(70,30))
        self.add_widget(self.fontsizeText)

    #FontOptions
        self.Font1=Label(text=f'1-{self.FontOptionsName[0]}',pos=(135,290-28*(0)),font_name=self.FontOptions[0],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font1)
        self.Font2=Label(text=f'2-{self.FontOptionsName[1]}',pos=(135,290-28*(1)),font_name=self.FontOptions[1],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font2)
        self.Font3=Label(text=f'3-{self.FontOptionsName[2]}',pos=(135,290-28*(2)),font_name=self.FontOptions[2],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font3)
        self.Font4=Label(text=f'4-{self.FontOptionsName[3]}',pos=(135,290-28*(3)),font_name=self.FontOptions[3],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font4)
        self.Font5=Label(text=f'5-{self.FontOptionsName[4]}',pos=(135,290-28*(4)),font_name=self.FontOptions[4],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font5)
        self.Font6=Label(text=f'6-{self.FontOptionsName[5]}',pos=(135,290-28*(5)),font_name=self.FontOptions[5],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font6)
        self.Font7=Label(text=f'7-{self.FontOptionsName[6]}',pos=(135,290-28*(6)),font_name=self.FontOptions[6],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font7)
        self.Font8=Label(text=f'8-{self.FontOptionsName[7]}',pos=(135,290-28*(7)),font_name=self.FontOptions[7],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font8)
        self.Font9=Label(text=f'9-{self.FontOptionsName[8]}',pos=(135,290-28*(8)),font_name=self.FontOptions[8],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font9)
        self.Font10=Label(text=f'10-{self.FontOptionsName[9]}',pos=(135,290-28*(9)),font_name=self.FontOptions[9],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font10)
        self.Font11=Label(text=f'11-{self.FontOptionsName[10]}',pos=(135,290-28*(10)),font_name=self.FontOptions[10],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font11)
        self.Font12=Label(text=f'12-{self.FontOptionsName[11]}',pos=(135,290-28*(11)),font_name=self.FontOptions[11],color=(0,0,0,1),font_size="20sp")
        self.add_widget(self.Font12)
            
    #ColorOptions    
        self.Color1=Label(text=f'1-{self.ColorOptionsName[0]}',pos=(365,290-28*(0)),color=self.ColorOptions[0],font_size="20sp")
        self.add_widget(self.Color1)
        self.Color2=Label(text=f'2-{self.ColorOptionsName[1]}',pos=(365,290-28*(1)),color=self.ColorOptions[1],font_size="20sp")
        self.add_widget(self.Color2)
        self.Color3=Label(text=f'3-{self.ColorOptionsName[2]}',pos=(365,290-28*(2)),color=self.ColorOptions[2],font_size="20sp")
        self.add_widget(self.Color3)
        self.Color4=Label(text=f'4-{self.ColorOptionsName[3]}',pos=(365,290-28*(3)),color=self.ColorOptions[3],font_size="20sp")
        self.add_widget(self.Color4)
        self.Color5=Label(text=f'5-{self.ColorOptionsName[4]}',pos=(365,290-28*(4)),color=self.ColorOptions[4],font_size="20sp")
        self.add_widget(self.Color5)
        self.Color6=Label(text=f'6-{self.ColorOptionsName[5]}',pos=(365,290-28*(5)),color=self.ColorOptions[5],font_size="20sp")
        self.add_widget(self.Color6)
        self.Color7=Label(text=f'7-{self.ColorOptionsName[6]}',pos=(365,290-28*(6)),color=self.ColorOptions[6],font_size="20sp")
        self.add_widget(self.Color7)
        self.Color8=Label(text=f'8-{self.ColorOptionsName[7]}',pos=(365,290-28*(7)),color=self.ColorOptions[7],font_size="20sp")
        self.add_widget(self.Color8)
        self.Color9=Label(text=f'9-{self.ColorOptionsName[8]}',pos=(365,290-28*(8)),color=self.ColorOptions[8],font_size="20sp")
        self.add_widget(self.Color9)
        self.Color10=Label(text=f'10-{self.ColorOptionsName[9]}',pos=(365,290-28*(9)),color=self.ColorOptions[9],font_size="20sp")
        self.add_widget(self.Color10)
        self.Color11=Label(text=f'11-{self.ColorOptionsName[10]}',pos=(365,290-28*(10)),color=self.ColorOptions[10],font_size="20sp")
        self.add_widget(self.Color11)
        self.Color12=Label(text=f'12-{self.ColorOptionsName[11]}',pos=(365,290-28*(11)),color=self.ColorOptions[11],font_size="20sp")
        self.add_widget(self.Color12)

        self.enternum=Label(text='''Note: Enter Corresponding
            Digits Only''',font_size="15sp",pos=(70,433),color=(0,0,0,1))
        self.add_widget(self.enternum)
        
    def exit1(self,instance):
        try:
            int(self.fontText.text) and int(self.fontcolorText.text) and int(self.fontsizeText.text)
            self.remove_widget(self.ok1)
            self.remove_widget(self.config1)
            self.remove_widget(self.setLabel1)
            self.remove_widget(self.setLabel2)
            self.remove_widget(self.setLabel3)
            self.remove_widget(self.setLabel4)
            self.remove_widget(self.fontText)
            self.remove_widget(self.fontsizeText)
            self.remove_widget(self.fontcolorText)
            self.remove_widget(self.enternum)
            self.main_font=self.FontOptions[int(str(self.fontText.text))-1]
            self.textColor=self.ColorOptions[int(str(self.fontcolorText.text))-1]
            self.fontsize=f"{self.fontsizeText.text}sp"
            
            self.note=self.writeBox.text
            self.remove_widget(self.writeBox)
            self.writeBox=TextInput(text=self.note,font_size=self.fontsize,background_color=(1,1,153/255,1),font_name=self.main_font,foreground_color=self.textColor,
                size =(750, 400),
                pos =(25,67))
            self.add_widget(self.writeBox)
        #FontOptionsremove    
            self.remove_widget(self.Font1)
            self.remove_widget(self.Font2)
            self.remove_widget(self.Font3)
            self.remove_widget(self.Font4)
            self.remove_widget(self.Font5)
            self.remove_widget(self.Font6)
            self.remove_widget(self.Font7)
            self.remove_widget(self.Font8)
            self.remove_widget(self.Font9)
            self.remove_widget(self.Font10)
            self.remove_widget(self.Font11)
            self.remove_widget(self.Font12)
    #ColorOptionsremove
            self.remove_widget(self.Color1)
            self.remove_widget(self.Color2)
            self.remove_widget(self.Color3)
            self.remove_widget(self.Color4)
            self.remove_widget(self.Color5)
            self.remove_widget(self.Color6)
            self.remove_widget(self.Color7)
            self.remove_widget(self.Color8)
            self.remove_widget(self.Color9)
            self.remove_widget(self.Color10)
            self.remove_widget(self.Color11)
            self.remove_widget(self.Color12)
        except ValueError:
            pass
        
    def Set2(self,instance):
        self.fontsize=self.fontsizeText.text
        self.remove_widget(self.noteBox)
        with open(f'{self.name.text}content.txt', 'r') as f:
            self.c = eval(f.read())
            
        if self.dateBox.text in self.c.keys():
            b=self.dateBox.text
            self.itsColor=self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"][str(self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]]
            self.itsFont=str(self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]
            
            self.noteBox=TextInput(text=f"{str(self.c[self.dateBox.text][str(self.c[self.latestDate].keys())[12:-3]].keys())[12:-3]}",font_size =self.fontsize,background_color=(1,1,153/255,1),font_name=self.itsFont,foreground_color=self.itsColor,
            size =(750, 400),readonly=True,
            pos =(25,67))
            self.add_widget(self.noteBox)
        else: 
            self.noteBox=TextInput(text="",font_size =self.fontsize,background_color=(1,1,153/255,1),font_name=self.main_font,foreground_color=self.textColor,
            size =(750, 400),readonly=True,
            pos =(25,67))
            self.add_widget(self.noteBox)

    def remove3(self):
        self.remove_widget(self.home)
        self.remove_widget(self.enterText)
        self.remove_widget(self.search1)
        self.remove_widget(self.searchBar1)
        self.remove_widget(self.writeBox)
        self.remove_widget(self.settings1)
        self.remove_widget(self.saveB)

    def homeTask1(self,instance):
        self.remove_widget(self.next)
        self.remove_widget(self.previous)
        self.remove_widget(self.home)
        self.remove_widget(self.noteBox)
        self.remove_widget(self.dateBox)
        self.remove_widget(self.fontsizer)
        self.remove_widget(self.FontLabel)
        self.remove_widget(self.DateLabel)
        self.remove_widget(self.fontsizeText)
        self.remove_widget(self.search2)
        self.remove_widget(self.searchBar2)
        self.homePage()

    def homeTask2(self,instance):
        self.remove3()
        self.homePage()

    def saveTask(self,instance):

        try: 
            datetime.strptime(self.searchBar1.text, '%d-%m-%Y')
            with open(f'{self.name.text}content.txt','r') as f:
                self.d=eval(f.read())
            if self.searchBar1.text not in self.d.keys():
                self.d[self.searchBar1.text]={str(len(self.d.keys())+1):{self.writeBox.text:{self.main_font:self.textColor}}}
            else:
                self.d[self.searchBar1.text]={str(self.d[self.searchBar1.text].keys())[12:-3]:{self.writeBox.text:{self.main_font:self.textColor}}}
            b=tuple(self.d) #date index
            for i in range(0,len(b)):
                for j in range(i,len(b)):
                    if i!=j:
                        k1=int(str(self.d[b[i]])[2:3])   #index
                        k2=int(str(self.d[b[j]])[2:3])
                        date1=datetime.strptime(b[i][6:10]+"-"+b[i][3:5]+"-"+b[i][0:2], "%Y-%m-%d")
                        date2=datetime.strptime(b[j][6:10]+"-"+b[j][3:5]+"-"+b[j][0:2], "%Y-%m-%d")
                        if (date1-date2).days>0:
                            if k1>k2:
                                continue
                            else:
                                self.d[b[i]]=eval(str(self.d[b[i]])[0:2]+str(k2)+str(self.d[b[i]])[3:]) #updated
                                self.d[b[j]]=eval(str(self.d[b[j]])[0:2]+str(k1)+str(self.d[b[j]])[3:])
                        else:
                            if k1<k2:
                                continue
                            else:
                                self.d[b[i]]=eval(str(self.d[b[i]])[0:2]+str(k2)+str(self.d[b[i]])[3:]) #updated
                                self.d[b[j]]=eval(str(self.d[b[j]])[0:2]+str(k1)+str(self.d[b[j]])[3:])  
                    else:
                                continue
            with open(f'{self.name.text}content.txt','w') as f:
                f.write(str(self.d))
                f.close()
            self.remove3()
            self.homePage()
            self.latestDate=self.searchBar1.text
            with open('password.txt','r') as f:
                readO=eval(f.read())
                readO[self.name.text]={self.password.text:self.latestDate}
            with open('password.txt','w') as f:
                f.write(str(readO))
                f.close()

        except ValueError:
            pass

    def show1(self,instance):

        try: 
            datetime.strptime(self.searchBar1.text, '%d-%m-%Y')
            self.remove_widget(self.writeBox)
            with open(f'{self.name.text}content.txt', 'r') as f:
                self.c = eval(f.read())
                
            if self.searchBar1.text in self.c.keys():
                self.writeBox=TextInput(text=f"{str(self.c[self.searchBar1.text][str(self.c[self.searchBar1.text].keys())[12:-3]].keys())[12:-3]}",font_size =self.fontsize,background_color=(1,1,153/255,1),font_name=self.main_font,foreground_color=self.textColor,
                size =(750, 400),
                pos =(25,67))
                self.add_widget(self.writeBox)
            
            else: 
                self.writeBox=TextInput(font_size =self.fontsize,background_color=(1,1,153/255,1),font_name=self.main_font,foreground_color=self.textColor,
                size =(750, 400),
                pos =(25,67))
                self.add_widget(self.writeBox)
        except ValueError:
            self.writeDetail

    def show2(self,instance):

        try: 
            datetime.strptime(self.searchBar2.text, '%d-%m-%Y')
            with open(f'{self.name.text}content.txt', 'r') as f:
                self.c = eval(f.read())
            if self.searchBar2.text in self.c.keys():
                self.remove_widget(self.noteBox)
                self.remove_widget(self.dateBox)
                b=self.searchBar2.text
                self.itsColor=self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"][str(self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]]
                self.itsFont=str(self.c[b][str(self.c[b])[2:3]][f"{str(self.c[b][str(self.c[b].keys())[12:-3]].keys())[12:-3]}"].keys())[12:-3]
                
                self.noteBox=TextInput(text=f"{str(self.c[self.searchBar2.text][str(self.c[self.searchBar2.text].keys())[12:-3]].keys())[12:-3]}",font_size =self.fontsize,background_color=(1,1,153/255,1),font_name=self.itsFont,foreground_color=self.itsColor,
                size =(750, 400),readonly=True,
                pos =(25,67))
                self.add_widget(self.noteBox)
                self.dateBox=TextInput(text=f"{self.searchBar2.text}",font_size ="25sp",background_color=(51/255,204/255,204/255,1),font_name=self.FontOptions[4],foreground_color=(102/255,51/255,0/255,1),
                size =(140, 40),readonly=True,
                pos =(25,470))
                self.add_widget(self.dateBox)
            else: 
                self.remove_widget(self.searchBar2)
                self.searchBar2=TextInput(font_size ="35sp",background_color=(1,1,1,1),font_name=self.FontOptions[4],
                size =(200, 50),
                pos =(300,550))
                self.add_widget(self.searchBar2)

        except ValueError:
            self.readDetail
   
class MyDiary(App):
    def build(self):
        return mywidget()

if __name__ == '__main__':
    MyDiary().run()

    
