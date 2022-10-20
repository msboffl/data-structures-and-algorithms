
import java.util.Scanner;

public class SmallInvestmentCompany {

    static Scanner input = new Scanner(System.in);

    static void inputData(StockAndData[] Data) {

        System.out.println("Enter name of stock");
        StockAndData.setName(input.nextLine());
        System.out.println("Enter price");
        Data[0] = new StockAndData(input.nextInt(), 0);
        for (int i = 1; i < Data.length; i++) {
            StockAndData fresh = new StockAndData();
            System.out.println("Enter price");
            fresh.setPrice(input.nextInt());
            input.nextLine();
            fresh.setProfit(fresh.getPrice() - Data[i - 1].getPrice());
            Data[i] = fresh;
        }
    }

    static void display(StockAndData[] Data) {
        for (int i = 0; i < Data.length; i++) {
            System.out.print("(" + Data[i].getPrice() + "," + Data[i].getProfit() + ")  ");
        }
    }

    public static void main(String... args) {
        System.out.println("Enter no. of days");
        int size = input.nextInt();
        input.nextLine();
        StockAndData Data[] = new StockAndData[size];
        inputData(Data);
        display(Data);
        subArrayinfo maxProfit = maxSubArrayProfit(Data, 0, size - 1);

        System.out.println(
                "Best Profit is " + maxProfit.getSum() + " from " + (maxProfit.getStarIndex() + 1) + " to "
                        + (maxProfit.getEndIndex() + 1));
    }

    static subArrayinfo maxCrossingProfit(StockAndData[] Data, int low, int mid,
            int high) {
        int profit = 0;
        int left_profit = Integer.MIN_VALUE;
        int left = mid;
        for (int i = mid; i >= low; i--) {
            profit = profit + Data[i].getProfit();
            if (profit > left_profit)
                left_profit = profit;
            left = i;
        }

        profit = 0;
        int right_profit = Integer.MIN_VALUE;
        int right = mid;
        for (int i = mid; i < high; i++) {
            profit = profit + Data[i].getProfit();
            if (profit > right_profit)
                right_profit = profit;
            right = i;
        }

        int cross_profit = left_profit + right_profit - Data[mid].getProfit();
        subArrayinfo result;
        if (cross_profit > left_profit && cross_profit > right_profit) {
            result = new subArrayinfo(cross_profit, left, right);
        } else if (left_profit > cross_profit && left_profit > right_profit) {
            result = new subArrayinfo(left_profit, left, mid);
        } else {
            result = new subArrayinfo(right_profit, mid, right);
        }
        return result;
    }

    static subArrayinfo maxSubArrayProfit(StockAndData[] Data, int low, int high) {
        if (low > high) {
            subArrayinfo result = new subArrayinfo(Integer.MIN_VALUE, 0, 0);
            return result;
        }
        if (low == high) {
            subArrayinfo result = new subArrayinfo(Data[low].getProfit(), 0, 0);
            return result;
        }

        int mid = (low + high) / 2;
        subArrayinfo result;
        subArrayinfo left = maxSubArrayProfit(Data, low, mid - 1);
        subArrayinfo right = maxSubArrayProfit(Data, mid + 1, high);
        subArrayinfo cross = maxCrossingProfit(Data, low, mid, high);

        if (left.getSum() > right.getSum() && left.getSum() > cross.getSum()) {
            result = left;

        } else if (cross.getSum() > left.getSum() && cross.getSum() > right.getSum()) {
            result = cross;
        } else {
            result = right;
        }

        return result;
    }

}

class StockAndData {

    private static String name;
    private int price;
    private int profit;

    public StockAndData() {

    }

    public StockAndData(int price) {
        this.price = price;
        this.profit = price;
    }

    public StockAndData(int price, int profit) {
        this.price = price;
        this.profit = profit;
    }

    public String getName() {
        return name;
    }

    public static void setName(String name) {
        StockAndData.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public int getProfit() {
        return profit;
    }

    public void setProfit(int profit) {
        this.profit = profit;
    }

}

class subArrayinfo {
    private int sum;
    private int starIndex;
    private int endIndex;

    public int getSum() {
        return sum;
    }

    public void setSum(int sum) {
        this.sum = sum;
    }

    public int getStarIndex() {
        return starIndex;
    }

    public void setStarIndex(int starIndex) {
        this.starIndex = starIndex;
    }

    public subArrayinfo(int sum, int starIndex, int endIndex) {
        this.sum = sum;
        this.starIndex = starIndex;
        this.endIndex = endIndex;
    }

    public int getEndIndex() {
        return endIndex;
    }

    public void setEndIndex(int endIndex) {
        this.endIndex = endIndex;
    }

}