from amaranth.build import *
from gowin import GowinPlatform

class GW1NSR_4C_TestPlatform(GowinPlatform):
    device = "GW1NSR-4C"
    pn = "GW1NSR-LV4CQN48PC6/I5"
    package = "QN48P"
    speed = "C6/I5"
    default_clk = "sys_clk"

    resources = [
        Resource("sys_clk",0,Pins("45",dir="i"),Clock(25e6),Attrs(IO_TYPE = "LVCMOS33")), 

        Resource("led_r",0,Pins("16",dir="o"),Attrs(IO_TYPE="LVCMOS33")),
        Resource("led_g",0,Pins("17",dir="o"),Attrs(IO_TYPE="LVCMOS33")),
        Resource("led_b",0,Pins("18",dir="o"),Attrs(IO_TYPE="LVCMOS33")),

        Resource("scl",0,Pins("27",dir="io"),Attrs(IO_TYPE="LVCMOS33",PULL_MODE="UP")),
        Resource("sda",0,Pins("28",dir="io"),Attrs(IO_TYPE="LVCMOS33",PULL_MODE="UP")),

    ]

    connectors = []

    def toolchain_prepare(self, fragment, name, **kwargs):
        overrides = {
            "add_options":
                """
                set_option -use_mode_as_gpio 1
                set_option -use_mspi_as_gpio 1
                set_option -use_done_as_gpio 1
                """,
           
        }
        return super().toolchain_prepare(fragment, name, **overrides, **kwargs)

 # "add_constraints":
 #               "create_clock -name sys_clk1 -period 400 -waveform {0 200} [get_nets {sys_clk}]"