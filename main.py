import base64
import secrets

def rand_nums(no_bytes: int) -> bytes:
    return secrets.token_bytes(no_bytes)

def main():
    no_bytes = int(input("How many bits: ")) // 8
    print(f"{no_bytes} bytes ({no_bytes * 8} bits)\n\n")
    b = rand_nums(no_bytes)

    url_b64 = base64.urlsafe_b64encode(b).decode("ascii")

    print(f"SecurePass0.:{url_b64}")

if __name__ == "__main__":
    main()
