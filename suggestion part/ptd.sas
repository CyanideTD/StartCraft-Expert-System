data ptd;
set platium_to_diamond;
if LeagueIndex=4 then Lb=0;
else 
   Lb=1;
run;
proc logistic data=ptd descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
