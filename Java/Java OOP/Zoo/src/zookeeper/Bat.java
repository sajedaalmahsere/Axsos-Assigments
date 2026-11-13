package zookeeper;

public class Bat extends Mammal {
	public Bat(int energy){
		super(energy);
	}
	
	public int fly() {
		this.energy -= 50;
		System.out.println("the bat is now airborne, His energy is:" + this.energy);
		return this.energy;
	}
	
	public int eatHumans() {
		this.energy += 25;
		System.out.println("The bat ate a human, His energy is:" + this.energy);
		return this.energy;
	}
	
	public int attackTown() {
		this.energy -= 100;
		System.out.println("The bat attacked a town, remaining energy: " + this.energy);
		return this.energy;
	}
}
