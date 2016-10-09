import sys

reload(sys)
sys.setdefaultencoding('utf8')

from git import *
import re
import collections
from collections import Counter
import time

Author = collections.namedtuple('Author', ['name', 'nickname'])

aaron = Author(name='aaronk', nickname='phrasemix')
alex = Author(name='alex', nickname='alexc')
bruno = Author(name='bruno', nickname='cribeiro')
claudivan = Author(name='claudivan', nickname='cribeiro')
daniel = Author(name='daniel', nickname='danielcohenlive')
josh = Author(name='joshua', nickname='josh')
marcondes = Author(name='marcondes', nickname='marcwebbie')
mauricio = Author(name='mauricio', nickname='mauriciovieira')
michael = Author(name='michael', nickname='michael.h')
rodrigo = Author(name='rodrigo', nickname='RatoX')
thiago = Author(name='thiago', nickname='thiago.ghisi')
vinicius = Author(name='vinicius', nickname='vinicius')

authors_list = [aaron, alex, bruno, claudivan, daniel, josh, marcondes, mauricio, michael, rodrigo, thiago, vinicius]

# joao = Author(name='joao', nickname='joaozinho')
# maria = Author(name='maria', nickname='mariazinha')
# thiago = Author(name='thiago', nickname='thiago.ghisi')
# zeh = Author(name='zeh', nickname='zezinho')

# authors_list = [joao, maria, thiago, zeh]

def build():
    repo = Repo('/home/user/repo')

    master = repo.heads.master
    pairs_dict = {}
    for commit in repo.iter_commits(master, since='2016-01-01+00:00', reverse=True):
        print "Commit email: ", str(commit.author.email), " - ", time.ctime(int(commit.committed_date))
        for author in authors_list:
            if author.name not in pairs_dict:
                pairs_dict[author.name] = Counter()

            if author.name in str(commit.author.email) or author.nickname in str(commit.author.email):
                paired_with = ''

                pair_match = re.search('pair\+(\w+)\+(\w+)', str(commit.author.email))
                if not pair_match:
                    paired_with = 'solo'
                else:
                    print "Matcher:", pair_match.group(1), pair_match.group(2)
                    if pair_match.group(1) == author.name or pair_match.group(1) == author.nickname:
                        paired_with = _get_author_name(pair_match.group(2))
                    else:
                        paired_with = _get_author_name(pair_match.group(1))
                    if paired_with not in (o.name for o in authors_list):
                        paired_with = 'other'
                print "Final Pair: ", author.name, paired_with
                pairs_dict[author.name][paired_with] += 1
                if paired_with not in pairs_dict:
                    pairs_dict[paired_with] = Counter()
                pairs_dict[paired_with][author.name] += 1
                break

    return pairs_dict


def print_table():
    solo = Author(name='solo', nickname='solo')
    other = Author(name='other', nickname='other')
    pairsList = authors_list + [solo, other]
    pairsDict = build()
    print(pairsDict)
    str = ''
    for index, person in enumerate(pairsList):
        if (index == 0):
            str += '|'.rjust(10) + person.name.ljust(9) + '\n'
        else:
            str += person.name.ljust(9) + '|'
            for paired in pairsList[:index]:
                count = pairsDict[person.name][paired.name]
                str += '{:<7}|'.format(count)
            str += person.name.ljust(9) + '\n'
    print str
    return str


def _get_author_name(author_info):
    for author in authors_list:
        if author.name == author_info or author.nickname == author_info:
            # print 'Found: ', author.name
            return author.name
    return 'other'



if __name__ == '__main__':
    print_table()
