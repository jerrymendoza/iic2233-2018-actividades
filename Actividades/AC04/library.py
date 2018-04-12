import datetime
import exeeepp as e

def tiempo_trending(publish_date, trending_date):
    e.probar(publish_date)

    publish_d = datetime.datetime.strptime(publish_date, "%y.%d.%m")
    trending_d = datetime.datetime.strptime(trending_date, "%y.%d.%m")
    days = (trending_d - publish_d).days

    return days


def like_dislike_ratio(likes, dislikes):
    e.digitos(likes)
    return int(likes) / int(dislikes)


def info_video(title, views, likes, dislikes, tags):

    print("El video {0} ha tenido {1} views, con {2} likes y {3} dislikes"
          .format(title, views, likes, dislikes))
