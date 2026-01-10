import queue

# create a visited_websites
visited_websites = queue.LifoQueue()
current_website = None

while True:
   website = input('Enter website name (0 for back): ')

   if website == '0':
      if visited_websites.empty():
         break
      else:
         print('<-- Going back to a previously visited website')
         current_website = visited_websites.get()

   elif website != "":
      if current_website is not None:
         visited_websites.put(current_website)
      current_website = website

   if current_website is not None:
        print('You are currently viewing:', current_website)
        print()