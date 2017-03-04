data gtp;
set gold_to_platium;
if LeagueIndex=3 then Lb=0;
else 
   Lb=1;
run;
proc logistic data=gtp descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
