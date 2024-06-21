# Frontend

## Node Version Manager installieren
Aktuelle Version im [NVM-Repository](https://github.com/nvm-sh/nvm/blob/master/README.md#install--update-script) ermitteln.
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
```

## Node.js installieren
Mit dem Alias `node` wird die aktuelle Version installiert.
```
nvm install node
```

## Svelte Template laden
Svelte Template im Ordner `frontend` klonen.
```
npm create svelte@latest frontend
```
- Option `Skeleton project` auswählen und bestätigen.
- Option `Yes, using TypeScript syntax` auswählen und bestätigen.
- Keine zusätzlichen Optionen wählen und bestätigen.

In der `frontend` Ordner navigieren und Pakete installieren.
```
cd frontend
npm install
```

Entwicklungsserver starten.
```
npm run dev
```

# Backend

Ordner `backend` erstellen und dorthin navigieren.
```
mkdir backend
cd backend
```

## Python aktualisieren
```
sudo apt update
sudo apt-get upgrade python3
```

## pip installieren
```
sudo apt install python3-pip
```

## Uvicorn installieren
```
sudo apt install uvicorn
```

## FastAPI installieren
```
pip3 install fastapi
```

## Test
Datei `main.py` erstellen und Beispielskript einfügen.
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Entwicklungsserver starten.
```
uvicorn main:app --reload
```
