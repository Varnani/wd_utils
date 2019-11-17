from wd_utils import wd_containers


def load():
    """
    Sets the DC parameters and returns the populated DCParameterContainer object.

    While this function and file is not required by the utility,
    you can use this for a starting point and quick reference.
    You can also copy this file and change the values for your own solution.

    :return: a DCParameterContainer instance
    """

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
    dc_params["perr"] = 1.570796327
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

    return dc_params