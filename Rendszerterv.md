<h1><b>Rendszerterv</b></h1>
<br />
Q-easy – <p></p>


<h2>A rendszer célja</h2>
A rendszer célja, hogy a diákok és tanárok munkáját megkönnyítse. Lehetőséget biztosít,hogy
a diák rendszerezetten, jól átláthatóan és játékosan tudjon tanulni és gyakorolni, valamint
előrehaladásáról és sikerességéről egyfajta visszacsatolást szerezzen. A tanárok részéről pedig
megadja azt a szabadságot, hogy a kvízek könnyen módosíthatóak és szerkeszthetőek, papírt és nyomtatási
összeget spórol, valamint leveszi a javítás okozta felelősséget és hibázási lehetőséget a tanárról, mivel
a rendszer automatikusan ellenőrzi, hogy a kvízek mely kérdései lettek helyesen kitöltve. A rendszer webes
felületen kell, hogy működjön, bármi egyéb felületen például mobilon, avagy számítógépes telepítés révén
a rendszer nem kell, hogy fusson. A diákok kvízeket tudnak kitölteni, amelyeket a tanárok állítottak össze
számukra. A tanároknak lehetősége lesz kvízeket készíteni, ezekre további személyeket meghívni, valamint
a kvízeiket módosítani. Szükséges egy adminisztrátor szerepkör is, aki szükség esetén beavatkozni képes a rendszer
működésébe és képes elhárítani az esetleges hibákat, valamint egyfajta "supervisor"-ként revízió alá tudja vonni
az elkészült termékeket, vagy más néven kvízeket. Az adminisztrátor szerepkör képes lesz jelszavakat visszaállítani,
kvízeket módosítani, kvízeket törölni, vagy új felhasználókat felvenni, esetleg egy meglévő felhasználó szerepkörét módosítani.

<h2>A frontend működése:</h2>

Az oldal dinamikusan jeleníti meg a tartalmát a felhasználó jogosultságai alapján. A következő jogosultságok különböztethetők meg: adminisztrátor, tanár és diák.

<h3>Diák jogosultság:</h3>

<b>Főoldal:</b> A kezdőoldal, ahol általános információk, hírek jelennek meg.<br>
<b>Kvízek:</b> Ezen a lapon találhatóak a rendelkezésre álló kvízek listája. A diák kiválaszthatja a kvízt, amelyhez részt szeretne venni.<br>
<b>Profil:</b> A felhasználó adatainak megtekintése lehetséges ezen az oldalon.<br>
<b>Kijelentkezés:</b> A felhasználó kijelentkezik az oldalról.<br>

<h3>Tanár jogosultság:</h3>

<b>Főoldal:</b> Ugyanazok az információk és hírek, mint a diákok számára.<br>
<b>Kvízek:</b> A tanár hozzáfér a kvízekhez, amelyeket létrehozott vagy amelyekhez hozzáférést kapott. Itt megjelenik a "Kvíz létrehozás" lehetőség, amellyel új kvízt hozhat létre.<br>
<b>Profil:</b> A felhasználó adatainak megtekintése lehetséges ezen az oldalon.<br>
<b>Felhasználók:</b> Amennyiben tanári jogosultságokkal rendelkezik a felhasználó abban az estben jelenik meg ez az opció a felső listában. Itt felhazsnálókat tud meghívni kvízekre. <br>
<b>Kijelentkezés:</b> A felhasználó kijelentkezik az oldalról.<br>

<h3>Adminisztrátor jogosultság:</h3>

<b>Főoldal:</b> Ugyanazok az információk és hírek, mint a diákok számára.<br>
<b>Kvízek:</b> Az adminisztrátor hozzáfér a kvízekhez, amelyekhez hozzáférést kapott. Itt megjelenik a "Kvíz törlése" lehetőség, amellyel a kvíz törölhető.<br>
<b>Profil:</b> A felhasználó adatainak megtekintése lehetséges ezen az oldalon.<br>
<b>Felhasználók:</b> Az adminisztrátor a felhasználók kezelésével kapcsolatos funkciókhoz fér hozzá. Ide tartozik az "Új felhasználó", "Szerepkör módosítása" és a "Jelszó helyreállítás" funkciók.<br>
<b>Kijelentkezés:</b> A felhasználó kijelentkezik az oldalról.<br>

Fontos megjegyezni, hogy a tanárnak és az adminisztrátornak minden olyan jogosultsága van, ami a diákoknak is megvan.

<h2>Projektterv</h2>

<h3>Projektszerepkörök, felelősségek</h3>
* Scrum master: Meetingeket szervez, egyeztet a csapat többi tagjával az előrehaladás
    állapotáról, beütemezi a teendőket, kontaktként szolgál a megrendelő számára
* Back-end developers: A készülő projekt adatbázis és szerver oldali logikájának és
    hierarchiájának kiépítésért felel, kommunikál a front-end-el, felépíti a request és
    response osztályokat
* Front-end developers: A készülő projekt vizuális és megjelenítési komponenseiért felel,
    folyamatosan kommunikál a back-end fejlesztőkkel és a megbeszélt request-eket küldi,
    valamint megjelenítő modelljeit a megbeszélt response-ok szerint építi fel
* Tester: A projekthez tartozó tesztlépéseket és tesztdokumentációkat készíti el,
    részletesen megfigyelve és ellenőrizve a szoftver helyes működését
* Product Owner: Hozzá tartozik az alkalmazás, megfigyeli, hogy a szoftver eleget tesz-e kéréseinek,
    tartalmazza-e elképzeléseit és elvárásait. Szükség esetén javaslatot tesz, új ötleteket és javítási
    methódikákat szorgalmaz, amennyiben indokolt

<h3>Projektmunkások és felelősségeik</h3>

Scrum master:
* Fülöp Martin

Back-end developers:
* Kovács-Szűcs Márton
* Bitó Sándor
* Fülöp Martin

Front-end developers:
* Bukovics Péter
* Tóth Norbert

Testers:
* Kovács-Szűcs Márton
* Bitó Sándor
* Fülöp Martin

Product Owners:
* Bukovics Péter
* Tóth Norbert

<h3>Mérföldkövek</h3>
* Első sikeres regisztráció és bejelentkezés
* Sikeres kvíz kitöltés
* Sikeres adminisztrátori módosítások
* Első demo project elkészítése
* Projekt átadása