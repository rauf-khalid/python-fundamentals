import string
import secrets
import re
import argparse

def build_charset(use_symbols: bool) -> str: 
    charset = string.ascii_letters + string.digits
    if use_symbols:
        charset += string.punctuation
    return charset

def generate_password(length: int = 12, use_symbols: bool = False) -> str:
    charset = build_charset(use_symbols)
    password_chars = [secrets.choice(charset) for _ in range(length)]
    password = "".join(password_chars)
    return password

def generate_password_guaranteed(length: int, use_symbols: bool) -> str:
    required_pools = [string.ascii_lowercase , string.ascii_uppercase , string.digits]
    if use_symbols:
        required_pools.append(string.punctuation)
    
    if length < len(required_pools):
        raise ValueError(
            f"Length {length} is too short to guarantee all required "
            f"character types ({len(required_pools)} needed)."
        )
    
    guaranteed_chars = [secrets.choice(pool) for pool in required_pools]

    full_charset = string.ascii_letters + string.digits
    if use_symbols:
        full_charset += string.punctuation
    
    remaining_count = length - len(guaranteed_chars)
    filler_chars = [secrets.choice(full_charset) for _ in range(remaining_count)]

    all_chars = guaranteed_chars + filler_chars

    secrets.SystemRandom().shuffle(all_chars)

    return "".join(all_chars)

def score_strength(has_pattern, reasons, description, priority: int = 1):
    count = 0
    if bool(has_pattern):
        count = priority
    else:
        reasons.append(description)
    return count
    
def label_strength(strength_count: int):
    if strength_count == 0:
        return "Very Weak"
    elif strength_count < 3:
        return "Weak"
    elif strength_count < 5:
        return "Medium"
    else:
        return "Strong"

def check_strength(password: str, threshold_length: int = 12):
    strength_count = 0
    reasons = []

    length = len(password)
    has_digit = re.search(r"\d", password)
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)

    symbols = f"[{re.escape(string.punctuation)}]"
    has_symbol = re.search(symbols, password)

    if length < threshold_length:
        reasons.append("Password is shorter than 12 characters.")
    else:
        strength_count += 1
 
    strength_count += score_strength(has_digit, reasons, "Missing a number.")
    strength_count += score_strength(has_lower, reasons, "Missing a lowercase letter.")
    strength_count += score_strength(has_upper, reasons, "Missing an uppercase letter.")
    strength_count += score_strength(has_symbol, reasons, "Missing a symbol.")

    label = label_strength(strength_count)

    return (label, reasons)
        
def main():
    parser = argparse.ArgumentParser(description="Generate a secure password or check an existing one's strength.")
    parser.add_argument("--length", type=int, default=12, help="Password length (Default: 12)")
    parser.add_argument("--symbols", action="store_true", help="Include symbols in generation")
    parser.add_argument("--check", type=str, default=None, help="Check the strength of a given password")
    parser.add_argument("--guaranteed", action="store_true", help="Guarantees a secure password including the required characters if enabled")

    args = parser.parse_args()

    if args.check:
        password = args.check
    elif args.guaranteed:
        password = generate_password_guaranteed(args.length, args.symbols)
    else:
        password = generate_password(args.length, args.symbols)

    print(f"Generated Password: {password}")

    label, reasons = check_strength(password)
    print(f"Strength: {label}")  
    for reason in reasons:
        print(f"  - {reason}")

if __name__ == "__main__":
    main()
