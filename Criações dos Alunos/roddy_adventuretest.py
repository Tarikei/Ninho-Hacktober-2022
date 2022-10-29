import array as arr

# Variables
i = 0
debug = 0
new_room = 1
room = "sala"
inventory = arr.array('I', [0, 0, 0, 0, 0, 0, 0, 0])
storyline_array = arr.array('I', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
time = 0
room_list = ["sala", "quarto", "cozinha", "banheiro"]
items_list = ["nothing", "chave"]

# Functions
# check input
def get_action(id):
    global new_room
    global room
    command = id[0]
    if (debug == 1):
        print("Comando:", command)
        print(room_list)

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

    if (command == "inventario"):
        displayInventory()

    if (command == "usar"):
        print("Ainda não implementei isso...")

    inputMode()

# get player input
def inputMode():
    global room
    global new_room
    if (debug == 1):
        print("new room?", new_room)
    if new_room == 1:
        print("Você agora está em:", room)
        new_room = 0
    print("")
    print("o que deseja fazer?")
    user_input = input("")
    get_action(user_input.split())

def displayInventory():
    if (inventory[0] == 0):
        print("Você tem nada no inventário!")
    else:
        print("Seu inventário:")
        i = 0
        while i < len(inventory):
            if inventory[i] != 0:
                print(items_list[inventory[i]])
            i += 1

        # x does not increment at all i don't know what i'm doing wrong
        # for x in inventory:
        #     if inventory[x] != 0:
        #         print(inventory[x], x)
        #         #print(items_list[inventory[x]])

# game start
if (debug == 1):
    inventory[0] = 1

print("(insira uma intro para uma história aqui)")
print("Por agora, tem uma porta trancada na sala...")
inputMode()

#print("você está em:", room_list[room])


    
