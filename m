from='data/'$1
tmp='/sdcard/'$1
to='/data/local/'$1
echo $from
echo $tmp
echo $to
adb push $from $tmp
adb shell su -c mv $tmp $to 