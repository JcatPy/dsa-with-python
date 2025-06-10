import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    end_times = []
    rooms = 0

    intervals.sort(key=lambda x: x[0])

    for i in intervals:
        while end_times and end_times[0] <= i[0]:
            heapq.heappop(end_times)
        heapq.heappush(end_times, i[1])
        rooms = max(rooms, len(end_times))

    return rooms
