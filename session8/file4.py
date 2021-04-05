
f = open("filename.txt", 'r')

f.write("Hey, I'm back for second time")


def save(highscore):
    file = open("highscores.txt", 'a')
    file.write(f"{highscore}\n")
    file.close()