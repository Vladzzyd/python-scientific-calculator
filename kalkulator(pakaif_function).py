import math

#KODE WARNA
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

print(f"\n{CYAN}PROGRAM KALKULATOR SEDERHANA{RESET}")

pilihan = ("+","-","*","/","%","**","sqrt","sin","cos","tan","log","ln","exp","factorial")
pilihanfungsi = ("riwayat","matematika","reset")
pilihanulang = ("y","n")
hasilsebelumnya = None
hasiltirgonometri = None
hasilfactorial = None
riwayat = []
ulang = True

def border():
    return CYAN + "="*40 + RESET

def header(operasi):
    print(border())
    if operasi in ("+","-","*","/","%","**"):
        print(CYAN + "========== OPERASI ARITMATIKA ==========" + RESET)
    elif operasi in ("sin","cos","tan"):
        print(CYAN + "========= OPERASI TRIGONOMETRI =========" + RESET)
    elif operasi in ("log","ln","exp"):
        print(CYAN + "====== OPERASI LOGARITMA & EXPONEN =====" + RESET)
    elif operasi == "factorial":
        print(CYAN + "=========== OPERASI FACTORIAL ==========" + RESET)
    print(border())


def input_angka(pesan):
    while True:
        try:
            return float(input(YELLOW + pesan + RESET))
        except ValueError:
            print(RED + "Input harus berupa angka! Coba lagi.\n" + RESET)

def input_desimal(pesan):
    while True:
        try:
            return int(input(YELLOW + pesan + RESET))
        except ValueError:
            print(RED + "input harus berupa angka bulat! coba lagi \n" + RESET)

def tampilkan_riwayat():
    print(border())
    print(CYAN + "========== RIWAYAT PENELUSURAN =========" + RESET)
    if not riwayat:
        print("belum ada riwayat")
    else:
        print(f"{'No':<4} | {'Operasi':<25} | {'Hasil':<15}")
        print("-"*40)
        for i, item in enumerate(riwayat, start=1):
            if "=" in item:
                op, hasil = item.split("=", 1)
                print(f"{i:<4} | {op.strip():<25} | {hasil.strip():<15}")
            else:
                print(f"{i:<4} | {item:<25} | {'':<15}")
    print(border())

def hitung(angka1,operasi,angka2=None):
    if operasi == "+":
        return angka1 + angka2, f"{angka1} + {angka2} = {angka1+angka2}"

    elif operasi == "-":
        return angka1 - angka2, f"{angka1} - {angka2} = {angka1-angka2}"

    elif operasi == "*":
        return angka1 * angka2, f"{angka1} * {angka2} = {angka1*angka2}"

    elif operasi == "/":
        if angka2 == 0:
            return None,RED + "Error: pembagian dengan 0 tidak bisa!" + RESET
        return angka1 / angka2, f"{angka1} / {angka2} = {angka1/angka2}"
    
    elif operasi == "**":
        return angka1 ** angka2, f"{angka1} ^ {angka2} = {angka1**angka2}"

    elif operasi == "%":
        nilai = angka1*angka2/100
        return nilai, f"{angka2}% dari {angka1} = {nilai:.2f}"
    
    elif operasi == "sqrt":
        if angka1 < 0:
            return None,RED + "Tidak bisa menghitung akar dari angka negatif!" + RESET
        nilai = math.sqrt(angka1)
        return nilai, f"√{angka1} = {nilai:.2f}"
    
    elif operasi == "sin":
        nilai = math.sin(math.radians(angka1))
        return nilai, f"sin({angka1}°) = {nilai:.4f}"
    
    elif operasi == "cos":
        nilai = math.cos(math.radians(angka1))
        return nilai, f"cos({angka1}°) = {nilai:.4f}"

    elif operasi == "tan":
        nilai = math.tan(math.radians(angka1))
        return nilai, f"tan({angka1}°) = {nilai:.4f}"
    
    elif operasi == "log":
        if angka1 <= 0:
            return None,RED + "ERROR: logaritma tidak bisa di angka 0 atau negatif" + RESET
        nilai = math.log10(angka1)
        return nilai, f"log10 ({angka1}) = {nilai}"

    elif operasi == "ln":
        if angka1 <= 0:
            return None,RED + "ERROR: logaritma tidak bisa di angka 0 atau negatif" + RESET
        nilai = math.log(angka1)
        return nilai, f"log ({angka1}) = {nilai}"
    
    elif operasi == "exp":
        nilai = math.exp(angka1)
        return nilai, f"exponen ({angka1}) = {nilai}"
    
    elif operasi == "factorial":
        global hasilfactorial
        if  angka1 < 0:
            return None,RED + "ERROR: factorial tidak bisa di angka negatif" + RESET
        angka1 = int(angka1)
        nilai = math.factorial(angka1)
        hasilfactorial = nilai
        return nilai, f"factorial ({angka1}) = {nilai}"
    
    return None,RED + "Operasi tidak dikenali!" + RESET

