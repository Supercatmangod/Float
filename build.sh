mkdir bin

gcc start_game.c -O3 -o ./bin/start-game
cp -r game ./bin/game

sudo apt install xterm
sudo pacman -S xterm

clear

echo Building Done.
echo Xterm Has Also Been Installed.
