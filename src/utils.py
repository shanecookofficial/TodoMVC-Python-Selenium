import random
import string


def generate_random_string(
    length: int,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_numbers: bool = True,
) -> str:
    """
    Generate a random string with the given parameters.

    Args:
        length (int): The length of the string to generate.
        use_lowercase (bool): Include lowercase letters.
        use_uppercase (bool): Include uppercase letters.
        use_numbers (bool): Include digits.

    Returns:
        str: The generated random string.

    Raises:
        ValueError: If no character sets are selected or length < 1.
    """
    if length < 1:
        raise ValueError("Length must be a positive integer.")

    char_pool = ""
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_numbers:
        char_pool += string.digits

    if not char_pool:
        raise ValueError(
            "At least one character set (lowercase, uppercase, numbers) must be True."
        )

    return "".join(random.choice(char_pool) for _ in range(length))
