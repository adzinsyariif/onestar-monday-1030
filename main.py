import os

# Judge criteria (from competition.yaml, most important first):
# 1. Reads as a one-star review of Monday as a restaurant
# 2. Sounds like a real diner complaint (table / server / dish / bill gone wrong)
# 3. Lands the joke about Monday itself (could not be about any other day)
# 4. Short and quotable (retype into group chat without trimming)
# 5. Plain text, <=25 words, no hashtags / stage directions / explanation
#
# --- Four candidates of my own, scored 1-5 per criterion ---
#
# Candidate A: "Waiter seated us at 9am sharp, served cold leftovers from Friday, then billed us for five more days. Never again."
#   C1=5 C2=5 (waiter+dish+bill) C3=5 (Friday leftovers + 5 more days = the work week) C4=4 C5=5 (20 words)  TOTAL=24
#
# Candidate B: "Table for one, alarm for six. The special was just last week's stress, reheated. Would not recommend."
#   C1=4 C2=4 (table+dish) C3=3 (alarm/stress could be any weekday) C4=5 C5=5 (17 words)  TOTAL=21
#
# Candidate C: "Booked for the weekend, got seated Monday instead. Coffee was watery, inbox was full, tip was my will to live."
#   C1=5 C2=4 (seating+coffee+tip) C3=5 (weekend vs Monday) C4=4 C5=5 (20 words)  TOTAL=23
#
# Candidate D: "Server never came, menu was just 'meetings', and they charged me 8 hours for a 2-hour meal. Avoid."
#   C1=4 C2=5 (server+menu+bill) C3=2 (meetings happen any day) C4=4 C5=5 (18 words)  TOTAL=20
#
# Winner: Candidate A (24/25) — most complete restaurant scene and the
# Friday-leftovers / five-more-days bill is Monday-specific.

# Revision 1: tightened to first-person diner voice ("me" not "us") and
# dropped filler "sharp" — reads more like a real review, easier to retype.
# Revision 2: sharpened dish + bill wording ("Friday's cold leftovers",
# "charged me") and cut two words — punchier, more quotable, still Monday-only.
LINE = "Waiter seated me at 9am, served Friday's cold leftovers, then charged me for five more days. Never again."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
