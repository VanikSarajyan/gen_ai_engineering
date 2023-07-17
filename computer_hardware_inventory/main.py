from cpu import CPU
from hdd import HDD
from ssd import SSD

cpu = CPU("Intel Core i7 11", "Intel", 16, "LGA", "AM4", 95, 5)
hdd = HDD("HDD", "AMD", 1000, 3, 7200, 5)
ssd = SSD("SSD", "AMD", 500, "PCIe NMVe 3.0", 10)


cpu.claim(3)
hdd.claim(3)
ssd.claim(3)

print(cpu)
print(repr(cpu))

cpu.freeup(2)
cpu.died(5)
print(repr(cpu))

ssd.freeup(2)
ssd.died(5)
print(repr(ssd))

print(cpu.total)
print(ssd.total)
