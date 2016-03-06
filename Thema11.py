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
print Name1_informs

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
 print "Tweets ->", Name1_informsN[0]
 print "Following ->", Name1_informsN[1]
 print "Followers ->", Name1_informsN[2]
 print "Likes ->", Name1_informsN[3]
 print "****************" 
 print "****************"

#Web Scraping sto twitter gia to deutero onoma, xrhsh regular expression:
htmlfile = urllib.urlopen("https://twitter.com/"+name2+"")
htmltext = htmlfile.read()
regex = '<span class="ProfileNav-value" data-is-compact="(.*)">(.*)</span>'
pattern1 = re.compile(regex)
Name2_informs=re.findall(pattern1,htmltext)
print Name2_informs

#Epeidi logw ths entolhs HTML pou ethesa ws parametro sthn regex, oi plirofories pou epairne
#apo to twitter perilambane tis posotites twn 'tweets, following' ktlp mazi me true h' false
#kai tis ebgaze se ena pinaka sto stil : [('true' , '11.4K'),('false' , '281'),('true' , 1.84M),('false' , '3.960')]
#kai auto epeidh sto '<span class="ProfileNav-value" data-is-compact="(.*)">(.*)</span>' to prwto r.e '(.*)' antikathista 
#timh true h false (analoga), kai to deutero r.e '(.*)' antikathista thn timh twn tweet/following/followers/like analoga 
#tote me thn parakatw entolh afairw apo ton pinaka ths times true false wste na mou 
#dimiourgithei enas kainourgios pinakas sto stil : ['11.4K','281','1.84','3.960'] 
Name2_informsN = [i[1] for i in Name2_informs]

if len(Name2_informsN) == 4: 
 print name2,':'
 print "Tweets ->", Name2_informsN[0]
 print "Following ->", Name2_informsN[1]
 print "Followers ->", Name2_informsN[2]
 print "Likes ->", Name2_informsN[3]


#Sigkrish meta3i twn duo pinakwn Name1_informsN kai Name2_informsN 
#H sigkrish tha mporouse na ginei kai me for/while loop pou tha 
#htan pio euanagnwsto alla kai ligotero "bareto" alla protimhsa
#ta if elif 
sum1=0
sum2=0

BoolName1_informs = [item[0] for item in Name1_informs]
print BoolName1_informs
BoolName2_informs = [item[0] for item in Name2_informs]
print BoolName2_informs

for i in range(0,4):
   if BoolName1_informs[i] == 'true' and BoolName2_informs[i] == 'true':  
      a = [Name1_informsN[i],Name2_informsN[i]]
      numbers = {"K": 1000, "M": 1000000}
      result = []
      for value in a:
          if value:
             i = value[-1]
             value = float(value[:-1].replace('.','.'))*numbers[i]
             result.append(int(value))
print result
if max(result) == result[0]:
   sum1 +=1
elif max(result) == result[1]:
   sum2 +=1 

for i in range(0,4):
   if BoolName1_informs[i] == 'false' and BoolName2_informs[i] == 'false':
      a = [Name1_informsN[i],Name2_informsN[i]]      
      result = []
      for value in a:
          if value:
             i = value[-1]
             value = float(value[:-1].replace(',','.'))
             result.append(int(value))
      if max(result) == result[0]:
         sum1 +=1
      elif max(result) == result[1]:
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
 print "scoor",sum1,"-",sum2
elif sum2 > sum1 :
 print name2,"win"
 print "scoor",sum1,"-",sum2