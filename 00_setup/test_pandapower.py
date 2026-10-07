import pandapower as pp

net = pp.create_empty_network()
b1 = pp.create_bus(net, vn_kv=20.0, name="MV bus")
b2 = pp.create_bus(net, vn_kv=0.4, name="LV bus")
b3 = pp.create_bus(net, vn_kv=0.4, name="Load bus")
pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid")
pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV")
pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, std_type="NAYY 4x50 SE")
pp.create_load(net, bus=b3, p_mw=0.1, q_mvar=0.05, name="Load")
pp.runpp(net)
print(net.res_bus)
print(net.res_line)
