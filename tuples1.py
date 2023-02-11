gas_volume = (0, 2, 66, 444, 888, 415)
new_val = (7775, 553)
new_gas_vol = gas_volume + new_val
value_to_remove = 888
idx = new_gas_vol.index(value_to_remove)
new_volume = new_gas_vol[:idx] + new_gas_vol[idx + 1 :]

print(new_gas_vol[0], new_gas_vol[-1])
print(new_gas_vol[1:4])
print(new_volume)
