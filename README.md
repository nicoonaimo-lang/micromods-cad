# micromods-cad

Toolkit CLI open source per avviare l'automazione CAD parametrica da prompt testuali. Questo scaffold trasforma un prompt in un oggetto JSON con geometria e dimensioni riconosciute; non genera ancora file STL o STEP.

## Requisiti

- Python 3.10 o successivo
- Nessuna dipendenza esterna per il prototipo

## Installazione e utilizzo

Clona il repository e avvia il CLI dalla directory del progetto:

```bash
python main.py "un cilindro alto 20 mm"
python main.py "a cube 2 cm wide" --output output/parameters.json
```

Il parser riconosce in modo basilare alcune forme (cube, box, cylinder, sphere, cone, cuboid) e misure in mm, cm e m, convertendole in millimetri. L'estrazione è una base dimostrativa: le dimensioni non vengono assegnate a specifici assi o proprietà della forma e vanno validate prima di usarle in un flusso di produzione o esportarle per la stampa 3D.

## Struttura

```text
.
├── main.py
├── config/
│   └── context.yaml
├── LICENSE
├── pyproject.toml
└── README.md
```

## Gestione del contesto

La configurazione iniziale si trova in `config/context.yaml`. Descrive le directory di progetto da includere, i percorsi da escludere e i limiti di raccolta del contesto. È una configurazione dichiarativa: l'integrazione con Graphify o con un altro indicizzatore è un passaggio futuro e non viene eseguita da questo scaffold.

## Sviluppo

Dopo aver installato il progetto, usa `micromods-cad "prompt"` per richiamare il comando. Per estendere il prototipo, separa l'estrazione del prompt dal backend CAD e aggiungi test per unità, vincoli geometrici e formati di esportazione.

## Licenza

Distribuito secondo la licenza MIT. Vedi [LICENSE](LICENSE).
