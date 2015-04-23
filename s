# /bin/bash
#adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > data/screen.png
adb shell screencap | perl -pe 's/\x0D\x0A/\x0A/g' > data/screenshot.raw