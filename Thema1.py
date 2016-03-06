import random

#To epipedo 10*10 pou xreiazomaste gia thn ulopoihsh tou paixnidiou mas:

rtable=[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],
        [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],
        [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],
        [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],
        [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],
        [6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[6,8],[6,9],[6,10],
        [7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[7,9],[7,10],
        [8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8],[8,9],[8,10],
        [9,1],[9,2],[9,3],[9,4],[9,5],[9,6],[9,7],[9,8],[9,9],[9,10],
        [10,1],[10,2],[10,3],[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10]]

treasureP = random.choice(rtable)
player_start_position = random.choice(rtable)

######################################################################################################################################################################
################################################################# ODHGIES GIA THN KATANOHSH TOU KWDIKA ###############################################################

#Gia tis kinhseis tou paixti panw katw de3ia aristera, prosthaitw/afairw (analoga) apo thn tuxaia thesh pou dinei
#o upologisths sthn metablhth player_start_position (dhl thn thesh tou paixth) to zhtoumeno pou tha dwsei o paixths 
#kai otan lew zhtoumeno ennow opoia kinhsh apofashsei na kanei. Gia tis kinhseis autes ousiastika prosthetw 2 listes
#h mia einai h thesi tou paixti p.x h [2,3] kai h allh einai auto pou xreiazomai na prosthesw wste na exw kai to antistoixo apotelesma
#ths kinhshs pou thelei na kanei o paixteis px: an edwse to key U dld na paei mia thesi epanw tote an h thesi tou paixti einai h [2,3]
#pou edwsa san paradeigma proigoumenos tote prepei na prosthesw sthn lista [2,3] thn lista [-1,0] dld ousiastika prosteto to antitheto tou 
#1 to -1 kai sto 3 to 0 wste na paei sthn [1,3] pou einai h "epanw" thesh. Oson afora tis kathodigiseis pou kanw dld ta minimata pou emfanizei 
#ston xrhsth to programma einai: 1o "You are Close" ean h thesi tou paixth einai sthn idia grammh h sthlh (analoga) kai diaferoun kata 2 theseis 
#px an einai o paixths sthn thesi [2,3] kai o thisauros einai sthn [2,5]. To 2o mnm einai "You are Close Enough" opws sto prwto me thn diafora oti emfanizetai  
#an diaferoun kata mia thesi. Trito minima einai "Not even close" otan h thesi tou paixth me thn thesh tou thusaurou, den exoun kanena koino stoixeio. 
#px player_start_position = [2,3] kai treasureP[8,9] edw blepoume pws player_start_position[0] != treasureP[0] kai player_start_position[1] != treasureP[1]
#Tetarto minima einai to "Not so Close" kai emfanizetai otan o paixths kai o thusauros exoun ena koino stoixeio px player_start_position = [2,3] kai treasureP = [2,7]
#Pempto minima einai to "Maybe Close" kai emfanizetai otan o paixths kai o thusauros exoun koino stoixeio kai apexoun 3 theseis opws kai sta alla 2 proigoumena minimata 
#Ekto minima einai to "You can go Left/Right/Up/Down here" analoga kai emfanizetai otan paixths ftanei stis akres tou pinaka kai tinei na "figei" apo ton pinaka
#Oi sigkriseis ginontai me if elif else kai sigkrinontai ta stoixeia twn pinakwn treasureP (= thesi thusaurou) kai player_start_position (= thesi paixth), mias kai oi theseis
#tous einai pinakes 2,2. Xrhsimopoiountai epeishs merika brake kai auto epeidh ginetai prospatheia sugxrwnsimou ton minimatwn oso to dunaton kalitera kai kaliptoun pisteuw
#oles tis periptwseis. Telos xrhsimopoieitai ena for loop kai auto epishs gia thn emfanish minimatwn pou sxetizonati me tis 2 theseis dld tou paixth kai tou thusaurou.
    

#Analoga minimata kai kena wste na ginetai poio "omorfo" to grafiko periballon
print "WELCOME TO HIDDEN TREASURE GAME"
print ""
print "Press ENTER to Start !!"

help_key = raw_input("Type H for view Help Messenger:")

if help_key == "H":
 print "Your position and treasure's position are hidden"
 print "So you have to move around and find the treasure"
 print "You can move by pressing  U , D , L or R "
 print "U for Up , D for Down , L for Left or R for Right"
 print "If you are pressing any other key you will not move"
 print "and you will remain at the current position. You can move"
 print "between 100 places but your position will remain hidden."
 print "Messengers will help you to understand if you are close"
 print "with treasure or not"
 print "Good Luck and Have Fun !!"
 
print ""
print "******************* S T A R T ******************"
print ""
print "Move : U for Up , D for Down , L for Left or R for Right"
print ""
#print player_start_position
#print treasureP

while treasureP != player_start_position :

  key = raw_input('Move :')
#******************KEY == "U"*******************
#***********************************************
  if key == "U" :
    list=[-1,0]
    player_start_position = [x + y for x, y in zip(player_start_position, list)]
	#Kathws afairw -1 apo to prwto stoixeio ths listas player_start_position kapoia stigmh
	#tha ftasei na einai sthn seira 1 kai tote me mia akomi entoli U tha mas paei sthn seira 0, -1
	#ktlp pragma pou den theloume mias kai to epipedo tou paixnidiou einai 10*10
    if player_start_position[0] == 0:
     list1 = [1,0]	
     player_start_position = [x + y for x, y in zip(player_start_position, list1)]
     print "You cant go Up here"
     print ""
	#Sigriseis gia ta analoga minimata 
    if player_start_position[0] == treasureP[0] and player_start_position[1]==treasureP[1]-2:
      if treasureP == player_start_position :
        break 	 
      print "You are CLOSE!!"
      print ""
    elif player_start_position[0] == treasureP[0] and treasureP[1]==player_start_position[1]-2:
      if treasureP == player_start_position :
        break 	 
      print "You are CLOSE!!"
      print ""
    elif player_start_position[1] == treasureP[1] and player_start_position[0]==treasureP[0]-2:
      if treasureP == player_start_position :
        break
      print "You are CLOSE!!"
      print ""
    elif player_start_position[1] == treasureP[1] and treasureP[0]==player_start_position[0]-2:
      if treasureP == player_start_position :
        break
      print "You are CLOSE!!"
      print ""
    elif player_start_position[0] == treasureP[0] and player_start_position[1]==treasureP[1]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[0] == treasureP[0] and treasureP[1]==player_start_position[1]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[1] == treasureP[1] and player_start_position[0]==treasureP[0]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[1] == treasureP[1] and treasureP[0]==player_start_position[0]-1 :
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    if player_start_position[0] != treasureP[0] and player_start_position[1] != treasureP[1] :
	 print "Not even close!!"
	 print ""
    if player_start_position[0] == treasureP[0]:
     if player_start_position[1]==treasureP[1]-3:
      print "Maybe Close"
     elif treasureP[1]==player_start_position[1]-3:
      print "Maybbe Close"
    if player_start_position[1] == treasureP[1]:
     if player_start_position[0]==treasureP[0]-3:
      print "Maybe Close"
     elif treasureP[0]==player_start_position[0]-3:
      print "Maybbe Close"
    for i in range (4,11):
     if player_start_position[1]==treasureP[1]:
      if player_start_position[0]==treasureP[0]-i:
       print "Not so Close!!"
      elif treasureP[0]==player_start_position[0]-i:
       print "Not so Close!!"
     if player_start_position[0]==treasureP[0]:
      if player_start_position[1]==treasureP[1]-i:
       print "Not so Close!!"
      elif treasureP[1]==player_start_position[1]-i: 
	   print "Not so Close!!"
 
#******************KEY == "D"*******************
#*********************************************** 
  elif key == "D" :
    list=[1,0]
    player_start_position = [x + y for x, y in zip(player_start_position, list)]
	#Kathws prosthaitw +1 sto prwto stoixeio ths listas player_start_position kapoia stigmh
	#tha ftasei na einai sthn seira 10 kai tote mia entolh D tha mas paei sthn seira 11, 12 ktlp 
	#pragma pou den theloume mias kai to epipedo tou paixnidiou einai 10*10
    if player_start_position[0] == 11:
	 list1 = [-1,0]
	 player_start_position = [x + y for x, y in zip(player_start_position, list1)]
	 print "You cant go Down here"
	 print ""
	 #Sigriseis gia ta analoga minimata 
    if player_start_position[0] == treasureP[0] and player_start_position[1]==treasureP[1]-2:
      if treasureP == player_start_position :
        break 	 
      print "You are CLOSE!!"
      print ""
    elif player_start_position[0] == treasureP[0] and treasureP[1]==player_start_position[1]-2:
      if treasureP == player_start_position :
        break 	 
      print "You are CLOSE!!"
      print ""
    elif player_start_position[1] == treasureP[1] and player_start_position[0]==treasureP[0]-2:
      if treasureP == player_start_position :
        break
      print "You are CLOSE!!"
      print ""
    elif player_start_position[1] == treasureP[1] and treasureP[0]==player_start_position[0]-2:
      if treasureP == player_start_position :
        break
      print "You are CLOSE!!"
      print ""
    elif player_start_position[0] == treasureP[0] and player_start_position[1]==treasureP[1]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[0] == treasureP[0] and treasureP[1]==player_start_position[1]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[1] == treasureP[1] and player_start_position[0]==treasureP[0]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[1] == treasureP[1] and treasureP[0]==player_start_position[0]-1 :
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    if player_start_position[0] != treasureP[0] and player_start_position[1] != treasureP[1] :
     print "Not even close!!"
     print ""
    if player_start_position[0] == treasureP[0]:
     if player_start_position[1]==treasureP[1]-3:
      print "Maybe Close"
     elif treasureP[1]==player_start_position[1]-3:
      print "Maybbe Close"
    if player_start_position[1] == treasureP[1]:
     if player_start_position[0]==treasureP[0]-3:
      print "Maybe Close"
     elif treasureP[0]==player_start_position[0]-3:
      print "Maybbe Close"
    for i in range (4,11):
     if player_start_position[1]==treasureP[1]:
      if player_start_position[0]==treasureP[0]-i:
       print "Not so Close!!"
      elif treasureP[0]==player_start_position[0]-i:
       print "Not so Close!!"
     if player_start_position[0]==treasureP[0]:
      if player_start_position[1]==treasureP[1]-i:
       print "Not so Close!!"
      elif treasureP[1]==player_start_position[1]-i: 
	   print "Not so Close!!"
  
#******************KEY == "L"*******************
#***********************************************
  elif key == "L" :
    list=[0,-1]
    player_start_position = [x + y for x, y in zip(player_start_position, list)]
	#Kathws afairw -1 apo to deutero stoixeio ths listas player_start_position kapoia stigmh
	#tha ftasei na einai sthn sthlh 1 kai tote me mia akomi entoli L tha mas paei sthn sthlh 0, -1
	#ktlp pragma pou den theloume mias kai to epipedo tou paixnidiou einai 10*10
    if player_start_position[1] == 0:
	list1 = [0,1]
	player_start_position = [x + y for x, y in zip(player_start_position, list1)]
	print "You cant go Left here"
	print ""
	#Sigriseis gia ta analoga minimata 
    if player_start_position[0] == treasureP[0] and player_start_position[1]==treasureP[1]-2:
      if treasureP == player_start_position :
        break 	 
      print "You are CLOSE!!"
      print ""
    elif player_start_position[0] == treasureP[0] and treasureP[1]==player_start_position[1]-2:
      if treasureP == player_start_position :
        break 	 
      print "You are CLOSE!!"
      print ""
    elif player_start_position[1] == treasureP[1] and player_start_position[0]==treasureP[0]-2:
      if treasureP == player_start_position :
        break
      print "You are CLOSE!!"
      print ""
    elif player_start_position[1] == treasureP[1] and treasureP[0]==player_start_position[0]-2:
      if treasureP == player_start_position :
        break
      print "You are CLOSE!!"
      print ""
    elif player_start_position[0] == treasureP[0] and player_start_position[1]==treasureP[1]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[0] == treasureP[0] and treasureP[1]==player_start_position[1]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[1] == treasureP[1] and player_start_position[0]==treasureP[0]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[1] == treasureP[1] and treasureP[0]==player_start_position[0]-1 :
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    if player_start_position[0] != treasureP[0] and player_start_position[1] != treasureP[1] :
     print "Not even close!!"
     print ""	
    if player_start_position[0] == treasureP[0]:
     if player_start_position[1]==treasureP[1]-3:
      print "Maybe Close"
     elif treasureP[1]==player_start_position[1]-3:
      print "Maybbe Close"
    if player_start_position[1] == treasureP[1]:
     if player_start_position[0]==treasureP[0]-3:
      print "Maybe Close"
     elif treasureP[0]==player_start_position[0]-3:
      print "Maybbe Close"
    for i in range (4,11):
     if player_start_position[1]==treasureP[1]:
      if player_start_position[0]==treasureP[0]-i:
       print "Not so Close!!"
      elif treasureP[0]==player_start_position[0]-i:
       print "Not so Close!!"
     if player_start_position[0]==treasureP[0]:
      if player_start_position[1]==treasureP[1]-i:
       print "Not so Close!!"
      elif treasureP[1]==player_start_position[1]-i: 
	   print "Not so Close!!"	 
     
#******************KEY == "R"*******************
#***********************************************
  elif key == "R" :    
    list=[0,1]
    player_start_position = [x + y for x, y in zip(player_start_position, list)]
	#Kathws prosthaitw +1 sto deuetro stoixeio ths listas player_start_position kapoia stigmh
	#tha ftasei na einai sthn sthlh 10 kai tote mia entolh R tha mas paei sthn sthlh 11, 12 ktlp 
	#pragma pou den theloume mias kai to epipedo tou paixnidiou einai 10*10
    if player_start_position[1] == 11:
	list1 = [0,-1]
	player_start_position = [x + y for x, y in zip(player_start_position, list1)]
	print "You cant go Right Here"
	print ""
	#Sigriseis gia ta analoga minimata 
    if player_start_position[0] == treasureP[0] and player_start_position[1]==treasureP[1]-2:
      if treasureP == player_start_position :
        break 	 
      print "You are CLOSE!!"
      print ""
    elif player_start_position[0] == treasureP[0] and treasureP[1]==player_start_position[1]-2:
      if treasureP == player_start_position :
        break 	 
      print "You are CLOSE!!"
      print ""
    elif player_start_position[1] == treasureP[1] and player_start_position[0]==treasureP[0]-2:
      if treasureP == player_start_position :
        break
      print "You are CLOSE!!"
      print ""
    elif player_start_position[1] == treasureP[1] and treasureP[0]==player_start_position[0]-2:
      if treasureP == player_start_position :
        break
      print "You are CLOSE!!"
      print ""
    elif player_start_position[0] == treasureP[0] and player_start_position[1]==treasureP[1]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[0] == treasureP[0] and treasureP[1]==player_start_position[1]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[1] == treasureP[1] and player_start_position[0]==treasureP[0]-1:
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    elif player_start_position[1] == treasureP[1] and treasureP[0]==player_start_position[0]-1 :
      if treasureP == player_start_position :
        break
      print "You are CLOSE enough!!"
      print ""
    if player_start_position[0] != treasureP[0] and player_start_position[1] != treasureP[1] :
	 print "Not even close!!"
	 print ""
    if player_start_position[0] == treasureP[0]:
     if player_start_position[1]==treasureP[1]-3:
      print "Maybe Close"
     elif treasureP[1]==player_start_position[1]-3:
      print "Maybbe Close"
    if player_start_position[1] == treasureP[1]:
     if player_start_position[0]==treasureP[0]-3:
      print "Maybe Close"
    elif treasureP[0]==player_start_position[0]-3:
	 print "Maybe Close"
    for i in range (4,11):
     if player_start_position[1]==treasureP[1]:
      if player_start_position[0]==treasureP[0]-i:
       print "Not so Close!!"
      elif treasureP[0]==player_start_position[0]-i:
       print "Not so Close!!"
     if player_start_position[0]==treasureP[0]:
      if player_start_position[1]==treasureP[1]-i:
       print "Not so Close!!"
      elif treasureP[1]==player_start_position[1]-i: 
	   print "Not so Close!!"
  
  

  
  	 

print"Congratulations you find the treasure !!!"  