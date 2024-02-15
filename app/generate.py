import secrets


if __name__ == "__main__":
    api_key = secrets.token_hex(16)
    print(api_key)
    