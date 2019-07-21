from plyer import notification
import requests
from bs4 import BeautifulSoup
from sys import argv



def message(title, message):
  message = message[:200]
  notification.notify (
    title = title,
    message = message + '....',
  )

class CodechefContestAnnouncer:
	def __init__(self, contrequeest_link):
		self.contest_link = contest_link
  	
	def run(self):
		contest_link = self.contest_link
		current_annoucement = ''
		while True:
			try:
				html = requests.get(contest_link)
				soup = BeautifulSoup(html.text, 'lxml')
				data = soup.find('div', {'id' : 'announce_content'})
				announcement = str(data.text)
				l = len(announcement)
				if l > 1 and current_annoucement != announcement:
					message("Codechef Announcement", announcement)
					current_annoucement = announcement
			except:
				pass

if __name__ == '__main__':


	#Get contest code from command line
	if len(argv) > 1: # If there is  argument
		contest_link = "https://www.codechef.com/" + argv[1]
	else:
		contest_link = "https://www.codechef.com/" + input("Enter contest code : ")
	Contest = CodechefContestAnnouncer(contest_link)
	Contest.run()
