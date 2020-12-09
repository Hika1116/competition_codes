
# 選択ソート
# def sort_practice(list):
#     sorted_list = []
#     for i in range(len(list)):
#         sorted_list.append(min(list))
#         list.remove(min(list))
#     return sorted_list


def select_sort(arr):
    for i in range(0, len(arr) -1):
        select_min(arr, i)

def select_min(arr, i):
    min = i
    for j in range(i + 1, len(arr)):
        if arr[min] < arr[j]:
            min = j

    # 最小要素と先頭要素を交換
    arr[i], arr[min] = arr[min], arr[i]


list = [4, 3, 12, 45, 10, 44, 7, 5]

# print(sort_practice(list))
