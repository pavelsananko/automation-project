# Automatizēšanas projekts

Darba autors: Pāvels Ananko, 231RDB106

## Uzdevuma apraksts

**Uzdevuma nosacījumi**

Noslēguma projekts ir jūsu iespēja izmantot jauniegūtās prasmes, lai izstrādātu pilnvērtīgo programmatūru noteikto uzdevuma risināšanai. Projektā jāizmanto zināšanas, kas ir iegūtas kursa laikā, bet projekta uzdevumu jāģenerē jums pašiem. Mēs gribam, lai Jūs izveidotu sistēmu, kas automatizēs kādu no jūsu ikdienas uzdevumiem.

**Pašģenerētais uzdevums**

Izveidot tīmekļa skrāpēšanas rīku, kas atvieglo datorspēļu meklēšanu internetveikalā [Steam](https://store.steampowered.com/). Jābūt iespējai atlasīt datorspēles pēc to atsauksmju procentuālās vērtības, atsauksmju daudzuma, cenas un tagiem. Jābūt arī iespējai norādīt maksimālo skrāpēto lapu skaitu. Atlasīto datorspēļu dati jāsaglabā izklājlapā un jāsakārto pēc atlaides.

## Lietošanas instrukcija

Lai palaistu rīku, izmantojiet komandu:

```
python main.py
```

Ievadiet spēļu meklēšanas iestatījumus:

| Iestatījums        | Apraksts                                | Atļautās vērtības              | Piemērs     |
|--------------------|-----------------------------------------|--------------------------------|-------------|
| Min review percent | Minimālā atsauksmju procentuālā vērtība | Vesels skaitlis, no 0 līdz 100 | 80          |
| Min review count   | Minimālais atsauksmju skaits            | Vesels skaitlis, vismaz 0      | 1000        |
| Max product price  | Maksimālā cena                          | Vesels skaitlis, vismaz 0      | 30          |
| Tags to search     | Tagi vai žanri                          | Teksts, atdalīti ar komatu     | fps, puzzle |
| Pages to scrape    | Meklēto lapu skaits                     | Vesels skaitlis, vismaz 1      | 50          |

> [!WARNING]
> *Ievadot tagu, tam jāatbilst tā Steam lapai. Piemēram, lai meklētu [First Person Shooter](https://store.steampowered.com/tags/en/FPS) spēles, jāievada `fps`.*
>
> *Atšķirībā no parastās Steam meklēšanas, spēle tiks atlasīta, ja tās tagi satur vismaz vienu no meklētajiem tagiem.*

Atlasītās spēles tiks saglabātas failā `result.xlsx`.

## Rīka darbības apraksts

Pirms meklēšanas, rīks prasa ievadīt meklēšanas iestatījumus un pārveido tos pareizajos datu tipos.

Pēc iestatījumu ievadīšanas, tas skrāpē katra ievadītā taga Steam lapu, atrod tā identifikatoru lapas HTML saturā, un pievieno to meklēto tagu identifikatoru sarakstam.

Tad rīks skrāpē spēļu kataloga lapas līdz norādītajam meklēto lapu skaitam (vai kataloga beigām, ja tas tiek sasniegts). Katras lapas HTML saturā tas atrod visus spēļu ierakstu elementus un iziet tiem cauri ar ciklu. Katras spēles ieraksta saturā rīks atrod spēles nosaukumu, hipersaiti uz spēles lapu, tās tagu sarakstu, atsauksmju procentuālo vērtību un daudzumu, cenu un atlaidi (ja saturā pastāv cenas un atlaides elementi). Pirms pievienot spēles datus atlasīto spēļu sarakstam, tiek pārbaudīts, vai tie atbilst meklēšanas iestatījumiem. Atlasītās spēles tiek sakārtotas pēc atlaides.

Pēc kataloga lapu skrāpēšanas, atlasīto spēļu saraksts tiek saglabāts Excel izklājlapu failā. Šis fails sastāv no kolonnām - nosaukums (ar hipersaiti uz spēles lapu), atsauksmju procentuālā vērtība, atsauksmju daudzums, cena, atlaide. Šīs kolonnas tiek formatētas attiecīgi to saturam un galvene (pirmā rinda) ir sasaldēta.

## Izmantotās bibliotēkas

[Requests](https://pypi.org/project/requests/) interneta lapas satura iegūšanai.

[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) iegūtā satura parsēšanai.

[OpenPyXL](https://pypi.org/project/openpyxl/) rezultātu saglabāšanai izklājlapā.
