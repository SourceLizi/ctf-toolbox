import angr
p = angr.Project('./SimpleVM',auto_load_libs=False)
st = p.factory.entry_state()
sm = p.factory.simulation_manager(st)
sm.explore(find = 0x080488BB,avoid = [0x08048907,0x080486E1])
flag = sm.found[0].posix.dumps(0)
print(flag)
