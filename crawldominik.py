import sys
import time
sys.path.append("/Library/Python/2.7/site-packages")
import re


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




startyear=2005
endyear=2005
oldfilenum=0


ziplist=[]
inilist=[]

with open ("/Users/domonikboddin/Documents/Crawling/Current/zip.txt", encoding="utf16") as rfile:
    for line in rfile:
        


        ziplist.append(line.strip('\n'))
rfile.close()
print(len(ziplist))

initial=1


if oldfilenum>0:
    for n in range(1,oldfilenum+1):
        with open("/Users/dominikboddin/Documents/Crawling/Current/output_"+str(startyear)+"_"+str(oldfilenum)+".txt", encoding="utf16") as inifile:
            i=0
            for line in inifile:
                i+=1
                if i>1:
                    eles=line.split('\t')
                    oldzip=eles[0]
                    if not oldzip in inilist:
                        inilist.append(eles[0])
        inifile.close()

    print(len(inilist))
                
                
            
        
driver =webdriver.Firefox()
#driver =webdriver.PhantomJS("/Library/Python/2.7/site-packages/phantomjs-2.0.0-macosx/bin/phantomjs")
for year in range (startyear,endyear+1):
    url="/Users/dominikboddin/Documents/Crawling/Current/output_"+str(year)+".txt"
    with open (url,"w",encoding="utf16") as wfile:
        
        wfile.write("zip")
        wfile.write('\t')
        wfile.write('year')
        wfile.write('\t')
        wfile.write('total')
        wfile.write('\t')
        wfile.write('patent')
        wfile.write('\t')
        wfile.write('Hauptklasse')
        wfile.write('\t')
        wfile.write('Anmeldetag')
        wfile.write('\t')
        wfile.write('Erstveroffen')
        wfile.write('\t')
        wfile.write('Anmelder')
        wfile.write('\t')
        wfile.write('Anmelderforeign1')
        wfile.write('\t')
        wfile.write('Anmelderforeign2')
        wfile.write('\t')
        wfile.write('Anmelderforeign3')
        wfile.write('\t')
        wfile.write('Anmelderforeign4')
        wfile.write('\t')
        wfile.write('Anmelderforeign5')
        wfile.write('\t')
        wfile.write('Vertreter')
        wfile.write('\t')
        wfile.write('VerZipCode')
        wfile.write('\t')
        wfile.write('Neben1')
        wfile.write('\t')
        wfile.write('Neben2')
        wfile.write('\t')
        wfile.write('Neben3')
        wfile.write('\t')
        wfile.write('Neben4')
        wfile.write('\t')
        wfile.write('Neben5')
        wfile.write('\t')
        wfile.write('Neben6')
        wfile.write('\t')
        wfile.write('Neben7')
        wfile.write('\t')
        wfile.write('Neben8')
        wfile.write('\t')
        wfile.write('Neben9')
        wfile.write('\t')
        wfile.write('Neben10')
        wfile.write('\t')        
        wfile.write('\n')
                    
    
        for k in ziplist:

            if year==startyear and k in inilist:
                continue
                
            number=0

            query="SART = patent und inh=("+str(k)+") und (at >= 01.01."+str(year)+" und at <= 31.12."+str(year)+")"
            print(query)

