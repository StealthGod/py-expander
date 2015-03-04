import urllib
from xml.dom import minidom
from pyexpander import config
from pyexpander.log import get_logger

logger = get_logger('plex')

#source_type = ['movie', 'show'] # Valid values: artist (for music), movie, show (for tv)
base_url = 'http://%s:32400/library/sections' % config.PLEX_HOST
refresh_url = '%s/%%s/refresh' % base_url

def update_plex():
	try:
		xml_sections = minidom.parse(urllib.urlopen(base_url))
		sections = xml_sections.getElementsByTagName('Directory')
		for s in sections:
			if s.getAttribute('title') in config.PLEX_SOURCE_TITLES:
				url = refresh_url % s.getAttribute('key')
				x = urllib.urlopen(url)				
	except:
		pass
