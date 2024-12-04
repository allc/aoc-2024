import java.io.*;
import java.util.*;

public class Day04Part1 {
    public static void main(String[] args) {
        List<char[]> grid = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                grid.add(line.toCharArray());
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }

        String target = "XMAS";
        int[][] directions = {
            {0, 1}, // right
            {1, 0}, // down
            {0, -1}, // left
            {-1, 0}, // up
            {1, 1}, // down right
            {1, -1}, // down left
            {-1, -1}, // up left
            {-1, 1} // up right
        };

        int count = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(0).length; j++) {
                if (grid.get(i)[j] != target.charAt(0)) {
                    continue;
                }

                for (int[] direction : directions) {
                    if (i + (target.length() - 1) * direction[0] >= grid.size() || i + (target.length() - 1) * direction[0] < 0 || j + (target.length() - 1) * direction[1] >= grid.get(0).length || j + (target.length() - 1) * direction[1] < 0) {
                        continue;
                    }
                    for (int k = 1; k < target.length(); k++) {
                        if (grid.get(i + k * direction[0])[j + k * direction[1]] != target.charAt(k)) {
                            break;
                        }
                        if (k == target.length() - 1) {
                            count++;
                        }
                    }
                }
            }
        }
        System.out.println(count);
    }
}