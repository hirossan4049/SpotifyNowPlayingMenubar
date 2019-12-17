import rumps
import datetime
import subprocess
import osascript

TIMER_MODE = 'timer'
go_home_time = '18:00:00'
track_osa = 'tell application "Spotify" to name of current track as string'
artist_osa = 'tell application "Spotify" to artist of current track as string'
play_stop_osa = 'tell application "Spotify" to playpause'
next_osa = 'tell application "Spotify" to next track'
back_osa = 'tell application "Spotify" to back track'
ICON_NEUTRAL = 'clear.png'

@rumps.clicked(u'一時停止')
def switchTimer(sender):
    out = osascript.run(play_stop_osa)

@rumps.clicked(u'next')
def switchTimer(sender):
    out = osascript.run(next_osa)
    

@rumps.timer(5)
def dispTimer(sender):
    #app.icon = ICON_NEUTRAL
    track = osascript.run(track_osa)[1]
    artist = osascript.run(artist_osa)[1]
    app.title = artist + " - " + track
    

if __name__ == "__main__":
    display_state= TIMER_MODE
    app = rumps.App("Spoplayer", title='plz wait...')
    app.run()


#get = subprocess.Popen(track_cmd.split(), stdout=subprocess.PIPE)
#print(get.communicate())
#code,out,err = osascript.run(track_osa)
#print(out)
#code,out,err = osascript.run(artist_osa)
#print(out)
