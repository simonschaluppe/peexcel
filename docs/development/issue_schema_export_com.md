# Schema-Generierung: optionaler Einstieg über Excel COM

Optional die aktuelle PEExcel-Datei oder ausdrücklich die DEV-Version über die bestehende COM-Schnittstelle ansprechen und das Makro `ExportSchema` ausführen. Danach den bisherigen Schema-Konvertierungs- und Generierungsablauf unverändert fortsetzen.

- Voraussetzung: Dateidialog aus `ExportSchema` abstrahieren; Exportpfad als Parameter ermöglichen.
- Bestehender Einstieg über eine bereits exportierte Datei bleibt erhalten.
- Abnahme: ausführbares How-to für beide Einstiege; Exportfehler stoppen die nachfolgende Generierung.
