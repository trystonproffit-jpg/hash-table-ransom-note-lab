def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.
    """

    letter_counts = {}

    for char in magazine:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    for char in ransomNote:
        if char not in letter_counts or letter_counts[char] == 0:
            return False
            
        letter_counts[char] -= 1

    return True