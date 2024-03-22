import random

def generate_teams():
    team_size = int(input("Enter team size: "))
    members = []
    
    print("Enter team members (type 'done' to finish):")
    while True:
        member = input("Member name: ")
        if member.lower() == "done":
            break
        members.append(member)

    random.shuffle(members)

    num_teams = len(members) // team_size
    leftover_members = len(members) % team_size

    teams = []
    start = 0
    for i in range(num_teams):
        end = start + team_size
        teams.append(members[start:end])
        start = end

    if leftover_members > 0:
        teams.append(members[-leftover_members:])

    print("\nTeams:")
    for i, team in enumerate(teams):
        print(f"Team {i+1}: {', '.join(team)}")

if __name__ == "__main__":
    generate_teams()
