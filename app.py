from twitter import Twitter
import time
from media import Media

#test pancing ke heroku supaya keluar dyno

tw = Twitter()
media = Media()
def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) is not 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) is not 0 and len(message) < 280:
                    if ".menfessem" in message:
                        message = message.replace(".menfessem", "[Kudus Menfess]")
                        if len(message) is not 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])
                                tw.delete_dm(id)
                        else:
                            if ".quotem" in message:
                                if "https://" not in message and "http://" not in message:
                                    message = message.replace(".quotem", "[Kudus Quote]")
                                    screen_name = tw.get_user_screen_name(sender_id)
                                    media.download_image()
                                    media.process_image(message, screen_name)
                                    tw.post_tweet()
                                    tw.delete_dm(id)
                                else:
                                    media.download_image()
                                    media.process_image(message, None)
                                    tw.post_tweet()
                                    tw.delete_dm(id)
                            else:
                                print("DM deleted because its empty..")
                                tw.delete_dm(id)
                    else:
                        print("DM will be deleted because does not contains keyword..")
                        tw.delete_dm(id)

            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) is 0:
                time.sleep(60)

if __name__ == "__main__":
    start()