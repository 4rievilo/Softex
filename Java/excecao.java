package Java;
public static void main (String[] args) {
try {
    int a = Integer.parseInt(JOptionPane.showInputDialog("Digite uma idade"));
    System.out.println(a);
} 
catch (Exception excecao) {
    System.out.println("Digite apenas números.");
}
    System.out.println("Fim");
}