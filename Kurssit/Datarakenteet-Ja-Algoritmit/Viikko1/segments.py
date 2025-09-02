def find_segments(data):
    segments = []
    segment_letter = data[0]
    segment_length = 0

    for letter in data:
        if letter == segment_letter:
            segment_length += 1
        else:
            segments.append((segment_length, segment_letter))
            segment_letter = letter
            segment_length = 1

    segments.append((segment_length, segment_letter))
    return segments

