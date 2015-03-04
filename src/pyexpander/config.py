TV_PATH = 'Z:\Media\TV.Shows\{series}\Season {season:02d}'
MOVIE_PATH = 'Z:\Media\Movies\{title}'
APP_PATH = 'Z:\Media\Other'
MUSIC_PATH = 'Z:\Media\Music'
DEFAULT_PATH = 'Z:\Media'

# Formatting for messages sent by PushBullet
TV_TITLE = '{series} - S{season:02d}E{episode:02d}'
MOVIE_TITLE = '{title} - {year}'

LOGFILE = 'Z:\Media\pyexp.log'

EXTRACTION_FILES_MASK = '777'
EXTRACTION_TEMP_DIR_NAME = '_extracted'
# Currently only 7z is supported.
EXTRACTION_EXECUTABLE = '7z'

# Updates Plex Sources when new media has been processed
PLEX_UPDATE_ENABLED = True
PLEX_HOST = '127.0.0.1'
PLEX_SOURCE_TITLES = ['Movies', 'TV Shows'] # Change these to the NAMES of the source titles, add more as you like

# Sends a PushBullet notification when a torrent has been processed
PUSHBULLET_ENABLED = True
PUSHBULLET_API_KEY =  'YOUR API KEY HERE'