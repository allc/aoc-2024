#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main()
{
    std::ifstream file("input.txt");
    std::vector<int> col1, col2;
    int num1, num2;
    while (file >> num1 >> num2)
    {
        col1.push_back(num1);
        col2.push_back(num2);
    }

    std::sort(col1.begin(), col1.end());
    std::sort(col2.begin(), col2.end());

    int totalDistance = 0;
    for (int i = 0; i < col1.size(); i++)
    {
        totalDistance += abs(col1[i] - col2[i]);
    }

    std::cout << totalDistance << std::endl;
}