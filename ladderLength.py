from collections import deque

def ladderLength(begin, end, wordList):
    wordSet = set(wordList)
    q = deque([(begin, 1)])

    while q:
        word, steps = q.popleft()
        if word == end:
            return steps

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + c + word[i+1:]
                if nxt in wordSet:
                    wordSet.remove(nxt)
                    q.append((nxt, steps + 1))
    return 0

print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
