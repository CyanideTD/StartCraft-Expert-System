data upgrade1_to_2;
set level1_to_level2;
if LeagueIndex=1 or LeagueIndex=2 then Lb=0;
else 
   Lb=1;
run;
proc logistic data=upgrade1_to_2 descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
data upgrade2_to_3;
set level2_to_level3;
if LeagueIndex=3 or LeagueIndex=4 or LeagueIndex=5 then Lb=0;
else 
   Lb=1;
run;
proc logistic data=upgrade2_to_3 descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
data upgrade3_to_4;
set level3_to_level4;
if LeagueIndex=6 or LeagueIndex=7 then Lb=0;
else 
   Lb=1;
run;
proc logistic data=upgrade3_to_4 descending;
model Lb =apm numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;

