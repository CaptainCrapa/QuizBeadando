<b>Követelményspecifikáció</b>
<br />
<h3>Áttekintés</h3>
Q-easy – <p></p>

A Q-easy egy böngészős alkalmazás, mely tanároknak segít feladatválasztós quizeket létrehozni, valamint ezen kvízekhez tanulóit invitálni. Nyomon követheti, hogy mely tanulója milyen sikerekkel képes elvégezni az elkészített kérdéssorokat. 
Külsős személyek ne tudjanak regisztrálni a rendszerbe.
A Q-easy lehetőséget nyújt arra, hogy a tanulók megtekinthessék eredményeiket.
Legyen egy olyan szerepkör, aki tud rögzíteni felhasználókat és tudja kezelni őket, valamint be is tudja állítani, hogy az illető személy Tanár vagy Diák.
Egy felhasználó rendelkezhessen több szerepkörrel is.
Ezen adatokat az alkalmazás adatbázisban kell, hogy tárolja.
Az adatok visszaállítására legyen lehetőség.

<h3>Jelenlegi helyzet</h3>

Jelen álláspont szerint a diákok legtöbbször papír alapon tudnak kvízeket kitölteni,
és azt nem kell részletezni, hogy ez milyen többletmunkát, nyomtatási papírmennyiséget
és időt emészt fel. A diákok általában 1-1 kvízt tudnak kitölteni és ezáltal gyakorolni egy
esetleges vizsgára. A Q-easy rendszer segítségével a nyomtatott papírok mennyisége csökken,
a tanárok pedig néhány kattintás segítségével tudják kvízeiket összeállítani. Ez megkönnyíti a
tanárok munkáját és segíti a diákokat, hogy egy esetleges dolgozatra hatékonyabban legyenek képesek
felkészülni a tanár által biztosított gyakorló kvízek segítségével. A papír alakú kvízekkel
továbbá probléma, hogy a tanár csak kijavítja, bejelöli, hogy az adott kérdésre a válasza helytelen,
de nem jelzi, hogy mi lett volna a helyes, valamint a diákok nem tudnak annyit tanulni, amennyit esetlegesen
kellene nekik, avagy szeretnének. A Q-easy szoftverben összeállított kérdéssorok alapján a diák akár egy témakörben
több kérdésből összeállított random kérdéseken keresztül effektívebben tud tanulni, és akkor és annyiszor veszi
elő a szoftvert és tanul, ahányszor csak szeretne.
<hr />
<h3><b>Funkcionális követelmények:</b></h3>
Roles:<br />

* Adminisztrátor: <p>
Az adminisztrátor felvehet új felhasználókat a rendszerbe. <br />
Az adminisztrátor módosíthatja a felhasználók szerepkörét. <br />
Az adminisztrátor törölhet Quizeket. <br/>
Az adminisztrátor állíthat vissza jelszót.
* Tanár: <p>
A tanár létrehozhat igaz/hamis kérdéseket a kvízhez. <br />
A tanár meghívhat felhasználókat az általa létrehozott kvízekhez.
* Felhasználó: <p>
A felhasználó ki tudja tölteni a kvízeket.

Kvíz: <br />
 * A kvíz kérdéseket tartalmaz. <br />
 * A tanár és az adminisztrátor szerkesztheti a kvízeket. <p>

Kérdés:<br />
 * A kérdés igaz/hamis állításokra épül. <p>


<h3><b>Nem funkcionális követelmények:</b></h3><br />

* A rendszer biztonságosan tárolja és kezeli a felhasználók adatait.
* A weboldal felhasználóbarát, könnyen használható és átlátható legyen.
* A webalkalmazás gyorsan és megbízhatóan működjön.
* Az alkalmazás megfelelően működjön különböző böngészőkben és különböző eszközökön.
* Az elkészített szoftver legyen hibatűrő
* A rendszer legyen versenyképes a ma ismert hasonló szoftverekkel szemben.

<h3><b>Az alkalmazás használi eset diagrammja:</b></h3>

![Használati eset diagramm](./Diagramms/hasznalati_eset_diagramm.png)

<h3>Megbízhatóság</h3>

Az web szolgáltatás hozzáférhetőségét és megfelelő működését a szolgáltató folyamatosan biztosítja. 
Ezalól kivételt képez az időközönkénti karbantartás miatti vagy rendkívüli helyzet miatti leállások. 
A karbantartási leállási idő havonta körülbelül 1-2 óra a nem frekventált időtájban történik meg 
(esi órákban). A rendkívüle helyzet jelentése olyan események, amelyekkel a szolgáltató előre nem tud 
számolni, a bekövetkezés ideje és a leállás időtartama előre nem megbecsülhető. Ezek közés sorolható 
többek között kibertámadás a rendszer vagy a szolgáltató ellen, természeti katasztrófák, illetve 
huzamosabb ideig tartó elektromos ellátás hiánya. A fentieken túl, soron kívüli karbantartási elállás 
történhet abban az esetben, ha a szolgáltató súlyos biztonsági hibát észlel az ellenőrzések során.
Ebben az esetben a hiba azonnali javítása érdekében a rendszer szintén nem frekventált időben, soron kívül 
javítási célre 1-2 órára leáll. Errőr a felhasználók igény esetén értesítést kaphatnak.

<h3>Támogatottság</h3>

A szolgáltató folyamatos támogatást biztosít a rendszernek. Havonta kötelező leállásokkal hibakeresés 
(scanning), illetve szükség esetén frissítések telepítése történik meg. A frissítés hibák javítása, új 
funkcionalitás beépítése vagy biztonsági megerősítéseket tartalmazhatnak. A szolgáltató folyamatosan nyomon 
követi a rendszer ellenállóságát az esetleges kibertámadásokkal szemben, rendszeresen teszteni a biztonsági 
funkciókat és észlelt hiba esetén, annak súlyosságától függően soron kívül, vagy a következő karbantartási 
leállással javítja a hibát és a rendszert frissíti. A szolgáltató továbbá igény esetén tájékoztatja a felhasználókat 
a tervezett rendszerleállításokról, illetve a rendszert érintő rendkívüli eseményekről és az esetleges szükséges 
teendőkről. Ezen kívül a felhasználók a különböző észlelt hibákkal kapcsolatban e-mailen felvehetik a szolgáltatóval 
a kapcsolatot, hogy a hiba egy későbbi frissítéssel kijavításra kerüljön.

<h3>Tervezési korlátozás</h3>

A webszolgáltatás eredeti célja egy olyan online quiz és vizsga rendzser létrehozása, ahol könnyen létrehozhatóak 
tesztek, vizsgág, illetve quizek a tanárok által és aztán ezeket a hozzárendelt diákok kitölthetik. A rendszer ezt 
követően értékeli a tesztet és visszajelzést küld a diákoknak. A rendszer jelenleg nem vezet pontos statisztikákat 
arról, hogy a hány teszt, milyen arányú helyes és helytelen válasszal lett elvégezve. A jövőben a program bővíthető 
lenne ebben az irányba. A statisztikai adatok részletesen lekérdezhetőek lehetnének a tanárok és diákok által, továbbá 
a rendszer akár grafikusan is megjeleníthatné ezt a felhasználóknak. Ezen túl a bővíthetőség iránya több teszt vagy 
kérdéstípus hozzáadása a szolgáltatáshoz. Az igaz-hamis és a kiválasztós feladatokon túl, sorba rendezős, összekötős illetve algoritmikailag a leginehezebben kiértékelhető: a rövid szöveges válaszadási feladat típusok integrálása.