#            driver =webdriver.PhantomJS("/Library/Python/2.7/site-packages/phantomjs-2.0.0-macosx/bin/phantomjs")
            for m in range (0,4):
                driver.get("https://register.dpma.de/DPMAregister/pat/experte")
                if "Expertenrecherche" in driver.title:
                    break
                else:
                    if m>2:
                        time.sleep(180)
                    else:
                        time.sleep(10)
                    

            if initial==1:
                first=driver.find_element_by_id("eingabefeld")
                driver.find_element_by_id("checkbox_0").click()
                driver.find_element_by_id("checkbox_3").click()
                driver.find_element_by_id("checkbox_4").click()
                driver.find_element_by_id("checkbox_5").click()
                driver.find_element_by_id("checkbox_6").click()
                driver.find_element_by_id("checkbox_8").click()
                driver.find_element_by_id("checkbox_9").click()
                driver.find_element_by_id("checkbox_10").click()
                initial=0
            else:
                first=driver.find_element_by_id("eingabefeld")
                first.clear()
                    
                
                


            second=Select(driver.find_element_by_id("trefferProSeite"))
            cl=driver.find_element_by_id("rechercheStarten")
            first.send_keys(query)
            second.select_by_value("1000")
            cl.click()
            if not "Trefferliste zu lang" in driver.page_source:
                if not "Es sind folgende Fehler aufgetreten" in driver.page_source:
                    if not "Die Datenbankabfrage lieferte keine Treffer" in driver.page_source:

                        if "Treffer 1/1" in driver.page_source:
                            
                            number=1

                    

                            link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Aktenzeichen')]/following-sibling::*[2]")

                            
  #                          link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr[5]/td[4]")
                            patent=link.get_attribute('innerHTML')
                            print(patent)
                            

 #                           link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr[7]/td[4]")

                            link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Hauptklasse')]/following-sibling::*[2]/a[1]")
                            haupt=link.get_attribute('innerHTML')
                            if "(" in haupt:
                                pos=haupt.index("(")
                                haupt=haupt[:pos]
    

                            link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Anmeldetag')]/following-sibling::*[2]")
                            anmeldetag=link.get_attribute('innerHTML')
                            

                    
                            link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Offenlegungstag')]/following-sibling::*[2]")
                            erstver=link.get_attribute('innerHTML')
 
                        
                    
                    
                            link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Anmelder')]/following-sibling::*[2]")
                            anmeld=link.get_attribute('innerHTML')
                            anmeld=anmeld.replace("amp;","")
                            leftposes=[m.start() for m in re.finditer('\(',anmeld)]
                            rightposes=[m.start() for m in re.finditer('\)',anmeld)]
                            num=len(leftposes)
                            if num>0:
                               

                                for j in range(0,num):
                                    if ";" in anmeld[leftposes[j]:rightposes[j]]:
                                        anmeldcopy=anmeld
                                        anmeld=anmeldcopy[0:leftposes[j]].strip()+anmeldcopy[rightposes[j]+1:].strip()
                               


  
                            anmlist=anmeld.split("; ")
                            foreignlist=[]
                            for item in anmlist:
                                lasttwo=item[-2:]
                                if not lasttwo=="DE":
                                    foreignlist.append(lasttwo)
                                if k in item:
                                    pos=item.index(",")
                                    anmelder=item[:pos]
                            
                            try:
                                link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Vertreter')]/following-sibling::*[2]")

                                vertreter=link.get_attribute('innerHTML')

                                
                                
                                if vertreter=="":
                                    vertreter="None"
                                    verzip="None"
                                else:
                                    vertreter=vertreter.replace("amp;","")
                                    verziplist=re.findall('\d{5}|O-\d{4}|W-\d{4}|\d{4}',vertreter)
                                    if len(verziplist)==0:
                                        verzip="unknown"
                                    else:
                                        verzip=verziplist[0]
                            except:
                                vertreter="None"
                                verzip="None"
                            
      
                    
            
                            wfile.write(str(k))
                            wfile.write('\t')
                            wfile.write(str(year))
                            wfile.write('\t')
                            wfile.write(str(number))
                            wfile.write('\t')
                            wfile.write(str(patent))
                            wfile.write('\t')
                            wfile.write(str(haupt))
                            wfile.write('\t')
                            wfile.write(str(anmeldetag))
                            wfile.write('\t')
                            wfile.write(str(erstver))
                            wfile.write('\t')
                            wfile.write(str(anmelder))
                            wfile.write('\t')
                            for i in range(0,5):
                                if not foreignlist:
                                    wfile.write("None")
                                else:
                                    wfile.write(foreignlist.pop(0))
                                wfile.write('\t')

                            wfile.write(str(vertreter))
                            wfile.write('\t')
                            wfile.write(str(verzip))
                            wfile.write('\t')


                            try:
                                link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Nebenklasse')]")
                                nomore=0
                                    
                                for i in range(1,11):
                                    if nomore==0:
                                        try:
                                            link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Nebenklasse')]/following-sibling::*[2]/a[%s]" %i)
                                            neben=link.get_attribute('innerHTML')
                                            if "(" in neben:
                                                pos=neben.index("(")
                                                neben=neben[:pos]
                                                                                                                                                     
                                                    
                                        except:
                                            nomore=1
                                            neben="None"
                                    else:
                                        neben="None"
                            
                                    wfile.write(str(neben))
                                    wfile.write('\t')
                            except:
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')
                                wfile.write('None')
                                wfile.write('\t')

                            try:

                                link=driver.find_element_by_xpath("//table[@id='stammdaten_tabelle']/tbody/tr/td[contains(text(),'Erfinder')]/following-sibling::*[2]")
                                erfind=link.get_attribute('innerHTML')
      
                                erflist=erfind.split("<br>")
                                del erflist[-1]
                                for item in erflist:
                                    lasttwo=item[-2:]
                                    if lasttwo=="DE":
                                        erf=re.findall('\d{5}|O-\d{4}|W-\d{4}|\d{4}',item)
                                        if len(erf)==0:
                                            erfinder="unknown"
    
                                        else:
                                            erfinder=erf[0]
                                    else:
                                        erfinder=lasttwo
                                    wfile.write(str(erfinder))
                                    wfile.write('\t')
                            except:
                                wfile.write('')
                                    
                                            
                                            
                    

                            wfile.write('\n')
                            
                            
                        else:
                            if "DPMAregister" in driver.title:
                                result=driver.find_element_by_xpath("//form[@id='form']/p[2]/span[1]")
                                output=result.get_attribute('innerHTML')
                                output=output.replace('\n',' ')
                                pos=output.index("/em")
                                output=output[pos+4:]
                                posk=output.index("Treffer")
                                output=output[:posk-1]
                                number=int(output)

                                for m in range(2,2+number):
                                    link=driver.find_element_by_xpath("//form[@id='form']/table[1]/tbody[1]/tr[%s]/td[3]/a[1]" %m)
       
                                    
                                    patent=link.get_attribute('innerHTML')

                                    link=driver.find_element_by_xpath("//form[@id='form']/table[1]/tbody[1]/tr[%s]/td[4]/a[1]" %m)
                                    haupt=link.get_attribute('innerHTML')
                                    if "(" in haupt:
                                        pos=haupt.index("(")
                                        haupt=haupt[:pos]
                                   

                                    link=driver.find_element_by_xpath("//form[@id='form']/table[1]/tbody[1]/tr[%s]/td[6]" %m)
                                    anmeldetag=link.get_attribute('innerHTML')
                                    

                                    link=driver.find_element_by_xpath("//form[@id='form']/table[1]/tbody[1]/tr[%s]/td[7]" %m)
                                    erstver=link.get_attribute('innerHTML')
                                  
                                    
                                    link=driver.find_element_by_xpath("//form[@id='form']/table[1]/tbody[1]/tr[%s]/td[8]" %m)
                                    anmeld=link.get_attribute('innerHTML')
                                    anmeld=anmeld.replace("amp;","")
                                    leftposes=[m.start() for m in re.finditer('\(',anmeld)]
                                    rightposes=[m.start() for m in re.finditer('\)',anmeld)]
                                    num=len(leftposes)
                                    if num>0:
                                        print(anmeld)

                                        for j in range(0,num):
                                            if ";" in anmeld[leftposes[j]:rightposes[j]]:
                                                anmeldcopy=anmeld
                                                anmeld=anmeldcopy[0:leftposes[j]].strip()+anmeldcopy[rightposes[j]+1:].strip()
                                        print(anmeld)




                                    
                                    anmlist=anmeld.split("; ")

                                    foreignlist=[]
                                    for item in anmlist:
                                        lasttwo=item[-2:]
                                        if not lasttwo=="DE":
                                            foreignlist.append(lasttwo)
                                        if k in item:
                                            pos=item.index(",")
                                            anmelder=item[:pos]
                                    
                                  

                                    
                                    link=driver.find_element_by_xpath("//form[@id='form']/table[1]/tbody[1]/tr[%s]/td[10]" %m)
                                    vertreter=link.get_attribute('innerHTML')
                                    

                                    
                                    if vertreter=="":
                                        vertreter="None"
                                        verzip="None"
                                    else:
                                        vertreter=vertreter.replace("amp;","")
                                        verziplist=re.findall('\d{5}|O-\d{4}|W-\d{4}|\d{4}',vertreter)
                                        if len(verziplist)==0:
                                            verzip="unknown"
                                        else:
                                            verzip=verziplist[0]
                                    
                                    
                                        
        
                                    wfile.write(str(k))
                                    wfile.write('\t')
                                    wfile.write(str(year))
                                    wfile.write('\t')
                                    wfile.write(str(number))
                                    wfile.write('\t')
                                    wfile.write(str(patent))
                                    wfile.write('\t')
                                    wfile.write(str(haupt))
                                    wfile.write('\t')
                                    wfile.write(str(anmeldetag))
                                    wfile.write('\t')
                                    wfile.write(str(erstver))
                                    wfile.write('\t')
                                    wfile.write(str(anmelder))
                                    wfile.write('\t')
                                    for i in range(0,5):
                                        if not foreignlist:
                                            wfile.write("None")
                                        else:
                                            wfile.write(foreignlist.pop(0))
                                        wfile.write('\t')

                                    wfile.write(str(vertreter))
                                    wfile.write('\t')
                                    wfile.write(str(verzip))
                                    wfile.write('\t')

                                    nomore=0
                                    
                                    for i in range(1,11):
                                        if nomore==0:
                                            try:
                                                link=driver.find_element_by_xpath("//form[@id='form']/table[1]/tbody[1]/tr[%s]/td[5]/a[%s]" %(m,i))
                                                neben=link.get_attribute('innerHTML')
                                                if "(" in neben:
                                                    pos=neben.index("(")
                                                    neben=neben[:pos]
                                                                                                    
                                                        
                                                        
                                            except:
                                                nomore=1
                                                neben="None"
                                        else:
                                            neben="None"
                                
                                        wfile.write(str(neben))
                                        wfile.write('\t')

                                    try:
                        
                                        link=driver.find_element_by_xpath("//form[@id='form']/table[1]/tbody[1]/tr[%s]/td[9]" %m)
                                        erfind=link.get_attribute('innerHTML')     
              
                                        erflist=erfind.split("<br>")
                                        del erflist[-1]
                                        for item in erflist:
                                            lasttwo=item[-2:]
                                            if lasttwo=="DE":
                                                erf=re.findall('\d{5}|O-\d{4}|W-\d{4}|\d{4}',item)
                                                if len(erf)==0:
                                                    erfinder="unknown"
            
                                                else:
                                                    erfinder=erf[0]
                                            else:
                                                erfinder=lasttwo
                                            wfile.write(str(erfinder))
                                            wfile.write('\t')
                                    except:
                                        wfile.write("None")
                                                    
                                                    
                            

                                    wfile.write('\n')
                            else:
                                wfile.write(str(k))
                                wfile.write('\t')
                                wfile.write(str(year))
                                wfile.write('\t')
                                wfile.write("-1")
                                wfile.write('\t')
                                wfile.write("-1")
                                wfile.write('\n')
                                time.sleep(30)


                            
                    else:
                        number=0
                        wfile.write(str(k))
                        wfile.write('\t')
                        wfile.write(str(year))
                        wfile.write('\t')
                        wfile.write(str(number))
                        wfile.write('\t')
                        wfile.write("0")
                        wfile.write('\n')
                else:
                    number=0
                    wfile.write(str(k))
                    wfile.write('\t')
                    wfile.write(str(year))
                    wfile.write('\t')
                    wfile.write(str(number))
                    wfile.write('\t')
                    wfile.write("0")
                    wfile.write('\n')
            else:
                number=1001

                wfile.write(str(k))
                wfile.write('\t')
                wfile.write(str(year))
                wfile.write('\t')
                wfile.write(str(number))
                wfile.write('\t')
                wfile.write("0")
                wfile.write('\n')

                
                                               

            
            
        wfile.close()

driver.close()





