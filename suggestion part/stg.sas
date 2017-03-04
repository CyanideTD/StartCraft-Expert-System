data stg;
set silver_to_gold;
if LeagueIndex=2 then Lb=0;
else 
   Lb=1;
run;
proc logistic data=stg descending;
model Lb =age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused  /selection=STEPWISE;
quit;
