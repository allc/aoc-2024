#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>

int main()
{
    std::ifstream file("input.txt");
    std::vector<int> col1;
    std::unordered_map<int, int> col2;
    int num1, num2;
    while (file >> num1 >> num2)
    {
        col1.push_back(num1);
        col2[num2]++;
    }

    int similarityScore = 0;
    for (int i : col1)
    {
        similarityScore += i * col2[i];
    }

    std::cout << similarityScore << std::endl;
}