import subprocess as sp


def quality(video_quality):
    """ To return the format code based on the video quality requested """
    return {
             "best": "22",
             "1080p": "137",
             "720p": "136",
             "480p": "135",
             "360p": "134",
             "240p": "133",
             "144p": "160"
    }[video_quality]


def download(url, video_quality, path):
    """ To download the youtube video using youtube-dl library """
    command = ['youtube-dl', '-o']
    command.append(path + "%(title)s " + video_quality + ".%(ext)s")
    command.append('-f ' + quality(video_quality))
    command.append(url)
    return sp.check_output(command).decode("utf-8")




