from concurrent.futures import as_completed, ProcessPoolExecutor
from tqdm import tqdm


def process_param(param):
    return param


params = range(100000)
executor = ProcessPoolExecutor(20)
jobs = [executor.submit(process_param, param) for param in params]

results = []
for job in tqdm(as_completed(jobs), total=len(jobs)):
    results.append(job.result())
