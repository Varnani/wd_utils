from wd_utils import wd_io
from resources import kic7385478_lc_params
from matplotlib import pyplot

"""
An example file for using LC functions of wd_utils.
Limited documentation is available in the source code.
Also, be sure to check .py files inside the resources folder.
"""

lc_params = kic7385478_lc_params.load()

# add spot
lc_params.add_spot(1, 1.71127, 1.61975, 0.22156, 1.02222, 50800, 50900, 50930, 51100)

# set synthetic curve
lc_params.set_synthetic_curve(26, 10.5, 1, 0.5, 0.5, 0, 0, 0, 0, 8, 1, 0.592, 0, 0)

# add spectral lines
lc_params.add_spectral_line(2, 0.55, 0.00001, 0.5, 0)

# create WDIO object with parameter container and relevant paths
lcio = wd_io.LCIO(lc_params, wd_path="/home/varnani/WD",
                             lc_binary_name="lc_precompiled_linux")

# fill input for synthetic light curve
lcio.fill_for_synthetic_light_curve()

# save the input
lcio.save()

# call the WD binary
lcio.run()

# read the results for synthetic light curve
results = lcio.read_synthetic_light_curve()

# also, these functions can be chained like so:
# results = lcio.fill_for_synthetic_light_curve().save().run().read_synthetic_light_curve()

# plot results
pyplot.plot(results[1], results[4], "ko", markersize=2)
pyplot.show()
