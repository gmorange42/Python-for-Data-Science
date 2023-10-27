from datetime import datetime

def getTime():
    now = datetime.now()
    epoch = datetime.fromtimestamp(0)
    epoch_to_now = (now - epoch).total_seconds()
     
    print("Seconds since January 1, 1970: {:,.4f}".format(epoch_to_now),
        "or", format(epoch_to_now,'.2e'), "in scientific notation")
    print(now.strftime("%b %d %Y"))

getTime()
