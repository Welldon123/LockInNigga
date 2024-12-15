#Variable
banned_id = 'agus'
pass_agus = 'Agus_Sedih_Banget'
known_id = 'ilham'
pass_ilham = "ilhamkeren"
pe = " "
pe2 = " "
id_terlarang = ""
#Login pengulangan
login = input('Masukan Id anda:')
if login == banned_id:
    skibidi = input('Masukan Password anda:')
    if skibidi == pass_agus:
        print('Anda di banned!')
elif login == known_id:
    pe2 = input('Id Sudah Ada! Masukan password:')
    while pe2 != pass_ilham:
        pe2 = input('Password salah! Masukan password(1 = keluar):')
        if pe2 == "1":
            break
    print('Password benar!')
elif login == id_terlarang:
    while login == id_terlarang:
        login = input('Masukan Id anda:')
        if login == banned_id:
            skibidi = input('Masukan Password anda:')
            if skibidi == pass_agus:
                print('Anda di banned!')
        elif login == known_id:
            pe2 = input('Id Sudah Ada! Masukan password:')
            while pe2 != pass_ilham:
                pe2 = input('Password salah! Masukan password(1 = keluar):')
                if pe2 == "1":
                    break
            print('Password benar!')
else:
    pe = input('anda belum terdaftar! apakah anda ingin login ulang? (1 = login ulang| 2 = Buat akun baru | 3 = keluar)')
    while pe == "1":
        login = input('Masukan Id anda:')
        if login == banned_id:
            print('Anda Terbanned!')
            break
        elif login == known_id:
            pe2 = input('Id Sudah Ada! Masukan password:')
            while pe2 != pass_ilham:
                pe2 = input('Password salah! Masukan password(1 = keluar):')
                if pe2 == "1":
                    break
            print('Password benar!, silahkan masuk!')
        else:
            pe = input('anda belum terdaftar! apakah anda ingin login ulang? (1 = login ulang | 2 = Buat akun baru | 3 = keluar)')
        break
    while pe == "2":
        newid = input('Masukan Id baru anda:')
        if newid == known_id:
            print('Id sudah ada didata!')
        else:
            pass_new = input('Masukan Password anda:')
            rep_pass = input('Ulangi Password anda:')
            while rep_pass != pass_new:
                print('Password Salah! ulangi password:')
                rep_pass = input('>>')
            print('Id dan password anda terdaftar!')
        break
    if pe == "3":
        print('\nAnda keluar!')
    while pe != '1' and pe != '2' and pe != '3':
        print('Invalid masukan opsinya kembali!')
        pe = input('(1 = login ulang| 2 = Buat akun baru | 3 = keluar)')
        while pe == "1":
            login = input('Masukan Id anda:')
            if login == banned_id:
                print('Anda Terbanned!')
                break
            elif login == known_id:
                print('Anda terdaftar! silahkan masuk.')
                break
            else:
                pe = input(
                    'anda belum terdaftar! apakah anda ingin login ulang? (1 = login ulang | 2 = Buat akun baru | 3 = keluar)')
        while pe == "2":
            newid = input('Masukan Id baru anda:')
            if newid == known_id:
                print('Id sudah ada didata!')
            else:
                pass_new = input('Masukan Password anda:')
                rep_pass = input('Ulangi Password anda:')
                while rep_pass != pass_new:
                    print('Password Salah! ulangi password')
                    rep_pass = input('>>')
                print('Id dan password anda terdaftar!')

            break