import rumps
import datetime
import osascript

TIMER_MODE = 'timer'
track_osa = 'tell application "Spotify" to name of current track as string'
artist_osa = 'tell application "Spotify" to artist of current track as string'
play_stop_osa = 'tell application "Spotify" to playpause'
next_osa = 'tell application "Spotify" to next track'
back_osa = 'tell application "Spotify" to back track'


@rumps.clicked(u'一時停止')
def switchTimer(sender):
    out = osascript.run(play_stop_osa)

@rumps.clicked(u'next')
def switchTimer(sender):
    out = osascript.run(next_osa)
    

@rumps.timer(5)
def dispTimer(sender):
    track = osascript.run(track_osa)[1]
    artist = osascript.run(artist_osa)[1]
    app.title = artist + " - " + track
    

if __name__ == "__main__":
    display_state= TIMER_MODE
    app = rumps.App("Spoplayer", title='plz wait...')
    app.run()


