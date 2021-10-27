package de.nerdwest.tsp;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.table.DefaultTableModel;
import javax.swing.JTabbedPane;
import javax.swing.JTextField;
import javax.swing.JTable;
import java.awt.SystemColor;

/**
 * Das ist die Fenster-Klasse, sie enthaelt die grafischen Anzeige- und Bedienelemente. 
 * @author Prof. Dr. Oliver S. Lazar
 * @version 1.0
 *
 */

public class TSPFrame extends JFrame implements ActionListener{

	private static final long serialVersionUID = 1L;
	private static final String PREFERRED_LOOK_AND_FEEL = null;
	private Rundreise rrAktuell, rrInitial;
	private JTextField anzahl, sigma, sigmaReduktion, abbruch, zeit;
	private JButton start, stop, init;
	private SimulatedAnnealing sa;
	private JTabbedPane tabbedPane;
	private JTable table;
	private DefaultTableModel model;

	/**
	 * Konstruktor
	 */
	public TSPFrame() {
		super("TSP mit Simulated Annealing [1.0] - Prof. Dr. Oliver S. Lazar");

		tabbedPane = new JTabbedPane(JTabbedPane.TOP);
		getContentPane().add(tabbedPane, BorderLayout.CENTER);

		JPanel panel = new JPanel();
		getContentPane().add(panel, BorderLayout.SOUTH);
		panel.setLayout(new GridLayout(1,2));
		
		JPanel panelLeft = new JPanel();
		panelLeft.setLayout(new GridLayout(4,1));
		
		JPanel panel2 = new JPanel();
		panel2.setLayout(new FlowLayout(FlowLayout.LEFT, 5, 5));
		JPanel panel3 = new JPanel();
		panel3.setLayout(new FlowLayout(FlowLayout.LEFT, 5, 5));
		JPanel panel4 = new JPanel();
		panel4.setLayout(new FlowLayout(FlowLayout.LEFT, 5, 5));
		JPanel panel5 = new JPanel();
		panel5.setLayout(new FlowLayout(FlowLayout.LEFT, 5, 5));
		
		panelLeft.add(panel2);
		panelLeft.add(panel3);
		panelLeft.add(panel4);
		panelLeft.add(panel5);
		panel.add(panelLeft);

		JLabel lblAnzahl = new JLabel("Anzahl Staedte:");
		panel2.add(lblAnzahl);

		anzahl = new JTextField(3);
		anzahl.setText("20");
		panel2.add(anzahl);
		
		init = new JButton("Generiere Zufallsrundreise");
		init.addActionListener(this);
		panel2.add(init);

		JLabel lblSigma = new JLabel("Toleranzwert Sigma:");
		panel3.add(lblSigma);

		sigma = new JTextField(5);
		sigma.setText("10000");
		panel3.add(sigma);

		JLabel lblReduktion = new JLabel("Sigma Reduktion:");
		panel3.add(lblReduktion);

		sigmaReduktion = new JTextField(5);
		sigmaReduktion.setText("0.005");
		panel3.add(sigmaReduktion);

		panel4.add(new JLabel("Abbruch nach "));
		abbruch = new JTextField(3);
		abbruch.setText("40");
		panel4.add(abbruch);
		panel4.add(new JLabel("stabilen Iterationen (zum Deaktivieren -1)"));
		
		zeit = new JTextField(3);
		zeit.setText("5");
		panel5.add(zeit);
		panel5.add(new JLabel("ms pro Iteration          "));
		start = new JButton("Rundreise optimieren");
		start.addActionListener(this);
		panel5.add(start);
		stop = new JButton("Stop");
		stop.addActionListener(this);
		panel5.add(stop);
		
		
		table = new JTable(5,2);
		table.setBackground(SystemColor.window);
		table.setRowSelectionAllowed(false);
		table.setColumnSelectionAllowed(true);
		table.setCellSelectionEnabled(true);
		model = (DefaultTableModel)table.getModel();
		model.setValueAt("Sigma", 0, 0);
		model.setValueAt("Iterationen", 1, 0);
		model.setValueAt("stabile Iterationen", 2, 0);
		model.setValueAt("Initialdistanz", 3, 0);
		model.setValueAt("Finaldistanz", 4, 0);
		table.setEnabled(false);
		panel.add(table);

		// Fenstergroesse setzen.
		setSize (820, 600);

		// Definieren, was beim Schliessen des Fensters geschehen soll.
		setDefaultCloseOperation (EXIT_ON_CLOSE);

		// mittig ausrichten
		this.setLocationRelativeTo(null);

		// Fenster anzeigen.
		setVisible (true);
		
		erzeugeRundreise();
		
	}


