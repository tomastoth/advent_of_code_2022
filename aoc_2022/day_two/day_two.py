import enum
# 1st col A -> ROCK, B-> PAPER, C-> SCISSORS,

# 2nd col X -> ROCK, Y -> PAPER, Z -> SCISSORS

# win -> 6 points, draw -> 3 points
# 1 -> rock, 2 -> paper, 3 -> scissors

class Outcome(enum.Enum):
    LOSS = 0
    DRAW = 1
    WIN = 2

class Choice(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def get_choice_points(choice: Choice) -> int:
    match choice:
        case Choice.ROCK:
            return 1
        case Choice.PAPER:
            return 2
        case Choice.SCISSORS:
            return 3
    return 0

def parse_opponent(choice: str) -> Choice:
    match choice:
        case "A":
            return Choice.ROCK
        case "B":
            return Choice.PAPER 
        case "C":
            return Choice.SCISSORS 

def parse_me(choice: str) -> Choice:
    match choice:
        case "X":
            return Choice.ROCK 
        case "Y":
            return Choice.PAPER 
        case "Z":
            return Choice.SCISSORS 

def parse_needed_outcome(choice: str) -> Outcome:
    match choice:
        case "X":
            return Outcome.LOSS
        case "Y":
            return Outcome.DRAW
        case "Z":
            return Outcome.WIN

def get_choice_to_win(opponent_choice: Choice) -> Choice:
    match opponent_choice:
        case Choice.ROCK:
            return Choice.PAPER 
        case Choice.PAPER:
            return Choice.SCISSORS 
        case Choice.SCISSORS:
            return Choice.ROCK 

def get_choice_to_loose(opponent_choice: Choice) -> str:
    match opponent_choice:
        case Choice.ROCK:
            return Choice.SCISSORS
        case Choice.PAPER:
            return Choice.ROCK
        case Choice.SCISSORS:
            return Choice.PAPER


def determine_win_points(opponent: Choice, me: Choice) -> int:
    #wins 
    rock_over_scissors = me == Choice.ROCK and opponent == Choice.SCISSORS 
    paper_over_rock = me == Choice.PAPER and opponent ==Choice.ROCK 
    scissors_over_paper = me == Choice.SCISSORS and opponent == Choice.PAPER 
    #draw
    if any([rock_over_scissors, paper_over_rock, scissors_over_paper]):
        return 6
    if me == opponent:
        return 3
    return 0

def get_our_choice_for_second_round(needed_outcome: Outcome, opponent_choice: Choice) -> Choice:
    match needed_outcome:
        case Outcome.LOSS:
            return get_choice_to_loose(opponent_choice)
        case Outcome.DRAW:
            return opponent_choice
        case Outcome.WIN:
            return get_choice_to_win(opponent_choice)

def get_round_points_second_part(opponent_unparsed:str, me_unparsed:str) -> int:
    opponent = parse_opponent(opponent_unparsed)
    needed_outcome = parse_needed_outcome(me_unparsed)
    me = get_our_choice_for_second_round(needed_outcome, opponent)
    return get_choice_points(me) + determine_win_points(opponent, me)

            

    

def get_round_points_first_part(opponent_unparsed:str, me_unparsed:str) -> int:
    opponent = parse_opponent(opponent_unparsed)
    me = parse_me(me_unparsed)
    return determine_win_points(opponent, me) + get_choice_points(me)


def main():
    first_part_total_points = 0
    second_part_total_points = 0
    with open("./input.txt", "r") as input_file:
        for line in input_file:
            line = line.replace("\n", "")
            split = line.split(" ")
            opponent = split[0]
            me = split[1]
            first_part_total_points += get_round_points_first_part(opponent, me)
            second_part_total_points += get_round_points_second_part(opponent, me)

    assert (get_round_points_first_part("A","Y")) == 8
    assert (get_round_points_first_part("B","X")) == 1
    assert (get_round_points_first_part("C","Z")) == 6
    print(f"first part result  {first_part_total_points}")
    assert get_round_points_second_part("A","Y") == 4
    assert get_round_points_second_part("B","X") == 1
    assert get_round_points_second_part("C","Z") == 7
    print(f"second part result  {second_part_total_points}")



if __name__ == "__main__":
    main()