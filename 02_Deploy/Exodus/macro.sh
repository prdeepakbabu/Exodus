Xvfb :19 -screen 0 1024x768x16 &
export DISPLAY=:19
firefox "imacros://run/?m=ad.js" && touch /home/dev/Exodus/started.txt

