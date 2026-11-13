
package zookeeper;

public class Gorilla extends Mammal {

    public Gorilla(int energy) {
        super(energy);
    }

    public int throwSomething() {
        this.energy -= 5;
        System.out.println("The gorilla has thrown an object, My energy is: " + this.energy);
        return this.energy;
    }

    public int eatBananas() {
        this.energy += 10;
        System.out.println("Thank you for feeding me, My energy is: " + this.energy);
        return this.energy;
    }

    public int climb() {
        this.energy += 10;
        System.out.println("The gorilla has climbed a tree, His energy is: " + this.energy);
        return this.energy;
    }
}
