from wd_utils import wd_containers, wd_io
import numpy


dc_params = wd_containers.DCParameterContainer()

# general params
dc_params["jdphs"] = 2
dc_params["ifcgs"] = 0
dc_params["mode"] = 5
dc_params["icor1"] = 0
dc_params["icor2"] = 0

# system params
dc_params["hjd0"] = 54954.534784
dc_params["pzero"] = 1.655473
dc_params["dpdt"] = 0
dc_params["pshift"] = 0.0015983790
dc_params["delph"] = 0
dc_params["nga"] = 1
dc_params["e"] = 0
dc_params["a"] = 7.51
dc_params["f1"] = 1
dc_params["f2"] = 1
dc_params["vga"] = -16.2446
dc_params["xincl"] = 70.966
dc_params["tavh"] = 7000
dc_params["tavc"] = 4293
dc_params["phsv"] = 4.9582
dc_params["pcsv"] = 2.2574
dc_params["rm"] = 0.21
dc_params["perr0"] = 1.570796327
dc_params["dperdt"] = 0
dc_params["the"] = 0
dc_params["vunit"] = 1
dc_params["abunin"] = 0
dc_params["dpclog"] = 1.83714

# surface params
dc_params["ifat1"] = 1
dc_params["ifat2"] = 1
dc_params["gr1"] = 0.320
dc_params["gr2"] = 0.270
dc_params["ipb"] = 0
dc_params["mref"] = 1
dc_params["nref"] = 1
dc_params["n1"] = 30
dc_params["n2"] = 30
dc_params["alb1"] = 0.5
dc_params["alb2"] = 0.699
dc_params["ld1"] = 1
dc_params["ld2"] = 1
dc_params["xbol1"] = 0.471
dc_params["xbol2"] = 0.531
dc_params["ybol1"] = 0
dc_params["ybol2"] = 0

# third body
dc_params["if3b"] = 0
dc_params["a3b"] = 0
dc_params["p3b"] = 0
dc_params["xincl3b"] = 0
dc_params["e3b"] = 0
dc_params["perr3b"] = 0
dc_params["tc3b"] = 0

# general dc params
dc_params["isym"] = 1
dc_params["maglite"] = 0
dc_params["linkext"] = 0
dc_params["desextinc"] = 0
dc_params["n1l"] = 30
dc_params["n2l"] = 30

# spot params
dc_params["nomax"] = 0
dc_params["kspev"] = 0
dc_params["kspot"] = 1
dc_params["fspot1"] = 1
dc_params["fspot2"] = 1
dc_params["ifsmv1"] = 0
dc_params["ifsmv2"] = 0

# add spots
dc_params.add_spot(1, 1.71127, 1.61975, 0.22156, 1.02222, 50800, 50900, 50930, 51100)

# which spots to fit?
dc_params["kspa"] = 1
dc_params["nspa"] = 1
dc_params["kspb"] = 0
dc_params["nspb"] = 0

# params that can remain in their default values
# lc_params["ko"]
# lc_params["kdisk"]
# lc_params["ifder"]
# lc_params["iflcin"]
# lc_params["ifoc"]

# params that should not be modified, utility handles these itself
# lc_params["ifvc1"]
# lc_params["ifvc2"]
# lc_params["nlc"]
# lc_params["iftime"]
# lc_params["nppl"]

# add observations
lc = numpy.loadtxt("kic7385478_phase_intensity.dat", unpack=True)
vr1 = numpy.loadtxt("kic7385478_vr1.dat", unpack=True)
vr2 = numpy.loadtxt("kic7385478_vr2.dat", unpack=True)

dc_params.add_light_curve(26, 10.732025, 1, 0.462, 0.344, 0, 0, 0, 0.000178, 1, 0, 0, 0, 0,
                          lc[0], lc[1], lc[2], wla=0.592)
dc_params.add_velocity_curve(1, 9, 1, 0.592, vr1[0], vr1[1], vr1[2])
dc_params.add_velocity_curve(2, 25, 1, 0.592, vr2[0], vr2[1], vr2[2])

# adjust keeps
dc_params.keeps["xincl"] = 0
dc_params.keeps["pshift"] = 0
dc_params.keeps["tavc"] = 0
dc_params.keeps["hla"] = 0
dc_params.keeps["phsv"] = 0

dcio = wd_io.DCIO(dc_params)
dcio.fill_for_solution().save()
