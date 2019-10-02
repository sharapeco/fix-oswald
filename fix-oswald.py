## Google Fonts からダウンロードした Oswald-*.ttf の variant が全部 Regular になっているので修正する
##
## Requires:
##     pip install fonttools

import sys

from fontTools.ttLib import TTFont

weights = [
	'ExtraLight',
	'Light',
	'Regular',
	'Medium',
	'SemiBold',
	'Bold',
]

for weight in weights:
	font = TTFont('src/Oswald-' + weight + '.ttf')
	namerecord_list = font["name"].names
	
	for record in namerecord_list:
		if record.nameID == 2:
			record.string = weight
			break
	
	output_path = 'dest/Oswald-' + weight + '.ttf'
	try:
		font.save(output_path)
	except Exception as e:
		sys.stderr.write('ERROR: unable to write "' + output_path + '"')
		sys.exit(1)
