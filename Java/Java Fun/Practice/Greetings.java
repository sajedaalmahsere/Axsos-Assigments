import java.util.Date; //imports the Date class.
public class Greetings {
    
    public String getCurrentDate() {
        Date date = new Date(); //creates a Date object.
        return "Current date is: " + date; //sends the date back as a String.
    }
}