	private static void installLnF() {
		try {
			String lnfClassname = PREFERRED_LOOK_AND_FEEL;
			if (lnfClassname == null)
				lnfClassname = UIManager.getCrossPlatformLookAndFeelClassName();
			UIManager.setLookAndFeel(lnfClassname);
		} catch (Exception e) {
			System.err.println("Cannot install " + PREFERRED_LOOK_AND_FEEL
					+ " on this platform:" + e.getMessage());
		}
	}

	/**
	 * Startmethode
	 */
	public static void main(String[] args) {
		installLnF();
		SwingUtilities.invokeLater(new Runnable() {			
			public void run() {
				new TSPFrame();				
			}
		});
	}



	public void actionPerformed(ActionEvent e) {
		
		if(e.getSource()==init){
			
			erzeugeRundreise();
					
			
		}else if(e.getSource()==start){

			// Ueberpruefe die Eingaben	
			try{
				boolean check = true;
				double sigma = Double.parseDouble(this.sigma.getText());
				double sigmaReduktion = Double.parseDouble(this.sigmaReduktion.getText());
				double abbruch = Double.parseDouble(this.abbruch.getText());
				double zeit = Double.parseDouble(this.zeit.getText());
				
				if(sigma<1){
					JOptionPane.showMessageDialog(this, "Sigma: Ungueltiger Wert");
					check = false;
				}
				if(sigmaReduktion<=0){
					JOptionPane.showMessageDialog(this, "Reduktion: Ungueltiger Wert");
					check = false;
				}
				if(abbruch==0){
					JOptionPane.showMessageDialog(this, "Stabile Iterationen: Ungueltiger Wert");
					check = false;
				}
				if(zeit<0){
					JOptionPane.showMessageDialog(this, "Geschwindigkeit: Ungueltiger Wert");
					check = false;
				}
				
				if(check){
					sa = new SimulatedAnnealing(this, rrAktuell, sigma, sigmaReduktion);
					sa.start();
				}
				
			}catch(NumberFormatException ex){
				JOptionPane.showMessageDialog(this, "Ungueltiger Wert");
			}


		}else if(e.getSource()==stop){
			if(sa!=null && sa.isAlive()){

				sa.stopThread();
			}
		}
	}

	/**
	 * Erzeugt eine zufällige Rundreise (initiale Route).
	 */
	private void erzeugeRundreise(){
		try{
			boolean check = true;
			int anzahl = Integer.parseInt(this.anzahl.getText());
			
			if(anzahl<=1){
				JOptionPane.showMessageDialog(this, "Anzahl Staedte: Ungueltiger Wert");
				check = false;
			}
			
			if(check){
				// Rundreise erzeugen
				rrAktuell = new Rundreise(anzahl);
				rrInitial = new Rundreise(0);	
				rrInitial.setRundreise(rrAktuell.getRundreise());


				tabbedPane.removeAll();
				tabbedPane.addTab("Aktuelle Rundreise", null, rrAktuell, "Zeigt die aktuelle Rundreise");
				tabbedPane.addTab("Initiale Rundreise", null, rrInitial, "Zeigt die initiale Rundreise");
				repaint();
				
				model.setValueAt(rrInitial.getDistanz(), 3, 1);
				model.setValueAt("", 0, 1);
				model.setValueAt("", 1, 1);
				model.setValueAt("", 2, 1);
				model.setValueAt("", 4, 1);
			}
			
		}catch(NumberFormatException ex){
			JOptionPane.showMessageDialog(this, "Anzahl Staedte: Ungueltiger Wert");
		}
	}

	public JButton getStart() {
		return start;
	}
	
	public JButton getInit() {
		return init;
	}
	
	public int getAbbruch(){
		return Integer.parseInt(abbruch.getText());
	}
	
	public int getZeit(){
		return Integer.parseInt(zeit.getText());
	}
	
	/**
	 * Aktualisiert die Tabellenwerte in der GUI
	 * @param sigma Aktueller Toleranzwert
	 * @param iterationen Anzahl Iterationen
	 * @param stabileIterationen Anzahl stabiler Iterationen (ohne Staedtetausch)
	 * @param distanz Die aktuelle Distanz der Rundreise
	 */
	public void setTableValues(double sigma, int iterationen, int stabileIterationen, int distanz){
		model.setValueAt(sigma, 0, 1);
		model.setValueAt(iterationen, 1, 1);
		model.setValueAt(stabileIterationen, 2, 1);
		model.setValueAt(distanz, 4, 1);
	}
}
