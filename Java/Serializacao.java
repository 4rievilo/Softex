package Java;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serial;
import java.io.Serializable;

public class Serializacao {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        ProductOnLine productOnLine = new ProductOnLine ("calça", "20 reais")
        System.out.println(productOnLine);

        ObjectOutputStream objectOutput = new ObjectOutputStream(new FileOutputStream("product.bytejava"));
        objectOutput.writeObject(productOnLine);
        objectOutput.close();

        ObjectInputStream objectInput = new ObjectInputStream(new FileInputStream("product.bytejava"));
        ProductOnLine productOnLine = (ProductOnLine) objectInput.readObject();
        objectInput.close();
        System.out.println(productOnLine);
    }
}
