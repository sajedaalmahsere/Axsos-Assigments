public class TestGreetings {
    public static void main(String[] args) {

        Greetings greeterApp = new Greetings();
    //  className variableName newObj Constructor
    //  We created an object (instance) from the Greetings class.
        String dateMessage = greeterApp.getCurrentDate();
                            //objectName.methodName();
        // The dot (.) allows us to access methods and properties of an object.
        System.out.println(dateMessage);
    }
}
