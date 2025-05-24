#include <iostream>
#include <unordered_map>
#include <vector>
#include <cstdlib> // For random values

class Atom {
public:
    int id;
    double sti;  // Short-Term Importance (STI)
    
    Atom(int _id, double _sti) : id(_id), sti(_sti) {}
    
    void updateSTI(double amount) {
        sti += amount;
    }
};

class ImportanceDiffusionSimulator {
private:
    std::unordered_map<int, Atom*> atoms;
    std::unordered_map<int, std::vector<int>> connections; // Graph of atom links
    double maxSpreadPercentage = 0.1; // 10% of STI spreads

public:
    void addAtom(int id, double sti) {
        atoms[id] = new Atom(id, sti);
    }

    void addConnection(int from, int to) {
        connections[from].push_back(to);
        connections[to].push_back(from); // Assume undirected links
    }

    void spreadImportance() {
        std::cout << "Starting importance diffusion...\n";

        for (const auto& [id, atom] : atoms) {
            double diffusionAmount = atom->sti * maxSpreadPercentage;
            std::cout << "[INFO] Atom " << id << " diffuses " << diffusionAmount << " STI\n";

            for (int neighbor : connections[id]) {
                atoms[neighbor]->updateSTI(diffusionAmount / connections[id].size());
                std::cout << " -> Atom " << neighbor << " receives " 
                          << diffusionAmount / connections[id].size() << " STI\n";
            }
        }

        std::cout << "Diffusion process complete.\n";
    }

    void printAtoms() {
        std::cout << "=== Atom Importance Values ===\n";
        for (const auto& [id, atom] : atoms) {
            std::cout << "Atom " << id << " | STI: " << atom->sti << "\n";
        }
    }

    ~ImportanceDiffusionSimulator() {
        for (auto& [id, atom] : atoms) delete atom;
    }
};

int main() {
    ImportanceDiffusionSimulator simulator;

    // Create atoms with initial STI values
    simulator.addAtom(1, 1.0);
    simulator.addAtom(2, 2.0);
    simulator.addAtom(3, 3.0);
    simulator.addAtom(4, 4.0);

    // Create connections (graph links)
    simulator.addConnection(1, 2);
    simulator.addConnection(2, 3);
    simulator.addConnection(3, 4);
    simulator.addConnection(4, 1);

    // Show initial state
    simulator.printAtoms();

    // Run importance diffusion simulation
    simulator.spreadImportance();

    // Show final state
    simulator.printAtoms();

    return 0;
}
