import sqlite3

with sqlite3.connect('Favicons') as conn:
	cursor = conn.cursor() 

	cursor.execute("""
        select  favicons.url,
                icon_mapping.page_url,
                datetime(((favicon_bitmaps.last_updated -11644473600000000)/1000000),
                        'unixepoch','localtime') [last_updated]
        from favicons
                inner join icon_mapping
                 on favicons.id = icon_mapping.icon_id
                inner join favicon_bitmaps
                 on icon_mapping.icon_id = favicon_bitmaps.icon_id
	""")
	for row in cursor.fetchall(): 
		url, page_url,last_updated = row
		print '\'%-25s\', \'%-25s\', \'%-25s\'' % (url, page_url,last_updated)
