from openpyxl import Workbook
import argparse
import json
import datetime as dt


def main(jsonfile):

    # Create a new Excel workbook
    wb = Workbook()

    # grab the active worksheet
    ws = wb.active


    # Opening JSON file
    f = open(jsonfile, 'r')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # header row
    ws.append(['post_id', 'datetime', 'username', 'likes', 'n_comments', 'n_unique_commenters', 'n_owner_comments', 'media_link', 'caption', 'is_video'])

    # Iterating through the json
    # list
    i = 0
    for post in data['GraphImages']:
        print("post", i+1, "of", len(data["GraphImages"]))
        datestamp = dt.datetime.fromtimestamp(post['taken_at_timestamp']).strftime('%Y-%m-%d %H:%M:%S')

        post_owner_id = post['owner']['id']

        #print('post number ', i)
        # Compute number of unique commenters, and number of times the user comments on the thread
        commenters = set()
        n_owner_comments = 0
        for comment in post['comments']['data']:
            #print('  comment number ', j)
            commenters.add(comment['owner']['id'])
            if comment['owner']['id'] == post_owner_id:
                n_owner_comments = n_owner_comments + 1

        #print("now tabulating n_commenters")
        n_commenters = len(commenters)

        ws.append([post['id'],
                   datestamp,
                   post['username'],
                   post['edge_media_preview_like']['count'],
                   len(post['comments']['data']),
                   n_commenters,
                   n_owner_comments,
                   '=HYPERLINK("https://www.instagram.com/p/{}", "https://www.instagram.com/p/{}")'.format(post['shortcode'], post['shortcode']),
                   post['edge_media_to_caption']['edges'][0]['node']['text'],
                   post['is_video']
                  ])
        i = i+1

    # Closing file
    f.close()

    # Save the file
    wb.save("ig_metadata.xlsx")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile', help='filepath to json file')

    args = parser.parse_args()

    main(args.jsonfile)
