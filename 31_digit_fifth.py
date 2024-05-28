#no shotgunning

#try dynamic progamming approach building a table of solutions from the bot

total_solutions = 0

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.reverse()


def build_children(value, last_used_coin):
    #print("build_children(", value, last_used_coin)
    for coin in coins:
        new_value = value - coin
        if coin > value or coin > last_used_coin:
            continue
        if new_value == 0:
            global total_solutions
            total_solutions += 1
            #print("total ",total_solutions, coin)
            continue
        build_children(new_value, coin)


build_children(200, 200)
#OLD ANSWER = 340436
print(total_solutions)
