import java.util.HashMap;
import java.util.Set;

public class Map {
    public static void main(String[] args) {
        HashMap <String,String> trackList = new HashMap<String,String>();
        trackList.put("Perfect", "Ed Sheeran");
        trackList.put("Shape of You", "Ed Sheeran");
        trackList.put("Someone Like You", "Adele");
        trackList.put("Blinding Lights", "The Weeknd");

        System.out.println(trackList.get("Someone Like You"));

        Set<String> track = trackList.keySet();
        for (String title: track){
                System.out.println(title + " Contains these traks: " + trackList.get(title));
        }
    }
}
