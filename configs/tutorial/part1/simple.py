from gem5.prebuilt.demo.x86_demo_board import X86DemoBoard
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

board = X86DemoBoard()

workload = obtain_resource("x86-ubuntu-24.04-boot-no-systemd")

board.set_workload(workload)

simulator = Simulator(board=board)

simulator.run(20_000_000_000)
