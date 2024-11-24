# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(str1,str2,sep = ","):
    """Разбиваем по sep, преобразуем во множество, пересекаем множества,
    преобразуем в список, сортируем"""
    return sorted(list(set(str1.split(sep)) & set(str2.split(sep))))

print(find_common_participants(participants_first_group,participants_second_group, sep = "|"))
