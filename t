# /bin/bash
perl -pi -e 's/\[  //g' data/raw.txt
perl -pi -e 's/\]//g' data/raw.txt
perl -pi -e 's/\./\-/g' data/raw.txt
java -jar translate.jar data/raw.txt data/evt.txt