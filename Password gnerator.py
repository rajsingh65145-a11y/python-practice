# password_gen.py - Strong Random Password Generator
import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    char_pool = ""
    
    if use_upper:
        char_pool += string.ascii_uppercase      # A-Z
    if use_lower:
        char_pool += string.ascii_lowercase      # a-z
    if use_digits:
        char_pool += string.digits               # 0-9
    if use_symbols:
        char_pool += string.punctuation          # !@#$% etc.

    if not char_pool:
        return "Error: Kam se kam ek character type select karo!"

    # Randomly pick characters and shuffle them for better randomness
    password_list = random.choices(char_pool, k=length)
    random.shuffle(password_list)  # extra mixing
    return ''.join(password_list)

def main():
    print("=" * 40)
    print("   🔒 Strong Password Generator")
    print("=" * 40)

    try:
        length = int(input("Password length (e.g. 16): "))
        if length < 4:
            print("Length kam se kam 4 rakhna behtar hai.")
            return

        incl_upper = input("Include Uppercase (A-Z)? (y/n): ").strip().lower() == 'y'
        incl_lower = input("Include Lowercase (a-z)? (y/n): ").strip().lower() == 'y'
        incl_digits = input("Include Digits (0-9)? (y/n): ").strip().lower() == 'y'
        incl_symbols = input("Include Symbols (!@#)? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, incl_upper, incl_lower, incl_digits, incl_symbols)
        
        print("\n" + "-" * 40)
        print(f"✅ Generated Password: {password}")
        print(f"🔑 Length: {len(password)} characters")
        print("-" * 40)

    except ValueError:
        print("❌ Invalid input! Sirf number daalo length ke liye.")

if __name__ == "__main__":
    main()