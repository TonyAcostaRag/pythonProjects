def countingValleys(steps, path):
    # 1. Identify the direction of the first step.
    altitude = 0
    total_valleys = 0

    # 2. After having the start of the step direction, within a loop adds +1 when
    # reaching the sea level again only for valleys. And return the number of valleys traversed.
    for step in path:

        if step == 'U':
            altitude += 1
            if altitude == 0:
                total_valleys += 1
        elif step == 'D':
            altitude -= 1

    return total_valleys


print(countingValleys(8, ['U','D','D','D','U','D','U','U']))
print(countingValleys(12, ['D','D','U','U','D','D','U','D','U','U','U','D']))
