# Sembilan belas  tahun yang lalu, umur  Anak  setengah tahun lebih muda dari seperempat umur Ibunya.
# Umur anak sekarang 19 tahun lebih tua dari sepertujuh  umur Ibunya.
# Berapa umur Ibu  saat melahirkan anaknya ?



# Umur andi dan ayahnya sekarang jumlahnya 50 tahun,
# 4 tahun yang lalu,umur ayah 6 kali umur andi.
# Umur andi dan umur ayahnya saat ini berturut turut adalah?

totUmur = 50
lalu = 4
rasio = 6
x = totUmur-(lalu*2)
muda = int(x/(rasio+1))
tua = muda*rasio

print(f'Saat ini umur Andi adalah {muda+lalu} tahun, sedangkan umur Ayahnya adalah {tua+lalu} tahun')