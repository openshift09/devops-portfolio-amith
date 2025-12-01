import base64
import os

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def encrypt(text):
    """Encrypt text using base64 encoding."""
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def decrypt(encoded):
    """Decrypt base64 encoded text."""
    try:
        decoded_bytes = base64.b64decode(encoded.encode("utf-8"))
        return decoded_bytes.decode("utf-8")
    except:
        return "Invalid encrypted text!"

print("Choose an option:")
print("1. Encrypt text")
print("2. Decrypt text")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    plain = input("Enter text to encrypt: ")
    encrypted = encrypt(plain)

    out_file = os.path.join(output_folder, "encrypted.txt")
    with open(out_file, "w") as f:
        f.write(encrypted)

    print("\nEncrypted text:")
    print(encrypted)
    print(f"\nSaved to {out_file}")

elif choice == "2":
    encoded = input("Enter text to decrypt: ")
    decrypted = decrypt(encoded)

    print("\nDecrypted text:")
    print(decrypted)

else:
    print("Invalid choice!")
