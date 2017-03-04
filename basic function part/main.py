# -*- coding: utf-8 -*-
"""
Created on Thu May 05 21:30:12 2016

@author: Spock
"""
from sklearn.externals import joblib
import numpy as np
modle = joblib.load("train_model.m")
test=[0 for i in range(18)]
vab=[("Age:",0),("HoursPerWeek:",1),("TotalHours:",2),("APM:",3),("UniqueHotkeys:",6),("MinimapAttacks:",7),("MinimapRightClicks:",8),
     ("ActionsInPAC:",12),("TotalMapExplored:",13),("WorkersMade:",14),("UniqueUnitsMade:",15),
     ("ComplexUnitsMade:",16)]
'''
[("SelectByHotkeys:",4),("AssignToHotkeys:",5),
     ("UniqueHotkeys:",6),("MinimapAttacks:",7),("MinimapRightClicks:",8),("NumberOfPACs:",9),("GapBetweenPACs:",10),
     ("ActionLatency:",11),("ActionsInPAC:",12),("TotalMapExplored:",13),("WorkersMade:",14),("UniqueUnitsMade:",15),
     ("ComplexUnitsMade:",16),("ComplexAbilitiesUsed:",17)]
'''
linear={(0.00008552,-0.00571):(4,3),(0.00000250,0.00008041):(5,3),(0.00001244,0.00201):(9,3),(-0.18997,62.59690):(10,3),
        (-0.26755,95.05584):(17,16)}
        
        
s=["                     ◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇",
"                     ◆◇◆◇◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇",
"                     ◆◇◆◇◆◇◇◇◆◆◇◇◇◇◆◆◆◇◇◇◆◆◆◇◇◇◇◆◆◇◇◇◇◇◆◆",
"                     ◆◇◆◇◆◇◆◆◇◇◆◇◆◆◆◆◆◆◇◆◆◆◆◆◇◆◆◆◆◆◆◇◆◆◆◆",
"                     ◆◇◆◇◆◇◆◆◆◆◆◇◆◆◇◇◆◆◇◇◆◆◆◇◇◆◆◇◇◆◆◇◆◆◇◇",
"                     ◆◇◆◇◆◇◆◆◇◇◇◇◆◆◇◇◆◆◇◇◆◆◆◇◇◆◆◇◇◆◆◇◆◆◇◇",
"                     ◆◇◆◇◆◇◆◆◆◆◆◇◆◆◇◇◆◆◇◇◆◆◆◇◇◆◆◆◆◆◆◇◆◆◇◇",
"                     ◆◇◆◇◆◇◇◆◆◆◆◇◆◆◇◇◆◆◇◇◇◆◆◆◆◇◆◆◆◆◇◇◆◆◇◇"]
for i in s:
    print(i)
    
    
for i in vab:
    x=input(i[0])
    test[i[1]]=x
for k in linear:
    test[linear[k][0]]=k[0]*test[linear[k][1]]+k[1]
tes=np.array(test)
print(tes)
tes.shape=(1,18)
print(tes)
answer = modle.predict(tes)  
print(answer)

if (answer==[0.]):
    print("Level 1 : Bronze, Silver")
    print("Suggestion:You have to practice your ability to use hotkeys to control your units. For example, if you are protoss try to use BB to build a gateway instead of using your cursor. Once you master the skill using hotkeys, try to focus on the minimap. Use minimap to control your units to attack to explore and to harass. It saves plenty of time compared with  switching screen. You also have to be able to do multiple taskes at the same time. Use the hotkeys to  form multiple locations. Always remember to warp more probes when you have little pressure to defense.")
if (answer==[1.]):
    print("Level 2 : Gold, Platinum, Diamond")
    print("Suggestion:At this level you can master the skill to use hotkeys, to do multiple tasks at the same time. Now you have to move forward to the master of the starcraft. You have to be able to harass your enemy and build your troops at the same time. Meanwhile you have to try to think of the tactics to defeat your enemy. What kind of unit counter your emeny, what your enemy are doing. These are the questions you have to think deeply. You have to build various kind of units to accomplish your objective. You have to use their unique ability. You get to learn the combination of different kinds of units. Good Luck!")
if (answer==[2.]):
    print("Level 3 : Master, GrandMaster")
    print("Suggestion:If you are willing to step into the professional players` field, there is only one thing that differ you and your opponent, tactics. The basic skill is no longer a important factor, because every professional players spend hour thouands of hour practing their basic skill. You have to apply unpredictable tactics to defeat your enemy.")
if (answer==[3.]):
    print("Level 4 : Professional leagues")
    print("Suggestion:Just attent a real professional contest! ")
