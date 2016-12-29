from bs4 import BeautifulSoup
import urllib

visited = {}
queue = []

def checkIfSite(url):
	if url.find('css') == -1 and url.find('js') == -1 and url.find('png') == -1 and url.find('gif') == -1 and url.find('jpeg') == -1 and url.find('fonts.googleapis') == -1 and url[0] != '#':
		return True
	return False

def extractSite(url):
	queue2 = []
	try:
		handle = urllib.urlopen(url)
		soup = BeautifulSoup(handle, 'html.parser')
		for link in soup.find_all('a'):
			tmpUrl = link.get('href')
			tmpUrl = str(tmpUrl)
			if not checkIfSite(tmpUrl):
				continue
			if tmpUrl.find('http') != -1:
				queue2.append(tmpUrl)
			else:
				queue2.append(url + tmpUrl)
		return queue2

	except IOError:
		return []

def bfs(source):
	queue.append(source)
	while len(queue) != 0:
		node = queue.pop(0)
		if(node in visited.keys()):
			continue
		visited[node] = True
		print(node)
		arr = extractSite(node)
		for link in arr:
			if link not in visited.keys():
				queue.append(link)

if __name__ == '__main__':
	url = raw_input('enter url: ')
	bfs(url)