from wd_utils import wd_containers, wd_io


lc_params = wd_containers.LCParameterContainer()

# general params
lc_params["jdphs"] = 2
lc_params["ifcgs"] = 0
lc_params["mode"] = 5
lc_params["icor1"] = 0
lc_params["icor2"] = 0

# system params
lc_params["hjd0"] = 54954.534784
lc_params["pzero"] = 1.655473
lc_params["dpdt"] = 0
lc_params["pshift"] = 0.0015983790
lc_params["delph"] = 0
lc_params["nga"] = 1
lc_params["e"] = 0
lc_params["a"] = 7.51
lc_params["f1"] = 1
lc_params["f2"] = 1
lc_params["vga"] = -16.2446
lc_params["xincl"] = 70.966
lc_params["tavh"] = 7000
lc_params["tavc"] = 4293
lc_params["phsv"] = 4.9582
lc_params["pcsv"] = 2.2574
lc_params["rm"] = 0.21
lc_params["perr"] = 1.570796327
lc_params["dperdt"] = 0
lc_params["the"] = 0
lc_params["vunit"] = 1
lc_params["abunin"] = 0
lc_params["dpclog"] = 1.83714

# surface params
lc_params["ifat1"] = 1
lc_params["ifat2"] = 1
lc_params["gr1"] = 0.320
lc_params["gr2"] = 0.270
lc_params["ipb"] = 0
lc_params["mref"] = 1
lc_params["nref"] = 1
lc_params["n1"] = 30
lc_params["n2"] = 30
lc_params["alb1"] = 0.5
lc_params["alb2"] = 0.699
lc_params["ld1"] = 1
lc_params["ld2"] = 1
lc_params["xbol1"] = 0.471
lc_params["xbol2"] = 0.531
lc_params["ybol1"] = 0
lc_params["ybol2"] = 0

# third body
lc_params["if3b"] = 0
lc_params["a3b"] = 0
lc_params["p3b"] = 0
lc_params["xincl3b"] = 0
lc_params["e3b"] = 0
lc_params["perr3b"] = 0
lc_params["tc3b"] = 0

# spot params
lc_params["nomax"] = 0
lc_params["kspev"] = 0
lc_params["kspot"] = 1
lc_params["fspot1"] = 1
lc_params["fspot2"] = 1
lc_params["ifsmv1"] = 0
lc_params["ifsmv2"] = 0

# noise
lc_params["stdev"] = 0.0
lc_params["noise"] = 0.0
lc_params["seed"] = 138472375

# steps
lc_params["hjdst"] = 50000
lc_params["hjdsp"] = 51000
lc_params["hjdin"] = lc_params["pzero"].get() / 100.0
lc_params["phstrt"] = 0
lc_params["phstop"] = 1
lc_params["phin"] = 0.001

# normalization
lc_params["phn"] = 0.25

# temperature estimation params
lc_params["phobs"] = 0.25
lc_params["lsp"] = 1
lc_params["tobs"] = 7000

# line profile parameters
lc_params["binwm1"] = 0.00001
lc_params["sc1"] = 1.0
lc_params["sl1"] = 0.0
lc_params["nf1"] = 1

lc_params["binwm2"] = 0.00001
lc_params["sc2"] = 1.0
lc_params["sl2"] = 0.0
lc_params["nf2"] = 1

# add spots
lc_params.add_spot(1, 1.71127, 1.61975, 0.22156, 1.02222, 50800, 50900, 50930, 51100)

# set synthetic curve
lc_params.set_synthetic_curve(26, 10.5, 1, 0.5, 0.5, 0, 0, 0, 0, 8, 1, 0.592, 0, 0)

# add spectral lines
lc_params.add_spectral_line(2, 0.55, 0.00001, 0.5, 0)

lcio = wd_io.LCIO(lc_params)
lcio.fill_for_synthetic_light_curve().save()
