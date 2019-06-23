class PostTypeParser:
    def __init__(self):
        pass
    def getPostType(posttype):
        switch = {
            "Photo" : 1,
            "Video" : 2,
            "Album" : 3
        }
        return [switch.get(posttype)]