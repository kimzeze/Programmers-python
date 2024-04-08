def solution(participant, completion):
    participant_count = {}
    completion_count = {}

    # Count occurrences in participant list
    for name in participant:
        participant_count[name] = participant_count.get(name, 0) + 1

    # Count occurrences in completion list
    for name in completion:
        completion_count[name] = completion_count.get(name, 0) + 1

    # Check for excess participants
    for name, count in participant_count.items():
        if count > completion_count.get(name, 0):
            return name

participant = ["Alice", "Bob", "Alice", "Charlie"]
completion = ["Bob", "Charlie"]

print(solution(participant, completion))  # Output: "Alice"
