# Automatizēšanas projekts "Steam Store Scraper"

Darba autors: Pāvels Ananko, 231RDB106

## Uzdevuma apraksts

### Uzdevuma nosacījumi

Noslēguma projekts ir jūsu iespēja izmantot jauniegūtās prasmes, lai izstrādātu pilnvērtīgo programmatūru noteikto uzdevuma risināšanai. Projektā jāizmanto zināšanas, kas ir iegūtas kursa laikā, bet projekta uzdevumu jāģenerē jums pašiem. Mēs gribam, lai Jūs izveidotu sistēmu, kas automatizēs kādu no jūsu ikdienas uzdevumiem.

### Pašģenerētais uzdevums

Izveidot tīmekļa skrāpēšanas programmu, kas meklē datorspēles internetveikalā Steam un saglabā tās izklājlapā.

Palaižot programmu, lietotājam jābūt iespējai norādīt filtrus:
* minimālais atsauksmju procents,
* minimālais atsauksmju daudzums,
* maksimālā datorspēles cena,
* pieļauto tagu/žanru saraksts,
* maksimālais meklēto lapu daudzums.

Programmai jāsaglabā atlasītās datorspēles un to galvenie dati izklājlapā, kārtojot tās pēc atlaides dilstošā secībā.

## Izmantotās bibliotēkas

[Requests](https://pypi.org/project/requests/) interneta lapas satura iegūšanai.

[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) iegūtā satura parsēšanai.

[OpenPyXL](https://pypi.org/project/openpyxl/) rezultātu saglabāšanai izklājlapā.

## Lietošanas instrukcija

Lai palaistu programmu, izmantojiet komandu:

```
python main.py
```

{...}