file=VERSION
NEW_VERSION=$(shell cat ${file})

version:
	sed -i "s/VERSION/${NEW_VERSION}/" vimde
	sed -i "s/VERSION/${NEW_VERSION}/" doc/vimde.1
	sed -i "s/VERSION/${NEW_VERSION}/" doc/vimde.md

