import random
import string

import pyfiglet
result = pyfiglet.figlet_format('Mahmud AlfaCyber')
print(result)

def generate_random_suffix(length=12):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_random_url(username):
    random_suffix = generate_random_suffix()
    random_query_params = generate_random_suffix(length=6)
    random_fragment = generate_random_suffix(length=8)
    return (
        f"https://instagram.com/{username}/cookies/{random_suffix}"
        f"?session_id={random_query_params}"
        f"&auth_token={random_query_params}"
        f"#redirect_{random_fragment}"
    )

def validate_username(username):
    """Memvalidasi nama pengguna untuk memastikan memenuhi kriteria dasar."""
    if not username:
        return False, "Nama pengguna tidak boleh kosong."
    if len(username) < 3:
        return False, "Nama pengguna harus terdiri dari setidaknya 3 karakter."
    return True, ""

def main():
    print("create by alfa team cyber indonesia, mahmud code edited")
    
    while True:
        username = input("Masukkan nama pengguna Instagram: ").strip()

        is_valid, error_message = validate_username(username)
        if not is_valid:
            print(f"Kesalahan: {error_message}")
            continue

        random_url = generate_random_url(username)
        print(f"URL yang dihasilkan: {random_url}")
        
        another = input("Apakah Anda ingin menghasilkan URL lain? (ya/tidak): ").strip().lower()
        if another not in ["ya", "y"]:
            print("Kepo boleh resikonya sakit hato, menyalaaaaaa")
            break

if __name__ == "__main__":
    main()
