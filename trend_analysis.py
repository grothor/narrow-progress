# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from taxonomy import *
from scales import *

import data.vision as vis
import data.awty as awty
import data.wer as wer
import data.stem as stem
import data.video_games as video_games
import data.strategy_games as strategy_games
import data.acoustics as acoustics
import data.generative as generative
import data.language as language
import time


total_data_points = 0
total_metrics = 0
all_gaps = []
all_scaled_advances = []
all_rates = []

metrics_by_trend_type = {
}

solved_metrics = open("solved_metrics.csv", "w")
forecasted_metrics = open("forecasted_metrics.csv", "w")
linear_data = open("linear_data.agr", "w")
metrics_summary = open("metrics_summary.csv", "w")

solved_metrics.write(
    "Metric\tState of the art date\textrapolated superhuman date\tdate surpassed humans\textrapolation error\n")
forecasted_metrics.write(
    "Metric\tState of the art date\textrapolated superhuman date\tdate surpassed humans\textrapolation error\n")
metrics_summary.write(f"Metric name\t"
                      f"Has target\t"
                      f"Total data points\t"
                      f"Data before target\t"
                      f"Data after target\t"
                      f"Data contains target\t"
                      f"Data contains nonsense\t"
                      f"Has extrapolation\t"
                      f"State of the art date\t"
                      f"Extrapolated date\t"
                      f"Superhuman date\t"
                      f"Extrapolated date"
                      f"\n")


def twoPointExtrapolation(start, finish, target, scale):
    if start["date"] >= finish["date"] or scale.improvement(start["value"], finish["value"]) <= 0:
        return None

    lin_start = scale.pseudolinear(start["value"])
    lin_finish = scale.pseudolinear(finish["value"])
    lin_target = scale.pseudolinear(target)

    if lin_target < lin_finish:
        return None
    elif lin_target == lin_finish:
        return finish["date"]
    else:
        return start["date"] + (finish["date"] - start["date"]) * (lin_target - lin_start) / (lin_finish - lin_start)


def getInterpDate(early_date, later_date, early_value, later_value, target):
    proportion = (target - early_value) / (later_value - early_value)
    return proportion * (later_date - early_date) + early_date


def interpSuperhumanDate(metric, target=None):
    date_just_before = date(1, 1, 1)
    date_just_after = None
    value_just_before = None

    if not target:
        target = metric.target

    if not target and not metric.target:
        return None

    for data_point in metric.measures:
        if data_point.value == target:
            return data_point.date
        elif metric.scale.improvement(target, data_point.value) > 0:
            if value_just_before == None:
                return data_point.date
            date_just_after = data_point.date
            return getInterpDate(date_just_before, date_just_after, value_just_before, data_point.value, target)
        else:
            date_just_before = data_point.date
            value_just_before = data_point.value

    return None


def getSuperhumanDate(eff_problem, alt_target=None):
    if alt_target:
        human_target = alt_target
    else:
        human_target = eff_problem.target
    if not human_target:
        return None
    eff_problem.getFrontier()
    for data_point in eff_problem.frontier:
        if eff_problem.scale.improvement(human_target, data_point["value"]) >= 0:
            return data_point

    return None


def getLastSubhumanDate(eff_problem, alt_target):
    if alt_target:
        human_target = alt_target
    else:
        human_target = eff_problem.target
    if not human_target:
        return None
    eff_problem.getFrontier()
    if eff_problem.frontier == []:
        return None
    last_data_point = {}
    for data_point in eff_problem.frontier:
        if eff_problem.scale.improvement(human_target, data_point["value"]) >= 0:
            if last_data_point == {}:
                return None
            return last_data_point
        else:
            last_data_point = data_point
    return last_data_point

