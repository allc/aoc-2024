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

        int count = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(0).length; j++) {
                if (grid.get(i)[j] != 'A') {
                    continue;
                }

                if (i < 1 || i >= grid.size() - 1 || j < 1 || j >= grid.get(0).length - 1 || j < 1 || j >= grid.get(0).length - 1) {
                    continue;
                }

                if (
                    (
                        (grid.get(i - 1)[j - 1] == 'M' && grid.get(i + 1)[j + 1] == 'S') || (grid.get(i - 1)[j - 1] == 'S' && grid.get(i + 1)[j + 1] == 'M')
                    ) && (
                        (grid.get(i - 1)[j + 1] == 'M' && grid.get(i + 1)[j - 1] == 'S') || (grid.get(i - 1)[j + 1] == 'S' && grid.get(i + 1)[j - 1] == 'M')
                    )
                ) {
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}