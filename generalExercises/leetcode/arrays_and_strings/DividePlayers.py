from tests import TestExecutor


def dividePlayers(skill: list[int]) -> int:
    skill_frequency = [0] * 1001
    total_skill = sum(skill)
    for i in range(len(skill)):
        skill_frequency[skill[i]] += 1

    if total_skill % (len(skill) // 2) != 0:
        return -1

    target_team_skill = total_skill // (len(skill) // 2)
    chemistry_team = 0
    for i in range(len(skill)):
        partner_skill = target_team_skill - skill[i]
        if skill_frequency[partner_skill] == 0:
            return -1

        skill_frequency[partner_skill] -= 1
        chemistry_team += partner_skill * skill[i]

    return chemistry_team // 2


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[3, 2, 5, 1, 3, 4]],
        [[3, 4]],
        [[1, 1, 2, 3]]
    ], [
        22,
        12,
        -1
    ],
        dividePlayers
    )
