#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:53:37 2020

@author: internet
"""
import numpy
from numpy import array
#from math import *
import math

def entropy(ccc,ddd):
    x=0
    if ccc!=ddd:
        x=-(ddd/ccc)*math.log2(ddd/ccc)-((ccc-ddd)/ccc)*math.log2((ccc-ddd)/ccc)
    return (x)


#chart for the applying decision tree
a =array([
    ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast','overcast', 'rainy'],
    ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool','mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
	['high', 'high', 'high', 'high', 'normal', 'normal', 'normal','high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    ['weak', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong','weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'strong'],
	[0,0,1,1,1,0,1,0,1,1,1,1,1,0]
    ])
print(a)
print(" ")
print(" ")
print("")



#step 0 find the total entropy which called E(s)
print("#step 0:find the total entropy which called E(s)")
c=0
d=0
for b in a[4]:
    c=1+c
    d=d+int(b)
entropy(c,d)
print(" ")
print("  total entropy of the system:", entropy(c,d))
print(" ")
print(" ")
print("")



#step 1 find each columns E, Info and Infografic Gain (IG)
print("#step 1: find each columns E, Info and Infografic Gain (IG)")
      
   #outlook
print("")
print("      outlook")
sunny=0
rainy=0
overcast=0
for line in a[0]:
    k=line.split()
    if 'sunny' in k:
        sunny=sunny+1
    elif 'rainy' in k:
        rainy=rainy+1
    elif 'overcast' in k:
        overcast=overcast+1

dd=[]
cc=-1
uu=[]
for bb in a[4]:
    cc=1+cc
    if int(bb)==1:
        dd=dd+[cc]
        uu=uu+[a[0][dd.pop()]]

ssunny=0
rrainy=0
oovercast=0
for lline in uu:
    kk=lline.split()
    if 'sunny' in kk:
        ssunny=ssunny+1
    elif 'rainy' in kk:
        rrainy=rrainy+1
    elif 'overcast' in kk:
        oovercast=oovercast+1
print(" ")
print("  sunny true are :",ssunny)
print("  rainy true are :",rrainy)
print("  overcast true are :",oovercast)
print(" ")

sunny_no=sunny-ssunny
rainy_no=rainy-rrainy
overcast_no=overcast-oovercast
print("  sunny no are:",sunny_no)
print("  rainy no are:",rainy_no)
print("  overcast no are:",overcast_no)
print(" ")

sunny_entropy=-(ssunny/sunny)*math.log2((ssunny/sunny)+0.0001)-((sunny-ssunny)/sunny)*math.log2(((sunny-ssunny)/sunny)+0.0001)
print("  sunny entropy:",sunny_entropy)
rainy_entropy=-(rrainy/rainy)*math.log2((rrainy/rainy)+0.0001)-((rainy-rrainy)/rainy)*math.log2(((rainy-rrainy)/rainy)+0.0001)
print("  rainy entropy:",rainy_entropy)
overcast_entropy=-(oovercast/overcast)*math.log2((oovercast/overcast)+0.0001)-((overcast-oovercast)/overcast)*math.log2(((overcast-oovercast)/overcast)+0.0001)
print("  overcast entropy:",overcast_entropy)
print(" ")

info=(sunny/c)*sunny_entropy+(rainy/c)*rainy_entropy+(overcast/c)*overcast_entropy
print("  outlook info:",info)
outlook_info_gain=entropy(c,d)-info
print("  outlook infografic gain:",outlook_info_gain)
print(" ")


   #temperature
print("")
print("      temperature")

hot=0
mild=0
cool=0
for line in a[1]:
    k=line.split()
    if 'hot' in k:
        hot=hot+1
    elif 'mild' in k:
        mild=mild+1
    elif 'cool' in k:
        cool=cool+1

dd2=[]
cc2=-1
uu2=[]
for bb2 in a[4]:
    cc2=1+cc2
    if int(bb2)==1:
        dd2=dd2+[cc2]
        uu2=uu2+[a[1][dd2.pop()]]

hhot=0
mmild=0
ccool=0
for llline in uu2:
    kkk=llline.split()
    if 'hot' in kkk:
        hhot=hhot+1
    elif 'mild' in kkk:
        mmild=mmild+1
    elif 'cool' in kkk:
        ccool=ccool+1
print(" ")
print("  hot true are :",hhot)
print("  mild true are :",mmild)
print("  cool true are :",ccool)
print(" ")

hot_no=hot-hhot
mild_no=mild-mmild
cool_no=cool-ccool
print("  hot no are:",hot_no)
print("  mild no are:",mild_no)
print("  cool no are:",cool_no)
print(" ")

hot_entropy=-(hhot/hot)*math.log2((hhot/hot)+0.0001)-((hot-hhot)/hot)*math.log2(((hot-hhot)/hot)+0.0001)
print("  hot entropy:",hot_entropy)
mild_entropy=-(mmild/mild)*math.log2((mmild/mild)+0.0001)-((mild-mmild)/mild)*math.log2(((mild-mmild)/mild)+0.0001)
print("  mild entropy:",mild_entropy)
cool_entropy=-(ccool/cool)*math.log2((ccool/cool)+0.0001)-((cool-ccool)/cool)*math.log2(((cool-ccool)/cool)+0.0001)
print("  cool entropy:",cool_entropy)
print(" ")

iinfo=(hot/c)*hot_entropy+(mild/c)*mild_entropy+(cool/c)*cool_entropy
print("  outlook info:",iinfo)
temperature_info_gain=entropy(c,d)-iinfo
print("  outlook infografic gain:",temperature_info_gain)
print(" ")


   #humidity
print("")
print("      humidity")
high=0
normal=0
for line in a[2]:
    k=line.split()
    if 'high' in k:
        high=high+1
    elif 'normal' in k:
        normal=normal+1

dd3=[]
cc3=-1
uu3=[]
for bb3 in a[4]:
    cc3=1+cc3
    if int(bb3)==1:
        dd3=dd3+[cc3]
        uu3=uu3+[a[2][dd3.pop()]]

hhigh=0
nnormal=0
for lllline in uu3:
    kkkk=lllline.split()
    if 'high' in kkkk:
        hhigh=hhigh+1
    elif 'normal' in kkkk:
        nnormal=nnormal+1
print(" ")
print("  high true are :",hhigh)
print("  normal true are :",nnormal)
print(" ")

high_no=high-hhigh
normal_no=normal-nnormal
print("  high no are:",high_no)
print("  normal no are:",normal_no)
print(" ")

high_entropy=-(hhigh/high)*math.log2((hhigh/high)+0.0001)-((high-hhigh)/high)*math.log2(((high-hhigh)/high)+0.0001)
print("  high entropy:",high_entropy)
normal_entropy=-(nnormal/normal)*math.log2((nnormal/normal)+0.0001)-((normal-nnormal)/normal)*math.log2(((normal-nnormal)/normal)+0.0001)
print("  normal entropy:",normal_entropy)
print(" ")

iiinfo=(high/c)*high_entropy+(normal/c)*normal_entropy
print("  humidity info:",iiinfo)
humidity_info_gain=entropy(c,d)-iiinfo
print("  humidity infografic gain:",humidity_info_gain)
print(" ")


   #windy
print("")
print("      windy")

strong=0
weak=0
for line in a[3]:
    k=line.split()
    if 'strong' in k:
        strong=strong+1
    elif 'weak' in k:
        weak=weak+1

dd4=[]
cc4=-1
uu4=[]
for bb4 in a[4]:
    cc4=1+cc4
    if int(bb4)==1:
        dd4=dd4+[cc4]
        uu4=uu4+[a[3][dd4.pop()]]

sstrong=0
wweak=0
for lllline in uu4:
    kkkk=lllline.split()
    if 'strong' in kkkk:
        sstrong=sstrong+1
    elif 'weak' in kkkk:
        wweak=wweak+1
print(" ")
print("  strong true are :",sstrong)
print("  weak true are :",wweak)
print(" ")

strong_no=strong-sstrong
weak_no=weak-wweak
print("  strong no are:",strong_no)
print("  weak no are:",weak_no)
print(" ")

strong_entropy=-(sstrong/strong)*math.log2((sstrong/strong)+0.0001)-((strong-sstrong)/strong)*math.log2(((strong-sstrong)/strong)+0.0001)
print("  strong entropy:",strong_entropy)
weak_entropy=-(wweak/weak)*math.log2((wweak/weak)+0.0001)-((weak-wweak)/weak)*math.log2(((weak-wweak)/weak)+0.0001)
print("  weak entropy:",weak_entropy)
print(" ")

iiiinfo=(strong/c)*strong_entropy+(weak/c)*weak_entropy
print("  windy info:",iiiinfo)
windy_info_gain=entropy(c,d)-iiiinfo
print("  windy infografic gain:",windy_info_gain)
print(" ")
print("")
print("")



#step 2 compare each columns IG
print("#step 2: compare each columns IG")
print("")
print("  outlook IG:",outlook_info_gain)
print("  temperature IG:",temperature_info_gain)
print("  humidity IG:",humidity_info_gain)
print("  windy IG:",windy_info_gain)
print("")
if  outlook_info_gain>temperature_info_gain and outlook_info_gain>humidity_info_gain and outlook_info_gain>windy_info_gain:
    ig="outlook"
if temperature_info_gain>outlook_info_gain and temperature_info_gain>humidity_info_gain and temperature_info_gain>windy_info_gain:
    ig="temperature"
if humidity_info_gain>outlook_info_gain and humidity_info_gain>temperature_info_gain and humidity_info_gain>windy_info_gain:
    ig="humidity"
if windy_info_gain>outlook_info_gain and windy_info_gain>temperature_info_gain and windy_info_gain>humidity_info_gain:
    ig="windy"
print("")
print("")



#step 3 show which column become root node and which column interior node
print("#step 3: show which column become root node")
print("")
print(" ROOT NODE IS: ",ig,"       (note: this codes include functions and stack)")
print("")
print("")



#step 4 show which column interior node
print("")
print("#step 4: show which column become interior node")
print("")

if ig=="outlook":
    matrix=a[0]
    mt1=a[1]
    mt2=a[2]
    mt3=a[3]
    
    abc1="temperature"
    abc2="humidity"
    abc3="windy"
    
    
    word1a="hot"
    word1b="mild"
    word1c="cool"
    word2a="high"
    word2b="normal"
    word3a="strong"
    word3b="weak"
    
    name1="sunny"
    name11=sunny
    total1=sunny
    positive1=ssunny
    negative1=sunny_no
    es=entropy(sunny,ssunny)
    
    name2="rainy"
    total2=rainy
    positive2=rrainy
    negative1=rainy_no
    er=entropy(rainy,rrainy)
    
    name3="overcast"
    total3=overcast
    positive3=oovercast
    negative3=overcast_no
    eo=entropy(overcast,oovercast)
    
elif ig=="temperature":
    matrix=a[1]
    mt1=a[0]
    mt2=a[2]
    mt3=a[3]
    
    
    abc1="outlook"
    abc2="humidity"
    abc3="windy"
    
    
    word1a="sunny"
    word1b="rainy"
    word1c="overcast"
    word2a="high"
    word2b="normal"
    word3a="strong"
    word3b="weak"
    
    name1="hot"
    total1=hot
    positive1=hhot
    negative1=hot_no
    es=entropy(hot,hhot)
    
    name2="mild"
    total2=mild
    positive2=mmild
    negative2=mild_no
    er=entropy(mild,mmild)
    
    name3="cool"
    total3=cool
    positive3=ccool
    negative=cool_no
    eo=entropy(cool,ccool)
    
elif ig=="humidity":
    matrix=a[2]
    mt1=a[0]
    mt2=a[1]
    mt3=a[3]
      
    abc1="outlook"
    abc2="temperature"
    abc3="windy"
    
    
    word1a="sunny"
    word1b="rainy"
    word1c="overcast"
    word2a="hot"
    word2b="mild"
    word3a="cool"
    word3b="strong"
    word3c="weak"
    
    name1="high"
    total1=high
    positive1=hhigh
    negative1=high_no
    es=entropy(high,hhigh)
    
    name2="normal"
    total2=normal
    positive2=nnormal
    negative2=normal_no
    er=entropy(normal,nnormal)
    
elif ig=="windy":
    matrix=a[3]
    mt1=a[0]
    mt2=a[1]
    mt3=a[2]
    
    abc1="outlook"
    abc2="temperature"
    abc3="humidity"
    
    word1a="sunny"
    word1b="rainy"
    word1c="overcast"
    word2a="hot"
    word2b="mild"
    word3a="cool"
    word3b="high"
    word3c="normal"
    
    total1=strong
    positive1=sstrong
    negative1=strong_no
    es=entropy(strong,sstrong)
    
    windy2="weak"
    total2=weak
    positive2=wweak
    negative2=weak_no
    er=entropy(weak,wweak)


   #1.interior node

print("  1.interior node entropy:",es)

if es==0:
    if positive1<negative1:
        print("   (due to zero entropy",name1,"directly goes to leaf node (with no))")
    if positive1>negative1:
        print("   (due to zero entropy ",name1,"directly goes to leaf node (with yes))")
else:  
    print("kurtarma")
     
      #1. under group of 1.interior node  
xdd=[]
xcc=-1
xuu=[]
for xbb in matrix:
    xcc=1+xcc
    if str(xbb)==name1:
        xdd=xdd+[xcc]
        xuu=xuu+[mt2[xdd.pop()]]
print(xuu)

wrd=0
wrd2=0

for llline in xuu:
    kkk=llline.split()
    if word2a in kkk:
        wrd=wrd+1
    elif word2b in kkk:
        wrd2=wrd2+1

print(" ")
print("  ",word2a,"  are :",wrd)
print("  ",word2b,"  are :",wrd2)
print(" ")

xddd=[]
xccc=-1
xuuu=[]
for xbbb in a[4]:
    xccc=1+xccc
    if int(xbbb)==1:
        xddd=xddd+[xccc]
        xuuu=xuuu+[mt2[xddd.pop()]]
print(xuuu)

xdddd=[]
xcccc=-1
xuuuu=[]
for xbbbb in a[4]:
    xcccc=1+xcccc
    if int(xbbbb)==1:
        xdddd=xdddd+[xcccc]
        xuuuu=xuuuu+[matrix[xdddd.pop()]]
print(xuuuu)

xddddd=[]
xccccc=-1
xuuuuu=[] #in sunny in humidity in normal 2 yes
for xbbbbb in xuuuu:
    xccccc=1+xccccc
    if str(xbbbbb)==name1:
        xddddd=xddddd+[xccccc]
        xuuuuu=xuuuuu+[xuuu[xddddd.pop()]]
print(xuuuuu)


ffs_value=0
for llline in xuuuuu:
    kkk=llline.split()
    if word2b in kkk:
        ffs_value=ffs_value+1
print(ffs_value)
        #---------------------------------------------
xdddddd=[]
xcccccc=-1
xuuuuuu=[]
for xbbbbbb in a[4]:
    xcccccc=1+xcccccc
    if int(xbbbbbb)==0:
        xdddddd=xdddddd+[xcccccc]
        xuuuuuu=xuuuuuu+[matrix[xdddddd.pop()]]
print(xuuuuuu)

fff_value=0
for llline in xuuuuuu:
    kkk=llline.split()
    if name1 in kkk:
        fff_value=fff_value+1
print(fff_value)


if name11==fff_value+ffs_value:
    fff_value_entropy=0
    print("  fff entropy:0")
    ffs_value_entropy=0
    print("  ffs entropy:0")
else:
    fff_value_entropy=entropy(fff_value+ffs_value,fff_value)
    print("  fff entropy:",fff_value)
    ffs_value_entropy=entropy(fff_value+ffs_value,ffs_value)
    print("  ffs entropy:",ffs_value_entropy)

ff_info=(fff_value/name11)*fff_value_entropy+(ffs_value/name11)*ffs_value_entropy
print(" ff outlook info:",ff_info)
ff_outlook_info_gain=es-ff_info
print("  ff outlook infografic gain:",ff_outlook_info_gain,"after root node division(",name1,")","interior node:",abc2)
print(" ")



      #2. under group of 1.interior node


      #3. under group of 1.interior node


      #max IG under group


print(" 1. interior node:")
      
print("")


   #2.interior node
print("")

print("  2.interior node total entropy:",er)

if er==0:
    if positive2<negative2:
        print("   (due to zero entropy ",name2,"directly goes to leaf node (with no))")
    if positive2>negative2:
        print("   (due to zero entropy ",name2,"directly goes to leaf node (with yes))")
else:
    print("kurtarma")
      #1. under group of 2.interior node


      #2. under group of 2.interior node


      #3. under group of 2.interior node


      #max IG under group


print("")    


   #3.interior node
print("")
if er!=entropy(normal,nnormal) or er!=entropy(weak,wweak):
    print("  3.interior node total entropy:",eo)
    
    if eo==0:
        if positive3<negative3:
            print("   (due to zero entropy ",name3,"directly goes to leaf node (with no))")
        if positive3>negative3:
            print("   (due to zero entropy ",name3,"directly goes to leaf node (with yes))")
else:
    print("kurtarma")
      #1. under group of 3.interior node


      #2. under group of 3.interior node


      #3. under group of 3.interior node


      #max IG under group


print("")
print("")



#step 5 show the leaf nodes and general decision tree
print("")
print("#step 5: show the leaf node and general decision tree")
print("")
print(" ROOT NODE IS: ",ig,"       (note: this codes include functions and stack)")
print("  ff outlook infografic gain:",ff_outlook_info_gain,"after root node division        interior node:   leaf nodes:   -no     -yes ")
print("sf outlook infografic gain:",es,"after root node division          interior node:    leaf nodes:     -no      -yes")
#Erdem Erbaba

