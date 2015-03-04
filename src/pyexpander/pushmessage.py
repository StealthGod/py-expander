import os
from pyexpander import config
from pyexpander.log import get_logger
from pyexpander.categorize import get_title
from pushbullet import Pushbullet

logger = get_logger('pushbullet')

def push_finished(torrent_path):
    if os.path.isdir(torrent_path):
        folder = os.path.join(torrent_path, '')
        torrent_name = os.path.basename(os.path.dirname(folder))
		
        title = get_title(os.path.join(torrent_name, ''))
        if title is not None:
            push_message('[Done]: %s' % title, torrent_name)
    else:
        torrent_name = os.path.splitext(os.path.basename(torrent_path))[0]
        filename = os.path.basename(torrent_path)
		
        title = get_title(os.path.join(torrent_name, filename))
        if title is not None:
            push_message('[Done]: %s' % title, torrent_name)

def push_message(title, body):
    try:
        logger.info('PushBullet: %s' % title)
        pb = Pushbullet(config.PUSHBULLET_API_KEY)
        push = pb.push_note(title, body)
    except:
        logger.exception("Could not send PushBullet message")
        raise