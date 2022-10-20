import java.util.Scanner;

public class SachinTravels {
    static Scanner input = new Scanner(System.in);

    public static void merge(PetrolPumpAndDistance[] PetrolPumps, int low, int mid, int high) {
        int size1 = mid - low + 1;
        int size2 = high - mid;

        PetrolPumpAndDistance array1[] = new PetrolPumpAndDistance[size1];
        PetrolPumpAndDistance array2[] = new PetrolPumpAndDistance[size2];

        for (int iter1 = 0; iter1 < size1; ++iter1)
            array1[iter1] = PetrolPumps[low + iter1];
        for (int iter2 = 0; iter2 < size2; ++iter2)
            array2[iter2] = PetrolPumps[mid + 1 + iter2];

        int iter1 = 0, iter2 = 0;

        int mergeIter = low;
        while (iter1 < size1 && iter2 < size2) {
            if (array1[iter1].getDistance() <= array2[iter2].getDistance())
                PetrolPumps[mergeIter++] = array1[iter1++];
            else
                PetrolPumps[mergeIter++] = array2[iter2++];
        }

        while (iter1 < size1)
            PetrolPumps[mergeIter++] = array1[iter1++];

        while (iter2 < size2)
            PetrolPumps[mergeIter++] = array2[iter2++];
    }

    public static void mergeSort(PetrolPumpAndDistance[] PetrolPumps, int low, int high) {
        if (low < high) {
            int mid = low + (high - low) / 2;

            mergeSort(PetrolPumps, low, mid);
            mergeSort(PetrolPumps, mid + 1, high);

            merge(PetrolPumps, low, mid, high);
        }
    }

    public static void makeDistanceRelative(PetrolPumpAndDistance[] PetrolPumps) {
        for (int i = 1; i < PetrolPumps.length; i++) {
            PetrolPumps[i].setDistance(PetrolPumps[i].getDistance() - PetrolPumps[i - 1].getDistance());
        }
    }

    public static void inputPP(PetrolPumpAndDistance[] PetrolPumps) {
        for (int i = 0; i < PetrolPumps.length; i++) {
            PetrolPumpAndDistance fresh = new PetrolPumpAndDistance();
            System.out.println("Enter name of petrol Pump");
            fresh.setName(input.nextLine());
            System.out.println("Enter distance");
            fresh.setDistance(input.nextInt());
            input.nextLine();
            PetrolPumps[i] = fresh;
        }
    }

    public static void inputCar(Car car) {
        System.out.println("Enter car name : ");
        car.setName(input.nextLine());
        System.out.println("Enter car mileage : ");
        car.setMileage(input.nextInt());
        System.out.println("Enter car capacity : ");
        car.setCapacity(input.nextInt());
        input.nextLine();
    }

    public static void display(PetrolPumpAndDistance[] PetrolPumps) {
        for (int i = 0; i < PetrolPumps.length; i++) {
            System.out.print("(" + PetrolPumps[i].getName() + "," + PetrolPumps[i].getDistance() + ")  ");
        }
    }

    public static PetrolPumpAndDistance[] giveOptimizedRoute(PetrolPumpAndDistance[] PetrolPumps, Car car) {
        PetrolPumpAndDistance[] tempPetrolPumps = new PetrolPumpAndDistance[PetrolPumps.length];
        int limit = car.getCapacity() * car.getMileage();
        int tempIter = 0;
        int iter = 0;
        tempPetrolPumps[tempIter++] = PetrolPumps[iter++];

        for (iter = 1; iter < PetrolPumps.length - 1; iter++) {
            if (PetrolPumps[iter + 1].getDistance() < limit) {
                continue;
            }
            tempPetrolPumps[tempIter++] = PetrolPumps[iter];
        }

        PetrolPumpAndDistance[] optimizedPetrolPumps = new PetrolPumpAndDistance[tempIter];

        for (iter = 0; iter < optimizedPetrolPumps.length; iter++) {
        optimizedPetrolPumps[iter] = tempPetrolPumps[iter];
        }

        return optimizedPetrolPumps;
    }

    public static void main(String... args) {
        Car car = new Car();
        inputCar(car);
        System.out.println("Enter no. of petrol pumps");
        int size = input.nextInt();
        input.nextLine();
        PetrolPumpAndDistance PetrolPumps[] = new PetrolPumpAndDistance[size];
        inputPP(PetrolPumps);
        mergeSort(PetrolPumps, 0, size - 1);
        PetrolPumpAndDistance[] optimizedPetrolPumps = giveOptimizedRoute(PetrolPumps, car);
        display(optimizedPetrolPumps);

    }

}

class PetrolPumpAndDistance {

    private String name;
    private int distance;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

}

class Car {
    private String name;
    private int mileage;
    private int capacity;

    public Car() {
    }

    public Car(String name, int mileage) {
        this.name = name;
        this.mileage = mileage;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setMileage(int mileage) {
        this.mileage = mileage;
    }

    public int getMileage() {
        return mileage;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public int getCapacity() {
        return capacity;
    }

}
