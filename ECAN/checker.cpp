#include <iostream>
#include <cmath>
#include <cassert>

#define GROUP_SIZE 8
#define GROUP_NUM 12
#define IMPORTANCE_INDEX_SIZE 104

typedef int sti_t;  // Assuming sti_t is an integer type

size_t importanceBin(sti_t impo) {
    short importance = static_cast<short>(impo);

    if (importance < 0)
        return 0;
    if (importance < 2 * GROUP_SIZE)
        return importance;

    short imp = std::ceil((importance - GROUP_SIZE) / static_cast<double>(GROUP_SIZE));

    int sum = 0;
    int i;
    for (i = 0; i <= GROUP_NUM; i++) {
        if (sum >= imp)
            break;
        sum += std::pow(2, i);
    }

    int ad = GROUP_SIZE - std::ceil(importance / std::pow(2, (i - 1)));
    size_t bin = ((i * GROUP_SIZE) - ad);

    if (bin > IMPORTANCE_INDEX_SIZE)
        std::cerr << "Warning: ibin = " << bin << "\n";

    assert(bin <= IMPORTANCE_INDEX_SIZE);
    return bin;
}

// Test function
int main() {
    int testValues[] = {10, 20, 50, 50, 100, 200};
    for (int val : testValues) {
        std::cout << "importanceBin(" << val << ") = " << importanceBin(val) << "\n";
    }
    return 0;
}
