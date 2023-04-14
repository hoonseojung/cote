def solution(players, callings):
    run = {player: i for i, player in enumerate(players)}
    for call in callings:
        temp = players[run[call] - 1]
        players[run[call] - 1] = players[run[call]]
        players[run[call]] = temp
        run[players[run[call]]] += 1
        run[call] -= 1
    return players