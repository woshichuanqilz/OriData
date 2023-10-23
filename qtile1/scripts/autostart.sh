#!/usr/bin/env bash
# ---
# Use "run program" to run it only if it is not already running
# Use "program &" to run it regardless
# ---
# NOTE: This script runs with every restart of AwesomeWM
# TODO: run_once


function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

run picom -CGb &
run feh --recursive --bg-fill --randomize ~/wallpaper/ori
run dunst
run /home/lizhe/OriNote/wikiScripts/Utils/GitPullNote.py
run cfw
run goldendict
run autokey-qt
run copyq
run fcitx

# run gammy
# run mathpix-snipping-tool
# run systemctl start mpd.service --user 
# run redshift -P -O 3600K
