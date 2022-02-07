import user


def q_loop():
    n =0
    while(n < 10):
        user.question()
        n += 1
    print("All done")

user.welcome()
q_loop()