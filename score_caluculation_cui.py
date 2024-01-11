def main():
    # Score
    score_individual = [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    score_relay = [30, 26, 24, 22, 20, 18, 16, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    
    # Scores of participating schools
    scores_school = {
        "School_1": 0.0,
        "School_2": 0.0,
        "School_3": 0.0,
        "School_4": 0.0,
        "School_5": 0.0,
        "School_6": 0.0,
        "School_7": 0.0,
        "School_8": 0.0,
        "School_9": 0.0,
        "School_10": 0.0,
        "School_11": 0.0,
        "School_12": 0.0,
        "School_13": 0.0,
        "School_14": 0.0,
        "School_15": 0.0,
        "School_16": 0.0,
        "School_17": 0.0,
        "School_18": 0.0,
        "School_19": 0.0,
        "School_20": 0.0
    }

    # Check which event
    which = int(input("個人種目:1 リレー種目:2 >> "))

    # Check if there is a tie
    is_same_rank = bool(int(input("同順位はありますか？ 0：いいえ 1：はい >> ")))
    n = 0
    if is_same_rank == True:
        n = int(input("n位とn+1位が同じです。 nの値は？ >> "))
        print(f"{n}位と{n + 1}位もそのまま入力してください。")
        
    print("学校名を入力してください。")
    
    # Add scores
    # Individual event
    if which == 1:
        for i in range(len(score_individual)):
            # Ask person school
            person_school = input(f"{i + 1}位： ")
            
            # Same rank
            if i == n - 1 or i == n:
                scores_school[person_school] += (score_individual[i] + score_individual[i + 1]) / 2
            # Different rank
            else:
                scores_school[person_school] += score_individual[i]
                
    # Relay event
    elif which == 2:
        for j in range(len(score_relay)):
            # Ask relay school
            relay_school = input(f"{j + 1}位： ")
            
            # Same rank
            if j == n - 1 or j == n:
                scores_school[relay_school] += (score_relay[j] + score_relay[j + 1]) / 2
            # Different rank
            else:
                scores_school[relay_school] += score_relay[j]
    # Error
    else:
        print("再度やり直してください。")
        return False
        
    print("\nScores of each school")
    print_scores(scores_school)
    

# Print scores  
def print_scores(school):
    for key, value in school.items():
        if value >= 1:
            print(f"{key}: {value}")
        
    
if __name__ == "__main__":
    main()
