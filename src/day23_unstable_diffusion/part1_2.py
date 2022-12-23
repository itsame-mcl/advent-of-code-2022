from src.day23_unstable_diffusion.elves import ElvesController


def do_rounds_and_compute_empty_tiles(path, rounds=10):
    controller = ElvesController(path)
    for _ in range(rounds):
        controller.do_round()
    return controller.compute_empty_tiles()


def do_complete_simulation_and_compute_rounds(path):
    controller = ElvesController(path)
    simulation_completed = False
    rounds = 0
    while not simulation_completed:
        initial_positions = {elf.position for elf in controller.elves}
        controller.do_round()
        final_positions = {elf.position for elf in controller.elves}
        rounds += 1
        if len(initial_positions.symmetric_difference(final_positions)) == 0:
            simulation_completed = True
    return rounds