# FUNGSI UTAMA KALKULATOR SEDERHANA NYA
while ulang:
    print(border())
    fungsi = input(YELLOW + "pilihan fungsi (riwayat, matematika, reset): " + RESET).lower()

    if fungsi == "riwayat":
        tampilkan_riwayat()
        continue

    elif fungsi == "reset":
        hasilsebelumnya = None
        hasiltirgonometri = None
        hasilfactorial = None
        print(f"{CYAN}hasil sebelumnya sudah di-reset{RESET}")
        continue

    elif fungsi == "matematika":
        operasi = input(YELLOW + "Masukkan operasi (+ - * / % ** sqrt sin cos tan log ln exp factorial): " + RESET)
        while operasi not in pilihan:
            print(RED + "Operasi tidak dikenali!" + RESET)
            operasi = input(YELLOW + "Masukkan operasi (+ - * / % ** sqrt sin cos tan log ln exp factorial): " + RESET)

        if hasilsebelumnya == None:
            if operasi == "factorial":
                angka1 = input_desimal("masukkan angka 1: ")
            else:
                angka1 = input_angka("masukkan angka 1: ")
        else:
            if operasi in ("sin","cos","tan") and hasiltirgonometri is not None:
                angka1 = hasiltirgonometri
                print(f"{CYAN}menggunakan input derajat trigonometri sebelumnya sebagai angka 1 dengan nilai = {hasiltirgonometri}{RESET}")
            elif operasi == "factorial" and hasilfactorial is not None:
                print(f"{CYAN}menggunakan input factorial sebelumnya sebagai angka 1 dengan nilai = {hasilfactorial}{RESET}")
            else:
                angka1 = hasilsebelumnya
                print(f"{CYAN}menggunakan hasil sebelumnya sebagai angka 1 dengan nilai = {hasilsebelumnya}{RESET}")

        if operasi not in ("sqrt","sin","cos","tan","log","ln","exp"):
            angka2 = input_angka("masukkan angka 2: ")
        else:
            angka2 = None
        
        header(operasi)
        nilai, tekshasil = hitung(angka1,operasi,angka2)
        print(GREEN + str(tekshasil) + RESET if nilai is not None else tekshasil)
        print(border())

        if nilai is not None:
            hasilsebelumnya = nilai
            if operasi in ("sin","cos","tan"):
                hasiltirgonometri = angka1
            riwayat.append(tekshasil)

    else:
        print(RED + "fungsi tidak dikenali!!" + RESET)

    pengulangan = input(YELLOW + "Ingin menghitung lagi? (y/n): " + RESET).lower()
    while pengulangan not in pilihanulang:
        pengulangan = input(YELLOW + "Ingin menghitung lagi? (y/n): " + RESET).lower()
    
    ulang = (pengulangan == "y")

