import java.util.HashMap;
import java.util.Set;
public class Map {
    public static void main(String[] args) {
        HashMap <String,String> countryCapitals = new HashMap <>() ;
            countryCapitals.put("France ","Paris");
            countryCapitals.put("Palestine","Jerusalem");
            countryCapitals.put("Japan","Tokyo");
            countryCapitals.put("Egypt","Cairo"); 
            countryCapitals.put("Brazil","Brasilia");
            
            // String country = countryCapitals.get("Palestine");
            // System.out.println(country);
            // System.out.println(countryCapitals);

            Set<String> keys = countryCapitals.keySet();
            for(String key:keys){
                System.out.println(key);
                // System.out.println(countryCapitals.get(key));
            }
            System.out.println("The capital of Palestine is " + countryCapitals.get("Palestine"));
    }
}