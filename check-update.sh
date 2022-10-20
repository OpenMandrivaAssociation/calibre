#!/bin/sh
curl -k -I -L https://code.calibre-ebook.com/dist/src 2>/dev/null|grep 'location:' |tail -n1 |sed -e 's,.*calibre-,,;s,\.tar.*,,'
