from database import Database
from gameDB import Game

db = Database("bolt://107.23.80.166:7687", "neo4j", "till-accessory-taxis")
game = Game(db)

op = 0

while op != 9:
    print("1 - Criar jogador")
    print("2 - Listar jogadores")
    print("3 - Ler jogador")
    print("4 - Atualizar jogador")
    print("5 - Deletar jogador")
    print("6 - Criar partida")
    print("7 - Listar partidas de um jogador")
    print("8 - Ler partida")
    print("9 - Sair")
    op = int(input("Digite a opção desejada: "))
    
    if op == 1:
        name = input("Digite o nome do jogador: ")
        game.create_player(name)
    elif op == 2:
        players = game.read_players()
        for player in players:
            print(player["p"]["name"])
    elif op == 3:
        player_id = int(input("Digite o ID do jogador: "))
        player = game.read_player(player_id)
        print(player[0]["p"]["name"])
    elif op == 4:
        player_id = int(input("Digite o ID do jogador: "))
        name = input("Digite o novo nome do jogador: ")
        game.update_player(player_id, name)
    elif op == 5:
        player_id = int(input("Digite o ID do jogador: "))
        game.delete_player(player_id)
    elif op == 6:
        players = []
        while True:
            player_id = int(input("Digite o ID de um jogador participante (ou 0 para parar): "))
            if player_id == 0:
                break
            players.append(player_id)
        winner = int(input("Digite o ID do jogador vencedor: "))
        game.create_match(players, winner)
    elif op == 7:
        player_id = int(input("Digite o ID do jogador: "))
        matches = game.read_player_matches(player_id)
        for match in matches:
            print(match["m"]["winner"])
    elif op == 8:
        match_id = int(input("Digite o ID da partida: "))
        match = game.read_match(match_id)
        print(match[0]["m"]["winner"])
    elif op == 9:
        db.close()
    else:
        print("Opção inválida")