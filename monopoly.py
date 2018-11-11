#!/usr/bin/python3.6
import random

board = ["GO", "OLD_KENT_ROAD", "COMMUNITY_CHEST", "WHITECHAPEL", "TAX", "KINGS_X_STATION", "ANGEL_ISLINGTON", "CHANCE", "EUSTON_ROAD", "PENTONVILLE", "JAIL", "PALL_MALL", "UTIL|ELECTRIC", "WHITEHALL", "NORTHUMBERLAND", "MARYLEBONE_STATION", "BOW_STREET", "COMMUNITY_CHEST", "MARLBOROUGH", "VINE_STREET", "FREE_PARKING", "STRAND", "CHANCE", "FLEET_STREET", "TRAFALGAR", "FENCHURCH_STATION", "LEICESTER_SQUARE", "COVENTRY_STREET", "UTIL|WATER", "PICCADILLY", "GO_TO_JAIL", "REGENT_STREET", "OXFORD_STREET", "COMMUNITY_CHEST", "BOND_STREET", "LIVERPOOL_STATION", "CHANCE", "PARK_LANE", "TAX", "MAYFAIR"]

community_chest_master = ["ADVANCE_TO_GO", "_", "_", "_", "GET_OUT_OF_JAIL_FREE", "GO_TO_JAIL", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

chance_master = ["GOTO_GO", "GOTO_TRAFALGAR", "GOTO_PALL_MALL", "GOTO_NEXT_UTILILTY", "GOTO_NEXT_STATION", "_", "GET_OUT_OF_JAIL_FREE", "GO_BACK_3", "GO_TO_JAIL", "_", "_", "GOTO_KINGS_X ", "GOTO_MAYFAIR", "_", "_", "_"]

def roll_dice():
    """ Returns a pair, the number attained and a bool saying if it is a double """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2:
        return dice1 + dice2, True
    return dice1 + dice2, False

def advance(steps):
    """ Advances the position by the number of steps given """
    global position
    position = (position + steps) % 40

def get_comm_deck():
    community_chest_cards = list(community_chest_master)
    random.shuffle(community_chest_cards)
    return iter(comm_cards)

def get_chance_deck():
    chance_cards = list(chance_master)
    random.shuffle(chance_cards)
    return iter(chance_cards)

position = 0
in_jail = False
num_doubles = 0
num_goojf_cards = 0
comm_deck = get_comm_deck()
chance_deck = get_chance_deck()

for _ in range(100):
    if in_jail:
        # Do stuff
        continue

    total, double = roll_dice()
    num_double += 1 if double else 0
    if num_double == 3:
        position = 10 # Jail
        in_jail = True
        if num_goojf_cards:
            in_jail = False
            num_goojf_cards -= 1
            continue

    advance(total)
    if board[position] == "CHANCE":
        try:
            card = next(chance_deck)
        except:
            chance_deck = get_chance_deck()
            card = next(chance_deck)
        if card == "GOTO_GO":
            position = 0 
        elif card == "GOTO_TRAFALGAR":
            position = 24
        elif card = "GOTO_PALL_MALL":
            position = 11
        elif card = "GOTO_NEXT_UTILILTY":
            while not board[position].startswith("UTIL"):
                advance(1)
        elif card = "GOTO_NEXT_STATION":
            while not board[position].endswith("STATION"):
                advance(1)
        elif card = "GET_OUT_OF_JAIL_FREE":
            num_goojf_cards += 1
        elif card = "GO_BACK_3":
            advance(-3)
        elif card = "GO_TO_JAIL":
            position = 10
            in_jail = True
            num_doubles = 0
        elif card = "GOTO_KINGS_X":
            position = 5
        elif card = "GOTO_MAYFAIR":
            position = 39

    elif board[position] == "COMM_CHEST":
        pass
    elif board[position] == "GO_TO_JAIL":
        pass

