const L = "\n";
iimPlayCode("TAB T=1" + L +"SET !ERRORIGNORE YES"  + L );

for (i = 1; i < 194; i++) {
    iimSet("loop", i);
    iimPlayCode("SET !ERRORIGNORE YES"  + L + "SET !DATASOURCE URL.csv" + L + "SET !DATASOURCE_LINE {{loop}}" + L + "URL GOTO={{!COL1}}" + L + "WAIT SECONDS=10" + L +"SAVEAS TYPE=HTM FOLDER=* FILE={{!COL1}}_{{!NOW:yyyymmdd_hhnnss}}" + L);
}
