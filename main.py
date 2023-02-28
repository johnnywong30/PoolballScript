import csv
from colorama import Fore, Style

answers = {}
responses = {}
scores = {}
headers = [] 

def get_correct_responses():
    with open('answers.csv', newline='') as csvfile:
        answer_reader = csv.reader(csvfile)
        answer_list = []
        for i, row in enumerate(answer_reader):
            if i == 0:
                global headers
                headers = row
            if i == 1:
                answer_list = row
        for i in range(2, len(headers)):
            global answers
            answers[headers[i]] = answer_list[i]

def read_responses(filename='responses.csv'):
    with open(filename, newline='') as csvfile:
        response_reader = csv.reader(csvfile)
        for i, row in enumerate(response_reader):
            if i == 0:
                continue
            person = row[1]
            response = {}
            for j in range(2, len(row)):
                response[headers[j]] = row[j]
            global responses
            responses[person] = response
        

def calculate_score(guesser):
    guesses = responses[guesser]
    score = 0
    print(f'{Fore.YELLOW}GUESSER: {guesser}{Style.RESET_ALL}\n')
    for i, header in enumerate(guesses.keys()):
        compare = guesses[header] == answers[header]
        color = Fore.GREEN if compare else Fore.RED
        print(f'{color}{header} | {guesses[header]}{Style.RESET_ALL}')
        parse_score_from_header = [int(s) for s in header.split() if s.isdigit()]
        score_increment = parse_score_from_header[0] if len(parse_score_from_header) > 0 else 1 
        score += score_increment if compare else 0
    print(f'{Fore.CYAN}FINAL SCORE: {score}{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}============END GUESS============{Style.RESET_ALL}\n')
    global scores
    scores[guesser] = score
    
def write_scores():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    score_string = '\n'.join([f'{person} - {score}' for person, score in sorted_scores])
    f = open('finalscores.txt', 'w')
    f.write(score_string)
    f.close()

def main():
    get_correct_responses()
    read_responses()
    for response in responses.keys():
        calculate_score(response)
    write_scores()
    
if __name__ == "__main__":
    main()