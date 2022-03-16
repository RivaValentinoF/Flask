#si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta.
#l'utente deve poter inserire il nome della squadra e la data di fondazione e la città.
#deve inoltre poter effetuare delle ricerche inserendo uno dei valori delle colonne e ottenendo i dati presenti.

from flask import Flask, render_template,request
app = Flask(__name__)
import pandas as pd
lista=[] #struttura dati temporanea va salvata sulla ram 

@app.route('/', methods=['GET'])
def home():
    return render_template('squadraHome.html')

@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('inserisci.html')

@app.route('/dati', methods=['GET'])
def dati():
    # inserimento dei dati nel file csv
    # lettura dei dati dal form html 
    squadra = request.args['Squadra']
    anno = request.args['Anno']
    citta = request.args['Citta']
    # lettura dei dati daal file nel dataframe
    df1 = pd.read_csv('/workspace/Flask/templates/dati.csv')
    # aggiungiamo i nuovi dati nel dataframe 
    nuovi_dati = {'squadra':squadra,'anno':anno,'citta':citta}
    
    df1 = df1.append(nuovi_dati,ignore_index=True)
    # salviamo il dataframe sul file dati.csv
    df1.to_csv('/workspace/Flask/templates/dati.csv', index=False)
    return df1.to_html()

@app.route('/datiricerca', methods=['GET'])
def ricerca():
    return render_template('datiricerca.html')

@app.route('/ricerca', methods=['GET'])
def ric():
    squadra = request.args['Squadra']
    anno = request.args['Anno']
    citta = request.args['Citta']
    #caricamento dati dal file csv a un dataframe 
    df2= pd.read_csv('/workspace/Flask/templates/dati.csv')
    


    #ricerca dei dati 
    df3=df2[df2['squadra']==squadra]
    return df3.to_html()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)