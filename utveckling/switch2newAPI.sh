find www -name '*.js' | xargs grep -l 'garm-test.isof' | xargs sed -i.bak s/garm-test.isof.se/ull-test.isof.se/g
find www -name '*.js' | xargs grep -l 'garm.isof' | xargs sed -i.bak s/garm.isof.se/ull-test.isof.se/g
