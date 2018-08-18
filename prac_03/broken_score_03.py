"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    comment = calculate_comment_from_score(score)
    print(comment)

def calculate_comment_from_score(score):
    if score < 0 or score > 100:
        comment = "Invalid score"
    elif score >= 90:
        comment = "Excellent"
    elif score >= 50:
        comment = "Passable"
    else:
        comment = "Bad"
    return comment

main()