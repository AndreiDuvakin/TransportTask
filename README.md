[🇷🇺 Русский](README_RU.md)

# Transport problem: delta method

## About the project

This project was developed as part of the internship program in the specialty **09.02.07 Information Systems and Programming** (PM.02 Implementation of Software Module Integration). The program solves a classic transportation problem using the **delta method** (a combination of the northwest angle method and the potential method).
The project is designed to optimize the transportation plan from suppliers (warehouses) to consumers (stores) with minimal total costs.

## Purpose of creation

- Gaining practical experience integrating software modules.
- Implementing an economic-mathematical model in practice.
- Demonstrating skills in:
- Developing requirements for software modules;
- Writing and debugging code;
- Creating test scripts;
- Inspecting code for compliance with standards.

## What the program does

1. Accepts input data:
   - Number of suppliers and customers;
   - Inventory (warehouses) and demand (stores);
   - Transportation cost matrix.
2. Automatically generates the initial matrix (manual input is possible).
3. Solves the transportation problem using the delta method.
4. Outputs:
   - Optimal transportation plan;
    - Minimum total transportation cost.

The program also reports if the problem cannot be solved by this method.

## Report

The internship report is in the file [Report.pdf](Report.pdf)

## Algorithm

1. Transformation of the cost matrix → increment table.
2. Finding cells with a single zero increment.
3. Building and optimizing a transportation plan.
4. Redistributing supplies across supply chains.
5. Testing optimality using the potential method.

## Authors
Duvakin A.A.

Mikryukova A.A.

Group: ISPP-21-2
Multidisciplinary College, G. I. Nosov Moscow State Technical University
Magnitogorsk, 2024

## License
MIT. See file [LICENSE](LICENSE).
