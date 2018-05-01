from __future__ import print_function
import pickle
import sys

try:
    with open('peers.pkl', 'rb') as peerfile:
        peers = pickle.load(peerfile)
except:
    peers = dict()

for line in sys.stdin:
    [_, ip, _, last_seen] = line.split()
    [days, hours, minutes, seconds] = last_seen.split('.')
    last_seen_in_seconds = (int(days[1:]) * 60 * 60 * 24 +
                            int(hours[1:]) * 60 * 60 +
                            int(minutes[1:]) * 60 +
                            int(seconds[1:]))
    peers[ip] = last_seen_in_seconds

count = 0
for key in peers.keys():
    if peers[key] < 60 * 60 * 3:
        count += 1

print(str(count) + " peers known to be active in the last three hours")

with open('peers.pkl', 'wb') as peerfile:
    pickle.dump(peers, peerfile, pickle.HIGHEST_PROTOCOL)
