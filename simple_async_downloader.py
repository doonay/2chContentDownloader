import aiohttp		
import aiofiles
import asyncio
import os

import requests
import os

def list_downloader_backup_backup(content_list):
	responses = {url: requests.get(url, stream=True) for url in content_list}
	streams = {url: responses[url].iter_content(chunk_size=1024)
			for url in content_list}
	handles = {url: open(os.path.basename(url), 'wb') for url in content_list}
	while streams:
		for url in list(streams.keys()):
			try:
				chunk = next(streams[url])
				print("Received {} bytes for {}".format(len(chunk), url))
				handles[url].write(chunk)
			except StopIteration: # no more contenet
				handles[url].close()
				streams.pop(url)


async def downloader_backup(queue, session):
	filelink = queue.get_nowait()
	filename = os.path.basename(filelink)
	async with aiohttp.ClientSession() as session:
		async with session.get(filelink) as resp:
			if resp.status == 200:
				f = await aiofiles.open(filename, mode='wb')
				await f.write(await resp.read())
				await f.close()


async def list_downloader_backup(content_list):
	loop = asyncio.get_event_loop()
	queue = asyncio.Queue()
	for link in content_list:
		queue.put_nowait(link)

	#timeout = aiohttp.ClientTimeout(total=60*60, sock_read=240)
	connector = aiohttp.TCPConnector(force_close=True, limit=5)

	async with aiohttp.ClientSession(connector=connector) as session:
		await asyncio.gather(*[downloader(queue, session) for link in content_list])

def file_downloader(url):
	filename = os.path.basename(url)
	try:
		response = requests.get(url=url)

		with open(filename, 'wb') as file:
			file.write(response.content)

		print(filename, 'successfully downloaded!')

	except Exception as _ex:
		print('fuck!')

def list_downloader(urllist):
	for url in urllist:
		file_downloader(url)


if __name__ == '__main__':
	content_list = ('https://2ch.hk/hry/thumb/643175/16547925263770s.jpg', 'https://2ch.hk/hry/src/643175/16547925263781.png', 'https://2ch.hk/hry/thumb/643175/16547925263782s.jpg')
	#asyncio.run(list_downloader(content_list))
	list_downloader(content_list)	