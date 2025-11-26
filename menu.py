from jadwal import Jadwal
import stopwatch
from admin import kal
import time

a = Jadwal()
c = kal()

nama = "nafqi"
pas = "123"

def main_menu():
    login()
    while True:
        print("\n=== Menu Utama ===")
        print("1. Jadwal")
        print("2. Stopwatch")
        print("3. Kalkulator")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            jadwal_menu()
        elif choice == "2":
            stopwatch_menu()
        elif choice == "3":
            c.run()
        elif choice == "0":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.\n")


def jadwal_menu():
    while True:
        print("\n=== Menu Jadwal ===")
        print("1. Tambah Tugas")
        print("2. Lihat Jadwal")
        print("0. Kembali")

        choice = input("Pilih: ")

        if choice == "1":
            a.add_task()
        elif choice == "2":
            a.show_tasks()
        elif choice == "0":
            return
        else:
            print("Pilihan tidak valid.\n")


def stopwatch_menu():
    print("\n=== STOPWATCH ===")
    print("Tekan q + ENTER untuk kembali ke menu.\n")

    while True:
        stopwatch.show()
        time.sleep(1)
        stopwatch.time()

        if stopwatch.second % 5 == 0:
            if input("Tekan q untuk keluar atau Enter untuk lanjut: ") == "q":
                return


def login():
    while True:
        user = input("Masukkan username: ")
        pw = input("Masukkan password: ")

        if pw == pas and user == nama:
            print("Login berhasil!\n")
            break
        elif pw == pas and user != nama:
            print("Username salah")
        elif pw != pas and user == nama:
            print("Password salah")
        else:
            print("Username dan password salah!\n")


if __name__ == "__main__":
    main_menu()