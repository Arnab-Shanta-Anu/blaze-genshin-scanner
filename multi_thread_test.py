# import time
# import threading

# def captureScreen(numImage):
#     threads = []
#     for i in range(numImage):
#         print(f"capturing image... {i}")
#         time.sleep(2)
#         thread = threading.Thread(target=processImage, args=(i,))
#         thread.start()
#         threads.append(thread)

#         for thread in threads:
#             thread.join()

# def processImage(i):
#     print(f"processing image... {i}")
#     time.sleep(5)

# def main():
#     startTime = time.time()
#     captureScreen(10)
#     endTime = time.time()
#     print(f"execution time = {endTime-startTime} sec")


# if __name__ == "__main__":
#     main()

import asyncio
import time

async def capture_screen(num_image):
    tasks = []
    for i in range(num_image):
        print(f"capturing image... {i}")
        await asyncio.sleep(2)  # Simulates capturing time
        task = asyncio.create_task(process_image(i))
        tasks.append(task)

    await asyncio.gather(*tasks)  # Wait for all tasks to finish

async def process_image(i):
    print(f"processing image... {i}")
    await asyncio.sleep(5)  # Simulates processing time

async def main():
    start_time = time.time()
    await capture_screen(10)
    end_time = time.time()
    print(f"execution time = {end_time - start_time} sec")

if __name__ == "__main__":
    asyncio.run(main())
