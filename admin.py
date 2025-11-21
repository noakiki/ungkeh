class kal:
    def run(self):
        print("\n=== Kalkulator Sederhana ===")
        x = float(input("Angka pertama: "))
        op = input("Operator (+ - * /): ")
        y = float(input("Angka kedua: "))

        if op == "+":
            print("Hasil:", x + y)
        elif op == "-":
            print("Hasil:", x - y)
        elif op == "*":
            print("Hasil:", x * y)
        elif op == "/":
            print("Hasil:", x / y if y != 0 else "Error: pembagian nol")
        print("")
