<b>Funkcionális specifikáció</b>
<br />
Q-easy – <p></p>

Jelen funkcionális specifikáció azon követelményeket tartalmazza, amelyekre
a szoftvernek reagálnia szükséges és definiálja azt is, hogy ez milyen
módon történjen meg.

<h2>Követelménylista</h2>
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
<h2>Felhasználói kézikönyv</h2>

<h3><b>GYIK</b></h3>

<h3><b>Bemutatás</b></h3>

<h3><b>Verzió</b></h3>

<h3><b>Kompatibilitás</b></h3>
Az program különböző operációs rendszereken is használható és széles körű kompatibilitást kínál a felhasználók számára.<br>
<b>Windows:</b> Az alkalmazás működik Windows operációs rendszeren, ideértve a legújabb verziókat is, mint például a Windows 11.<br>
<b>macOS:</b> Az kvízoldal támogatja a macOS-t, így futtatható az Apple gépeken is, például MACBookokon vagy iMAC-eken.<br>
<b>Linux:</b> Az alkalmazás kompatibilis a különböző Linux disztribúciókkal, például Ubuntu, Fedora. A legelterjedtebb Linux változatokon futtatható.<br>

<b>Webböngészők:</b> Az applikáció megfelelően működik a legtöbb webböngészőben, mint például a Google Chrome, Mozilla Firefox, Edge, Safari vagy Opera.<br>
<b>Python:</b> A Django backend Python programozási nyelven íródott, ezért Python 3+ verzió szükséges a backend futtatásához.<br>
<b>Django:</b> Az alkalmazás Django keretrendszerre épül, tehát a Django telepítése és konfigurálása szükséges a backend működéséhez.

Összességében, az alkalmazás különböző operációs rendszerekkel és széles körű segédprogram-támogatással rendelkezik, így lehetővé teszi a felhasználók számára, hogy a saját preferenciáik szerint használják és élvezzék az alkalmazás által nyújtott előnyöket és funkciókat.

<h3><b>Hibák, Hibaüzenetek</b></h3>
Az alkalmazásban jelenleg számos státusz-/hibakódba lehet ütközni. Ezeket fogja összegezni ez a bekezdés.<br>
<b>(status=200)</b> Sikeres bejelentkezés! A 200-as üzenet jelzi, hogy a felhasználó sikeresen bejelentkezett a webalkalmazásba. Ebben az esetben nincs hiba, és a bejelentkezés folyamata sikeresen lezajlott.<br>
<b>(status=201)</b> Sikeres regisztráció! Ez az üzenet jelzi, hogy a felhasználó sikeresen regisztrált a webalkalmazásban. Ebben az esetben nincs hiba, és a regisztráció folyamata sikeresen lezajlott.<br>
<b>(status=400)</b> Ilyen névvel vagy e-mail címmel már történt regisztráció! Ez azt jelzi, hogy a felhasználó már regisztrált a megadott névvel vagy e-mail címmel. Ebben az esetben a regisztráció nem sikerült, mert a megadott adatok már foglaltak.<br>
<b>(status=404)</b> Nem található ilyen felhasználónév és jelszó párosítás! Ebben az esetben a megadott felhasználónév és jelszó párosítás nem található a rendszerben. Javasolt ellenőrizni a név és jelszó helyes bevitelét, hiszen a leggyakoribb esetben az adatok elgépelésekor jelenik meg ez a hiba.<br>
<b>(status=500)</b> Adatbáziskapcsolati hiba történt! Ez a hibaüzenet azt jelzi, hogy valamilyen adatbáziskapcsolati probléma merült fel. Ez lehet például az adatbázis nem elérhetősége vagy az adatbázis leállása. Ebben az esetben az javasolt újra próbálkozni vagy ellenőrizni a kapcsolatot az adatbázissal.<br>
Ezen felül több helyen is találkozhatunk hibaüzenetekkel, amik nincsenek külön státuszkóddal ellátva. Például a regisztrációnál ha esetleg egy adatot kihagyunk akkor azonnali visszajelzést kapunk arról, hogy azt nem lehet üresen hagyni. Ilyen üzenetek az applikáció minden részén megtalálhatóak.
<h3><b>Támogatás</b></h3>
Ha a felhasználónak segítségre van szüksége az oldal használatával vagy bármilyen kérdés merül fel, akkor a következő módon tudják felvenni a kapcsolatot: <br>
<b>E-mail:</b> A felhasználó e-mailben felvehetik a kapcsolatot az oldal adminisztrátorával az alábbi e-mail címen: quiz@uni-eszterhazy.hu.<br>
<b>Telefon:</b> Az kvízoldalon telefonos segítségnyújtás elérhető a következő telefonszámon: [+36 12 345 678].<br>
<b>Személyes találkozó:</b> A felhasználó előzetes időpont egyeztetése után személyesen is felkereshetik az EKKE jászberényi helyszínét, hogy segítséget kérjenek/kapjanak az oldal használatával kapcsolatban.<br>
<br>


<h2>Jelenlegi üzleti folyamatok modellje</h2>

A mai modern korban az oktatás és a tanulást segíti, egyszerűsítő technológiák használata
még nem ment keresztül elég széleskörű térhódításan a közoktatásban. A diákok sokszor keresik
a tanulást segíti és interaktív megoldásokat céljaik elérésében. A legtöbb tanár papír alapon
ad "tesztdolgozatokat" avagy rövid kvízeket, hogy a diákok tudását felmérje, és, hogy a diákok
gyakorolni tudjanak. Az ebből származó kinyomtatott formájú papírok, pedig elég magas nyomdai
költséget jelentenek, valamint a tanárnak egyesével kell a dolgozatokat javítania, amely ismételten
időt és pénzt emészt fel. A XXI. században pedig ezen költségek jelentősen csökkenthetőek lennének.


<h3><b>A készülendő szoftver navigációs vázlata:</b></h3>


![Navigációs vázlat](./Diagramms/navigacios_vazlat.png)