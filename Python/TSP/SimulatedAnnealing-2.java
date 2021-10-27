package de.nerdwest.tsp;

import javax.swing.JOptionPane;

/**
 * Diese Klasse enthaelt den Algorithmus mit Simulated Annealing 
 * @author Prof. Dr. Oliver S. Lazar
 * @version 1.0
 */
public class SimulatedAnnealing extends Thread{

	private Rundreise rr;
	private TSPFrame tspFrame;
	private double sigma;
	private double sigmaReduktion;
	private boolean doInterrupt;
	private int abbruchZaehler;

	/**
	 * Konstruktor
	 * @param rr Die zu optimierende Rundreise
	 */
	public SimulatedAnnealing(TSPFrame tspFrame, Rundreise rr, double sigma, double sigmaReduktion){
		this.tspFrame = tspFrame;
		this.rr = rr;
		this.sigma = sigma;
		this.sigmaReduktion = sigmaReduktion;
		this.doInterrupt = false;

	}

	/**
	 * Es wird bestimmt, ob der neue Wert toleriert wird.
	 * @param alterWert der bisherige Distanzwert
	 * @param neuerWert der neue Distanzwert
	 * @param sigma Toleranzlevel
	 * @return 
	 */
	private boolean akzeptiereTausch(int alterWert, int neuerWert, double sigma) {

		// Wenn der neue Wert besser ist, dann akzeptiere
		if (neuerWert < alterWert) {
			return true;
		}
		//Wenn der neue Wert schlechter ist, dann bestimme die Akzeptanz per Funktion
		double delta = neuerWert - alterWert;
		double calc = Math.exp(-delta / sigma);
		if(calc > Math.random()){
			return true;
		}else{
			return false;
		}
	}
	
	/**
	 * Startmethode des Threads
	 */
	public void run() {	

		tspFrame.getStart().setEnabled(false);
		tspFrame.getInit().setEnabled(false);

		
		// Wiederholen, bis die Toleranz (sigma) <= 1 ist
		int i=1;
		abbruchZaehler = 0;
		while (sigma > 1) {

			optimiereRundreise();
			tspFrame.setTableValues(sigma, i, abbruchZaehler, rr.getDistanz());
			rr.repaint();
			try {
				Thread.sleep(tspFrame.getZeit());
			} catch (InterruptedException e1) {
				JOptionPane.showMessageDialog(null,
						e1.getMessage(),
						"Fehler",
						JOptionPane.ERROR_MESSAGE);
			}
			i++;
			if(doInterrupt || (tspFrame.getAbbruch()>=0 && abbruchZaehler>=tspFrame.getAbbruch())){
				this.interrupt();
				break;
			}
		}

		tspFrame.getStart().setEnabled(true);
		tspFrame.getInit().setEnabled(true);


	}

	/**
	 * In dieser Methode werden zwei zufaellige Staedte ausgewaehlt
	 * und bestimmt, ob die Rundreise durch Tausch dieser Staedte 
	 * veraendert werden soll.
	 */
	private void optimiereRundreise(){

		// Aktuelle Distanz bestimmen
		int distanzAktuell = rr.getDistanz();

		// Bestimme zwei zufaellige Positionen (nur der Startknoten muss bleiben)
		int index1, index2;
		while((index1 = (int) (rr.getRundreise().length * Math.random())) == 0);
		while((index2 = (int) (rr.getRundreise().length * Math.random())) == 0);

		// Bestimme dazu die zugehoerigen Staedte
		Stadt tausch1 = rr.getStadt(index1);
		Stadt tausch2 = rr.getStadt(index2);

		// Staedte tauschen
		rr.setStadt(index2, tausch1);
		rr.setStadt(index1, tausch2);

		// neue Distanz bestimmen
		int distanzNeu = rr.getDistanz();

		// Soll der Tausch akzeptiert werden?
		if (!akzeptiereTausch(distanzAktuell, distanzNeu, sigma)) {
			
			// Staedte zuruecktauschen
			rr.setStadt(index2, tausch2);
			rr.setStadt(index1, tausch1);
			
			abbruchZaehler++;

		}else{
			abbruchZaehler = 0;
		}

		// Sigma reduzieren
		sigma *= 1-sigmaReduktion;
	}

	/**
	 * Beendet den Thread.
	 */
	public void stopThread(){
		doInterrupt = true;
	}
}
