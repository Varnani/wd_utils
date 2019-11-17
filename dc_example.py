from wd_utils import wd_io, wd_constants
from resources import kic7385478_dc_params
import numpy

"""
An example file for using DC functions of wd_utils.
Limited documentation is available in the source code.
Also, be sure to check .py files inside the resources folder.
"""

dc_params = kic7385478_dc_params.load()

# add spots
dc_params.add_spot(1, 1.71127, 1.61975, 0.22156, 1.02222, 50800, 50900, 50930, 51100)

# add observations
lc = numpy.loadtxt("resources/kic7385478_phase_intensity.dat", unpack=True)
vr1 = numpy.loadtxt("resources/kic7385478_vr1.dat", unpack=True)
vr2 = numpy.loadtxt("resources/kic7385478_vr2.dat", unpack=True)

# light curve
dc_params.add_light_curve(26, 10.732025, 1, 0.462, 0.344, 0, 0, 0, 0.000178, 1, 0, 0, 0, 0,
                          lc[0], lc[1], lc[2], wla=0.592)

# velocity curves
dc_params.add_velocity_curve(1, 9, 1, 0.592, vr1[0], vr1[1], vr1[2])
dc_params.add_velocity_curve(2, 25, 1, 0.592, vr2[0], vr2[1], vr2[2])

# adjust keeps
dc_params.keeps["xincl"] = 0
dc_params.keeps["pshift"] = 0
dc_params.keeps["tavc"] = 0
dc_params.keeps["hla"] = 0
dc_params.keeps["phsv"] = 0

# create WDIO object with parameter container and relevant paths
dcio = wd_io.DCIO(dc_params, wd_path="/home/varnani/WD",
                             dc_binary_name="dc_precompiled_linux")

# fill input for solution
dcio.fill_for_solution()

# save the input
dcio.save()

# call the wd binary
dcio.run()

# read solution results
results = dcio.read_results()

# also, these functions can be chained like so:
# results = dcio.fill_for_solution().save().run().read_results()

# print results. check read_results() source code for output shape information
print("Solution results:\n-----------")
for result in results:
    output = " " + wd_constants.DC_KEEPS_ID_NAME_DICT[result[0]] + ":\n" \
             "  Input: " + str(result[2]) + "\n" \
             "  Correction: " + str(result[3]) + "\n" \
             "  Output: " + str(result[4])

    if result[1] != 0.0:
        output = output + "\n  (for curve #" + str(int(result[1])) + ")"

    print(output)
