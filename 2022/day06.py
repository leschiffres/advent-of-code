# part 1
def get_start_of_packet(message, distinct_characters):
    i = distinct_characters
    while i < len(message):
        s = message[i-distinct_characters: i]
        i = i + 1
        if len(set(s)) == distinct_characters:
            break
    return i - 1

filename = "input/day06.txt"
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(get_start_of_packet(line, 4))
        print(get_start_of_packet(line, 14))

# lines = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb', 'bvwbjplbgvbhsrlpgdmjqwftvncz', 'nppdvjthqldpwncqszvftbrmjlhg', 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
# for line in lines:
#     print(get_start_of_packet(line, 4))
#     print(get_start_of_packet(line, 14))