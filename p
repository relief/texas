while true
do 
echo ------------------------------------------
adb shell screencap | perl -pe 's/\x0D\x0A/\x0A/g' > data/screenshot.raw;  # slow 2.6s
python img.py  #slow 1.38s
./r qipai > /dev/null
sleep 10
done