# The following function was shamelessly stolen from stackoverflow user ninjagecko
def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = datetime.date(year=year, month=1, day=1)
    startOfNextYear = datetime.date(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction


def get_node(eff_problem, extrapolate=False, write_linear_data=False, verbose=False, skip_atari=False):
    global total_data_points
    global total_metrics
    global all_gaps
    global all_scaled_advances


    if eff_problem.subproblems:
        if verbose:
            print("{eff_problem} has subproblems:".format(eff_problem=eff_problem))
        for sub in eff_problem.subproblems:
            get_node(sub, extrapolate=extrapolate, write_linear_data=write_linear_data)
    if eff_problem.metrics:
        if verbose:
            print("{eff_problem} has metrics:".format(eff_problem=eff_problem))
        for metric in eff_problem.metrics:
            if skip_atari and metric.atari:
                continue
            if verbose:
                print(f"{total_metrics} {metric.name}")
            if extrapolate:
                extrapolation = getExtrapolation(metric)
                metric.extrapolation.update(extrapolation)

                n_data_points = metric.trend_type["total data points"]
                data_before_target = metric.trend_type["data before target"]
                data_after_target = metric.trend_type["data after target"]
                has_target = metric.trend_type["has target"]
                data_contains_target = metric.trend_type["data contains target"]
                data_contains_nonsense = metric.trend_type["data contains nonsense"]
                has_extrapolation = extrapolation["has extrapolation"]

                metrics_summary.write(f"{metric.name}\t"
                                      f"{has_target}\t"
                                      f"{n_data_points}\t"
                                      f"{data_before_target}\t"
                                      f"{data_after_target}\t"
                                      f"{data_contains_target}\t"
                                      f"{data_contains_nonsense}\t"
                                      f"{has_extrapolation}\t")
                if extrapolation["has extrapolation"]:
                    superhuman_date = extrapolation.get("superhuman date", None)
                    extrapolation_error = extrapolation.get("extrapolation error", None)
                    extrapolated_date = extrapolation.get("extrapolated date", None)
                    soa_date = metric.frontier[-1]["date"]
                    if extrapolation_error:
                        solved_metrics.write(
                            f"{metric.name}\t{soa_date}\t{extrapolated_date}\t{superhuman_date}\t{extrapolation_error.days}\n")

                        metrics_summary.write(
                            f"{soa_date}\t"
                            f"{extrapolated_date}\t"
                            f"{superhuman_date}\t"
                            f"{extrapolation_error.days}\n")
                    else:
                        forecasted_metrics.write(f"{metric.name}\t{soa_date}\t{extrapolated_date}\t\t\n")
                        metrics_summary.write(f"{soa_date}\t{extrapolated_date}\t\t\n")
                else:
                    metrics_summary.write(f"\t\t\t\t\n")

            if write_linear_data:
                if metric.target:
                    metric.getFrontier()
                    linear_data.write(f"# {metric.name}\n")
                    linear_data.write(f"@target G0.S{total_metrics}\n")
                    linear_target = metric.scale.pseudolinear(metric.target)
                    if metric.performance_floor:
                        linear_floor = metric.scale.pseudolinear(metric.performance_floor)
                    else:
                        linear_floor = None

                    not_first = False
                    last_date = 0
                    last_value = 0

                    for data_point in metric.frontier:
                        this_date = toYearFraction(data_point["date"])
                        if linear_floor:
                            this_value = 0
                            this_value = metric.scale.pseudolinear(data_point["value"]) - linear_floor
                            this_value = this_value/(linear_target - linear_floor)
                        elif linear_target > 0:
                            this_value = metric.scale.pseudolinear(data_point["value"])/linear_target
                        elif linear_target < 0:
                            this_value = metric.scale.pseudolinear(data_point["value"]) / (-1*linear_target) + 2
                        else:
                            this_value = metric.scale.pseudolinear(data_point["value"]) + 1

                        linear_data.write(f"{this_date} {this_value}\n")
                        metric.human_scale_frontier.append({"date": this_date, "value": this_value})
                        if not_first:
                            all_gaps.append(this_date - last_date)
                            all_scaled_advances.append(this_value - last_value)
                            if all_gaps[-1] != 0:
                                all_rates.append(all_scaled_advances[-1]/all_gaps[-1])
                            if all_rates[-1] <0:
                                print(f"{metric.name} has negative rate at {this_date} for {metric.scale}")
                        last_value = this_value
                        last_date = this_date
                        not_first = True
            for data_point in metric.measures:
                total_data_points += 1

            total_metrics += 1
    return total_data_points



def showFrontier(metric):
    metric.getFrontier()
    superhuman_date = getSuperhumanDate(metric)
    for item in metric.frontier:
        if superhuman_date["date"] == item["date"]:
            tag = "<<"
        else:
            tag = ""
        print("{date}, {value} {superhuman}".format(date=item["date"], value=item["value"], superhuman=tag))

def getTrendType(metric, alt_target=None):
    metric.getFrontier()
    trend_type = {}
    if alt_target:
        metric_target = alt_target
    else:
        metric_target = metric.target

    trend_type["total data points"] = len(metric.frontier)
    trend_type["data before target"] = 0
    trend_type["data after target"] = 0
    trend_type["data contains target"] = False
    trend_type["data contains nonsense"] = False

    if not metric_target:
        trend_type["has target"] = False
    else:
        trend_type["has target"] = True
        for data_point in metric.frontier:
            improvement = metric.scale.improvement(data_point["value"], metric_target)
            if improvement:
                if improvement > 0:
                    trend_type["data before target"] += 1
                elif improvement < 0:
                    trend_type["data after target"] += 1
                else:
                    trend_type["data contains target"] = True
                    trend_type["data after target"] += 1
            else:
                trend_type["data contains nonsense"] = True

    trend_type["can extrapolate"] = trend_type["data before target"] > 1

    return trend_type

def getExtrapolation(metric, alt_target=None):
    metric.getFrontier()
    extrapolation = {}
    if alt_target:
        metric_target = alt_target
    else:
        metric_target = metric.target

    trend_type = getTrendType(metric, metric_target)
    metric.trend_type.update(trend_type)

    if not trend_type["can extrapolate"]:
        return {"has extrapolation": False}
    else:
        extrapolation.update({"has extrapolation": True})

    metric_start = metric.frontier[0]
    metric_finish = metric.frontier[trend_type["data before target"] - 1]
    metric_scale = metric.scale

    metric_extrapolation = twoPointExtrapolation(metric_start, metric_finish, metric_target, metric_scale)
    extrapolation["extrapolated date"] = metric_extrapolation

    if metric_extrapolation:
        metric_superhuman = getSuperhumanDate(metric, metric_target)
        if metric_superhuman:
            metric_forecast_error = metric_superhuman["date"] - metric_extrapolation
            extrapolation["extrapolation error"] = metric_forecast_error
            extrapolation["superhuman date"] = metric_superhuman["date"]

    metric.extrapolation = extrapolation
    return extrapolation

all_problems = Problem("All problems")

for item in problems.values():
    if item.superproblems == []:
        if item != all_problems:
            all_problems.add_subproblem(item)
            # print(f"Adding {item.name} to {item.superproblems}")

import scrapers.atari

get_node(all_problems, extrapolate=True, write_linear_data=True)


# get_node(awty.vision, extrapolate=True, write_linear_data=True)
# get_node(wer.speech_recognition, extrapolate=False, write_linear_data=True)
# get_node(generative.image_generation, extrapolate=True, write_linear_data=True)
# get_node(generative.scene_generation, extrapolate=True, write_linear_data=True)
# get_node(language.modelling_english, extrapolate=True, write_linear_data=True)
# get_node(stem.read_stem_papers, extrapolate=True, write_linear_data=True)
# get_node(stem.solve_technical_problems, extrapolate=True, write_linear_data=True)
# get_node(strategy_games.abstract_strategy_games, extrapolate=True, write_linear_data=True)
# get_node(video_games.computer_games, extrapolate=True, write_linear_data=True)

# showFrontier(strategy_games.computer_chess)

solved_metrics.close()
forecasted_metrics.close()
linear_data.close()
metrics_summary.close()

# print(total_data_points)

# awty.cifar10.graph()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/