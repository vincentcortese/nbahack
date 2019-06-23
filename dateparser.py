class DateParser:
    def __init__(self):
        pass
    def getDate(datestring):
        raw_date = datestring[0:10]
        date_array = raw_date.split("-")
        
        return_date = []
        for s in date_array:
            return_date.append(int(s))
        return return_date
    def getTime(datestring):
        raw_time = datestring[11:19]
        time_array = raw_time.split(":")

        return_time = []
        for s in time_array:
            return_time.append(int(s))
        return return_time
    def getDateTime(datestring):
        return DateParser.getDate(datestring) + DateParser.getTime(datestring)
