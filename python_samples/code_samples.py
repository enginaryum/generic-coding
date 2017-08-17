# from __future__ import print_function

class1 = [20, 10, 90, 10, 80, 70]
class2 = [50, 40, 90, 30, 80, 70]
class3 = [70, 90, 90, 80, 80, 70]

all_exam_results = [class1, class2, class3]

all_exam_results_dict = {
  'class1': [20, 10, 90, 10, 80, 70],
  'class2': [50, 40, 90, 30, 80, 70],
  'class3': [70, 90, 90, 80, 80, 70],
}


# 1. Calculate Mean - function definition -

# def calculate_mean(list):
#   total = 0
#   for number in list:
#     total += number
#   return total / len(list)
#
# calculate_mean(class1)
# calculate_mean(class2)
# calculate_mean(class3)
#
# results = []
# for _class in all_exam_results:
#   results.append(calculate_mean(_class))
# print results


# 2. Calculate Mean for each classes - map function -

# print map(calculate_mean, all_exam_results)


# 3. Calculate mean - lambda function -

# print map(lambda x: calculate_mean(x), all_exam_results)


# 4. Calculate mean - reduce function -

# def calculate_mean(_list):
  #return reduce(lambda x, y: x + y, _list) / len(_list)


# 5. Calculate Mean - lambda function -

# calculate_mean = lambda list: reduce(lambda x,y: x+y, list) / len(list)
#
# print calculate_mean(class1)


# 6. Calculate mean for each classes - list format -
# print map(calculate_mean, all_exam_results)


# 7. Calculate mean for each classes - dict format -

# print map(lambda (k,v) : {k: calculate_mean(v)}, all_exam_results_dict.iteritems())


# 8. Calculate mean for each class in dict and return new dict with mean and notes

# print map(lambda (k, v) : {k: {'mean': calculate_mean(v), 'notes': v}}, all_exam_results_dict.iteritems())
# print all_exam_results_dict


# 9 - Calculate mean for each classes in dict and return same dict with new keys
# map(lambda (k, v) : all_exam_results_dict.update({k : {'mean': calculate_mean(v), 'notes': v}}), all_exam_results_dict.iteritems())
#
# print all_exam_results_dict



