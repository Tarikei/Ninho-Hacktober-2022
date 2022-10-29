import array as arr

# Variables
i = 0
debug = 0
new_room = 1
last_room = 1
room = "sala"
inventory = arr.array('I', [0, 0, 0, 0, 0, 0, 0, 0])
storyline_array = arr.array('I', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
time = -1
room_list = ["sala", "quarto", "cozinha", "banheiro"]
items_list = ["nothing", "chave"]

# Functions
# check input
def get_action(id):
    global new_room
    global room
    global items_list
    global inventory
    global storyline_array
    global time
    global last_room
    command = id[0]
    if (debug == 1):
        print("DEBUG: Comando:", command)
        print("DEBUG:", room_list)
    if (command == "help"):
        print("""     Comandos Disponiveis
ir para:
 Vai a um Quarto Disponivel
   Quartos Disponiveis:
 sala
 quarto
 cozinha
 banheiro

sair:
 Fecha o programa

tempo:
 Olha o tempo

inventario:
 Mostra os itens no inventario

usar:
 um item que voce tem no inventario

voltar:
 Volta ao quarto em que voce estava
""")

    if (command == 'voltar'):
        if last_room == 1:
            print("Voce ainda nao foi para nenhum lugar")
        else:
            auxiliar = last_room
            last_room = room
            room = auxiliar
            new_room = 1


    if (command == "ir"):
        if (id[1] == "para"):
            if id[2] in room_list:
                room = id[2]
                new_room = 1
            else:
                print("uhh... acho que não.")
        else:
            print("ir ", id[1], "... ok. Tente denovo.", sep='')

    if (command == "sair"):
        exit()

    if (command == "tempo"):
        print("Você olha o tempo...")
        s = time
        if (time < 10):
            s = "0" + str(time)
        print("São 6:", s, ". E você perdeu 1 minuto lendo isso.", sep='')

    if (command == "inventario"):
        displayInventory()

    if (command == '"inventario"'):
        if (storyline_array[15] == 1):
            print("ASSIM NÃO!!!")
        else:
            print("???")

    if (command == "usar"):
        #item
        if (len(id) == 1):
            print("Usar... o quê???")
        else:
            #item
            if (id[1] == "item"):
                if (len(id) <= 2):
                    print("Que item?")
                    if (storyline_array[15] == 0):
                        print('Use o comando "inventario" para exibir a lista de itens.')
                        storyline_array[15] = 1
                    else:
                        print('Comando "inventario"... lembra?')
                else:
                    # Verifique se o item existe
                    if checkItem(id[2]) != 0:
                        if (len(id) <= 3):
                            print("Usar ", id[2], "... Mas em quê?", sep='')
                        else:
                            if (id[3] == "em"):
                                if (len(id) <= 4):
                                    print("boa ideia! vou usar em nada. Tente denovo.")
                                else:
                                    # room dependant actions
                                    if (room == "sala"):
                                        if (id[4] == "porta"):
                                            # usar chave
                                            if (id[2] == "chave"):
                                                if (storyline_array[0] == 0):
                                                    storyline_array[0] = 1
                                                    print("A porta foi destrancada!")
                                                else:
                                                    print("Não vou destrancar algo duas vezes.")
                                            else:
                                                print("Não posso usar isso aqui.")
                    else:
                        print("Eu não tenho esse item!")
            
            #room dependant actions
            if (room == "sala"):
                if (id[1] == "porta"):
                    if (storyline_array[0] == 0):
                        print("Está trancada... Preciso de uma chave.")
                    else:
                        print("Você consegue sair a tempo em", time, "minutos")
                        exit()

    # Action ended, go back to input mode.
    inputMode()

# get player input
def inputMode():
    global time
    time += 1
    if (time >= 60):
        print("Você não consegue sair a tempo... O que aconteceu depois? Não sei.")
        exit()

    global room
    global new_room
    if (debug == 1):
        print("DEBUG: new room?", new_room)
    if new_room == 1:
        print("Você agora está em:", room)
        new_room = 0
    print("")
    print("o que deseja fazer?")
    user_input = input("")

    get_action(user_input.split())

def displayInventory():
    storyline_array[15] = 1
    if (inventory[0] == 0):
        print("Você tem nada no inventário!")
    else:
        print("Seu inventário:")
        i = 0
        while i < len(inventory):
            if inventory[i] != 0:
                print(items_list[inventory[i]])
            i += 1

def checkItem(item):
    global inventory
    global items_list
    if item in items_list:
        item = items_list.index(item)
    else:
        return 0

    if (debug == 1):
        print("DEBUG: Checking for item with ID ", item, "...", sep='')
    
    haveit = 0
    i = 0
    while i < len(inventory):
        if inventory[i] == item:
            haveit = 1
        i += 1
    return haveit

def sortItems():
    print("ojpabsgbjoçasgbkljasg")


# game start
# start with a key in your inventory
inventory[0] = 1

print("(insira uma intro para uma história aqui)")
print("Por agora, tem uma porta trancada na sala.")
print("E olha só, uma chave já no seu inventário. Easy mode.")
inputMode()
