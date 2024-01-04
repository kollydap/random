import multiprocessing


def worker(task_queue, result_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break
        result = process_task(task)
        result_queue.put(result)




def process_task(task):

    task = task + str(90)
    return task


def distribute_task(tasks: list, num_processes: int):
    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    for task in tasks:
        task_queue.put(task)

    for _ in range(num_processes):
        task_queue.put(None)

    processes = [
        multiprocessing.Process(target=worker, args=(task_queue, result_queue))
        for _ in range(num_processes)
    ]
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()

    results = []
    while not result_queue.empty():
        result = result_queue.get()
        results.append(result)

    return results


tasks_to_be_processed = ["TAsk1", "kola", "joseph"]

num_processes = 3

results = distribute_task(tasks=tasks_to_be_processed, num_processes=num_processes)

for result in results:
    print(result)
