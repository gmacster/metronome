import sched, time, winsound

def main():

    s = sched.scheduler(time.time, time.sleep)
    s.enter(0, 0, tick, (s,))
    s.run()

def tick(s):
    bpm = 80
    delay = 1 / bpm * 60
    winsound.PlaySound("click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    s.enter(delay, 0, tick, (s,))

if __name__ == "__main__":
    main()
