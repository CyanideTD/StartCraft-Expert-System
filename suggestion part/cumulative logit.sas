proc logistic;
model LeagueIndex= age hoursperweek totalhours apm selectbyhotkeys assigntohotkeys uniquehotkeys minimapattacks 
minimaprightclicks numberofpacs gapbetweenpacs actionlatency actionsinpac totalmapexplored workersmade 
uniqueunitsmade complexunitsmade complexabilitiesused / scale=none aggregate;
run;
