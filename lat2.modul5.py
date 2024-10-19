def hitung_tiket():
    total_harga = 0.0
    
    while True:
        umur_input = input("Masukkan umur : ")
        
        if umur_input == "":
            break
        
        try:
            umur = int(umur_input)
        except ValueError:
            print("Masukkan nilai yang valid untuk umur.")
            continue
        
        if umur <= 2:
            harga = 0.0
        elif 3 <= umur <= 12:
            harga = 14.0
        elif umur >= 65:
            harga = 18.0
        else:
            harga = 23.0
        
        total_harga += harga
        print(f"Harga : ${harga:.2f}")
        print(f"Running Total : ${total_harga:.2f}")
    
    print(f"Total harga : ${total_harga:.2f}")

    uang = float(input("Masukkan jumlah uang: "))
    
    if uang > total_harga:
        kembalian = uang - total_harga
        print(f"Kembalian : ${kembalian:.2f}")
    elif uang < total_harga:
        print("Uang tidak cukup.")
    else:
        print("Pembayaran uang pas, tidak ada kembalian.")

hitung_tiket()