Python v.3.13.3
Node.js 10.9.2
Assumendo di avere già installato nel pc Python e Node.js:

Avvio backend
Creazione di ambiente di sviluppo con il comando
- py -3 -m venv .venv

Avviare l'ambiente di sviluppo
- .venv\Scripts\activate

Installare tutte le dipendenze di python necessarie salvate in requirements.txt
- pip install -r requirements.txt

Avviare il backend 
- flask run --debug 
assicurarsi che la porta usata sia 5000, altrimenti
- flask run --debug --port=5000

Se tutti i passaggi sono andati a buon fine, possiamo passare al frontend

Apriamo un'altra console ed entriamo nella cartella client col comando 
- cd client

qui installiamo tutte le dipendenze con
- npm install

Dovrebbero installarsi Vue.js per gestire il frontend, Axios per comunicare tra frontend e backend, bootstrap per la gestione layout e chart.js per i grafici