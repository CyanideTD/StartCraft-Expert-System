
data siklllevel1;
set skill;
if LeagueIndex=1 or LeagueIndex=2 then Lb=1;
else 
   Lb=0;
run;
data siklllevel2;
set skill;
if LeagueIndex=3 or LeagueIndex=4 or LeagueIndex=5 then Lb=1;
else 
   Lb=0;
run;
data siklllevel3;
set skill;
if LeagueIndex=6 or LeagueIndex=7 then Lb=1;
else 
   Lb=0;
run;
data sikllpro;
set skill;
if LeagueIndex=8 then Lb=1;
else 
   Lb=0;
run;

proc logistic data=siklllevel1 descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
proc logistic data=siklllevel2 descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
proc logistic data=siklllevel3 descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
proc logistic data=sikllpro descending;
model Lb =apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
