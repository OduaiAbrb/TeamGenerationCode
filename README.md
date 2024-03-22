# Team Generator

## Overview
This Python script generates random teams from a list of input members. It prompts the user to input the team size and the names of team members. After inputting the member names, it shuffles them and divides them into teams of equal size as much as possible. If there are leftover members, an additional team with fewer members will be created.

## Author
- **Author:** OduaiAburub

## Instructions
1. Run the script.
2. Input the team size when prompted.
3. Enter the names of team members one by one. Type 'done' when finished.
4. The script will generate random teams based on the input and display them.

## Usage
```python
python team_generator.py
```

## Functionality
- **generate_teams()**: 
  - Prompts the user to input the team size and member names.
  - Randomly shuffles the member names.
  - Divides the members into teams of equal size as much as possible.
  - Displays the generated teams.

## Example
```
Enter team size: 3
Enter team members (type 'done' to finish):
Member name: Alice
Member name: Bob
Member name: Charlie
Member name: David
Member name: Emily
Member name: Frank
Member name: done

Teams:
Team 1: Bob, Alice, Emily
Team 2: Frank, David, Charlie
```

## Note
- The number of teams generated might be one less than expected if there are leftover members after dividing equally into teams.
