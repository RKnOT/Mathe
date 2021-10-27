package de.nerdwest.tsp;

/**
 * Diese Klasse repraesentiert eine Stadt 
 * @author Prof. Dr. Oliver S. Lazar
 * @version 1.0
 */

public class Stadt{
    
	/**
	 * Die X-Koordinate der Stadt
	 */
	private int x;
	/**
	 * Die Y-Koordinate der Stadt
	 */
	private int y;
  
    
    /**
     *  Konstruktor fuer eine zufaellig platzierte Stadt
     */
    public Stadt(){
        this.x = (int)(Math.random()*800);
        this.y = (int)(Math.random()*400);
    }
      
    
    /**
     * Berechnet den Abstand zur uebergebenen Stadt
     * @param stadt
     * @return Abstand zur stadt
     */
    public double berechneAbstand(Stadt stadt){
        int xAbstand = getX() - stadt.getX();
        int yAbstand = getY() - stadt.getY();
        double abstand = Math.sqrt((xAbstand*xAbstand) + (yAbstand*yAbstand));
        
        return abstand;
    }


	public int getX() {
		return x;
	}


	public int getY() {
		return y;
	}
    
    
}