from numpy.random import default_rng
import math
import matplotlib.pyplot as plt
import statistics as stats


def logNormalMuSigmaFromMeanStdev(var, mean):
    sigma = (math.log(var ** 2 / mean ** 2 + 1)) ** (1 / 2)
    mu = math.log(mean) - 0.5 * sigma ** 2
    return mu, sigma


rng = default_rng()

advancements = 0

w_i = []
t_i = [0]

model_1 = [0]
a_i = []

model_2 = [0]
r_i = []

model_3 = [0]
delta_y = []
r = 1. / 365.

w = 0

all_AI_w_mean = 0.848
all_AI_w_stdev = .965
all_AI_w_mu, all_AI_w_sigma = logNormalMuSigmaFromMeanStdev(all_AI_w_mean, all_AI_w_stdev)

all_AI_a_mean = 1.379
all_AI_a_stdev = 3.933
all_AI_a_mu, all_AI_a_sigma = logNormalMuSigmaFromMeanStdev(all_AI_a_mean, all_AI_a_stdev)

# while advancements < 20:
#     w += 1
#     flip = rng.random() < .004
#     if flip:
#         advancements += 1
#         w_i.append(w)
#         w = 0

for i in range(20):
    w = rng.lognormal(all_AI_w_mu, all_AI_w_sigma)
    w_i.append(w)

for i in w_i:
    t_i.append(t_i[-1] + i)

    a = rng.lognormal(all_AI_a_mu, all_AI_a_sigma)
    a_i.append(a)
    model_1.append(model_1[-1] + a)

    r_2 = math.tan(max(min(rng.normal(math.pi / 4, math.pi / 12), .99 * math.pi / 2), 0.01 * math.pi / 2))
    r_i.append(r_2)
    model_2.append(model_2[-1] + r_2 * i)

    no_y = True
    while no_y:
        dy = rng.normal(0, 0.05, 1)
        y_3 = model_3[-1] + r * t_i[-1] + dy
        if y_3 > model_3[-1]:
            no_y = False
            model_3.append(y_3)
