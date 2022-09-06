# Máltækni—Verkefni 2

## Lýsing

### Samsetning gagnasafns

Í þessum hluta verkefnisins eigið þið að safna saman textum í eitt textasafn (eða velja einn mjög langan texta). Þið munið vinna með þetta textasafn í nokkrum verkefnum yfir þessa önn, svo við mælum með því að þið veljið texta sem þið hafið áhuga á að vinna með.

Textasafnið þarf að vera a.m.k. 20.000 (tuttugu þúsund) orð á lengd. Þið megið velja á hvaða tungumáli textarnir eru. Þið ráðið því alfarið hvaðan textarnir koma. Þið getið t.d. sótt texta á netið um efni sem þið hafið áhuga á eða þið getið skoðað gagnasöfn sem til eru (t.d. á Clarin.is) og notað þau.

### Tölfræðileg vinnsla með orð

Þegar textasafnið er tilbúið getið þið byrjað að vinna með það og greina textana nánar í einingar. Í þessum hluta verkefnisins eru 8 hlutar. Athugið að þið megið nota öll forritasöfn sem ykkur dettur í hug, t.d. þau sem fjallað var um í 2. tíma (sjá glærur á Canvas), við vinnslu þessa hluta.

Texti = textasafnið sem þið söfnuðuð saman í 1)

1. Skrifið fall sem skilar heildarfjölda orða í textanum.
2. Skrifið fall sem skilar heildarfjölda mismunandi orða (orðmynda) í textanum. (Í textanum „Api sá apa vera að apa eftir öðrum apa“ eru 7 mismunandi orðmyndir, því apa birtist þrisvar.)
3. Skrifið fall sem telur öll orðin í textanum og raðar þeim eftir því hversu oft þau birtast.
    1. Hver eru 10 algengustu orðin?
4. Endurtakið 3, nema breytið öllum hástöfum í lágstafi.
    1. Er einhver munur á tíu algengstu orðunum hér og í 3.1?
    2. Hver gæti verið ástæðan fyrir því?
5. Skrifið fall sem reiknar hlutfall einstakra orða og heildarfjölda orða.
6. Skrifið fall sem reiknar hlutfall orða sem eru lengri en 8 stafir (e. characters).
7. Skrifið fall sem skilar öllum nafnorðum textans. Raðið þeim eftir því hversu oft þau birtast í textunum.
    1. Eru 10 algengustu nafnorðin lýsandi fyrir textasafnið? Eða eru þau kannski frekar almenn?
8. Skrifið fall sem skilar orðinu sem inniheldur lengsta samhljóðaklasann og lengd samhljóðaklasans. (Samhljóðaklasi er samfelld runa af samhljóðum. Orðið sem inniheldur lengsta samhljóðaklasann í setningunni „Ég drekk ferskvatn“ væri þá „ferskvatn“ (r, s, k og v eru samhljóðar, ásamt fleiri bókstöfum) og lengd samhljóðaklasans er fjórir.)

### Umræður um samsetningu gagnasafnsins í síðustu viku

Í þessum hluta eigið þið að fjalla um eigin hugleiðingar varðandi samsetningu
umorðunarmálheildarinnar í síðustu viku. Þið þurfið að svara þessum spurningum (og
endilega fleirum, ef ykkur dettur eitthvað annað í hug).

1. Voru einhver álitamál sem komu upp hjá ykkur?
2. Hvað gerðuð þið ef þið voruð ekki viss hvaða einkunn þið vilduð gefa setningapari?
3. Hvaða gagnabjagi (e. data bias) gæti komið fram í þessum gögnum? (Ath. að það er einhver bjagi í öllum gögnum.)
4. Hvað fannst ykkur um viðmótið? Hefðuð þið viljað breyta einhverju?

## Lausn

Keyra:

```bash
> pip -r requirements.txt
> python -m unittest discover .  
> jupyter notebook
```

Sjá [verkefni2.ipynb](./verkefni2.ipynb).
