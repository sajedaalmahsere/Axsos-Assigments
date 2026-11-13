package zookeeper;

public class TestMammal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Gorilla monkey1 = new Gorilla(60);
		monkey1.eatBananas();
        monkey1.climb();
        monkey1.throwSomething();
        
        Bat bat = new Bat(200);
		bat.fly();
		bat.attackTown();
		bat.eatHumans();
		bat.displayEnergy();
	}

}
