data mtgr;
set master_to_grandmaster;
if LeagueIndex=6 then Lb=0;
else 
   Lb=1;
run;
proc logistic data=mtgr descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
