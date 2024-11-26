# 1. Code Development

## 1.1 Development Schedule

| Task Number | Task Description                                           | Owner(s)             | Start Date   | End Date     | Dependencies           |
|-------------|------------------------------------------------------------|----------------------|--------------|--------------|------------------------|
| 1           | Cleaning the data                                          | Harvey               | 10/22/2024   | 10/28/2024   | N/A                    |
| 2           | Visualize speed contour diagram with SR_19 and US101 data  | Xinyang, Nolan       | 10/22/2024   | 11/04/2024   | Task 1                 |
| 3           | Visualize fundamental diagram with SR_19 and US101 data    | Xinyang, Nolan       | 10/22/2024   | 11/11/2024   | Task 1                 |
| 4           | Model optimization                                         | Harvey               | 11/11/2024   | 11/18/2024   | Task 1                 |
| 5           | Write PPT presentation                                     | Harvey, Xinyang, Nolan| 11/19/2024   | 11/25/2024   | Tasks 1, 2, 3, 4       |

## 1.2 Timeline
- **Project Start Date**: 10/22/2024
- **Project End Date**: 11/30/2024

## 1.3 Notes
- Task 2, 3, and 4 depend on the completion of Task 1.
- Task 5 depends on the completion of Tasks 1, 2, 3, and 4.
- Owner mainly focuses on given tasks, but feel free to play with other tests if you want.

# 2. Writing Report

## 2.1 Report Writing Assignment

| Sections                             | Owner        |
|--------------------------------------|--------------|
| Introduction, Background, Methodology| Harvey Jing  |
| Result for US101SB                   | Xinyang      |
| Result for SR91                      | Nolan        |
| Conclusion                           | Harvey Jing  |

## 2.2 Report Writing Instruction
1. Run the code in `project_task_01.ipynb`, `project_task_02.ipynb`, and `project_task_03.ipynb`.
2. Review the result output in each notebook.
3. Review the output CSV files under `Group 2 US101SB` and `SR_91_Bottleneck_B_150-200`.
4. Write the report based on the reviewed results and outputs.

# 3. CSV File Descriptions

## 3.1 Group 2 US101SB

- **US101SB_{date}.csv**: The original data.
- **Stations_US101.csv**: Station data.
- **Zone_Readings_{date}.csv**: Aggregated data.
- **speed_contour_{date}.csv**: Speed contour.
- **volume_contour_{date}.csv**: Volume contour.
- **density_contour_{date}.csv**: Density contour.
- **v_fitted_{date}.csv**: Fitted speed value using five models.

## 3.2 SR_91_Bottleneck_B_150-200

- **Inventory.csv**: Station data.
- **Zone_Readings_{date}.csv**: Aggregated data.
- **speed_contour_{date}.csv**: Speed contour.
- **volume_contour_{date}.csv**: Volume contour.
- **density_contour_{date}.csv**: Density contour.
- **v_fitted_{date}.csv**: Fitted speed value using five models.