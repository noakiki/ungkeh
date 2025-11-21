class Jadwal:
    def __init__(self):
        self.tasks = {
            "senin": [],
            "selasa": [],
            "rabu": [],
            "kamis": [],
            "jumat": [],
            "sabtu": [],
            "minggu": []
        }

    def add_task(self):
        print("Pilih hari:")
        print("Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu")

        day = input("Masukkan hari: ").lower()

        if day not in self.tasks:
            print("Hari tidak valid!\n")
            return

        task = input("Masukkan nama tugas: ")
        time = input("Jam (contoh 14:00): ")

        self.tasks[day].append((task, time))
        print("Tugas ditambahkan!\n")

    def show_tasks(self):
        print("\n=== Jadwal Mingguan ===")

        for day, task_list in self.tasks.items():
            print(f"\n--- {day.capitalize()} ---")

            if len(task_list) == 0:
                print("Tidak ada tugas")
            else:
                for t, time in task_list:
                    print(f"{time} - {t}")

        print("")

objek = Jadwal()
objek.show_tasks()
