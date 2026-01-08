# PCB Dataset
## Introduction to PCBs
The PCB dataset is primarily a dataset of images of Printed Circuit Boards.
Printed Circuit board is the most important element in an electronic device. A great number of elements are placed on the PCB, Hence its quality has a direct impact on the device performance.

## Aim of the dataset
The PCB is a complex device, and it has become increasingly difficult to detect and classify its defects.
This dataset provides a colourized synthesized PCB dataset, with the 6 major defects in PCBs classified for model training.

## Structure
The dataset is divided into 4 part, each part is placed inside a folder: Annotations, images, PCB_USED, rotation.
![alt text](image.png)
PCB_DATASET
├───Annotations
│   ├───Missing_hole
│   ├───Mouse_bite
│   ├───Open_circuit
│   ├───Short
│   ├───Spur
│   └───Spurious_copper
├───images
│   ├───Missing_hole
│   ├───Mouse_bite
│   ├───Open_circuit
│   ├───Short
│   ├───Spur
│   └───Spurious_copper
├───PCB_USED
└───rotation
    ├───Missing_hole_rotation
    ├───Mouse_bite_rotation
    ├───Open_circuit_rotation
    ├───Short_rotation
    ├───Spurious_copper_rotation
    └───Spur_rotation