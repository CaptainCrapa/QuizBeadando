<b>Tesztelési Dokumentáció</b>
<br />
Q-easy – <p></p>

<h2>Első backend teszt</h2>

|            |                                                                                         |
|------------|-----------------------------------------------------------------------------------------|
| Dátum:     | 2023.05.09. 19:00                                                                       |
| Indította: | Fülöp Martin                                                                            |
| Teszt:     | Regisztrációs unit test lefuttatása a tests.py-ból |
 | Kimenet:   | A teszt sikeresen lefutott hiba nélkül                                                              |
 | Parancs:           | "python manage.py test --pattern="tests.py"                                             |

<h2>Második backend teszt</h2>

|            |                                                |
|------------|------------------------------------------------|
| Dátum:     | 2023.05.09. 20:10                              |
| Indította: | Fülöp Martin                                   |
| Teszt:     | Bejelentkezési integrációs test és a Regisztrációs unit test lefuttatása a tests.py-ból |
 | Kimenet:   | A teszt sikeresen lefutott                     |
 | Parancs:           |     "python manage.py test --pattern="tests.py"|

<h2>Harmadik backend teszt</h2>

|            |                                                                                    |
|------------|------------------------------------------------------------------------------------|
| Dátum:     | 2023.05.13. 17:00                                                                  |
| Indította: | Fülöp Martin                                                                       |
| Teszt:     | Regisztrációs végpont tesztelése swagerrel                                         |
 | Kimenet:   | A teszt sikeresen lefutott, a végpont minden bemenetelre jól reagált               |
 | Parancs:           | A localhost:8000/api/docs-on keresztül swagger végpont request és response tesztje |
 | Böngésző: | Google Chrome                                                                      |

<h2>Negyedik backend teszt</h2>

|            |                                                                                    |
|------------|------------------------------------------------------------------------------------|
| Dátum:     | 2023.05.13. 17:00                                                                  |
| Indította: | Fülöp Martin                                                                       |
| Teszt:     | Bejelentkezési végpont tesztelése swagerrel                                        |
 | Kimenet:   | A teszt eredményeképpen a végpont minden bemenetelre jól reagált                   |
 | Parancs:           | A localhost:8000/api/docs-on keresztül swagger végpont request és response tesztje |
 | Böngésző: | Google Chrome                                                                      |


<h2>Ötödik backend teszt</h2>

|            |                                                                                    |
|------------|------------------------------------------------------------------------------------|
| Dátum:     | 2023.05.13. 17:00                                                                  |
| Indította: | Fülöp Martin                                                                       |
| Teszt:     | Adminisztrátori jelszómódosítási jogosultság végpont tesztelése swagerrel          |
 | Kimenet:   | A teszt minden inputra jól reagált                                                 |
 | Parancs:           | A localhost:8000/api/docs-on keresztül swagger végpont request és response tesztje |
 | Böngésző: | Google Chrome                                                                      |


<h2>Hatodik backend teszt</h2>

|            |                                                                                    |
|------------|------------------------------------------------------------------------------------|
| Dátum:     | 2023.05.13. 17:00                                                                  |
| Indította: | Fülöp Martin                                                                       |
| Teszt:     | Adminisztrátori felhasználó regisztrálási végpont tesztelése swagerrel             |
 | Kimenet:   | A teszt minden inputra jól reagált                                                 |
 | Parancs:           | A localhost:8000/api/docs-on keresztül swagger végpont request és response tesztje |
 | Böngésző: | Google Chrome                                                                      |
