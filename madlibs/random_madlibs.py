from sample_madlibs import hp, code
import random

# to choose a random madlib from sample_madlibs
if __name__ == "__main__":
    m = random.choice([hp, code])
    print(m)
    m.madlib()
