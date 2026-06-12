# Switch map service api for javascript apps if needed
find www -name '*.js' | xargs grep -l 'ull.isof.se/folkeservice/api/lm' | xargs sed -i.bak s,ull.isof.se/folkeservice/api/lm,garm.isof.se/folkeservice/api/lm,g
find www -name '*.js' | xargs grep -l 'garm.isof.se/folkeservice/api/lm' | xargs sed -i.bak s,garm.isof.se/folkeservice/api/lm,ull.isof.se/folkeservice/api/lm,g
