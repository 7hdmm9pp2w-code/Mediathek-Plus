# Alle Versionen

Was in welcher Version neu dazukam und was behoben wurde – die neueste steht oben.
Zum Herunterladen: [neueste Version](https://github.com/7hdmm9pp2w-code/Mediathek-Plus/releases/latest) · [Hilfe](https://7hdmm9pp2w-code.github.io/Mediathek-Plus/hilfe/)

## 4.2.2

### Behoben
- Film des Tages: Nach „⬇ Herunterladen“ zeigt der Knopf jetzt, was passiert – „Wartet“, „Lädt … 42 %“, „✓ Geladen“, beim Laden aufs NAS mit „NAS:“ davor; ein Klick öffnet die Warteschlange. Vorher blieb „Herunterladen“ stehen und lud zum zweiten Klick ein.

## 4.2.1

### Neu
- **Zurück und vor wie im Browser:** Die App merkt sich die letzten 20 Ansichten – Reiterwechsel, Suchen samt Treffern, „Neu bei …“, geöffnete Serien – mit Auswahl und Position. Zurück geht mit dem Knopf „‹ …“ neben dem Suchfeld, der Zurück-Taste der Maus oder ⌘[ bzw. Alt+←, vor mit der Vor-Taste der Maus oder ⌘] bzw. Alt+→. Bisher kam man nur aus Sprüngen in die Mediathek einen Schritt zurück. Frühere Suchen kommen ohne neue Anfrage zurück.

### Behoben
- Der Film des Tages war manchmal einer, den man schon in Jellyfin oder Emby hat: Kurz nach dem Start war der Bestand des Medienservers noch nicht geladen, und die Wahl galt dann für den ganzen Tag. Jetzt wartet die Auswahl kurz auf den Bestand und wählt neu, falls der Film doch schon dort liegt.
- ⬇ auf dem Plakat fehlt jetzt auch bei Filmen, die schon im Medienserver liegen – laden lässt er sich weiterhin über die Details.

## 4.2.0

### Neu
- **Serien mit vielen Staffeln übersichtlich:** In der Liste sind die Staffeln zugeklappt – eine Zeile je Staffel, etwa „This Is Us · Staffel 2 · Folge 1–18“, mit „Staffel laden“. Ein Klick (oder →) zeigt die Folgen, ← klappt wieder zu, mit ⌥/Alt alle auf einmal. Sucht man nur eine Staffel, steht sie gleich offen. In der Plakatansicht ist jede Serie eine Karte („16 Folgen · 2 Staffeln“) – „Neu bei ZDFneo“ zeigt so rund 130 Karten statt über 1600 Einträge.
- **Zurück-Taste der Maus:** wirkt wie „‹ Zurück“ bzw. „‹ Für dich“ neben dem Suchfeld – etwa von „Alle Folgen anzeigen“ zurück zu „Für dich“. Ohne vorige Ansicht führt sie von einer Serie zurück zu den Serienkarten oder schließt die Details.
- **Untertitel mit zwei Schaltern:** „In die Videodatei“ und „Als SRT-Datei daneben“ – wie bei den Filminfos (Datei, NFO). Beide an heißt: für alle Geräte; einer bleibt immer an. Die bisherige Einstellung bleibt erhalten.
- **Einstellungen verschiebbar:** Das Fenster lässt sich an der Titelzeile verschieben, etwa um dahinter etwas nachzusehen. Doppelklick auf die Titelzeile holt es zurück in die Mitte.

### Behoben
- ⬇ und ☆ auf dem Plakat verschwinden sofort, wenn der Download startet (auch aufs NAS), und bleiben bei wartenden, laufenden und geladenen Filmen weg – ☆ auch bei Filmen, die schon im Medienserver liegen. Steht ein Film schon auf der Merkliste, bleibt ★ zum Entfernen. Vorher standen die Knöpfe weiter da und luden zum zweiten Klick ein.
- Folgen mit dem Jahr als Staffel, etwa „(S2026/E03)“ bei ZDFneo, werden jetzt als Serie erkannt – mit „Staffel 2026“ beim Ablegen.
- Esc blendet den Film des Tages aus – auch direkt nach dem Wechsel vom Sofa, wenn der Fokus noch im Suchfeld steht.
- Einstellungen aufgeräumt: Werte und Knöpfe stehen überall in derselben Spalte – auch bei Feldern mit (i) wie „Ordner für Serien“, NAS-Passwort und API-Schlüssel; Benutzer, „Ändern“, „Trennen“ und „Filme prüfen“ beim Medienserver sind nicht mehr rechtsbündig. Der Auswahlrahmen der Reiter wird bei der Bedienung mit der Tab-Taste nicht mehr links abgeschnitten.

## 4.1.0

### Neu
- **Plakatgröße mit einem Klick:** kleine Knöpfe − und + unten rechts über den Plakaten, je eine Spalte mehr oder weniger. Bisher ging das nur mit Tastenkürzeln oder ⌘ + Mausrad. Die Plakate lassen sich außerdem kleiner stellen als bisher – praktisch, um lange Trefferlisten schnell durchzusehen.
- **„Probier mal“ jeden Tag neu und immer mit Treffern:** Die Beispielsuchen auf der Startseite der Mediathek stammen jetzt aus dem, was gerade läuft – eine Regisseurin oder ein Regisseur und eine Hauptdarstellerin oder ein Hauptdarsteller aus gut bewerteten Filmen in den Mediatheken, dazu zwei Reihen mit aktuellen Folgen. Jeder Vorschlag ist vorher geprüft, ein Klick findet also immer etwas. Jeden Tag gibt es andere.
- **Alles Neue von einem Sender:** Auf der Startseite der Mediathek steht unter „Probier mal:“ die Zeile „Neu bei: ARD · ZDF · ARTE · 3sat …“ (weitere Sender hinter „…“). Ein Klick zeigt alles von diesem Sender, das Neueste zuerst. Dasselbe geht mit einem Klick auf den Sendernamen in den Details – mit „‹ Zurück“ zur vorigen Suche. Die Senderauswahl im Filter bleibt dabei unverändert; ✕ am Schild „Neu bei …“ beendet die Ansicht.

## 4.0.3

### Neu
- **Genre-Filter findet Dokus und Konzerte.** „Doku“, „Konzert“ und „Musik“ erkennt die App jetzt auch an den Angaben der Sender – Thema (ARTE „Entdeckung der Welt“, „ARTE Concert“, 3sat „Natur“, „Musik“ …), Sender (ZDFinfo) und Anfang der Beschreibung. Bisher kannte der Filter nur Dokumentarfilme aus TMDB/Wikidata; Fernsehdokus, Doku-Reihen und Konzertmitschnitte fehlten fast immer (in der Filmliste rund 7.000 statt 2.200 Dokus ab 40 Minuten). Dokus über Musiker stehen unter „Doku“ und „Musik“, Mitschnitte und DJ-Sets unter „Konzert“ und „Musik“. „Dokumentarfilm“ heißt im Filter jetzt „Doku“. Wer einen eigenen Doku-Ordner eingestellt hat: Dort landen jetzt auch diese Beiträge und Konzerte.
- **Details neben den Plakaten:** Öffnen sich die Details, werden die Plakate daneben schmaler – alle bleiben ganz zu sehen, nichts rutscht mehr links aus dem Bild. Bisher war das eine Einstellung im Menü „Ansicht“, jetzt ist es immer so.
- **Plakate oder Tabelle mit einem Klick:** zwei Knöpfe oben rechts statt des Menüs „Ansicht“.

### Behoben
- **Suche: Gebärdensprache verdrängt nicht mehr die normale Fassung.** Beim HR (und vereinzelt anderen ARD-Sendern) zeigte die Suche oft nur „… (Gebärdensprache)“ – die normale Fassung fehlte, weil beide dieselbe Seite und Länge haben und die App sie für denselben Beitrag hielt. Seit 4.0.1 betraf das rund 200 Sendungen.
- **Gleicher Film oder dieselbe Doku bei zwei Sendern nur noch einmal.** Läuft ein Beitrag z. B. bei 3sat und ZDFinfo oder 3sat und Phoenix in gleicher Länge und Qualität, zeigt die Suche nur noch einen Eintrag (bevorzugt den mit dem saubereren Titel). Das gilt jetzt für alles ab 40 Minuten, nicht nur für Spielfilme ab einer Stunde; Satzzeichen wie „:“ statt „–“ im Titel stören nicht mehr. Hat einer Originalton, deutlich besseres Bild oder läuft deutlich länger, bleiben wie bisher beide – mit Hinweis. Der andere erscheint im Pro-Modus über „alle Fassungen“.
- **Dieselbe Sendung nicht mehr doppelt beim selben Sender.** Phoenix, SR, KiKA und RBB liefern viele Sendungen zweimal an die Filmliste – etwa über phoenix.de und die ARD-Mediathek. Gleicher Titel, gleiche Länge und gleiche Datei ergeben jetzt einen Eintrag in der besten Qualität (rund 600 Doppel weniger).
- **Mehr Fassungen erkannt.** Das ZDF kennzeichnet Originalfassungen inzwischen oft nur mit einem Kürzel – „(swe)“ bei „Mord im Mittsommer“, „(nld)“, „(ita)“, „(dan)“ … Die App kennt jetzt die gängigen Sprachkürzel und -namen (auch Niederländisch, Finnisch, Türkisch, Japanisch …), ebenso „(in Originalsprache)“ (ORF) und „(English Version)“. Solche Folgen erscheinen nicht mehr doppelt, sondern als „+ Schwedisch“ an der deutschen Fassung; der Originalton kommt beim Laden als zweite Tonspur mit. Österreichische Gebärdensprache „(ÖGS)“ und „(mit gesprochenen Untertiteln)“ (SRF) zählen jetzt als weitere Fassung, ebenso Gebärden- und Hörfassungen, die nur die ARD-Seitenadresse als solche verrät.
- **Film des Tages schlägt keine Filme vor, die du schon hast.** Bisher kam auch ein Film an die Reihe, der schon geladen ist, im Download-Ordner liegt oder im Medienserver (Jellyfin …) steht – mit „Herunterladen“-Knopf. Jetzt wählt die App einen anderen. Gibt es keinen neuen, oder lädst du den Film des Tages im Laufe des Tages, steht statt des Knopfs „✓ vorhanden“.
- **NAS und Web-App: Genres, Jahre und Plakate auch bei sehr vielen Treffern.** Ab etwa 1.500 Treffern (z. B. Suche „Musik“) lehnte der Server die Anfragen für Filminfos und Plakate als zu groß ab – Genre- und Jahresfilter und viele Plakate fehlten. Die Desktop-App war nicht betroffen.
- **Trailer belegen weniger Platz.** Geladene Trailer werden jetzt beim Start aufgeräumt (nach einer Woche) – bisher erst beim nächsten Trailer, bis dahin blieben auch Hunderte MB liegen. Und sie kommen höchstens in 720p statt 1080p, das halbiert ungefähr die Größe.

## 4.0.2

### Behoben
- **Fernseher-App: Live-TV wieder mit Senderliste und Sendung.** Seit der TV-App 1.1.0 läuft das Bild im ruckelfreien Android-Player – der verdeckte aber Senderliste, Sendungsanzeige und Bedienung. Jetzt liegen sie wieder darüber, und das Umschalten geht schneller (der Player startet schon nach einer Sekunde Puffer). Braucht die TV-App 1.1.2; sie lädt nach einem Update die Web-App frisch und schaltet nur mit passender Web-App durchsichtig – sonst bliebe das Bild schwarz.
- **„Über“ in der Web-App nennt die Versionen** von Web-App und TV-App.
- **Sofa: ORF nur, wo er läuft.** Außerhalb Österreichs sperrt der ORF Livestreams und viele Sendungen. Die App prüft das jetzt einmal beim Start: Ist der ORF gesperrt, fehlt sein Knopf in der Senderleiste, und Sendungen „nur für Österreich“ erscheinen weder in den Reihen noch in der Suche. Weltweit freigegebene ORF-Beiträge bleiben.
- **Sofa am Mac: Fenster lässt sich wieder verschieben** – an jeder freien Stelle der Kopfzeile (wie im Pro-Modus) und während ein Film läuft an der Titelzeile des Players. Seit 4.0 ging das im Sofa-Modus nur in einem schmalen Streifen auf Höhe der Fensterknöpfe, beim Abspielen gar nicht.
- **Sofa: eigener Lautstärkeregler im Player** oben rechts neben Einschlaf-Timer und Bild im Bild, mit Knopf zum Stummschalten. Der Regler des Mac-Players verschwand, sobald man ihn mit der Maus ansteuern wollte.
- **Sofa: Spulen von außen:** Filme melden dem System Länge und Position. Am Mac lässt sich so über die Wiedergabe-Anzeige im Kontrollzentrum bzw. in der Menüleiste und mit den Medientasten spulen (im Bild-im-Bild-Fenster selbst bietet der Mac das nicht an).
- **Sofa: „Meine Liste“ steht oben** – gleich nach „Weiterschauen“ und „Gespeichert“ statt als letzte Reihe ganz unten.
- **Sofa: Bilder bei „Weiterschauen“ und „Nächste Folge“.** In der Web-App und auf dem Fernseher blieben die Karten leer, sobald die Serie nicht mehr in den aktuellen Reihen stand. Jetzt merkt sich das Gerät das Bild beim Anschauen, und die Web-App kennt die Bilder vieler Serien auch über Tage hinweg.
- **Fernseher: Das Logo oben lässt sich nicht mehr anwählen.** Es führte dort nirgendwohin; zur Startseite geht es mit der Zurück-Taste.

## 4.0.1

### Neu
- **Der Rechner weiß, was auf dem NAS geladen wurde.** Filme und Folgen, die auf dem gekoppelten NAS geladen wurden, zeigen auch auf dem Rechner „✓ geladen“ (Hinweis: „Auf dem NAS geladen“), vor einem zweiten Download fragt die App nach, „Staffel laden“ überspringt sie, und „Passend zu dir“ zählt sie zum Geschmack und schlägt sie nicht mehr vor – auch nachdem sie aus der Warteschlange des NAS entfernt wurden. Der Rechner holt den Stand beim Verbinden und nach jedem fertigen NAS-Download. Am besten das NAS-Image mit aktualisieren; mit älteren NAS-Fassungen gilt nur, was noch in deren Bibliothek steht.
- **„✕ Nicht interessiert“ gilt auch auf dem NAS.** Was du bei „Passend zu dir“ wegklickst, schlagen auch der Sofa-Modus und die Web-App auf dem gekoppelten NAS nicht mehr vor – und umgekehrt. Abgeglichen wird beim Verbinden und nach jedem fertigen NAS-Download; dafür braucht auch das NAS 4.0.1.
- **Gleichzeitige Downloads frei wählbar.** Statt höchstens 5 lässt sich jetzt jede Zahl eintippen (bis 99).
- **Sofa-Modus: „● Live“ zoomt auf.** Wie bei den Senderkacheln fährt beim Klick auf den Live-Knopf eine Fläche in der Senderfarbe mit dem Sendernamen auf Fenstergröße auf, bis das Bild läuft.

### Behoben
- **„Passend zu dir“ schlägt Geladenes nicht mehr vor.** Ein Film, der auf dem NAS geladen wurde, stand weiter in den Vorschlägen – der Verlauf des Rechners kennt NAS-Downloads nicht. Auch was am selben Tag auf dem Rechner geladen wurde, blieb bis zum nächsten Tag stehen. Jetzt verschwindet ein Vorschlag, sobald er hier oder auf dem NAS in der Warteschlange steht oder fertig ist – auch im Sofa-Modus.
- **Filme der Landessender nur noch einmal – in bester Qualität.** Viele Beiträge führt die Filmliste doppelt, einmal unter „ARD“ und einmal unter dem Sender selbst (etwa „Könige der Welt“ bei ARD und NDR). Die App zeigte zwei Karten, und die eine lud mitunter nur die mittlere Qualität ohne HD. Jetzt erscheint der Film einmal, mit der besten Fassung.
- **„Fertige entfernen“ lässt Fehlgeschlagene stehen.** Bisher nahm der Knopf in der Warteschlange auch fehlgeschlagene Downloads mit – sie verschwanden, ehe man sie bemerkte. Jetzt gehen nur geladene und abgebrochene, wie man es vom Browser kennt; Fehlgeschlagene bleiben zum Wiederholen stehen und lassen sich einzeln mit ✕ entfernen. Gilt auch für die Liste auf dem NAS.
- **Details: Trailer wieder mit eigenem Knopf.** In der Schublade rutschte „Trailer“ ins Menü „⋯“, und in schmalen Schubladen waren die Knopfbeschriftungen abgeschnitten. Jetzt steht „Trailer“ neben „Vorschau“; ist wenig Platz, ordnen sich die Knöpfe in zwei Reihen – Vorschau und Trailer oben, Merken, Teilen und „⋯“ darunter.
- **Kein Pfeil mehr im Kopfbild.** Der Knopf für die große Ansicht wirkte wie ein Fremdkörper und ist weg. Die große Ansicht öffnet weiter ein Klick aufs Plakat oder die Leertaste.
- **Schrägstrich im Titel: Wörter bleiben getrennt.** Aus „Frankreich/Kanada“ wurde im Dateinamen „FrankreichKanada“, jetzt „Frankreich-Kanada“. Auch eigene Vorlagen wie „{serie}/S{staffel}E{folge}“ ergeben „Serie-S01E02“ statt zusammengeklebter Wörter. Schon geladene Filme mit altem Namen findet die App weiterhin.
- **Abgleich mit dem NAS sofort auch für HEVC, Downloads prüfen und die „neu“-Abzeichen.** Diese Einstellungen gingen bisher erst beim nächsten Abgleich (spätestens nach einer Minute) ans NAS, jetzt gleich nach der Änderung wie alle anderen.

## 4.0.0

Großes Reinemachen: Mediathek Plus sieht neu aus und ist einfacher zu bedienen. Alle Funktionen sind geblieben.

### Neu
- **Reiter oben statt Seitenleiste.** Für dich, Mediathek, Bibliothek und Merkliste stehen oben in der Kopfleiste (auch mit ⌘1–4, Windows: Strg+1–4). Rechts daneben: Downloads als Ring mit Fortschritt, Einstellungen, „Sofa-Modus“ und „Hilfe“ mit Hilfe öffnen, Problem melden…, Idee vorschlagen… und Über. Am Mac sitzen die Fensterknöpfe mit in der Leiste, unter Windows hat die App eigene Fensterknöpfe statt der hellen Systemleiste.
- **Nur noch zwei Modi: Sofa und Pro.** Der Wechsel ist immer einen Klick entfernt. Die Einstellungen zeigen allen die vier Bereiche aus dem bisherigen Profi-Modus, jede Einstellung genau einmal; was du eingestellt hattest, bleibt. Oben rechts wechselt der Knopf „Sofa-Modus“ in die Sofa-Welt.
- **Alles zum Eingrenzen unter „Filter“.** Sender, „nur ab 60 Min.“, Genre, Jahre, Bewertung, Fassungen und „In den Treffern suchen“ stehen in einem Fenster, aktive Filter als Schilder mit ✕. Die Trefferzahl steht im Suchfeld, die Sortierung gleich daneben.
- **Details als Schublade.** Ein Klick auf ein Plakat schiebt die Details von rechts herein, die Plakate rücken zur Seite; ein Klick daneben schließt sie. Wer lieber alle Plakate ganz sieht, stellt unter „Ansicht“ ein, dass sie neben den Details kleiner werden. Die Leertaste öffnet eine große Ansicht, die Pfeiltasten blättern weiter.
- **Der Download-Knopf zeigt, was mit dem Film passiert.** Nach dem Klick steht dort „Wartet – Platz 2“ oder „Lädt … 42 %“ – der Knopf füllt sich wie ein Balken, ein Klick öffnet die Warteschlange –, danach „✓ Geladen“. Auch für Downloads auf dem NAS. So sieht man in den Details sofort, dass ein Film schon lädt, und lädt ihn nicht doppelt.
- **Suche: Was die Filter ausblenden, steht dabei.** Ist eine Senderauswahl oder „nur ab 60 Min.“ eingestellt, nennt die Infozeile, wie viele Treffer es außerdem gibt – etwa „355 Videos gefunden · 2363 weitere (anderer Sender oder kürzer) · Alle zeigen“. Ohne einen einzigen Treffer zeigt „Ohne Filter suchen“ gleich die Zahl. Die Filter bleiben für die nächste Suche eingestellt.
- **Bibliothek:** Plakate zoomen mit ⌘ bzw. Strg + Mausrad oder zwei Fingern auf dem Trackpad. „Zufall“ gleitet zu einem Film. Mit NAS stehen auch dessen Downloads hier, mit Plakat. Logo-Archiv und „Senderlogos entfernen“ sind in die Bibliothek gezogen.
- **„Für dich“:** „Passend zu dir“ ist eine Reihe zum Blättern mit Pfeilen oder Schieben mit der Maus.
- **Sofa: Live-Fernsehen zum Anschauen.** Live-Kacheln zeigen das Bild der laufenden Sendung und nach kurzem Verweilen eine stumme Vorschau. Beim Klick fährt das Bild auf Fenstergröße auf, beim Schließen zurück auf die Kachel. „Sehenswert“ zeigt nichts mehr doppelt, was schon unter „Läuft bald ab“ steht.
- **Leere Mediathek mit Ideen.** „Probier mal:“ bietet Beispielsuchen an, die Suchtipps stehen hinter „?“ im Suchfeld.
- **Neues Über-Fenster** – mit genauerer Auskunft, welche Dienste die App wofür anfragt.
- **Fernseher: Hinweis auf die neue TV-App.** Fire TV und Android TV holen sich neue Versionen der App nicht selbst. Die Sofa-Seite weist deshalb einmal auf Version 1.1.0 hin und nennt den Downloader-Code; der Hinweis lässt sich wegklicken.
- **Schneller und schlanker.** Sofa, Einstellungen und Dialoge werden erst bei Bedarf geladen, der Start ist dadurch etwa halb so groß. Bibliothek, Plakate und „In den Treffern suchen“ reagieren flüssiger.

### Behoben
- **„Alle Fassungen“ aus blendet jetzt alle Fassungen aus.** Audiodeskription in der Schreibweise „… - Audiodeskription“, Fassungen in klarer oder leichter Sprache und in Gebärdensprache standen trotzdem in den Treffern.
- **Filminfos aus heißt jetzt ganz aus.** Wer „Filminfos“ in den Einstellungen abschaltet, bei dem fragt die App auch Wikipedia und die Szenenbilder nicht mehr an.
- **„Problem melden…“ schwärzt mehr.** Benutzernamen in Pfaden (auch unter Windows und auf dem NAS), Netzwerkfreigaben, Adressen im Heimnetz und Zusätze in Links kommen nicht mehr mit.
- **Originalton bleibt beim Wechsel von Sofa zu Pro an.** Wer bisher nur Sofa nutzte, verlor beim Umschalten die Einstellung, den Originalton als zweite Tonspur mitzuladen.
- **Merkliste: Zähler fürs automatische Laden gehen beim Abgleich nicht mehr verloren.**
- **NAS-Fassung besser abgesichert.** Wiederholte falsche Passwörter werden gebremst, nachgeladene Bilder folgen keiner Umleitung auf unsichere Adressen mehr und sind in der Größe begrenzt.

## 3.7.2

### Behoben
- **NAS: Aufräumen nur in den eingebundenen Ordnern.** „Filme prüfen“ löscht, verschiebt und stapelt auf dem NAS jetzt ausschließlich Dateien in den Ordnern, die in der yml eingebunden sind. Vorher prüfte das NAS nicht, wo eine Datei liegt, die ein gekoppeltes Gerät zum Aufräumen schickte. Bitte das NAS-Image aktualisieren.

## 3.7.1

### Neu
- **„Für dich“ beginnt gleich mit den Vorschlägen.** Der Film des Tages steht jetzt groß auf der Startseite der Mediathek und erscheint in „Für dich“ nicht noch einmal.

### Behoben
- **Filme prüfen: doppelte Serienfolgen.** „Mehrfach da“ zeigt jetzt auch Folgen, die in der Serienbibliothek zweimal liegen – etwa deutsch und „(Originalversion)“ als zwei Einträge. Verschiedene Fassungen lassen sich zu einer Folge mit Fassungswahl zusammenlegen, echte Doppel entfernen. Liegt eine Folge im Filmordner und zugleich schon in der Serienbibliothek, steht sie unter „Folgen im Filmordner“ als doppelt da und lässt sich ebenfalls entfernen. Bisher gab es für doppelte Folgen keine Funktion.
- **Folgen im Filmordner zählen als vorhanden.** Liegen Serienfolgen in Jellyfin oder Emby bei den Filmen (etwa „Poirot – S05E01 – …“), erkannte die App sie beim Suchen nicht als schon vorhanden – man lud eine Staffel leicht ein zweites Mal. Jetzt liest sie Serie, Staffel und Folge aus dem Dateinamen bzw. Ordner und zeigt die Folgen als vorhanden, auch wenn der Serienname etwas anders geschrieben ist.
- **Kein Trailer mehr beim Laden ganzer Staffeln.** „⬇ Alle“, „Staffel laden“ und „Neue laden“ bei verfolgten Serien luden kurze Trailer, Teaser und Vorschauen (etwa „Trailer … | Ab 15.11“) mit – sie landeten als eigener Film in einem eigenen Ordner. Jetzt bleiben sie weg und stehen auch nicht mehr in den Staffel-Gruppen. In der Trefferliste sind sie weiter zu sehen und lassen sich einzeln laden.
- **Krimifolgen mit falschem Plakat.** Folgen von „Tatort“, „Polizeiruf 110“ und anderen Krimireihen bekamen mitunter Plakat und Infos eines gleichnamigen Kinofilms – etwa „Tatort: Kaltblütig“ die von „Kaltblütig“ (1967). Jetzt nicht mehr; schon falsch zugeordnete Titel schlägt die App einmal neu nach.

## 3.7.0

### Neu
- **Film des Tages als Bühne.** Auf der Startseite der Mediathek steht er jetzt groß: Szenenbild des Films im Hintergrund, Plakat, Titel ohne Sender-Zusatz, Regie, Besetzung, Beschreibung und gleich „Herunterladen“ und „Merken“. Die Karte wächst mit dem Fenster – auf großen Bildschirmen groß, im schmalen Fenster ohne Plakat.
- **Profi: Eigene Dateinamen zusammenklicken.** „Eigene Vorlage …“ öffnet ein Fenster: Bausteine wie Titel, Jahr, Serie, Staffel, Folge oder Sender per Klick einfügen, Trenner dazwischen, ✕ am Baustein entfernt ihn. Die Vorschau zeigt gleich, wie die Datei heißen wird; gespeichert wird erst mit „Übernehmen“.
- **Profi: Untertitel – wohin auf einen Blick.** Statt zweier Schalter eine Auswahl: „In die Videodatei“, „Als SRT-Datei“ oder „Beides“.
- **Profi: Jellyfin und Emby aufräumen.** Einstellungen → Heimnetz & Medienserver → „Filme prüfen“ zeigt vier Listen:
  - **Falsch zugeordnet:** Die App liest Titel und Jahr aus jedem Dateinamen – bei stark abgekürzten Dateinamen aus dem Ordner darüber –, sucht den Film selbst und zeigt beide Plakate nebeneinander. „Übernehmen“ (einzeln oder für alle) ordnet ihn richtig zu, Plakat und Infos lädt der Medienserver selbst. Steht im Dateinamen das Sendejahr statt des Filmjahres, sucht sie auch ohne Jahr.
  - **Mehrfach da:** Filme, die doppelt in der Sammlung liegen, mit Tonspuren, Fassung, Auflösung und Größe. Bei echten Doppeln schlägt die App vor, welche Datei bleibt; die andere kommt auf Knopfdruck in den Papierkorb. Deutsche Fassung und Original lassen sich zu einem Film mit Fassungswahl zusammenlegen, und ein Film in mehreren Dateien (cd1, cd2 …) wird so benannt, dass der Medienserver ihn als einen Film zeigt.
  - **Folgen im Filmordner:** Serienfolgen, die bei den Filmen liegen und deshalb nur Standbilder zeigen, erkennt die App am Namen („S01E05“, „Folge 3“, „Teil 2“, auch alte Namen wie „(110)“ für Folge 1 von 10). Auf Knopfdruck kommen sie in den Serienordner, benannt nach Staffel und Folge („Serie – S01E01 – Titel“), samt Untertiteln. Der Serienname lässt sich vorher ändern, doppelte Folgen sind markiert.
  - **Nicht prüfbar:** was die App nicht sicher bestimmen konnte, gar nicht erkannte Filme zuerst. Extras wie Featurettes oder Making-ofs sind markiert und kommen auf Knopfdruck in den Unterordner „extras“ beim Film; TV-Mitschnitte und Online-Videos sind als solche gekennzeichnet.
  
  Passt ein Vorschlag nicht oder fand die App nichts, sucht man mit „Anderer Film …“ bzw. „Film wählen …“ selbst: Titel (gern mit Jahr, Tippfehler sind kein Problem) oder TMDB-Link eingeben, den richtigen Treffer mit Plakat und Regie anklicken, übernehmen – Jellyfin bzw. Emby muss man dafür nicht mehr öffnen. Bei Folgen lassen sich Staffel und Folge ändern.
  
  Deutsche und englische Titel gelten als gleich, wenn sie zum selben Film gehören (auch Alternativ- und Übersetzungstitel), und ein Ordner mit dem Namen eines Regisseurs hilft beim Finden. Große Sammlungen werden jetzt in einem Durchgang ganz geprüft, ein Balken zeigt den Fortschritt. Liegen die Filme auf dem NAS und am Rechner ist der Ordner nicht eingebunden, verschiebt, benennt und löscht die NAS-Fassung die Dateien.

### Behoben
- **ARTE: Filme im Original mit deutschen Untertiteln.** Steht ein Film ohne „(OmU)“ in der Mediathek – etwa unter „Aktuelles und Gesellschaft“ –, kam bisher nur die nackte Originalfassung an, die Untertitel blieben weg. Jetzt sind die deutschen Untertitel dabei, bei deutschem Ton als zuschaltbare Spur.
- **Untertitel „Als SRT-Datei“ gilt auch bei ARTE.** Was ARTE an Untertiteln mitliefert, landete immer in der Videodatei. Jetzt liegt es bei dieser Wahl als .srt neben dem Film.
- **Einstellungen → NAS: Schalter wieder normal.** „Downloads immer auf dem NAS“ und „Merkliste auf dem NAS“ waren zu langen Balken gezogen, an oder aus war kaum zu erkennen.
- **Suche: ✕ schließt die Treffer.** Bisher leerte ✕ nur das Suchfeld – die Treffer blieben stehen und kamen nach dem Wechsel der Reiter mit leerem Suchfeld und ohne ✕ zurück, man wurde sie nicht mehr los. Jetzt ist die Suche danach wieder leer; stehen Treffer ohne Suchbegriff da (etwa aus einer geteilten Liste), gibt es dafür auch ein ✕.
- **„Für dich“: ARTE-Miniserien als Serie.** Empfehlungen, die auf eine ARTE-Sammlung zeigen (etwa „Die Revoluzzer“, 8 Folgen), erscheinen als Serienkarte mit allen Folgen. Bisher galten sie als Film: Die Vorschau fand nichts, geladen wurde nur die erste Folge.
- **„Für dich“: Geladenes lässt sich wiederfinden.** Schon geladene Filme bleiben ausgeblendet – wer in „Für dich“ danach sucht, findet sie aber wieder (mit ✓). Serienkarten verschwinden nicht mehr, sobald eine Folge geladen ist.
- **Jellyfin, Emby & Co. erkennen geladene Filme richtig.** In der NFO-Datei und in den Infos der MP4 stand bei Filmen das Sendedatum als Erscheinungsdatum – der Medienserver suchte dann z. B. „Die innere Sicherheit“ aus 2026 und griff bei gleichnamigen Filmen daneben (falsches Plakat, falsche Infos). Jetzt stehen dort das echte Filmjahr und die TMDB-Kennung, damit nimmt der Medienserver genau diesen Film.

## 3.6.0

### Neu
- **Profi: Logo-Archiv.** Senderlogos auch aus Filmen entfernen, die schon auf der Platte liegen – auch aus solchen, die nicht mit der App geladen wurden. „Logo-Archiv“ in der Seitenleiste: Ordner wählen, die App zeigt alle Filme darin (mit Unterordnern) und ob das Logo noch drin ist. Je Film „Jetzt entfernen“ oder „Nachts entfernen“, dazu „Alle nachts entfernen“ für den ganzen Ordner. Erledigtes ist abgehakt, auch Filme, in denen kein Logo zu finden war. Läuft auch auf dem NAS (in den eingebundenen Ordnern).
- **Profi: Plakate zoomen.** In allen Poster-Ansichten (Bibliothek, Merkliste, Für dich, Suche) stellt ein Regler neben Poster/Tabelle die Größe der Plakate ein – von vielen kleinen bis zu wenigen großen. Auch mit ⌘+ / ⌘− / ⌘0 (Windows: Strg) und mit zwei Fingern auf dem Trackpad. Ganz klein zeigt die App nur noch die Plakate. Die Größe bleibt je Gerät gemerkt.
- **Profi: Beim Logo-Entfernen das Original behalten.** Neue Einstellung: Der Film ohne Logo kommt als „Name-ohne-logo.mp4“ neben das unveränderte Original. Gilt fürs Logo-Archiv und für „Senderlogo entfernen“ beim Download.

### Behoben
- **„Für dich“ empfiehlt nichts mehr, was schon im Medienserver liegt – auch bei Dateinamen wie im Sender.** Hieß ein Film in Jellyfin, Emby oder Plex wie die Sendung („Tödliches Kommando - Spielfilm, USA 2008“), erkannte die App ihn nicht und schlug ihn trotzdem vor. Jetzt zählt der Titel ohne den Zusatz, das Jahr kommt aus dem Zusatz. Filme, die nur Wikidata kannte, bekommen über die dort hinterlegte TMDB-Kennung außerdem Plakat und Bewertung.
- **Fernseher: Zurück beendet die App nicht mehr aus Versehen.** Auf der Startseite erscheint erst „Zum Beenden noch einmal Zurück drücken“ – beendet wird erst mit dem zweiten Druck binnen 3 Sekunden. Bisher reichte zweimal Zurück aus der Suche, und die App war zu.
- **Fernseher: Suche mit ✕ löschen.** Neben dem Suchbegriff steht ein ✕, erreichbar mit → am Ende des Textes – das eingebaute ✕ war mit der Fernbedienung nicht anzusteuern.
- **Fernseher: Hinweis auf die richtige Favoriten-Taste.** Der Player nennt auf Fire TV und Android TV „≡ Favorit“ statt der Taste S, die es auf der Fernbedienung nicht gibt.

## 3.5.3

### Behoben
- **Sofa: Filme und Live-TV überstehen Verbindungsaussetzer.** Bei schwachem WLAN (etwa am Fire-TV-Stick hinter dem Fernseher) brach das Bild ab und der Player meldete „Vielleicht ist es abgelaufen“ – obwohl nur das Netz kurz gehakt hatte. Jetzt lädt er an derselben Stelle nach, bis zu einer halben Minute lang; erst danach heißt es „Die Verbindung ist zu schwach“. Dazu behält er Gesehenes nur noch 30 Sekunden im Speicher – bei langen Filmen lief der knappe Speicher mancher Fernseher-Sticks sonst voll.
- **Jugendschutz: Download versucht es nach 22 Uhr erneut.** Filme ab 16 (bzw. 18) lädt die App von selbst ab 22 (bzw. 23) Uhr. Gab der Sender den Film da noch nicht frei – die ARD ist manchmal ein paar Minuten spät –, scheiterte der Download endgültig. Jetzt versucht die App es eine halbe Stunde lang alle 5 Minuten, ab der nächsten vollen Stunde noch einmal. Die Uhrzeit ist dabei immer die deutsche – auch auf Geräten im Ausland und auf dem NAS.
- **Sofa am Fernseher: Hoch in Sender- oder Kopfleiste rollt die Seite an den Anfang.** Wer mit ↑ zurück zu den Sendern, zur Suche oder zum Logo ging, sah darunter noch die Mitte der Seite – jetzt steht sie wieder oben beim Film des Tages. Auch ↑ im Suchfeld rollt nach oben.

## 3.5.2

### Neu
- **Sofa am Fernseher aufgeräumt** (getestet auf einem echten LG-Fernseher mit webOS 24): Lupe, Menü- und Mond-Symbol sind jetzt gezeichnet – manche Fernseher zeigten statt der Schriftzeichen leere Kästchen. Kein Scrollbalken mehr am Rand. Weg sind auf dem Fernseher, was dort nicht geht: Vollbild-Knopf (die App ist schon Vollbild), „Bild im Bild beim Wegwechseln“ und „Für später – mit der App“.
- **Fernseher: Filmtipp per QR-Code aufs Handy.** „Teilen“ in der Detailkarte zeigt am Fernseher einen QR-Code – mit dem Handy scannen, dann ist der Link auf dem Handy und lässt sich weiterschicken (öffnet den Film im Browser, in der App oder beim Sender).
- **Vorschau merkt sich die Lautstärke.** „▶ Vorschau“ in der Detailansicht startet mit der zuletzt eingestellten Lautstärke und Stummschaltung – gemeinsam mit dem Sofa-Player, je Gerät.

### Behoben
- **ORF: Downloads haben wieder Ton.** Der ORF liefert Bild und Ton seiner Streams seit Kurzem in getrennten Spuren – geladene Filme waren dadurch stumm (die Vorschau lief normal). Die App lädt ORF-Sendungen jetzt in der Fassung, in der Bild und Ton zusammen liegen (720p).

## 3.5.1

### Neu
- **Merkliste meldet die saubere Fassung.** Gibt es einen gemerkten Film nur „mit Untertitel“ (ins Bild eingebrannt), sucht die Merkliste bei jeder Prüfung nach einer Fassung ohne – deutsch oder mit abschaltbarem Originalton, auch bei einem anderen Sender. Findet sie eine, steht oben in der Merkliste „✨ jetzt ohne eingebrannte Untertitel“ mit „⬇ Laden“, dazu eine Mitteilung. Im Profi-Modus auf Wunsch auch für Filme, die du in den letzten 60 Tagen „mit Untertitel“ geladen hast (Einstellungen → Datenquellen).
- **Suche findet auch die deutsche ARTE-Fassung, wenn nur die französische passt.** Manchmal nennt nur die französische Beschreibung den Regisseur – „preminger“ fand dann „Sainte Jeanne“ auf ARTE (frz.), aber nicht „Die Heilige Johanna“. Jetzt sucht die App zu solchen Treffern die deutsche Fassung derselben Sendung nach und zeigt sie direkt davor (auch in der Sofa-Web-App).
- **Fernseher: QR-Code statt „App laden“.** Auf dem Fernseher zeigt „Mehr mit der App“ einen QR-Code und die kurze Adresse zum Abtippen am Rechner – ein Download-Knopf hilft dort nicht weiter. Auch „Als App auf den Home-Bildschirm“ fehlt dort jetzt im Menü.

### Behoben
- **Windows: Teilen kopiert jetzt den Filmtipp mit Link.** Über das Teilen-Menü von Windows kam der Link bei manchen nicht an. „Teilen“ legt den Text mit Link nun in die Zwischenablage („✓ Kopiert“) – zum Einfügen in Messenger oder Mail. Gilt auch für die Web-App im Browser unter Windows.
- **Fire TV: Senderleiste springt nicht mehr zurück.** Beim Blättern mit ← in der Senderleiste sprang der Fokus immer wieder nach rechts – die Leiste rollte unter dem unsichtbaren Zeiger durch, und der Fernseher hielt das für eine Zeigerbewegung. Jetzt zählen nur echte Bewegungen des Zeigers (LG Magic Remote).
- **Fire TV: App-Kachel füllt den Platz** – mit dem Breitbild-Banner statt des zugeschnittenen quadratischen Symbols (TV-App 1.0.3).

## 3.5.0

**Mediathek Plus 3.5: Fernsehen, wie es sein sollte.** Alle öffentlich-rechtlichen Sender live – ARD, ZDF, die Dritten, ARTE, 3sat und mehr – und zappen wie früher am Fernseher: ↑/↓, Senderliste, Lieblingssender und „Jetzt läuft“. Startet sofort, schaltet flott um, und das ohne Werbung, ohne Konto, ohne Tracking. Am Rechner, auf dem Handy, im Browser und auf dem Fernseher.

### Neue Funktionen

- **Live-TV wie am Fernseher:** „● Live“ in der Senderleiste startet sofort mit dem zuletzt gesehenen Sender (beim ersten Mal ARD). ↑/↓ zappt durch alle Sender (auch von einer Senderseite aus), am rechten Rand zeigt eine Senderleiste den aktuellen Sender groß und je vier davor und danach; mehrmals schnell gedrückt, lädt erst der Sender, auf dem man stehen bleibt. Enter öffnet die Senderliste, 1–9 wählt direkt, 0 springt zum letzten Sender zurück. **Jetzt läuft:** Kurz nachdem man auf einem Sender bleibt, erscheint unten in der Mitte für einen Moment, was gerade läuft und was danach kommt – auch in der Senderliste (ARD-Sender, Dritte, 3sat, ARTE, KiKA, phoenix; Programm der ARD). Die **Lautstärke** gilt einmal für alle Sender und Filme. **Lieblingssender:** ☆ in der Senderliste oder Taste S – auf dem Handy auch lange auf den Sender drücken. Favoriten stehen oben, bekommen die Nummern 1, 2, 3 … und ihre Sender rücken in der Senderleiste nach vorn. Am Rechner geht es auch mit dem Mausrad, auf Handy und Tablet mit Wischen: hoch/runter wechselt den Sender, nach links öffnet die Senderliste. Sender, die am eigenen Standort gesperrt sind (z. B. ORF außerhalb Österreichs), blendet die App aus – sie prüft das selbst bei den Sendern, ohne Ortungsdienst. Die WDR Lokalzeit Düsseldorf steht direkt hinter ARTE.
- **Vorschau: Mediathek Plus als App für Fire TV und Android TV** – die Sofa-Oberfläche mit Live-TV direkt auf dem Fernseher, bedient mit der Fernbedienung: zappen mit ↑/↓ (bzw. P+/P−), OK für die Senderliste, ≡ für Lieblingssender, Zurück schließt bzw. beendet. Die APK `MediathekPlus-TV.apk` steht bei diesem Release zum Herunterladen; auf dem Fire-TV-Stick mit der App „Downloader“ installieren (Anleitung in der README). Neue Funktionen kommen automatisch, ohne neue Installation.
- **Komfort beim Schauen:** Einschlaf-Timer im Player (☾ in 30/60/90 Min. oder nach der Sendung, sanft leiser), Untertitel auch beim Live-TV (ARD, ZDF), Sperrbildschirm und Kopfhörer-/Medientasten zeigen Sender und Sendung und zappen mit „Weiter/Zurück“. Im ☰-Menü: „Mit Live-TV starten“ und „Bild im Bild beim Wegwechseln“. Die Web-App lässt sich als App auf den Home-Bildschirm legen.
- **Sofa am Fernseher:** Die Zurück-Taste der Fernbedienung schließt, was offen ist, und beendet auf der Startseite die App. Die Programmwippe P+/P− zappt im Live-TV, ▶ und ⏸ spielen bzw. halten an, ⏪ ⏩ spulen. Nach dem Zeiger der LG-Fernbedienung machen die Pfeiltasten dort weiter, wo man war. Auf Fernsehern ist alles etwas größer und hat mehr Rand – am Rechner und Handy bleibt es, wie es ist.
- **Sofa: neue Detailansicht** – eine Karte über der durchscheinenden Startseite, oben ein großes Szenenbild mit Plakat; ein Klick daneben schließt sie (wie in der Web-App).
- **Sofa: Vollbild und Bild im Bild** – ⛶ oben rechts (oder F11 bzw. ⌃⌘F) zeigt die ganze Oberfläche im Vollbild, ideal am Fernseher. Im Player löst „Bild im Bild“ (oder Taste P) den Film als kleines, schwebendes Fenster ab – weiterstöbern, während er läuft. Auch in der Web-App.
- **Ablageort für die ganze Auswahl:** Neben „⬇ Herunterladen“ in der Auswahlleiste steht „Ablegen: automatisch / in Filme / Serien / Dokus“. Wer „Serien“ wählt, bekommt auch Beiträge ohne Folgennummer als Folgen: im Serienordner und nach Sendedatum benannt („Sendung – 2026-11-10 – Titel“), wie es Plex, Jellyfin und Kodi erkennen (Wunsch eines Testers).
- **Originalton nachrüsten:** Liegt ein Film nur auf Deutsch auf der Platte und gibt es inzwischen die Originalfassung, zeigt die Detailansicht „+ Englisch ergänzen“. Geladen wird nur die Tonspur; Bild und deutscher Ton bleiben unverändert. Passt die Originalfassung nicht (anderer Schnitt, andere Länge), lässt die App die Datei in Ruhe und sagt es.
- **Beste Fassung auf einen Blick:** Läuft derselbe Film bei mehreren Sendern, zeigt die Trefferliste „bestes Bild“ an der Fassung mit deutlich mehr Bildqualität (z. B. „Die Klapperschlange“: bei 3sat gut doppelt so viel wie in der ARD). Die Detailansicht der schwächeren Fassung sagt „Besser bei 3sat: besseres Bild“, und das Sofa zeigt gleich die schärfere. Dazu erkennt die App jetzt auch Titel wie „… - Spielfilm, USA 1981“ als denselben Film (Tester-Hinweis).
- **Sendedatum in der Detailkarte:** Bei Reportagen, Magazinen und Kurzbeiträgen zeigt das Sofa jetzt, wann sie gesendet wurden („gesendet 9.11.2026“) – so sieht man gleich, wie aktuell ein Beitrag ist. Bei Filmen steht wie bisher das Produktionsjahr (Tester-Wunsch).
- **Kurz & gut mit Bildern:** Die Kurzbeiträge zeigen jetzt das Vorschaubild des Senders – in der App und im Browser.
- **Profi: „H.265 bevorzugen“:** lädt bei ARTE die etwas kleinere H.265-Fassung, mit Erklärung, welche Geräte das nicht abspielen.
- **Linux: Metadaten fürs Softwarecenter** (AppStream) im AppImage und im .deb.
- **TMDB-Logo** im Über-Fenster (Pflicht laut TMDB-Bedingungen); dazu ausdrücklich: kostenlos, ohne Werbung, ohne Konto.

### Behoben

- **Trailer bei empfohlenen Filmen:** Bei Filmen aus „Sehenswert“ und „Läuft bald ab“ fehlte im Sofa der Trailer-Knopf – die Empfehlungen bringen Regie und Genre mit, aber nicht die Kennung, über die der Trailer gefunden wird. Die Detailkarte schlägt sie jetzt selbst nach.

- **Sicherheit (Prüfung des gesamten Codes):** Der NAS bremst Passwort-Durchprobieren jetzt wirksam (jeder Fehlversuch wartet länger, auch bei vielen gleichzeitigen) und weist übergroße Anfragen ab. Das Beispielpasswort „bitte-ändern“ aus der Vorlage ist gesperrt – wer es noch nutzt, bitte in der docker-compose.yml ändern (gekoppelte Geräte bleiben verbunden). Sitzungen und Geräteschlüssel sind nur noch für den Besitzer lesbar. Originalton und Untertitel kommen nur noch aus dem Netz, Dateiendungen nur aus einer festen Liste (nie „.exe“ o. Ä.), „Für später“ löscht nur wirklich für später Geladenes, yt-dlp ignoriert fremde Konfigurationsdateien, und Links öffnen nur Webseiten.

- **Teilen ohne Umweg:** „↗ Teilen“ in der Detailansicht öffnet direkt das Teilen-Menü des Systems (AirDrop, Nachrichten, Mail, Kopieren …) statt erst eine Auswahlliste. Ohne System-Teilen wird der Text kopiert. „App empfehlen“ steht im Über-Fenster.
- **Mittelteiler zwischen Liste und Detailansicht** ist deutlicher zu sehen und leichter zu greifen.

## 3.0.2

### Behoben

- **Heller Modus wieder lesbar:** Mit dem Button „Zurück zum Sofa“ in der Seitenleiste wurde der Hintergrund von Standard und Profi im hellen Modus dunkel – Überschriften und Titel waren kaum zu lesen (gemeldet unter Windows). Betraf 3.0.0 und 3.0.1 bei hellem Systemdesign.

## 3.0.1

### Behoben

- **Linux: Die App startet wieder.** Seit Version 1.2.1 brach sie unter Linux sofort beim Start ab – die Sperre gegen einen zweiten Programmstart verwendete einen Namen, den Linux (D-Bus) nicht zulässt. Mac, Windows und NAS waren nicht betroffen. Danke an die Prüfung des AppImage-Katalogs, die den Fehler gefunden hat.
- **AppImage heißt jetzt „Mediathek-Plus-…-x86_64.AppImage“** (ohne „Linux“), wie es der AppImage-Katalog vorsieht.

## 3.0.0

**Neu: Sofa – Mediathek Plus zum Entdecken und Schauen.** Eine eigene, ruhige Oberfläche: Filme, Serien, Dokus und Live-TV direkt abspielen, ohne Ordner, ohne Hilfsprogramme, ohne Einstellungen. Bei der Einrichtung vorausgewählt; Standard und Profi gibt es weiter für alle, die Filme sammeln.

### Neue Funktionen

- **Startseite mit Reihen:** Weiterschauen, Gespeichert, Passend zu dir, Sehenswert, Neu in den Mediatheken (Film-Themen aller Sender, Sender reihum), Läuft bald ab, Serien, Dokus, Kurz & gut, Für Kinder, Meine Liste – darüber der Film des Tages mit großem Bild.
- **Player:** füllt das Fenster, beste Qualität, **Weiterschauen** an der gemerkten Stelle (auch bei Wiederholungen), **„Nächste Folge in 10 s“**, **Ton & Untertitel** (Deutsch ↔ Original an derselben Stelle, Tonspuren bei ARTE, Untertitel – im Original notfalls die deutschen), **Trailer** (offizieller Trailer von TMDB).
- **Live-TV und Senderleiste:** ARD, ZDF, ARTE, 3sat … bis ARTE FR/EN; jede Senderseite mit „Tipp bei …“ und Live-Kachel (auch ZDFneo, ZDFinfo, ONE und ARD-alpha auf ihrer eigenen Seite, bei ARTE auch ARTE FR) – im Player mit ↑/↓ zum nächsten Sender zappen.
- **⬇ Für später:** ein Knopf, kein Ordner, keine Warteschlange – pausieren und abbrechen geht. Gespeicherte Filme laufen ohne Internet; nach dem Ansehen kündigt Sofa freundlich an, die Datei in den Papierkorb zu legen („Behalten“ geht immer).
- **Eine Karte je Film:** Fassungen (Originalversion, Audiodeskription, gleicher Film bei zwei Sendern) werden zusammengefasst, gespielt wird automatisch die beste. Serien erscheinen als eine Karte mit Staffeln und Folgen.
- **Sofa im Browser:** dieselbe Oberfläche als Web-App ohne Installation (Tablet, Handy, Fernseher-Browser) – Weiterschauen und Meine Liste je Gerät.
- **Originalton bei ARTE-Streams:** Führt die Mediathek einen ARTE-Film nur als Stream (z. B. „The Game“), liest die App dessen Tonspuren mit – die Suche zeigt „+ Englisch“, der Download nimmt Deutsch und das Original. Ist das Original nicht Englisch, kommt Englisch als dritte Spur dazu; Audiodeskription und „Klare Sprache“ bleiben weg.
- **Kurz & gut:** Kurzbeiträge von 1 bis 15 Minuten nach Themen – Ausstellungen, Fotografie, Kochen, Architektur, Musik, Theater, Bücher, Natur –, quer durch alle Sender, auch die Stücke aus Nachrichten- und Kulturmagazinen, die man sonst nie fände (Idee eines Testers).
- **Bibliothek aufräumen:** Filme, deren Datei gelöscht oder verschoben wurde, sind sofort zu erkennen (blass, „fehlt“). **🧹 Aufräumen** in der Statuszeile oder der Rechtsklick nimmt sie aus der Bibliothek – sie gelten weiter als geladen, die Merkliste holt sie nicht noch einmal (Wunsch eines Testers).
- **Zwischen den Modi wechseln:** ☰ → „Mehr Funktionen …“ erklärt erst, was Standard und Profi dazu bieten; ab dem zweiten Mal mit „Nicht mehr fragen“, danach geht es mit einem Klick. Zurück geht es über „🛋 Zurück zum Sofa“ – in allen Modi, abschaltbar.
- **Ganz mit Pfeiltasten bedienbar** – auch am Fernseher. Einfach lostippen sucht.
- **Gesehenes zählt:** Zu Ende geschaute Filme fallen aus den Reihen und fließen in „Passend zu dir“ ein.
- **Jugendschutz:** FSK-16/18-Filme der ARD zeigen tagsüber „🌙 Ab 22 Uhr“ statt eines Abspielfehlers.
- **Einstellungen neu geordnet und beruhigt:** Speicherorte & Dateinamen · Dateieigenschaften · Datenquellen · Heimnetz & Medienserver; eine Kante, Schalter statt Häkchen, Erklärungen über ⓘ, ausführlichere Beschriftungen (Wunsch eines Testers).
- **Rechtsklick in eine Mehrfachauswahl** gilt für die ganze Auswahl: „7 als nicht geladen markieren“, „7 herunterladen“, „7 URLs kopieren“, „Auswahl von der Merkliste entfernen“.
- **Profi: Klick auf die Adresse** in der Detailansicht kopiert sie.
- **Danke an die Tester:** besonders an Haiko und Marko, ebenso an Johannes, Jan und Philipp – und an alle anderen, die getestet und Ideen beigesteuert haben (im Über-Fenster).

### Behoben

- **ARTE immer in H.264:** ARTE bietet jede Qualität auch in H.265 an, das Windows und viele Fernseher nicht abspielen. Einzelne ARTE-Filme starteten unter Windows deshalb nicht, und Downloads konnten in H.265 landen (ARTE hatte seine Formatnamen geändert). Download und Player nehmen jetzt H.264.
- **ARTE-Streams mit der richtigen Tonspur:** Ohne Originalton lud ein ARTE-Stream eine zufällige Tonspur (z. B. Französisch) – jetzt gezielt Deutsch.
- **Gespeicherter Film ohne Bild** (Videoformat, das das System nicht abspielt): Sofa spielt ihn dann aus der Mediathek.
- **Zurück-Pfeil** im Player reagiert auch, wenn eine Fehlermeldung angezeigt wird.
- **Keine doppelte Ladeanzeige** im Player unter Windows.
- **Begrüßungshinweis** nach dem Wechsel aus dem Sofa kommt nach „Verstanden“ nicht wieder.
- **Dateigröße bei Streams** steht als „von ca. 1,5 GB“ da – sie wird beim Laden hochgerechnet und ändert sich noch.

## 2.4.3

- **Kein Staffel-Ordner bei Miniserien:** Nennt der Sender keine Staffel („Folge 3: …“, „(3/6)“), liegen die Folgen direkt im Serienordner („Das Vergessen – Spurlos im Moor/… – S01E03 – Verborgen.mp4“) statt in einem einzigen „Staffel 01“. Ist die Staffel genannt („(S02/E04)“, „Staffel 1 (3/8)“, Staffeln der Serienseite), bleibt der Staffel-Ordner. Schon geladene Folgen in „Staffel 01“ erkennt die App weiter als vorhanden.
- **Dateiname bei Folgen von Serienseiten:** Folgen, die über einen Link zur Serienseite geladen werden (z. B. zdf.de/serien/hacks-104), heißen jetzt auch „Hacks – S01E01 – Überschreitungen, immer.mp4“ statt nur „Überschreitungen, immer.mp4“. Den Ordner hatten sie schon richtig.
- **Merkliste lädt nichts doppelt:** Liegt eine neue Folge schon im Zielordner (z. B. nach Neuinstallation oder von einem zweiten Rechner aufs NAS geladen), lädt die Merkliste sie nicht noch einmal als „… (2).mp4“.
- **„✓ geladen“ auch quellenübergreifend bei Folgen:** Eine über die Serienseite geladene Folge gilt auch in der Suche als geladen (und umgekehrt) – bei gleicher Serie, Staffel, Folge und Fassung und, wo beide einen haben, gleichem Folgentitel. So gilt eine andere Folge nicht versehentlich als geladen, wenn eine Quelle anders zählt.
- **„Nur Ton“ zählt nicht als geladenes Video:** Wer erst den Ton geladen hat und später das Bild möchte, kann es ohne „Trotzdem herunterladen“ laden; die Merkliste lädt solche Folgen auch. In der Liste steht dann „♪ Ton vorhanden“. Gilt auch für ältere „Nur Ton“-Downloads aus dem Verlauf; automatisch lädt die Merkliste das Video dazu aber nicht – das entscheidet man selbst.
- **Warum „geladen“? – und selbst entscheiden:** Die Detailansicht nennt den Grund („Dieselbe Folge wurde am 03.11. aus einer anderen Quelle geladen als „Moment mal““, „Datei liegt schon im Zielordner“) und führt zur Datei: „Im Finder/Explorer zeigen“, im Browser auf dem NAS „Dateipfad kopieren“. Nur am Namen erkannte Treffer stehen als „✓ geladen?“ in der Liste. Liegt die App daneben: „Stimmt nicht“ bzw. „Als (nicht) geladen markieren“ im Menü am Download-Knopf und im Kontextmenü. Das gilt auch für die Merkliste.
- **Merkliste zeigt Übersprungenes:** Folgen und Treffer, die nur durch diesen Abgleich als geladen gelten, stehen aufklappbar unter „N übersprungen“ – mit „✓ Stimmt“ (bzw. „Alle stimmen“; danach erscheinen sie dort nicht mehr) und „⬇ Doch laden“.
- **Staffel von der Serienseite gilt:** Nennt die Senderseite Staffel 2, macht ein Titel „Folge 3: …“ daraus nicht mehr S01E03. Folgen ohne Staffelangabe bekommen Staffel 1 statt 0 (Jellyfin und Kodi hätten sie sonst unter „Specials“ einsortiert).
- **„Schon vorhanden“ zuverlässiger:** erkennt auch Dateien mit Jahr im Namen („Titel (2023)“), wenn die Filminfo gerade nicht bereitsteht, und Videos mit eigener Endung (MKV, WebM …).
- **Profi-Ansicht zeigt den echten Dateinamen:** „als „…“.mp4“ in der Detailansicht folgt jetzt den eigenen Namensvorlagen.
- **Bibliothek:** Über einen Seitenlink geladene Filme lassen sich dort wieder ansehen, und erneutes Laden holt die Originaltonspur mit (gilt für ab jetzt geladene Filme).

## 2.4.2

- **Serienseiten: Folgen landen im Serienordner.** Folgen, die von der Serienseite eines Senders kommen (z. B. ein eingefügter ZDF-Link zu „Hacks“), tragen jetzt den Seriennamen – sie gehen in den Serienordner („Hacks/Staffel 01/“) und bekommen das Namensschema für Folgen. Bisher galten sie als Filme, und die Ordnerwahl sprang bei jeder Folge auf „Filme“ zurück.
- **Serien in „Für dich“ (filmdienst.de):** Einträge wie „Serie: Hacks“ sind jetzt Serienkarten mit „📺 Alle Folgen zeigen“ – das öffnet die Serienseite des Senders mit allen Folgen (und Originalfassungen). Bisher lud ein Klick nur eine einzige Folge.
- **Geteilte Serien öffnen alle Folgen:** Ein geteilter Link zu einer Serie öffnet in der App die Serienseite des Senders statt einer Suche nach „Serie: …“, die nur einen falschen Treffer fand. Gilt auch für schon geteilte Links.

- **Miniserien ohne Staffel erkannt:** Folgen wie „Folge 3: Verborgen“ (ARD, Thema = Serie) oder „Das Vergessen – Spurlos im Moor (3/6): Verborgen“ (ORF) gelten jetzt als Staffel 1, Folge 3 – mit Serienordner, Namensschema und Staffel-Ansicht. Dieselbe Folge bei ARD und ORF erscheint nur einmal (die andere unter „alle Fassungen“).
- **Doku-Reihen bleiben bei den Dokus:** Erkennt die App eine Doku (Genre oder Reihe wie „Terra X“, „37 Grad“, „Reportage“), geht sie in den Dokuordner – auch wenn es Folgen einer Reihe sind. Dort liegen die Folgen wie bei Serien in „Reihe/Staffel 01/“, mit dem Namensschema für Folgen.

## 2.4.1

- **Fertige Datei aus der Mitteilung zeigen:** Die Mitteilung „Download fertig“ hat jetzt einen Knopf „Im Finder zeigen“ (Windows: „Im Explorer zeigen“, Linux: „Im Ordner zeigen“) – ein Klick darauf oder auf die Mitteilung selbst öffnet den Ordner mit der markierten Datei.
- **Mitteilung auch für NAS-Downloads:** Ist ein Film auf dem NAS fertig (oder fehlgeschlagen), meldet sich jetzt auch die App am Rechner – „Download fertig (NAS)“ mit dem Dateinamen. Bisher kam die Mitteilung nur in einem offenen Browser mit der NAS-Oberfläche.
- **Seitenleiste zeigt auch NAS-Downloads:** Laufende Downloads auf dem NAS stehen jetzt mit Titel, Fortschritt und Kennzeichen „NAS“ in der Karte unten links – bisher nur als Zahl.

## 2.4.0

- **Update direkt im Über-Fenster:** Findet „Nach Updates suchen“ eine neue Version, steht dort gleich „Jetzt aktualisieren“ bzw. „Jetzt neu starten“ (portable Fassung: „Herunterladen“) – kein Umweg mehr über die Leiste im Hauptfenster.
- **Richtige Sprache an der Original-Tonspur:** Bei „Deutsch + Original“ heißt die zweite Spur jetzt z. B. „Englisch (Original)“ und trägt die passende Sprachkennung (eng, fra …), statt die falsche Angabe des Senders zu übernehmen (das ZDF kennzeichnet auch die OV als Deutsch). Ist die Sprache unbekannt, steht dort „unbestimmt“. Player, die nach Sprache auswählen, finden die Spur so richtig.
- **Suche findet mehr:**
  - Englische und Originaltitel führen zum Film: „Anatomy of a Fall“ findet „Anatomie eines Falls“ (über TMDB, wenn Filminfos an sind).
  - Zusammengeschriebenes wird mitgesucht: „Spider Man“ findet auch „Spiderman“.
  - Keine Treffer? „Meintest du *Anatomie eines Falls*?“ bei Tippfehlern, „Ohne Filter suchen“, wenn Senderauswahl oder „nur ab 60 Min.“ aktiv sind.
  - Nichts in „Für dich“, der Merkliste oder der Bibliothek? „In der Mediathek suchen →“ sucht denselben Begriff in allen Mediatheken.
  - Gibt man einen bekannten Namen ein, erscheint „Filme mit Penélope Cruz →“ bzw. „Filme von …“.
  - Akzente spielen keine Rolle mehr: „mit: Penelope Cruz“ findet Penélope Cruz, auch beim Filtern in Merkliste, Bibliothek und „Für dich“.
- **Treffer sofort:** Die Ergänzung aus der ARTE-Mediathek (Filme, die MediathekViewWeb nicht führt) läuft jetzt im Hintergrund – die Liste wartet nicht mehr bis zu einigen Sekunden darauf.
- **„nur ab 60 Min.“ sagt, was fehlt:** Blendet der Haken Treffer aus, steht z. B. „7 Videos gefunden · 186 kürzere ausgeblendet – Zeigen“. Serien mit 30-Minuten-Folgen verschwinden so nicht mehr unbemerkt.
- **Sichtbar, wenn der Originalton dabei ist:** Folgen und Filme mit Originalfassung tragen in Liste und Postern „+ Englisch“ (bzw. die jeweilige Sprache, „+ Original“, wenn sie unbekannt ist); die Detailansicht zeigt „🔊 Deutsch + Englisch“ – oder „Englisch verfügbar“, wenn der Originalton nicht automatisch mitkommt. Bisher stand das nur im Tooltip.
- **Serienseiten mit Originalton:** Öffnet man die Seite einer Serie (z. B. ein geteilter ZDF-Link), sucht die App die Originalfassungen jetzt dazu – „Hacks“ bekommt so bei allen 27 Folgen „+ Englisch“.
- **Warteschlange höher ziehen:** Oben an der Warteschlange sitzt ein Greifer – ziehen macht sie höher oder flacher (gemerkt, Doppelklick = Standard). Auch die Trennlinie zur Detailansicht zeigt jetzt einen Greifer.
- **Weiterladen beim Zusammenführen:** Bei „Deutsch + Original“ gibt ein Download seinen Platz frei, sobald nur noch der Originalton angehängt wird – der nächste Download startet sofort.
- **Kein „yt-dlp“-Etikett mehr:** Von einer Senderseite gelesene Videos tragen nicht mehr den Namen des Hilfsprogramms.
- **Details aus der Warteschlange:** Ein Klick auf einen Titel in der Warteschlange zeigt rechts dessen Detailkarte (auch für Downloads auf dem NAS).
- **Seitenleiste nutzt den Platz:** Unten stehen die laufenden Downloads mit Titel und Fortschritt (bis zu drei, dazu „+ N warten“) – ein Klick öffnet wie bisher die Warteschlange. Abzeichen zeigen, wo es Neues gibt: neue Tipps in „Für dich“, neu geladene Filme in der Bibliothek, Neues in der Merkliste. Was du angesehen hast, gleichen Rechner und NAS ab; was du in Jellyfin, Emby oder Plex schon gesehen hast oder dort schon liegt, zählt nicht als neu – auch nicht als neue Folge einer verfolgten Serie.
- **Senderleiste:** „+ N weitere“ erscheint erst ab drei versteckten Sendern – vorher war der Knopf oft breiter als der eine Sender dahinter.
- **Hinweisleisten auf breiten Bildschirmen:** Die Knöpfe stehen direkt hinter dem Text statt ganz rechts außen.
- **Suchfeld auf breiten Bildschirmen:** höchstens etwa 720 px breit und mit Rahmen – ✕ und ➜ stehen direkt am Text.

## 2.3.0

- **Downloads geben nicht so schnell auf:** Bricht ein Server die Verbindung mit einem HTTP/2-Fehler ab („stream error“), lädt die App über HTTP/1.1 an derselben Stelle weiter – statt „Wiederholen“ von Hand. Dazu ein dritter Versuch nach 15 Sekunden.
- **„Deutsch + Original“ scheitert nicht mehr ganz:** Lässt sich der Originalton nicht anhängen, bleibt die deutsche Fassung gespeichert („✓ Fertig (nur Deutsch)“, Grund im Protokoll).
- **Besser bei …:** Läuft ein Spielfilm bei mehreren Sendern, zeigt die Detailansicht der schwächeren Fassung, wo es ihn besser gibt – z. B. „Besser bei ARTE: mit Originalton“ oder „länger verfügbar“.
- **Ablaufdatum auch bei der ARD:** Detailansicht und Merkliste zeigen jetzt auch bei ARD-Filmen, bis wann sie verfügbar sind – die Merkliste warnt so rechtzeitig vor dem Verschwinden.
- **Logo entfernen der Reihe nach:** Das Entfernen läuft jetzt immer als eigener Auftrag nach dem Download – der Download ist sofort fertig, der nächste startet gleich. Gerechnet wird immer nur an einem Film, mit voller Geschwindigkeit; zehn Serienfolgen bremsen sich nicht mehr gegenseitig aus. Vorher prüft die App, ob für die neu kodierte Datei genug Platz frei ist. In Warteschlange und Knöpfen heißt es kurz „Logo entfernen“.
- **Einstellungen zwischen Rechner und NAS zuverlässiger:** Gespeichert wird nur noch, was du änderst – eine offene NAS-Oberfläche mit altem Stand überschreibt nichts Neueres mehr. Geht die Uhr eines Geräts vor, gewinnt trotzdem die neueste Änderung, und ein Wert, den eine ältere App-Version nicht kennt, hält den Abgleich nicht mehr auf.
- **„Neu dabei“ bei den Empfehlungen:** Die App merkt sich, seit wann ein Tipp in der Liste steht – die neue Sortierung zeigt zuerst, was seit dem letzten Mal hinzugekommen ist. Beim ersten Mal gilt die Reihenfolge von filmdienst.de.
- **„Für dich“ zum Zuklappen:** Ein Klick auf die Überschrift klappt Film des Tages und „Passend zu dir“ zu, die Liste beginnt dann oben im Fenster (bleibt gemerkt). In schmalen Spalten brechen die Knöpfe beim Film des Tages um, Plakat und Beschreibung treten zurück.
- **Klassische Ansicht entfällt:** Es gibt nur noch den Aufbau mit Seitenleiste. Der Reiter „Ansicht“ in den Einstellungen ist weg; Standard und Profi schaltest du jetzt unten links im Einstellungsfenster um.
- **Leere Merkliste ist kein Fehler mehr:** Statt „Keine Treffer für „““ steht die Erklärung, wie Filme auf die Merkliste kommen.
- **Über-Fenster aufgeräumt:** Icon und „Entdecken. Laden. Teilen.“ führen jetzt zu Mediathek Plus auf GitHub (Doppelklick aufs Icon: wie bisher) (auch die Hilfe-Seite verlinkt dorthin und zeigt das App-Icon). „Hilfe“ als Knopf oben, Statistik übersichtlich, Danksagung und Rechtliches zum Aufklappen. „Per E-Mail“ beim Teilen entfällt – Teilen übers System und „Text kopieren“ bleiben.

## 2.2.0

- **Senderlogo entfernen – nicht mehr experimentell.** Die App kennt jetzt die Logos von 17 Sendern als genaue Masken (ARD, ZDF, arte, 3sat, BR, hr, NDR, rbb, SR, SWR, WDR, KiKA, Phoenix, ONE, ZDFneo, ZDFinfo, ARD-alpha) und deckt sie samt weichem Rand ab; vom Logo bleiben typischerweise nur rund 2 % übrig. Studiokulissen, Regale oder Spielstände hält sie nicht mehr für ein Logo – dort bleibt das Bild unberührt. Logos halb im Seitenbalken verschwinden spurlos.
  - **Schnell auf jedem Gerät:** Die App probiert beim ersten Film aus, welcher Hardware-Encoder sauber arbeitet (Mac: VideoToolbox; Windows: NVIDIA, Intel Quick Sync, AMD; NAS/Linux: VAAPI, NVIDIA, Quick Sync), sonst kodiert sie wie gewohnt mit libx264 – im Protokoll steht, welcher Encoder gewählt wurde und warum. Ein Spielfilm dauert auf einem aktuellen Mac rund 5 Minuten, auf einer Synology DS724+ rund 25 statt 2–3 Stunden. Auf dem NAS muss dafür die Grafikeinheit in den Container durchgereicht werden – im [Baukasten](https://7hdmm9pp2w-code.github.io/Mediathek-Plus/nas/) per Häkchen „Grafikeinheit für Logo-Entfernung nutzen“.
  - **Auch nachträglich:** Bei fertigen Downloads in der Warteschlange und in der Bibliothek gibt es „Senderlogo entfernen“ – im Profi-Modus ersetzt es bei geladenen Filmen mit Logo den Download-Knopf („Noch einmal laden“ steht dann im Pfeil-Menü). Das läuft als eigener Auftrag mit Fortschritt und Protokoll, auch auf dem NAS. Das lässt sich auf die Nacht legen (1–6 Uhr), auf dem NAS wie am Rechner: Downloads sind sofort da, gerechnet wird erst, wenn sonst nichts los ist – der Rechner bleibt dafür wach, muss aber eingeschaltet und die App geöffnet sein. „Jetzt entfernen“ in der Warteschlange startet einen wartenden Auftrag sofort.
  - Bearbeitete Filme tragen ein Kennzeichen in der Datei selbst (Name der Videospur: „Mediathek Plus ohne Senderlogo“) – so weiß die App auch nach Verschieben oder Umbenennen, dass das Logo schon weg ist.
  - Die Einstellung steht jetzt unter „Download“ (Profi-Modus) und gilt auch für Filme, die du vom Rechner aufs NAS schickst. Einzelne Filme lassen sich trotzdem mit Logo laden: Pfeil am Download-Knopf → „Mit Senderlogo laden“.
- **NAS als echte Fernsteuerung: Einstellungen abgeglichen.** Qualität, Untertitel, Originalton, Senderlogo, Dateinamen-Vorlagen und die übrigen Download-Einstellungen gelten auf Rechner und NAS gleich – eine Änderung auf einer Seite übernimmt die andere (die neuere gewinnt). Zielordner und Ansicht bleiben je Gerät.
- **„Standard“ statt „Einfach“, deutlich schlichter:** Die Einstellungen passen in Standard auf eine Seite – Zielordner, Qualität, Originalton, „Für Plex/Jellyfin/Kodi vorbereiten“, Filminfos und Modus. Alles andere (eigene Ordner für Serien und Dokus, Dateinamen, Geschwindigkeit, Untertitel, Senderlogo, klassische Ansicht, Poster/Tabelle-Umschalter) steht im Profi-Modus – NAS und Medienserver dort zusammen unter „Heimnetz“; der Umschalter sitzt nur noch in den Einstellungen. Lange Erklärungen klappt ein ⓘ auf. Bestehende Verbindungen und Einstellungen wirken in beiden Modi weiter.
- **Trailer:** In der Detailansicht steht bei vielen Filmen „Trailer ↗“ – öffnet den offiziellen Trailer bei YouTube im Browser, wenn möglich auf Deutsch (über TMDB, wie die übrigen Filminfos).
- **Hilfe zum Nachschlagen:** Im Über-Fenster führt „Hilfe“ zu einer kurzen [Hilfe-Seite](https://7hdmm9pp2w-code.github.io/Mediathek-Plus/hilfe/) – erster Start, Suchen (mit allen Kürzeln wie `!arte` oder `Regie: …`), Laden, Plex/Jellyfin/Kodi, Senderlogo, NAS und was tun, wenn etwas nicht klappt.
- **Jugendschutz-Filme laden abends von selbst:** Filme ab 16 oder 18 gibt der Sender erst ab 22 Uhr heraus. Statt zu scheitern (mit dem irreführenden Rat, yt-dlp zu aktualisieren), wartet der Download jetzt mit „Jugendschutz: wartet auf 22 Uhr“ (bei FSK 18: 23 Uhr) und startet dann von selbst. Bei der ARD erkennt die App die Sperre schon vor dem Start – kein halber Download, der mittendrin mit Netzwerkfehlern abbricht – auf dem NAS praktisch unbemerkt, am Rechner muss die App dann geöffnet sein. Das Warten übersteht einen Neustart.
- **Behoben: „Deutsch + Original“ bei ARTE-Filmen als Stream** (z. B. „Shaolin Kickers“) scheiterte mit „Originalton konnte nicht angehängt werden“ – auch beim Wiederholen. Die deutsche Fassung lädt jetzt richtig, mit deutschem Ton.
- **„Passend zu dir“ ohne graue Karten:** Hat TMDB kein Plakat, zeigt die Karte das Bild des Senders – wie die Kachelansicht.
- **Behoben: „Eigene Vorlage…“ bei Dateinamen zeigte kein Eingabefeld,** wenn die bisherige Vorlage einem der Vorschläge glich (z. B. „Datum – Sender – Titel“). Außerdem ragt der Fokusrahmen in den Einstellungen nicht mehr aus dem sichtbaren Bereich.

## 2.1.2

- **Behoben (Windows): Senderlogo entfernen schlug immer fehl** („No option name near …“) – der Pfad zur Maske war für ffmpeg falsch geschrieben. Das Original blieb dabei erhalten.

## 2.1.1

- **„Nach Updates suchen…“** im Mac-Menü und im Über-Fenster (auch Windows und Linux): Die App sieht sofort nach und sagt auch, wenn du schon die neueste Version hast. Ein gefundenes Update lädt sie wie gewohnt und bietet den Neustart an.
- **Behoben: Geteilte Liste ließ einen nicht mehr los.** Wer den Link einer geteilten Liste in „Für dich“ oder der Merkliste ins Suchfeld eingefügt hatte, landete danach bei jedem Klick auf diesen Bereich wieder in der Liste.
- **Senderlogo entfernen – noch experimentell, aber in Qualität und Geschwindigkeit stark verbessert:** Halbtransparente Logos (rbb, arte, zdf neo …) werden jetzt zurückgerechnet statt verwischt – das Bild darunter kommt wieder zum Vorschein. Steht das Logo im schwarzen Balken, wird es einfach schwarz übermalt; die Balkenkanten stören die Erkennung nicht mehr. Bearbeitet wird nur noch die Logo-Ecke, das geht ein Vielfaches schneller. Und wenn etwas schiefgeht, steht der Grund im Protokoll: Scheitert der Hardware-Encoder des Mac, versucht die App es mit dem Software-Encoder noch einmal, und das Ergebnis wird vor dem Ersetzen geprüft.

## 2.1.0

- **Jellyfin und Emby anbinden:** Unter Einstellungen → Medienserver Adresse und API-Schlüssel eintragen, Benutzer wählen – fertig. Was schon auf dem Medienserver liegt, trägt überall eine lila Marke („Jellyfin“, gesehen: „👁 gesehen“); bei „Sehenswert in Mediatheken“ stehen diese Filme am Ende unter „Schon in deiner Sammlung“. Die Bibliothek zeigt auch die Filme und Serien von dort – mit Plakat, Serien als eine Karte, neueste zuerst – und in den Details heißt der Hauptknopf „▶ In Jellyfin abspielen“. Nach jedem Download liest der Medienserver neu ein. Plex und Kodi sollen folgen.
- **„Passend zu dir“ lernt aus Jellyfin:** Gesehene Filme und Favoriten zählen für die Vorschläge mit – kürzlich Gesehenes stärker, mehrfach Gesehenes noch mehr, abgebrochene Filme gar nicht. Was du schon gesehen hast oder auf dem Server liegt, wird nicht mehr vorgeschlagen. Die Begründung sagt, woher es kommt („Regie: … – wie bei „…“ (gesehen in Jellyfin)“), und oben steht, worauf die Vorschläge beruhen.
- **Filme, Serien und Dokus in eigene Ordner:** Unter Einstellungen → Download gibt es jetzt je einen Zielordner für Filme, Serien und Dokus – passend zu getrennten Bibliotheken in Plex, Jellyfin oder Kodi. Serienfolgen und Dokus erkennt die App selbst; in der Detailansicht lässt sich die Art vor dem Laden ändern. Leer gelassen bleibt alles wie bisher im Filmordner.
- **Jeder Film in eigenem Ordner** (Einstellungen → Dateien): Ordner und Datei heißen gleich, .nfo und Untertitel liegen mit drin – so mögen es Plex, Jellyfin und Kodi am liebsten. Ein Wunsch aus der Runde der Tester.
- **Originalton immer dazu:** Die Einstellung „Originalton dazu“ gilt jetzt in beiden Ansichten und auch für Merkliste und NAS – Deutsch und Original landen dann immer in einer Datei. Einzelne Filme lassen sich über den Pfeil am Knopf trotzdem „Nur Deutsch“ laden.
- **„↻ Fehlgeschlagene wiederholen“** in der Warteschlange – für diesen Rechner und fürs NAS. Vom Sender entfernte Filme bleiben dabei außen vor.
- **NAS einfacher einrichten:** Der [yml-Baukasten](https://7hdmm9pp2w-code.github.io/Mediathek-Plus/nas/) erzeugt die `docker-compose.yml` aus deinen Freigaben – zum Hochladen im Container Manager oder als fertige Befehle für SSH. Filme, Serien und Dokus lassen sich auf dem NAS getrennt ablegen (`MX_SERIES`, `MX_DOKUS`). Wählt man in der App einen Ordner, den der Container nicht sieht, zeigt sie den passenden yml-Block zum Einfügen.
- **Warteschlange mit NAS:** Die Zeile „NAS“ bleibt beim Blättern oben stehen, und ohne eigene Downloads gelten „Fertige entfernen“ und „Wiederholen“ dem NAS – vorher waren sie ausgegraut.
- **Neue Download-Adresse:** Die Downloads liegen jetzt unter [github.com/7hdmm9pp2w-code/Mediathek-Plus](https://github.com/7hdmm9pp2w-code/Mediathek-Plus). Alte Links, geteilte Filme und Listen funktionieren weiter.
- **Danke an Philipp** fürs Testen und für viele Anregungen – jetzt auch im Über-Fenster.

## 2.0.2

- **Neu dabei: die Mediathekperlen – mit freundlicher Genehmigung der Mediathekperlen.** Neben den Tipps von filmdienst.de stehen bei „Sehenswert in Mediatheken“ jetzt auch die Film- und Serienempfehlungen der „Mediathekperlen“ (nexxtpress.de). Vielen Dank dafür! Gezeigt werden die empfohlenen Filme, die gerade in einer Mediathek laufen, und empfohlene Serien als eine Karte („Serie · 12 Folgen“) mit „📺 Alle Folgen zeigen“; in der Detailansicht steht, von wem die Empfehlung kommt, mit Link zum Beitrag. Der Feed wird höchstens zweimal am Tag abgerufen.
- **Hinweis bei zu altem ffmpeg:** Bis Version 6 liest ffmpeg die Untertitel mancher Sender (z. B. ARTE) leer. Die App prüft jetzt die Version und sagt Bescheid – unter Windows mit Knopf „Aktuelles ffmpeg für die App laden“ (die eigene Kopie hat dann Vorrang), auf dem Mac und unter Linux mit dem passenden Befehl. Auch der Hinweis im Protokoll bei leeren Untertitelspuren nennt jetzt „ab Version 7“.
- **Detailansicht aufgeräumt:** Ein Hauptknopf („⬇ Herunterladen“ bzw. „⬇ Auf dem NAS laden“, in der Bibliothek „▶ Abspielen“), die Varianten – auf diesem Rechner, auf dem NAS, nur Ton, Deutsch + Original – am kleinen Pfeil daneben. Darunter in einer Zeile, wohin geladen wird (in der Profi-Ansicht mit Dateiname), dann Vorschau, Merken und Teilen und eine Linkzeile (Beim Sender, Im Browser, Adresse kopieren). Die lange Video-Adresse steht nur noch in der Profi-Ansicht.
- **„Fertige entfernen“ für das NAS:** In der Warteschlange der Desktop-App blieben fertige NAS-Downloads stehen, obwohl das NAS sie entfernt hatte – die Liste wartete auf eine Meldung des NAS, die nicht immer ankam. Nach „Fertige entfernen“, Abbrechen, Wiederholen und Entfernen holt die App die Liste jetzt direkt neu. Angehaltene Downloads zählen nicht mehr als fertig.
- **Vorschau ohne Audiodeskription:** Bei manchen ARD-Filmen (z. B. Polizeiruf 110 „Bis Mitternacht“) spielte die Vorschau die Fassung mit Audiodeskription, weil die ARD sie zuerst nennt. Die Vorschau nimmt jetzt – wie der Download – die normale Fassung.

## 2.0.1

- **Downloads immer auf dem NAS:** Unter Einstellungen → NAS lässt sich einschalten, dass „⬇ Herunterladen“ überall aufs NAS lädt – auf Karten, in den Details, bei „Alle“ und „Staffel laden“. Einzelne Filme gehen per Rechtsklick oder in den Details trotzdem auf diesen Rechner. Ist das NAS nicht erreichbar, fragt die App, ob sie hier laden soll.
- **Suchbegriff je Bereich:** Der Begriff aus der Mediathek-Suche filtert nicht mehr Merkliste, Bibliothek und Für dich – die zeigen beim Wechsel alles. Mediathek und Kostenlose Filme teilen sich ihren Begriff; zurück in der Mediathek stehen die letzten Treffer sofort wieder da. Bleibt eine eigene Liste wegen eines Suchbegriffs leer, sagt die App das („Nichts in der Merkliste passt zu …“) und bietet „Alle zeigen“.
- **Bilder werden nur einmal geladen:** Filmplakate und Senderbilder speichert die App jetzt selbst (höchstens 200 MB, lange nicht gezeigte fallen weg) – beim nächsten Mal sind sie sofort da, auch offline. Beim Wechsel zwischen Für dich, Mediathek und Merkliste stehen die Bilder gleich wieder da, statt nachzuladen. Senderbilder füllen jetzt die ganze Kachel statt nur den oberen Rand.
- **Windows: „yt-dlp hat keine Datei gemeldet“ behoben:** Bei Titeln mit Gedankenstrich, Umlauten oder Akzenten (z. B. „2019 – Sibyl“) kam der Download vollständig an, wurde aber als fehlgeschlagen gemeldet und blieb als „.mx-download-…“ liegen. yt-dlp meldet jetzt in UTF-8, und findet die App den Pfad trotzdem nicht, sucht sie die fertige Datei selbst.
- **ARTE-Filme, die in der Suche fehlten:** Manche ARTE-Filme stehen nicht in der Mediathek-Liste, auf der die Suche aufbaut (z. B. „Sibyl – Therapie zwecklos“). Die App schaut jetzt bei jeder Suche zusätzlich im Verzeichnis aller ARTE-Sendungen nach (einmal am Tag geladen), holt fehlende Filme dazu und sortiert alles zusammen nach Relevanz – „sibyl“ bringt den Film auf Platz 1.
- **Mac: App-Ordner heißt jetzt auch „Mediathek Plus“.** Nach dem Update von 1.x hieß die App im Programme-Ordner noch „Mediathek-Extractor“ – auch in der Rückfrage des Browsers beim Öffnen eines geteilten Links. Beim ersten Start benennt sie sich einmal um und startet neu.
- **NAS: Untertitel bei ARTE wieder da.** ARTE liefert Untertitel neuerdings mit Farbangaben, die das ffmpeg im NAS-Image (Debian 12) nicht verstand – die Spuren kamen leer in die Datei, die .srt hatte 0 Bytes. Das Image läuft jetzt auf Debian 13 mit ffmpeg 7.1. Ist eine Untertitelspur trotzdem einmal leer (z. B. altes ffmpeg unter Linux), entfernt die App sie und legt keine leere .srt ab; das Protokoll sagt, warum.

## 2.0.0

- **Neuer Name: Mediathek Plus** (früher Mediathek-Extractor) – die App kann längst mehr als laden: Entdecken. Laden. Teilen. Einstellungen, Merkliste und Verlauf bleiben beim Update erhalten. Unter Windows ersetzt das Update die alte Fassung, statt sich daneben zu installieren. Dazu ein neues App-Symbol: der freche Fernseher.
- **Neue Oberfläche mit Seitenleiste:** links *Entdecken* (Für dich, Mediathek, Kostenlose Filme) und *Meine Filme* (Bibliothek, Merkliste). Filme erscheinen als Poster mit Filmplakat – bei Serien das Serienplakat, sonst das Vorschaubild des Senders; Laden und Merken direkt auf der Karte – oder als Tabelle, die sich per Klick auf die Spaltenköpfe sortieren lässt (umschalten oben rechts oder mit ⌘1/⌘2, Windows/Linux: Strg+1/2). Die Details stehen rechts daneben. Downloads laufen im Hintergrund; unten links zeigt ein kleiner Status, was gerade lädt, ein Klick öffnet die Warteschlange. Wer den bisherigen Aufbau lieber mag: Einstellungen → Ansicht → User Interface → Klassisch.
- **Für dich:** oben der Film des Tages als große Karte, darunter **„Passend zu dir“** – Filme aus den Mediatheken, die zu deinen bisherigen Downloads und deiner Merkliste passen, jeweils mit Begründung („Regie: Tom Tykwer – wie bei Lola rennt“). Was nicht interessiert, verschwindet mit ✕. Berechnet wird alles auf deinem Rechner; Vorschläge gibt es, sobald die App ein paar deiner Filme kennt.
- **Bibliothek:** alle bisher geladenen Filme an einem Ort – abspielen, im Finder bzw. Ordner zeigen, teilen. Ist eine Datei verschoben oder gelöscht, sagt die App das.
- **Mediathek Plus auf dem NAS:** Die App läuft jetzt auch als Docker-Container auf Synology & Co. – Oberfläche im Browser, mit Passwort, Downloads direkt auf die Freigaben.
- **Desktop-App steuert das NAS:** Unter Einstellungen → NAS einmal Adresse und Passwort eingeben, dann gibt es „⬇ Auf dem NAS laden“ im Rechtsklick-Menü und in den Details; die Warteschlange zeigt die Downloads des NAS live. Auf Wunsch liegen Merkliste und gemerkte Suchen auf dem NAS – dann lädt es neue Folgen rund um die Uhr, auch wenn der Rechner aus ist.

## 1.7.1

- **Merkliste leichter aufräumen:** Einträge mit ⌫ oder Entf entfernen (auch mehrere angehakte auf einmal), per ✕ beim Darüberfahren oder per Rechtsklick „Von der Merkliste entfernen“. Die Auswahl rückt dabei weiter, so geht ⌫ ⌫ ⌫ schnell. Keine Rückfrage – unten erscheint „Rückgängig“, und ⌘Z (Windows: Strg+Z) holt Entferntes zurück, auch mehrere Schritte. Treffer gespeicherter Suchen gelten danach als gesehen.
- **Filme bleiben erkennbar:** Mit „Infos in die Datei“ steht jetzt auch die Mediathek-Adresse in der MP4 (Feld „Gruppierung“). Daran kann die App einen Film später wiedererkennen, auch wenn er umbenannt oder verschoben wurde.

## 1.7.0

- **Einstellungen in einem eigenen Fenster:** Alle Einstellungen liegen jetzt übersichtlich nach Bereichen sortiert (Download, Dateien, Untertitel, Quellen & Daten, Ansicht) – erreichbar über ⚙ oben rechts, mit ⌘, (Windows/Linux: Strg+,) oder auf dem Mac im App-Menü. Jede Option ist kurz erklärt. Bisher steckten sie aufgeklappt unten in der Warteschlange.
- **Suche findet auch Regisseure und Darsteller:** Die Suche schaut jetzt auch in die Beschreibung der Sendungen – „Werner Herzog“ findet so auch Filme und Beiträge, in deren Titel der Name nicht steht. Treffer im Titel stehen weiter vorn.
- **Rechtsklick-Menü in der Trefferliste repariert:** „Herunterladen“, „Als MP3 herunterladen“ und „URL kopieren“ taten seit 1.5 nichts – jetzt wieder.
- **ARTE-Originalfassungen laden zuverlässiger:** Verweigert ARTE die Seite („not available in this language edition“), lädt die App automatisch die Datei aus der Mediathek – dann ohne Untertitel-Spur.
- Das Easter Egg im Über-Fenster zeigt sich jetzt schon nach zwei schnellen Klicks.

## 1.6.0

- **Filmtipps als eine Liste teilen:** Mehrere Filme gehen jetzt als übersichtliche, nummerierte Liste mit einem einzigen Link raus – statt je Film ein langer Link. Der Link öffnet eine Seite mit allen Filmen („Beim Sender ansehen“, „In der App öffnen“); wer die App hat, übernimmt mit einem Klick alle Filme und kann sie mit „★ Alle merken“ in die eigene Merkliste holen. Den Link kann man auch einfach ins Suchfeld einfügen. Die Liste steckt nur im Link, gespeichert wird nichts.
- **Vorschau beim Teilen:** Text vorher ansehen, einen eigenen Satz dazuschreiben („Für den Filmabend …“), wahlweise je Film einen Link und das Ablaufdatum. Bald Ablaufendes steht oben, Folgen einer Staffel werden zu einer Zeile zusammengefasst. In der Warteschlange wählt „Alle fertigen“ nur fertige Downloads.
- **Problem melden… / Idee vorschlagen…** im Über-Fenster und „Melden…“ an fehlgeschlagenen Downloads: öffnet ein kurzes Formular, Version ist schon eingetragen, der Fehlerbericht liegt zum Einfügen in der Zwischenablage. Verschickt wird nichts von selbst.
- **Sparsamer mit Daten:** neuer Schalter „Filminfos nachschlagen“ – aus, gehen keine Filmtitel an TMDB oder Wikidata. Verfolgte Serien fragen nur noch die neuesten Einträge ab statt aller Seiten, und die Merkliste merkt sich ihre Abfragen 15 Minuten lang – ist der Stand älter als 5 Minuten, erscheint „↻ Jetzt prüfen“. Protokollzeilen (mit Suchbegriffen) werden nach 14 Tagen gelöscht.

## 1.5.2

- **Filminfos schneller und nach und nach:** Bewertungen, Jahr und Genre erscheinen zuerst für die Filme, die gerade zu sehen sind, und dann laufend für den Rest – statt alle auf einmal nach bis zu einer Minute.
- **Suche ohne Hänger:** Große Suchen laden ihre Seiten gleichzeitig; antwortet eine Seite nicht, fragt die App nach 12 Sekunden noch einmal. Originalfassungen aus der ARD-Mediathek kommen im Hintergrund dazu („+ OV“ erscheint ein paar Sekunden später).
- **„🔔 Benachrichtigen, wenn es kommt“:** Findet die Suche nichts, kann man sie gleich merken. Taucht der Film später in einer Mediathek auf, meldet sich die App.
- **Zur Bewertung durchklicken:** In der Detailansicht führt „bei TMDB“ zur Filmseite mit allen Bewertungen.
- **Update bereit:** Liegt eine neue Version bereit, zeigt die App das jetzt auch bei Fehlerbehebungen an – mit „Jetzt neu starten“.
- **Datenschutz** kurz im Über-Fenster, mit Link zu den Einzelheiten.
- Unter der Haube: Update-Schritte und die Dauer der Suche stehen im Protokoll; die eigene yt-dlp-Kopie prüft die App nur noch wöchentlich auf Updates (nach einem gescheiterten Download täglich).

## 1.5.1

- **Bessere Treffer-Reihenfolge:** Die Suche sortierte bisher nur nach Datum. Jetzt steht oben, was am besten passt – Titel genau wie gesucht vor Treffern im Thema oder als Wortteil, Spielfilme vor Clips, Hauptfassungen vor Audiodeskription. Beispiel „transit“: Der Kinofilm steht jetzt auf Platz 1 statt auf Platz 39.
- **Ladebalken für Filminfos:** Beim Nachschlagen von Bewertungen, Jahr und Genre zeigt die App „Filminfos 37 / 120“; im Profi-Modus mit Quelle und Restzeit.
- **Nach dem Teilen** endet die Auswahl, kurz erscheint „✓ 3 Filmtipps kopiert“.
- **Danke** an Haiko, Marko, Johannes und Jan fürs Testen und für viele Anregungen (im Über-Fenster).
- **Download-Verlauf:** Die App merkt sich fertige Downloads ausführlicher (Titel, Sender, Dauer, Jahr) – als Grundlage für spätere Empfehlungen. Der Verlauf liegt nur auf deinem Rechner und wird nie verschickt.

## 1.5.0

- **Downloads anhalten und fortsetzen:** „⏸ Anhalten“ an jedem Download und „Alle anhalten“ über der Warteschlange. „▶ Fortsetzen“ lädt an der erreichten Stelle weiter – auch bei Streams und auch nach einem Neustart der App.
- **Genaue Suche:** Begriffe in Anführungszeichen finden nur das ganze Wort. „"Eis"“ findet das Eis, aber nicht mehr „Reise“, „Kreis“ oder „Preis“. Geht auch mit Vorzeichen, z. B. +"Das Boot" nur im Titel.
- **Mehr Originalfassungen bei der ARD:** Manche Originalversionen führt nur die ARD-Mediathek selbst, nicht das Verzeichnis, in dem die App sucht (z. B. „Amerikanische Fiktion“). Bei ARD-Spielfilmen ohne gefundene OV fragt die App jetzt dort nach – dann gibt es auch hier „+ OV“ und Deutsch + Original.
- **Mehrere Filme teilen:** In der Merkliste Häkchen setzen (in anderen Listen mit ⌘/Strg-Klick auswählen) und „Teilen…“ – als eine Nachricht mit allen Filmtipps und Links. Auch in der Warteschlange: „Teilen…“, Downloads ankreuzen, fertig.
- **Updates nebenbei:** Die App sieht jetzt auch während des Betriebs alle 4 Stunden und nach dem Aufwachen des Rechners nach neuen Versionen und lädt sie im Hintergrund. Fehlerbehebungen kommen ohne Hinweisleiste beim nächsten Start. Größere Versionen melden sich mit „Jetzt neu starten“. Nach einem Update sagt die App kurz Bescheid.
- **Bedienung mit der Tastatur:** ⌘/Strg+F springt ins Suchfeld. In der Trefferliste öffnen Menütaste oder Umschalt+F10 das Kontextmenü, Enter lädt herunter. Dialoge halten den Fokus, Esc schließt sie, danach geht der Fokus zurück. Menüs lassen sich mit den Pfeiltasten bedienen. Ein sichtbarer Rahmen zeigt, wo der Fokus gerade ist. Knöpfe mit Symbolen sind für VoiceOver und die Windows-Sprachausgabe beschriftet.
- Unter der Haube: Die Hauptseite ist in Bausteine aufgeteilt (Trefferliste, Filterleisten, Startseite, Kontextmenü, Merkliste). Das macht künftige Änderungen einfacher und sicherer.

## 1.4.0

- **Suche merken (Suchabo):** „🔔 Suche merken“ über der Trefferliste, z. B. für „Regie: Wim Wenders“ oder „Tatort“. Kommt etwas Neues dazu, erscheint es in der Merkliste, mit Mitteilung und auf Wunsch automatisch geladen.
- **Bewertungen:** Filme zeigen ihre TMDB-Bewertung (★ 7,8) in der Liste und in der Detailansicht. Die Liste lässt sich nach Bewertung sortieren oder mit „★ ab 7“ auf gute Filme beschränken.
- **Film des Tages:** Auf der Startseite gibt es jeden Tag einen gut bewerteten Film aus der Mediathek, mit Plakat. Wegklicken blendet ihn bis morgen aus.
- **Läuft bald ab:** Filme, die in den nächsten 3 Tagen verschwinden, zeigen „⏳ noch 2 Tage“. Neue Sortierung: „läuft bald ab“.
- **Filmplakate:** in der Detailansicht und für Plex, Jellyfin und Kodi als „Film-poster.jpg“ neben der Datei, wenn „.nfo-Datei“ an ist.
- **Nur Ton als M4A:** Im Profi-Modus lässt sich wählen, ob der Ton als MP3 oder M4A gespeichert wird. M4A übernimmt den Ton ohne Umwandeln.
- **Zahl am Dock-Symbol (Mac):** zeigt, wie viele Downloads laufen oder warten.
- **Behoben:** Die Personensuche („Regie: Christian Petzold“) übersah Filme, wenn ein anderer gesuchter Titel ein Allerweltswort war (z. B. „Phoenix“). Außerdem versteckte die App ARTE-Filme, die es außer mit Audiodeskription nur mit Untertiteln im Bild gibt (z. B. „Undine“, „Transit“), komplett als „weitere Fassung“.

## 1.3.0

- **Kein doppeltes Laden aus Versehen:** Steht ein Film schon in der Warteschlange oder wurde er schon geladen, fragt die App nach. Bei mehreren Filmen auf einmal lassen sich die schon vorhandenen überspringen. Nach dem Klick zeigt der Knopf kurz „✓ In der Warteschlange“.
- **Warteschlange bleibt nach dem Neustart:** Die letzten 50 Downloads (fertig, fehlgeschlagen, abgebrochen) erscheinen wieder. Was beim Beenden noch lief, steht als „Unterbrochen“ da und startet mit „Wiederholen“ neu.
- **Nicht mehr verfügbare Filme:** Hat der Sender ein Video entfernt (depubliziert), sagt das die Detailansicht schon vorher, und der Download-Knopf ist gesperrt. Scheitert ein Download daran, steht dort „Nicht mehr verfügbar“ statt eines Fehlercodes.
- **Kein Hängenbleiben:** Bleiben Daten aus, versucht die App es erneut (direkte Dateien, fortgesetzt an der erreichten Stelle). Streams über yt-dlp brechen nach 5 Minuten ohne Daten mit einer klaren Meldung ab.
- **yt-dlp:** Die App-eigene Kopie aktualisiert sich jetzt täglich. Ist ein selbst installiertes yt-dlp (Homebrew, winget …) veraltet, weist die App darauf hin und zeigt den passenden Befehl zum Aktualisieren. Der Fortschritt kommt in einem eigenen, festen Format von yt-dlp und hängt nicht mehr an dessen Textausgabe; er zeigt jetzt auch die Größe wie bei direkten Downloads.
- **🎲 Überrasch mich:** Der Würfel neben der Sortierung springt zu einem zufälligen Video der Liste.
- **Statistik:** Das Über-Fenster zählt die geladenen Filme und Folgen, ihre Laufzeit, die Größe und das Lieblingsgenre. Zum Angeben lässt sich das teilen. Bei runden Zahlen gibt es in der Fertig-Mitteilung einen kleinen Jubel.
- **Teilen mit Genre-Emoji:** Geteilte Filmtipps beginnen mit 📺 und einem Emoji zum Genre, z. B. 📺🤠 für einen Western oder 📺🔪 für einen Krimi.
- Beim Suchen ein Spruch aus der Fernsehwelt, und nachts ein Gruß zum Sendeschluss.
- Im Über-Fenster versteckt sich ein Easter Egg. 🤫

## 1.2.2

- **Geteilte Links öffnen die App:** Der Link im Teilen-Text führt auf eine kleine Seite, die den Film direkt in Mediathek-Extractor öffnet – ohne App zeigt sie die Sender-Seite und den Download. Funktioniert in jedem Messenger und per Mail.
- **Links in die App:** `mediathek-extractor://suche?q=…` (auch „Regie: …“/„mit: …“) und `mediathek-extractor://seite?url=…` (nur Seiten der Sender). Läuft die App schon, öffnet sich der Link im vorhandenen Fenster.

## 1.2.0

- **Filminfos jetzt für fast alle Filme:** Neben Wikidata nutzt die App **TMDB** (The Movie Database) – die kennt auch die vielen deutschen TV-Filme. Getestet an 200 Mediathek-Filmen: Infos zu 94 % (bisher 65 %), das Jahr stimmte in allen prüfbaren Fällen. Die Besetzung steht jetzt in Rollenreihenfolge (Hauptrollen zuerst). Auch „Regie: …“/„mit: …“ sucht über TMDB.
- **Filminfos treffsicherer:** Das Jahr aus der Senderangabe („Spielfilm Deutschland 2001 …“, 3sat: „… - Spielfilm, Frankreich 1990“) verhindert Verwechslungen mit gleichnamigen älteren Filmen. 3sat-Titel erscheinen in Dateinamen ohne diesen Zusatz.
- **Namen anklickbar:** In der Beschreibung (z. B. „Melanie (Melani Lenz)“) und bei Regie/Besetzung – ein Klick bietet „in dieser Liste“ oder „alle Filme suchen“.
- **Teilen:** „Teilen…“ in der Detailansicht – über das Teilen-Menü des Systems (Mac: AirDrop, Nachrichten, Mail …; Windows: Teilen-Dialog mit Mail, Teams, Geräten in der Nähe …), überall auch als Text zum Kopieren oder per E-Mail, mit Link zur Sender-Seite.
- **App empfehlen:** im Über-Fenster und im Teilen-Menü – Text mit Link zur Download-Seite.
- **Senderschreibweise** überall einheitlich (z. B. „3sat“).
- Detailansicht: Leerzeichen zwischen den Namen bei Regie und Besetzung.

## 1.1.0

- **Vorschau unter Windows** für ARD- und ARTE-Seiten (z. B. die filmdienst-Empfehlungen): neuere Windows-Versionen behaupten, solche Streams selbst abspielen zu können, scheitern aber – jetzt übernimmt immer der eingebaute Player.
- **Liste:** Die Filterzeile bricht bei schmaler Liste um, statt in die Detailansicht zu ragen.
- **Filminfos:** Zu Spielfilmen holt die App Jahr, Genre, Regie und Besetzung (aus Wikidata). Die Liste zeigt das Jahr; neue Leisten filtern nach **Genre** und **Jahrzehnt**; das Filterfeld findet auch Regie und Darsteller; in der Detailansicht filtert ein Klick auf einen Namen.
- **Filme einer Person suchen:** „Regie: Hitchcock“ oder „mit: Romy Schneider“ im Suchfeld – die App sucht alle Filme der Person in den Mediatheken (Titel, Jahr und Laufzeit müssen passen).
- **Dateinamen nach Wunsch:** „Jahr – Titel“, „Titel (Jahr)“, „Titel“, „Datum – Sender – Titel“ oder eine eigene Vorlage, getrennt für Filme und Serienfolgen, mit Vorschau. Das Jahr kommt bei Bedarf aus der Filminfo.
- **Untertitel zusätzlich als .srt-Datei** („Film.de.srt“, „Film.en.srt“) – die Windows-Medienwiedergabe zeigt in MP4 eingebettete Untertitel nicht an. Unter Windows standardmäßig an, sonst im Profi-Modus einschaltbar.

## 1.0.0

Die erste stabile Version – getestet auf Mac und Windows (Apple Silicon, Intel über Universal-App, Windows ARM in UTM). Gegenüber 0.7.2 nur Feinschliff:

- **Abgebrochene Serienfolgen** hinterlassen keine leeren Ordner „Serie/Staffel …“ mehr.
- **Geschwindigkeitsgrenze:** Hinweis, dass sie für Downloads gilt, die danach starten.

## 0.7.2

Für alle Systeme (Mac mit Apple Silicon und Intel, Windows, Linux).

- **Kleiner:** Das Programm ist um gut ein Drittel geschrumpft (z. B. Mac-App für Apple Silicon 5 statt 8 MB).
- **macOS:** Die Frage nach Zugriff auf den Ordner „Downloads“ kommt nur noch einmal (je Version) statt bei jedem Start – jetzt auch auf Intel-Macs (bisher nur 0.7.1 für Apple Silicon).
- Interner Umbau der Download-Steuerung (übersichtlicher, gleiches Verhalten); Updates nutzen die Verschlüsselung des Systems.

## 0.7.1

Nur für Macs mit Apple Silicon (M1 und neuer). Intel-Macs, Windows und Linux bleiben auf 0.7.0 – für sie ändert sich nichts.

- **macOS:** Die Frage nach Zugriff auf den Ordner „Downloads“ kommt nur noch einmal (je Version) statt bei jedem Start – die App ist jetzt vollständig (ad hoc) signiert.

## 0.7.0

- **Einrichtung beim ersten Start:** Zielordner, yt-dlp/ffmpeg mit einem Klick, „Für Plex/Jellyfin/Kodi vorbereiten“.
- **Fenster:** Die Liste links bleibt beim Vergrößern gleich breit (Trennlinie ziehbar, Doppelklick = Standard) – nur Vorschau und Beschreibung wachsen.
- **Später starten:** Warteschlange zu einer Uhrzeit starten (z. B. nachts); dazu Geschwindigkeit begrenzen (je Download).
- **Größe vorher:** Die Detailansicht zeigt die Dateigröße (bei Mediathek-Dateien) und warnt, wenn der Platz nicht reicht. Downloads starten nicht mehr auf ein volles Laufwerk.
- **„✓ vorhanden“:** Liegt eine Datei mit gleichem Namen schon im Zielordner, zeigt die Liste das – „Staffel laden“ überspringt sie.
- **„Fehler kopieren“:** Bei fehlgeschlagenen Downloads kopiert ein Knopf Meldung und Protokoll – zum Weiterschicken.
- **Einfach-Modus:** ein Schalter „Für Plex/Jellyfin/Kodi vorbereiten“ statt vier einzelner (Profi behält alle).
- **Merkliste** prüft auch bei laufender App alle 6 Stunden auf neue Folgen.
- **Deutsch + Original für alle Treffer:** Bei der Suche nach „originalversion“ sucht die App die deutsche Fassung jetzt für alle Filme nach (bisher nur für 10) und findet sie auch, wenn die ARD sie unter anderem Thema führt (z. B. „Perfect Days“). Filme, die es nur im Original gibt, zeigt die Liste als „nur Original“.
- **Untertitel als Spur statt eingebrannt:** Bei ARTE lädt die App immer das Bild ohne eingebrannte Untertitel und legt die deutschen Untertitel als zuschaltbare Spur dazu – bei Originalfassungen zusätzlich die Untertitel in der Originalsprache, falls ARTE sie anbietet (z. B. Englisch + Deutsch). ARTE-Originalfassungen aus der Mediathek-Suche kommen dafür über die ARTE-Seite. Fassungen „mit Untertitel“ (eingebrannt) stehen unter „alle Fassungen“, wenn es die saubere gibt.
- **Untertitel nicht mehr doppelt:** Bei Deutsch + Original kam dieselbe Untertiteldatei zweimal in die MP4 (die ARD hat eine Datei für alle Fassungen) – jetzt nur einmal.
- **Downloads:** kein .msi und kein .rpm mehr (Windows-Installer .exe, Linux AppImage/.deb bleiben).
- **Linux wieder dabei:** Abbrechen eines Downloads beendet nur noch den Download – in 0.6.0 konnte es alle Programme des Benutzers beenden (0.6.0 gab es deshalb nicht für Linux).

## 0.6.0

- **Deutsch + Original** auch, wenn man nach „Originalversion“ sucht – die deutsche Fassung wird automatisch dazugesucht.
- **„✓ geladen“** gilt nur für die tatsächlich geladene Fassung.
- **„Alle“** sagt, was es lädt („Deutsch + Original“ oder „nur Deutsch“).
- **Abbrechen** hinterlässt keine Teil-Dateien mehr (auch unter Windows); Reste werden beim Start aufgeräumt.
- **Empfehlungen/Merkliste:** keine Verwechslung mit der vorherigen Suche mehr.
- **Mehrfachauswahl:** ⌘/Strg-Klick, Shift-Klick für Bereiche, ⌘/Strg+A für alle – dann „Herunterladen“ oder „Merken“.
- **Windows portabel:** ZIP ohne Installation, alle Daten bleiben im Ordner neben dem Programm (z. B. auf einem USB-Stick). Updates dort per neuer ZIP.
- **Sortieren:** nach Datum, Titel, Dauer, Sender, „läuft bald ab“ oder Bewertung – je Quelle gemerkt.
- **Beschreibung nachladen:** Fehlt eine Beschreibung (Empfehlungen, eingefügte Seiten), holt die App sie vom Sender – oder aus der Wikipedia (nur wenn es eindeutig dieser Film ist, mit Quellenangabe).
- Suchverlauf entfernt.

## 0.5.0

- **Empfehlungen:** „Sehenswert in Mediatheken“ von filmdienst.de als eigene Quelle – mit Sternen, Ablaufdatum und Link zur Kritik.
- **Qualität wählen:** Beste (HD), Standard (bis 720p) oder Klein – spart Platz.
- **Übersichtlicher:** Senderleiste bricht um statt zu scrollen; Staffel-Ansicht nur bei echten Serien.
- **Audiodeskription und Gebärdensprache** sind standardmäßig ausgeblendet („alle Fassungen“ zeigt sie).
- **Einfach und Profi:** „Einfach“ zeigt nur das Nötigste (Suchen, Herunterladen, Vorschau – die Originalfassung kommt automatisch als zweite Tonspur mit). „Profi“ zeigt alle Optionen und ein **Protokoll** aller yt-dlp- und ffmpeg-Aufrufe.
- **Untertitel in die MP4** als zuschaltbare Spur statt separater Datei.
- **Infos in der Datei:** Titel, Sender, Datum, Beschreibung und bei Serien Serie/Staffel/Folge – Player und Plex/Jellyfin/Kodi zeigen sie an; auf Wunsch zusätzlich eine .nfo-Datei.
- **Merkliste (★):** Filme merken – die App erinnert beim Start, wenn sie in 3 Tagen ablaufen. Serien verfolgen – neue Folgen erscheinen in der Merkliste und lassen sich mit einem Klick (oder automatisch) laden.
- **Senderlogo entfernen (experimentell):** Die App findet das Logo (z. B. ZDF, ARTE) und kodiert das Video ohne Logo neu. Bei ruhigem Hintergrund unsichtbar, bei unruhigem bleibt ein weicher Fleck.

## 0.4.0

- **Serien nach Staffeln:** Folgen landen in „Serie/Staffel 02/Serie – S02E04 – Titel.mp4“ – so erkennen Plex, Jellyfin und Kodi sie sofort (abschaltbar in den Einstellungen).
- **Serien-Ansicht:** Treffer nach Serie und Staffel gruppiert, mit „Staffel laden“ für alle noch fehlenden Folgen.
- **Übersichtlichere Liste:** Hörfilm-, Gebärdensprach-, Untertitel- und OV-Fassungen sowie Wiederholungen werden zusammengefasst („alle Fassungen“ zeigt sie wieder).
- **„✓ geladen“:** Die App merkt sich, was schon heruntergeladen wurde.
- **Automatische Updates:** Neue Versionen meldet die App selbst und installiert sie auf Wunsch.

## 0.3.1

- **Bessere Titel beim Einfügen von Seiten-URLs:** Ein einzelnes Video heißt jetzt wie die Seite (z. B. „Ein unmöglicher Zufall“) statt wie die Datei.
- **Hinweis, wenn yt-dlp fehlt:** Bei ARTE, ZDF, ARD & Co. bietet die App yt-dlp zum Laden an – für Titel, Beschreibung, beste Qualität und alle Sprachen.
- **Über-Fenster mit Danksagung** an yt-dlp, FFmpeg, MediathekView und die anderen verwendeten Projekte (ⓘ oben rechts).
- **Hinweis:** Die App hat eine neue interne Kennung. Zielordner und Suchverlauf müssen einmalig neu eingestellt werden.

## 0.3.0

- **Senderauswahl:** Knopf „Sender“ unter der Suche, mehrere Sender gleichzeitig (Haupt-, Dritte, Sparten- und Auslandssender). Mit gewählten Sendern geht die Suche auch ohne Suchbegriff – z. B. „alles Neue von ARTE“.
- **Sender in der Ergebnisliste:** Leiste mit Trefferzahl je Sender, ein Klick filtert.
- **Filter „nur ab 60 Min.“:** blendet Trailer, Clips und kurze Beiträge aus.
- **Deutsch + Original in einer Datei:** Gibt es zu einem Film die Originalfassung („+ OV“ in der Liste), lädt die App das Bild einmal und legt deutschen Ton und Originalton als zwei Tonspuren in eine Datei – statt zwei Dateien mit je mehreren Gigabyte.
- **Alle Sprachen in einer Datei** bei ARTE-Seiten (z. B. Deutsch und Französisch).

## 0.2.0

Erste veröffentlichte Version.

- **Mediathek-Suche** über mediathekviewweb (ARD, ZDF, ARTE, 3sat, Dritte …) mit Titel, Sender, Dauer, Datum und Beschreibung.
- **Videos aus Seiten auslesen:** Seiten-URL einfügen – die App findet die Videos, auch auf Übersichtsseiten mit mehreren Filmen.
- **Downloads:** Warteschlange mit zwei parallelen Downloads, Fortschritt, Abbrechen und Wiederholen; abgebrochene Verbindungen werden automatisch fortgesetzt.
- **MP3** und **Untertitel** (als SRT) auf Wunsch.
- **Vorschau** direkt in der App.
- **Suchverlauf** mit den letzten fünf Suchen.
- Installer für macOS (Apple Silicon und Intel), Windows (auch ARM) und Linux.
