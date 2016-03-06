import urllib
import re

print "WECLOME TO TWITTER ACOUNT COMPARSION"
#zhtaei ta 2 onomata apo ton xrhsth
name1 = raw_input("Type the first twitter name :")
name2 = raw_input("Type the second twitter name:")
print "Please Wait ..."

#Web Scraping sto twitter gia to prwto onoma, xrhsh regular expression:
htmlfile = urllib.urlopen("https://twitter.com/"+name1+"")
htmltext = htmlfile.read()
regex = '<span class="ProfileNav-value" data-is-compact="(.*)">(.*)</span>'
pattern = re.compile(regex)
Name1_informs=re.findall(pattern,htmltext)


#Epeidi logw ths entolhs HTML pou ethesa ws parametro sthn regex, oi plirofories pou epairne
#apo to twitter perilambane tis posotites twn 'tweets, following' ktlp mazi me true h' false
#kai tis ebgaze se ena pinaka sto stil : [('true' , '11.4K'),('false' , '281'),('true' , 1.84M),('false' , '3.960')]
#kai auto epeidh sto '<span class="ProfileNav-value" data-is-compact="(.*)">(.*)</span>' to prwto r.e '(.*)' antikathista 
#timh true h false (analoga), kai to deutero r.e '(.*)' antikathista thn timh twn tweet/following/followers/like analoga 
#tote me thn parakatw entolh afairw apo ton pinaka ths times true false wste na mou 
#dimiourgithei enas kainourgios pinakas sto stil : ['11.4K','281','1.84M','3.960'] 
Name1_informsN = [i[1] for i in Name1_informs]

if len(Name1_informsN) == 4: 
 print name1,':'
 print "Tweets -->", Name1_informsN[0]
 print "Following -->", Name1_informsN[1]
 print "Followers -->", Name1_informsN[2]
 print "Likes -->", Name1_informsN[3]
 print "*********************" 
 print "*********************"

#Web Scraping sto twitter gia to deutero onoma, xrhsh regular expression:
htmlfile = urllib.urlopen("https://twitter.com/"+name2+"")
htmltext = htmlfile.read()
regex = '<span class="ProfileNav-value" data-is-compact="(.*)">(.*)</span>'
pattern1 = re.compile(regex)
Name2_informs=re.findall(pattern1,htmltext)


#Epeidi logw ths entolhs HTML pou ethesa ws parametro sthn regex, oi plirofories pou epairne
#apo to twitter perilambane tis posotites twn 'tweets, following' ktlp mazi me true h' false
#kai tis ebgaze se ena pinaka sto stil : [('true' , '11.4K'),('false' , '281'),('true' , 1.84M),('false' , '3,960')]
#kai auto epeidh sto '<span class="ProfileNav-value" data-is-compact="(.*)">(.*)</span>' to prwto r.e '(.*)' antikathista 
#timh true h false (analoga), kai to deutero r.e '(.*)' antikathista thn timh twn tweet/following/followers/like analoga 
#tote me thn parakatw entolh afairw apo ton pinaka ths times true false wste na mou 
#dimiourgithei enas kainourgios pinakas sto stil : ['11.4K','281','1.84','3.960'] 
Name2_informsN = [i[1] for i in Name2_informs]

if len(Name2_informsN) == 4: 
 print name2,':'
 print "Tweets -->", Name2_informsN[0]
 print "Following -->", Name2_informsN[1]
 print "Followers -->", Name2_informsN[2]
 print "Likes -->", Name2_informsN[3]

######################################################### E3HGHSH GIA THN SUGKRISH ##########################################################
#############################################################################################################################################
#Oso afora thn sugkrish ginetai me periego tropo dld meta apo arkrto psa3imo diapistwsa oti o html kwdikas tou
#twitter kai sugkekrimena to link pou xrhsimopoihsa egw : <span class="ProfileNav-value" data-is-compact="(.*)">(.*)</span>
#to prwto r.e pou egrapsa to (.*) antikathista opws anefera timh true and flase kai sugkekrimena diapistwsa oti to true anaferete
#se arithous tipou px 11.4K h' 1.84M dld arithous pou ekfrazontai me ta K h' M enw to false anaferetai se arithous pou den ekfrazonatai
#me ton proigoumeno tropo  opws px: 281 3.960 ktlp. Gia thn sugkrish loipon xrhsimopoiw tous diktes true and false kathws tous ebala se 
#3exwristh lista me onoma BoolName1_informs gia to true false tou prwtou onomatos kai BoolName2_informs gia ta true false tou deuterou
#Epishs kanw mia metatroph tous arithmous se morfh K kai M wste na ginei h sugkrish mono otan einai kai oi duo diktes true dld einai 
#se morfh authn. Otan h mia timh einai true kai h allh false automata thetw ton antistoixo arithmo poy exei timh true sum1 +=1 xwris na kanw
#sugkrish antistoixa kai gia to anapodo

 
sum1=0
sum2=0

BoolName1_informs = [item[0] for item in Name1_informs]
BoolName2_informs = [item[0] for item in Name2_informs]



for i in range(0,4):
   if BoolName1_informs[i] == 'true' and BoolName2_informs[i] == 'true':  
      a = [Name1_informsN[i],Name2_informsN[i]]
      numbers = {"K": 1000, "M": 1000000}
      result = []
      for value in a:
          if value:
             i = value[-1]
             value = float(value[:-1].replace(',','.'))*numbers[i]
             result.append(int(value))
if max(result) == result[0]:
   sum1 +=1
elif max(result) == result[1]:
   sum2 +=1 

		  
for i in range(0,4):
   if BoolName1_informs[i] == 'false' and BoolName2_informs[i] == 'false':
      a = [Name1_informsN[i],Name2_informsN[i]]      
      result2 = []
      for value in a:
          if value:
             i = value[-1]
             value = float(value[:-1].replace(',','.'))*1000
             result2.append(int(value))
      if int(result2[0]) - int(result2[1]) > 0:
         sum1 +=1   
      elif int(result2[1]) - int(result2[0]) > 0:
         sum2 +=1
      	 


for i in range(0,4):
   if BoolName1_informs[i] == 'true' and BoolName2_informs[i] == 'false':
      sum1 +=1

for i in range(0,4):
   if BoolName1_informs[i] == 'false' and BoolName2_informs == 'true':
      sum2 +=1 
	
#Tsekarei poio sum einai megalitero wste na emfanizei analogo mnm gia to scoor
if sum1 > sum2 :
 print name1,"win"
 print "score",sum1,"-",sum2
elif sum2 > sum1 :
 print name2,"win"
 print "score",sum1,"-",sum2