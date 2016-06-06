import requests
import json
import calendar
from datetime import datetime, timedelta

_t = "Insert your token here"
_d = "Insert your domain here"

if __name__ == '__main__':
    while 1:
        files_list_url = 'https://slack.com/api/files.list'
        date = str(calendar.timegm((datetime.now() + timedelta(-30))
            .utctimetuple()))
        data = {"t": _t, "ts_to": date}
        response = requests.post(files_list_url, data = data)
        while len(response.json()["files"]) > 0:
            if len(response.json()["files"]) == 0:
                break
            for f in response.json()["files"]:
                print "Deleting file " + f["name"] + "..."
                timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
                delete_url = "https://" + _d + ".slack.com/api/files.delete?t=" + timestamp
                requests.post(delete_url, data = {
                    "t": _t,
                    "file": f["id"],
                    "set_active": "true",
                    "_attempts": "1"})
    print "DONE!"
