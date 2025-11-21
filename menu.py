from jadwal import Jadwal
from stopwatch import waktu
from admin import kal

a = Jadwal()
b= waktu()
c= kal()

def main_menu():
    while True:
        print("=== Menu Utama ===")
        print("1. jadwal")
        print("2. stopwatch")
        print("4. Kalkulator")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            jadwal_menu()
        elif choice == "2":
            stopwatch_menu()
        elif choice == "3":
            calc.run()
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
    while True:
        b.show()
        b.time()

if __name__ == "__main__":
    main_menu()
