<b>Funkcionális specifikáció</b>
<br />
Q-easy – <p></p>

Jelen funkcionális specifikáció azon követelményeket tartalmazza, amelyekre
a szoftvernek reagálnia szükséges és definiálja azt is, hogy ez milyen
módon történjen meg.

<h3><b>Regisztráció:</b></h3>
Az alkalmazás használata kizárólag a regisztrációt követően válik elérhetővé.
Ehhez szükséges egy regisztrációs űrlap kitöltése. A regisztrációt űrlap
a következő mezőkkel fog tervezetten rendelkezni, ezek közül * jelzi a kötelező
mezőket:

Név*

Felhasználónév*

Jelszó*

Jelszó újra*

Email*

Születési dátum

* Amikor a felhasználó rákattint a regisztráció gombra, akkor egy új fülön
egy regisztráció ablaknak kell megnyílnia.
* Amikor a felhasználó az adatok begépelése közben egy kötelező mezőt üresen
hagyott, a programnak üzenettel kell tájékoztatni a kitöltendő mező fontosságáról.
* Amikor a felhasználó az összes szükséges adatot begépelte és rákattintott a
regisztráció gombra, a rendszernek meg kell vizsgálnia, hogy ilyen felhasználó
névvel történt-e már regisztráció, és amennyiben igen,tájékoztatnia kell erről
a regisztrációt indító felhasználót.
* Amennyiben a begépelt felhasználónév szabad, a rendszernek az adatokat lementve
létre kell hoznia egy felhasználói fiókot.
* Ha a fiók létrehozása sikeresen megtörtént, a rendszernek vissza kell irányítania
a felhasználót a bejelentkezési oldalra és tájékoztatnia a sikeres regisztrációról.
* Az adminisztrátorok létrehozására kizárólag hozzáadással legyen lehetőség, kimondottan
regisztrálni adminisztrátort tilos!

<h3><b>Bejelentkezés:</b></h3>
A regisztrációt követően a felhasználónak lehetősége nyílik a bejelentkezésre
és ezáltal a program nyújtotta további funkciók igénybevételére. Ehhez szükséges
egy bejelentkező űrlap, ahol a felhasználónak a regisztrációkor megadott
felhasználónevét és jelszavát kell használnia. Az űrlap tervezett mezői:

Felhasználónév

Jelszó

* Amikor a felhasználó begépeli a felhasználónevét és jelszavát, a rendszernek
le kell ellenőriznie, hogy van-e ilyen felhasználónév+jelszó kombinációval
felhasználó létrehozva.
* Amennyiben nincs, úgy tájékoztassa a felhasználót arról, hogy valamilyen adat
nem megfelelően lett begépelve.
* Amennyiben az adatok helyesek és a regisztrált fiók megtalálásra került,
jelentkeztessük be a felhasználót és töltődjön be számára az alkalmazás főoldala.
* A diákok, tanárok és adminisztrátorok bejelentkezése ugyan azon a bejelentkezési
fülön kell, hogy megtörténjen.


<h3><b>A készülendő szoftver navigációs vázlata:</b></h3>


![Navigációs vázlat](./Diagramms/navigacios_vazlat.png)