import requests
from lxml import html
import codecs

def tobytes(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    else:
        return s

def episode_index(season, episode):
    season = str(season).zfill(2)
    episode = str(episode).zfill(2)

    return "s{}e{}".format(season, episode)

def get_transcript(season, episode):

    params = {"tv-show": "parenthood",
            "episode": episode_index(season, episode)}
    r = requests.get("http://www.springfieldspringfield.co.uk/view_episode_scripts.php",
            params = params)

    content = codecs.decode(r.content, 'utf-8', 'replace')
    tree = html.fromstring(content)

    transcript = tree.xpath('//div[@class="scrolling-script-container"]/text()',
           encoding='latin-1')

    return transcript


def main():
    episodes_in_seasons = {1:13, 2:22, 3:18, 4:15, 5:22, 6:13}

    f = open('parenthood.txt', 'w')
    for season, n_episodes in episodes_in_seasons.items():
        print '----------', season, n_episodes, '-------------'
        for episode in range(1, n_episodes + 1):
            print 'Episode', episode
            transcript = get_transcript(season, episode)
            for line in transcript:
                line = line.replace('\r', '\n')
                f.write(tobytes(line))

    f.close()

if __name__ == '__main__':
    main()

