
from amaranth import *
from amaranth.build import Platform

from gw1nsr_4c_test_platform import GW1NSR_4C_TestPlatform

class test_led(Elaboratable):
    def __init__(self) -> None:
        super().__init__()

    def elaborate(self,platform:Platform) -> Module:
        m = Module()

        led_r = platform.request("led_r")
        led_g = platform.request("led_g")
        led_b = platform.request("led_b")

        m.domains.sync = ClockDomain(name="sync")
        sys_clk = platform.request("sys_clk")
        """
        sys_clk = Signal()
        m.submodules.oscz = Instance("OSCZ",
            p_FREQ_DIV = 100,
            p_S_RATE = "SLOW",
            i_OSCEN = 1,
            o_OSCOUT = sys_clk,
        )
        """
        sys_clk_o = Signal()
        clkoutp = Signal()
        clkoutd = Signal()

        m.submodules.pllvr = Instance("PLLVR",
            o_CLKOUT = sys_clk_o,
            i_RESET = 0,
            i_RESET_P = 0,
            i_CLKIN = sys_clk,
            i_CLKFB = 0,
            i_FBDSEL = Const(0,6),
            i_IDSEL = Const(0,6),
            i_ODSEL = Const(0,6),
            i_PSDA = Const(0,4),
            i_DUTYDA = Const(0,4),
            i_FDLY = Const(0,4),
            i_VREN = 1,
            o_CLKOUTP = clkoutp,
            o_CLKOUTD = clkoutd,
            p_FCLKIN = "25",
            p_DYN_IDIV_SEL  = "false",
            p_IDIV_SEL  = 0,
            p_DYN_FBDIV_SEL  = "false",
            p_FBDIV_SEL = 7,
            p_DYN_ODIV_SEL = "false",
            p_ODIV_SEL = 4,
            p_PSDA_SEL  = "0000",
            p_DYN_DA_EN  = "true",
            p_DUTYDA_SEL = "1000",
            p_CLKOUT_FT_DIR  = 1,
            p_CLKOUTP_FT_DIR = 1,
            p_CLKOUT_DLY_STEP = 0,
            p_CLKFB_SEL = "internal",
            p_CLKOUT_BYPASS = "false",
            p_CLKOUTP_BYPASS  = "false",
            p_CLKOUTD_BYPASS = "false",
            p_DYN_SDIV_SEL  = 2,
            p_CLKOUTD_SRC  = "CLKOUT",
            p_CLKOUTD3_SRC  = "CLKOUT",
            p_DEVICE = "GW1NSR-4C",
        )
        m.d.comb += ClockSignal().eq(sys_clk_o)


        # fdata.oe.eq(0),         # 0 input
        
        counter = Signal(25)
        # with m.If(fdata.i.all()):
        #     m.d.sync += counter.eq(counter+1)

        m.d.sync += counter.eq(counter +1)

        m.d.comb += [
            led_r.eq(counter[-1]),
            led_g.eq(counter[-2]),
            led_b.eq(counter[-3]),
        ]
        return m

if __name__ == "__main__":
    platform = GW1NSR_4C_TestPlatform()
    platform.build(test_led())


    