#prerequiste your whatsapp web should be opened in your default browser

import pywhatkit as kit

#number = '+91XXXXXXXXXX'#replace all the X with your desired contact number
group='L3HGbXSc9ZA41FznkLUZxv' #group id

#kit.sendwhatmsg(number,"Hi this message is scheduled to send from Python at time 11:00 p.m. Happy Diwali :)",22,0)
kit.sendwhatmsg_to_group(group,"Hi this message is scheduled to send from Python at time 11:02 p.m. Happy Diwali :)",23,2)