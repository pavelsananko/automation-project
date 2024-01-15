# Automatizēšanas projekts

Darba autors: Pāvels Ananko, 231RDB106

## Uzdevuma apraksts

**Uzdevuma nosacījumi**

Noslēguma projekts ir jūsu iespēja izmantot jauniegūtās prasmes, lai izstrādātu pilnvērtīgo programmatūru noteikto uzdevuma risināšanai. Projektā jāizmanto zināšanas, kas ir iegūtas kursa laikā, bet projekta uzdevumu jāģenerē jums pašiem. Mēs gribam, lai Jūs izveidotu sistēmu, kas automatizēs kādu no jūsu ikdienas uzdevumiem.

**Pašģenerētais uzdevums**

Izveidot tīmekļa skrāpēšanas rīku, kas atvieglo datorspēļu meklēšanu internetveikalā [Steam](https://store.steampowered.com/). Jābūt iespējai atlasīt datorspēles pēc to atsauksmju procentuālās vērtības, atsauksmju daudzuma, cenas un tagiem. Jābūt arī iespējai norādīt maksimālo skrāpēto lapu skaitu. Atlasīto datorspēļu dati jāsaglabā izklājlapā un jāsakārto pēc atlaides.

## Izmantotās bibliotēkas

[Requests](https://pypi.org/project/requests/) interneta lapas satura iegūšanai.

[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) iegūtā satura parsēšanai.

[OpenPyXL](https://pypi.org/project/openpyxl/) rezultātu saglabāšanai izklājlapā.

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
| Pages to scrape    | Meklēto lapu skaits                     | Vesels skaitlis, vismaz 1      | 20          |

⚠️ *Ievadot tagu, tam jāatbilst tā Steam lapai. Piemēram, lai meklētu [First Person Shooter](https://store.steampowered.com/tags/en/FPS) spēles, jāievada `fps`.*

⚠️ *Atlasītās spēles tiks saglabātas failā `result.xlsx`.*

## Sistēmas tehniskais apraksts

