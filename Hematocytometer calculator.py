#!/usr/bin/env python
# coding: utf-8

# In[76]:


# how many cells have you counted
cell_counts = 300
# how many quadrants have you counted
quadrant_counts = 2
# Number of cells you want to plate
number_required = 300000
# Always add additional wells for pipetting accuracy
number_well = 14
# working vol of each well (uL)
DMEM = 2000

number_of_cells_total_counted = cell_counts / quadrant_counts
print(
    "Your average counted cells in each quadrant is -->   "
    + str(number_of_cells_total_counted)
)

Cells_per_uL = number_of_cells_total_counted * 100
print("Your cell suspension conentration is --> " + str(Cells_per_uL) + " cells/uL")

Cell_suspension_vol = (number_required / Cells_per_uL) * number_well
print(
    "Total amount of cell suspension required ---> " + str(Cell_suspension_vol) + " uL"
)

number_DMEM = number_well * DMEM
number_DMEM_required = number_DMEM - Cell_suspension_vol

print(
    "To "
    + str(number_DMEM_required)
    + " uL of DMEM/FBS, add "
    + str(Cell_suspension_vol)
    + " uL of cell suspension"
)

