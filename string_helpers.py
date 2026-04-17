import re

def camel_to_snake(name: str) -> str:
    """Convert camelCase or PascalCase string to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case and punctuation."""
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def word_count(s: str) -> int:
    """Count the number of words in a string."""
    words = re.findall(r'\b\w+\b', s)
    return len(words)

def remove_punctuation(s: str) -> str:
    """Remove punctuation from a string."""
    return re.sub(r'[^\w\s]', '', s)