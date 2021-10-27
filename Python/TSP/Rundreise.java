package de.nerdwest.tsp;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.RenderingHints;

import javax.swing.ImageIcon;
import javax.swing.JPanel;

/**
 * Diese Klasse enthaelt die Stadtliste, welche in ihrer regulaeren Reihenfolge eine
 * Rundreise darstellt. Die Rundreise wird durch die paint(Graphics g)-Methode
 * als sichtbarer Graph auf der GUI gezeichnet.
 * @author Prof. Dr. Oliver S. Lazar
 * @version 1.0
 */
public class Rundreise extends JPanel{

	private static final long serialVersionUID = 1L;
	private Image img;
	
	/**
	 * Die Rundreise mit den Staedten
	 */
	private Stadt[] rundreise;


	/**
	 * Konstruktor, der eine Rundreise initiiert.
	 * @param size Anzahl der Staedte
	 */
	public Rundreise(int size){
		rundreise = new Stadt[size];
		for (int i = 0; i < size; i++) {
			rundreise[i] = new Stadt();
		}
		ImageIcon imgIcon = new ImageIcon(Rundreise.class.getResource("/images/middle-earth.png"));
		img = imgIcon.getImage();
	}

	/**
	 * 
	 * @return Die aktuelle Rundreise
	 */
	public Stadt[] getRundreise(){
		return rundreise;
	}
	
	public void setRundreise(Stadt[] stadtListe){
		this.rundreise = stadtListe.clone();
	}


	/**
	 * Liefert ein Stadt-Objekt passend zum Index
	 * @param position
	 * @return Stadt-Objekt von der Position position
	 */
	public Stadt getStadt(int position) {
		return rundreise[position];
	}

	/**
	 * Positioniert ein Stadt-Objekt an die Stelle position
	 * @param position 
	 * @param stadt
	 */
	public void setStadt(int position, Stadt stadt) {
		rundreise[position] = stadt;
	}

	/**
	 * liefert die komplette Distanz der Rundreise
	 * @return Distanz der Rundreise
	 */
	public int getDistanz(){
		
			int rrDistanz = 0;
			// Unsere Rundreise durchlaufen
			for (int i=0; i < rundreise.length; i++) {
				// Startstadt holen
				Stadt start = getStadt(i);
				// Reiseziel holen
				Stadt ziel;
				// Wenn wir bei der letzten Stadt in unserer Rundreise angekommen sind,
				// dann wird das Ziel auf die Startstadt gesetzt (ist ja eine Rundreise)
				if(i+1 < rundreise.length){
					ziel = getStadt(i+1);
				}
				else{
					ziel = getStadt(0);
				}
				// Die Abstaende zwischen jeweils zwei Staedten summieren
				rrDistanz += start.berechneAbstand(ziel);
			}
		return rrDistanz;
	}


	@Override
	public String toString() {
		String geneString = "|";
		for (int i = 0; i < rundreise.length; i++) {
			geneString += getStadt(i)+"|";
		}
		return geneString;
	}
	
	public void paint(Graphics g){	

		Graphics2D g2d = (Graphics2D) g;
		g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

		g2d.drawImage(img, 0, 0, 800, 400, null);
		
		
		for(int i=0; i<rundreise.length; i++){

			// Verbindungslinie zum Nachfolger zeichnen
			int zielIndex = 0;
			if(i<rundreise.length-1){
				zielIndex = i+1;
			}
			g2d.setColor(Color.WHITE);
			g2d.drawLine(rundreise[i].getX(), rundreise[i].getY(), rundreise[zielIndex].getX(), rundreise[zielIndex].getY());


			// Knoten zeichnen
			if(i==0)
				g2d.setColor(Color.RED);
			else
				g2d.setColor(Color.YELLOW);

			g2d.fillOval(rundreise[i].getX()-5, rundreise[i].getY()-5, 10, 10);

			g2d.setColor(Color.BLACK);
			g2d.drawOval(rundreise[i].getX()-5, rundreise[i].getY()-5, 10, 10);
			

		}
		// Damit der Startknoten schoen aussieht
		g2d.setColor(Color.RED);
		g2d.fillOval(rundreise[0].getX()-5, rundreise[0].getY()-5, 10, 10);
		g2d.setColor(Color.BLACK);
		g2d.drawOval(rundreise[0].getX()-5, rundreise[0].getY()-5, 10, 10);
	}
	
}


