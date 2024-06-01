#!/usr/bin/env python
# coding: utf-8

# In[32]:


# inputs for the calculator. Supports 6,12,24,48 and 96 well plates 
cell_counts = 52
quadrant_counts = 4
number_required = 10000
plate_kind = 96


###EXECUTION CODE

# if statement for the working volume.
if plate_kind == 96:
    working_volume = 100

elif plate_kind == 6:
    working_volume = 2000

elif plate_kind == 12:
    working_volume = 1000

elif plate_kind == 24:
    working_volume = 500

elif plate_kind == 48:
    working_volume = 200

else:
    working_volume = "unsupported plate kind"
    print(working_volume)
    

# if statement for the number of wells required.
if plate_kind == 96:
    number_of_wells = 100

elif plate_kind == 6:
    number_of_wells = 8

elif plate_kind == 24:
    number_of_wells = 26

elif plate_kind == 48: 
    number_of_wells = 52

else:
    working_volume = "unsupported number of well"
    print(working_volume)

avg_cell_count = cell_counts / quadrant_counts
cell_suspension_concentration = avg_cell_count * 100
cell_suspension_vol = (
    number_required / cell_suspension_concentration
) * number_of_wells
dmem_vol_tot = number_of_wells * working_volume
dmem_vol_req = dmem_vol_tot - cell_suspension_vol


print("Average cell per quadrant = " + str(avg_cell_count))
print(
    "The concentration of your cell suspension = "
    + str(cell_suspension_concentration)
    + " cells/uL"
)
print(
    "Add "
    + str(cell_suspension_vol)
    + " uL of cell suspension into "
    + str(dmem_vol_req)
    + " uL of DMEM/FBS"
)

