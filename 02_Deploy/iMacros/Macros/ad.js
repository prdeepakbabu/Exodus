const L = "\n";
iimPlayCode("TAB T=1" + L +"SET !ERRORIGNORE YES"  + L );

for (i = 1; i < 130; i++) {
    iimSet("loop", i);
    iimPlayCode("SET !DATASOURCE URL.csv" + L + "SET !DATASOURCE_LINE {{loop}}" + L + "URL GOTO={{!COL1}}" + L + "WAIT SECONDS=15" + L +"SAVEAS TYPE=HTM FOLDER=* FILE={{!COL1}}_{{!NOW:yyyymmdd_hhnnss}}" + L);
}
