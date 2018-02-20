win_combine = [[1,2,3],[1,4,7],[3,6,9],[7,8,9],
               [2,5,8],[4,5,6],[1,5,9],[7,5,3]]
total_move =[]
active_player = 1


def display():
    print (player)
    list=['[ ]']*9
    for index, _ in enumerate(list):
        for key in player.keys():
            if (index+1) in player[key]["move"]:
                list[index] = player[key]["present"]
    final_list = list[:3] + ["\n",] + list[3:6]+["\n",] +list[6:]
    print("".join(final_list))

def update(new_move):
    try:
        new_move = int(new_move)
    except TypeError:
        print("your_format is wrong please inout from 1->9 ")
        return True

    if new_move in total_move:
        print("this move exsited please print again")
        print("the existed move : {}".format(total_move.sort()))
        return True
    total_move.append(new_move)

    player[str(active_player)]["move"].append(new_move)
    display()
    return False

def check_if_this_line(player_move):
    print("this is data for {}".format(player_move))
    value = False
    for combine in win_combine:
        for coord in combine:

            if coord not in player_move:
                break
        else:
            print("the player {} win".format(active_player))
            value = True
    return value

def check_if_this_player_win():
    print(player[str(active_player)])
    print (player[str(active_player)]["move"])
    return check_if_this_line(player[str(active_player)]["move"])

if __name__ == "__main__":

    player = {
              "1": {"present": " * ","move": []},
              "2": {"present":" + ", "move": []}
              }

    while True :
        check_error = True
        while check_error:
            new_move = input("Please input your move the player {}: ".format(active_player))

            check_error = update(new_move)

        if check_if_this_player_win():
            break

        if active_player == 1 :
            active_player = 2
        else:
            active_player = 1