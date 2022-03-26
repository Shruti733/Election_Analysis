counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])


count = 7
while count < 10:
    print("Hello World")
    count = count +1

counties_dict = [{'Arapahoe':422829},{'Denver':463353},{'Jefferson':432438}]
for county in counties_dict:
    for county,value in county.items():
        print(f"{county} county has {value:,} registered voters" )



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:

     print(county_dict['registered_voters'])

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)