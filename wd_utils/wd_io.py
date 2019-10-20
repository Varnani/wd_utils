from wd_containers import _ParameterContainer


class _WDInput:
    def __init__(self, container):
        self._output = ""
        self.warning = ""
        self.error = ""
        self.has_warning = False
        self.has_error = False

        self.parameters = container

    @staticmethod
    def format_eccentricity(ipt):
        if ipt >= 1.0 or ipt < 0.0:
            raise ValueError("Invalid eccentricity value: " + repr(ipt))
        else:
            output = "{:6.5f}".format(ipt)
            return output[1:]


class LCInput(_WDInput):
    def __init__(self, container):
        _WDInput.__init__(self, container)

    def _format_input(self, mpage, ktstep=0):

        self.parameters.check_values()

        line1 = str(mpage) + " " + \
                self.parameters["nref"].format(1, 0, "") + " " + \
                self.parameters["mref"].format(1, 0, "") + " " + \
                self.parameters["ifsmv1"].format(1, 0, "") + " " + \
                self.parameters["ifsmv2"].format(1, 0, "") + " " + \
                self.parameters["icor1"].format(1, 0, "") + " " + \
                self.parameters["icor2"].format(1, 0, "") + " " + \
                self.parameters["if3b"].format(1, 0, "") + " " + \
                self.parameters["ld1"].format(2, 0, "", signed=True) + " " + \
                self.parameters["ld2"].format(2, 0, "", signed=True) + " " + \
                self.parameters["kspev"].format(1, 0, "") + " " + \
                self.parameters["kspot"].format(1, 0, "") + " " + \
                self.parameters["nomax"].format(1, 0, "") + " " + \
                self.parameters["ifcgs"].format(1, 0, "") + " " + \
                ((" " * (6 - len(str(ktstep)))) + str(ktstep)) + "\n"

        line2 = self.parameters["jdphs"].format(1, 0, "") + \
                self.parameters["hjd0"].format(15, 6, "F") + \
                self.parameters["pzero"].format(17, 10, "D") + \
                self.parameters["dpdt"].format(14, 6, "D") + \
                self.parameters["pshift"].format(10, 4, "D") + \
                self.parameters["delph"].format(8, 5, "F") + \
                self.parameters["nga"].format(3, 0, "") + \
                self.parameters["stdev"].format(11, 4, "D") + \
                self.parameters["noise"].format(2, 0, "") + \
                self.parameters["seed"].format(11, 0, "F") + "\n"

        line3 = self.parameters["hjdst"].format(14, 6, "F") + \
                self.parameters["hjdsp"].format(15, 6, "F") + \
                self.parameters["hjdin"].format(13, 6, "F") + \
                self.parameters["phstrt"].format(12, 6, "F") + \
                self.parameters["phstop"].format(12, 6, "F") + \
                self.parameters["phin"].format(12, 6, "F") + \
                self.parameters["phn"].format(12, 6, "F") + \
                self.parameters["phobs"].format(10, 4, "F") + \
                self.parameters["lsp"].format(2, 0, "") + \
                self.parameters["tobs"].format(8, 4, "F") + "\n"

        line4 = self.parameters["mode"].format(2, 0, "") + \
                self.parameters["ipb"].format(2, 0, "") + \
                self.parameters["ifat1"].format(2, 0, "") + \
                self.parameters["ifat2"].format(2, 0, "") + \
                self.parameters["n1"].format(4, 0, "") + \
                self.parameters["n2"].format(4, 0, "") + \
                self.parameters["perr0"].format(13, 6, "F") + \
                self.parameters["dperdt"].format(14, 6, "D") + \
                self.parameters["the"].format(8, 5, "F") + \
                self.parameters["vunit"].format(8, 2, "F") + "\n"

        line5 = self.format_eccentricity(self.parameters["e"].get()) + \
                self.parameters["a"].format(13, 6, "D") + \
                self.parameters["f1"].format(10, 4, "F") + \
                self.parameters["f2"].format(10, 4, "F") + \
                self.parameters["vga"].format(10, 4, "F") + \
                self.parameters["xincl"].format(9, 3, "F") + \
                self.parameters["gr1"].format(7, 3, "F") + \
                self.parameters["gr2"].format(7, 3, "F") + \
                self.parameters["abunin"].format(7, 2, "F") + \
                self.parameters["fspot1"].format(10, 4, "F") + \
                self.parameters["fspot2"].format(10, 4, "F") + "\n"

        tavh, tavc = self.parameters.get_temperatures()

        line6 = tavh + " " + tavc + \
                self.parameters["alb1"].format(7, 3, "F") + \
                self.parameters["alb2"].format(7, 3, "F") + \
                self.parameters["poth"].format(13, 6, "D") + \
                self.parameters["potc"].format(13, 6, "D") + \
                self.parameters["rm"].format(13, 6, "D") + \
                self.parameters["xbol1"].format(7, 3, "F") + \
                self.parameters["xbol2"].format(7, 3, "F") + \
                self.parameters["ybol1"].format(7, 3, "F") + \
                self.parameters["ybol2"].format(7, 3, "F") + \
                self.parameters["dpclog"].format(8, 5, "F") + "\n"

        line7 = self.parameters["a3b"].format(12, 6, "D") + \
                self.parameters["p3b"].format(14, 7, "D") + \
                self.parameters["xinc3b"].format(11, 5, "F") + \
                self.parameters["e3b"].format(9, 6, "F") + \
                self.parameters["perr3b"].format(10, 7, "F") + \
                self.parameters["tc3b"].format(17, 8, "F") + "\n"

        line8 = self.parameters.synthetic_curve["iband"].format(3, 0, "") + \
                self.parameters.synthetic_curve["hl"].format(13, 7, "D") + \
                self.parameters.synthetic_curve["cl"].format(13, 7, "D") + \
                self.parameters.synthetic_curve["xh"].format(7, 3, "F") + \
                self.parameters.synthetic_curve["xc"].format(7, 3, "F") + \
                self.parameters.synthetic_curve["yh"].format(7, 3, "F") + \
                self.parameters.synthetic_curve["yc"].format(7, 3, "F") + \
                self.parameters.synthetic_curve["el3"].format(12, 4, "D") + \
                self.parameters.synthetic_curve["opsf"].format(11, 4, "D") + \
                self.parameters.synthetic_curve["zero"].format(8, 3, "F") + \
                self.parameters.synthetic_curve["factor"].format(8, 4, "F") + \
                self.parameters.synthetic_curve["wl"].format(10, 6, "F") + \
                self.parameters.synthetic_curve["aextinc"].format(8, 4, "F") + \
                self.parameters.synthetic_curve["calib"].format(12, 5, "D") + "\n"

        star1_line_profiles = ""
        star2_line_profiles = ""

        if mpage == 3:
            star1_line_profiles = self.parameters["binwm1"].format(11, 5, "D") + \
                                  self.parameters["sc1"].format(9, 4, "F") + \
                                  self.parameters["sl1"].format(9, 2, "F") + \
                                  self.parameters["nf1"].format(3, 0, "") + "\n"

            for line in self.parameters.star1_lines:
                star1_line_profiles = star1_line_profiles + \
                                      line["wll"].format(9, 6, "F") + \
                                      line["ewid"].format(12, 5, "D") + \
                                      line["depth"].format(10, 5, "F") + \
                                      line["kks"].format(5, 0, "") + "\n"

            star1_line_profiles = star1_line_profiles + "-1.\n"

            star2_line_profiles = self.parameters["binwm2"].format(11, 5, "D") + \
                                  self.parameters["sc2"].format(9, 4, "F") + \
                                  self.parameters["sl2"].format(9, 2, "F") + \
                                  self.parameters["nf2"].format(3, 0, "") + "\n"

            for line in self.parameters.star2_lines:
                star2_line_profiles = star2_line_profiles + \
                                      line["wll"].format(9, 6, "F") + \
                                      line["ewid"].format(12, 5, "D") + \
                                      line["depth"].format(10, 5, "F") + \
                                      line["kks"].format(5, 0, "") + "\n"

            star2_line_profiles = star2_line_profiles + "-1.\n"

        star1_spots = ""
        star2_spots = ""

        for spot in self.parameters.star1_spots:
            star1_spots = star1_spots + \
                              spot["xlat"].format(9, 5, "F") + \
                              spot["xlong"].format(9, 5, "F") + \
                              spot["radsp"].format(9, 5, "F") + \
                              spot["temsp"].format(9, 5, "F") + \
                              spot["tstart"].format(14, 5, "F") + \
                              spot["tmax1"].format(14, 5, "F") + \
                              spot["tmax2"].format(14, 5, "F") + \
                              spot["tfinal"].format(14, 5, "F") + "\n"

        for spot in self.parameters.star2_spots:
            star2_spots = star2_spots + \
                              spot["xlat"].format(9, 5, "F") + \
                              spot["xlong"].format(9, 5, "F") + \
                              spot["radsp"].format(9, 5, "F") + \
                              spot["temsp"].format(9, 5, "F") + \
                              spot["tstart"].format(14, 5, "F") + \
                              spot["tmax1"].format(14, 5, "F") + \
                              spot["tmax2"].format(14, 5, "F") + \
                              spot["tfinal"].format(14, 5, "F") + "\n"

        eclipse_data = ""
        if mpage == 6 and ktstep == 0:

            if len(self.parameters.data["eclipse_times"]) == 0:
                raise ValueError("Eclipse times must be provided for mpage: 6, ktstep: 0")

            jd_formatter = _ParameterContainer.Parameter("jd", float)
            type_formatter = _ParameterContainer.Parameter("type", int)

            jd_list, type_list = self.parameters.data["eclipse_times"]

            for data in zip(jd_list, type_list):
                jd_formatter.set(data[0])
                type_formatter.set(data[1])

                eclipse_data = eclipse_data + jd_formatter.format(14, 5, "F") + type_formatter.format(6, 0, "") + "\n"

            eclipse_data = eclipse_data + "-10000.\n"

        self._output = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + \
                star1_line_profiles + star2_line_profiles + \
                star1_spots + \
                "300.00000  0.00000  0.00000  0.00000       0.00000       0.00000       0.00000       0.00000\n" + \
                star2_spots + \
                "300.00000  0.00000  0.00000  0.00000       0.00000       0.00000       0.00000       0.00000\n" + \
                "150.\n" + \
                eclipse_data + \
                "9"

    def input_synthetic_light_curve(self):
        self._format_input(1)

    def input_synthetic_velocity_curve(self):
        self._format_input(2)

    def input_spectral_lines(self):
        self._format_input(3)

    def input_component_dimensions(self):
        self._format_input(4)

    def input_star_positions(self):
        self._format_input(5)

    def input_etv(self):
        self._format_input(6)

    def input_conjunction(self, ktstep):
        self._format_input(6, ktstep=ktstep)

    def __str__(self):
        return self._output


class DCInput(_WDInput):
    def __init__(self, container):
        _WDInput.__init__(self, container)
