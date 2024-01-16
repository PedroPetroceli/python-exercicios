colonia_a = 4
colonia_b = 10
taxa_a = 0.03
taxa_b = 0.015
dias = 0

while colonia_a <= colonia_b:
  colonia_a *= 1 + taxa_a
  colonia_b *= 1 + taxa_b
  dias += 1
  
print(f'Irá levar {dias}dias para a colônia A ultrapassar a colônia')