import os
import sys
import datetime
def draw(startdate):
    os.system("""          
    python pogchamp.py
    git add .
    git commit -m "updates" --date=format:iso8601:"{data}"
    """.format(data=startdate))

def make_dates(startdate):
    date = datetime.datetime.strptime(startdate, "%Y-%m-%d")
    #start on a monday 
    dates = [str(date)]

    gaps = [1 for _ in range(4)] + [2] + [1 for _ in range(13)] + [2] + [1 for _ in range(4)] + [4]

    for _ in range(26):
        gaps = gaps + [1,1,5]

    gaps = gaps + [1,1,6]
    for g in gaps:
        date = date + datetime.timedelta(days=g)
        dates.append(str(date))
        #date = date + datetime.timedelta(days=6)
    return dates
if __name__ == '__main__':
    data = sys.argv[1]
    dates = make_dates(data)
    for d in dates:
        draw(d)


