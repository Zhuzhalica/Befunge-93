from structures.program import Program
from structures.debug import debug_command_state
from system.console_io import output_current_program_info, \
    ask_new_debug_command, print_program_execution_statistic, \
    output_debug_command_mistake


def program_execution(program: Program) -> None:
    """Executes the transmitted program until its completion
    and outputs the result"""
    program.start()

    while not program.PE:
        if program.debug.is_set:
            debug(program)
        else:
            program.execute_command_with_stat_and_move()
    else:
        program.end()
        print_program_execution_statistic(program)


def debug(program: Program) -> None:
    """Handles program execution in debug mode"""
    if program.current_command.command == ' ' and \
            not program.debug.go_to_point():
        program.execute_command_with_stat_and_move()

    elif program.debug.go_to_breakpoint() and \
            program.IP != program.debug.breakpoint_to_go():
        program.execute_command_with_stat_and_move()

    elif program.debug.go_to_next_breakpoint() and \
            program.IP not in program.debug.get_breakpoints():
        program.execute_command_with_stat_and_move()

    elif program.debug.go_to_point() and program.IP != program.debug.point():
        program.execute_command_with_stat_and_move()

    else:
        if program.debug.go_to_point():
            program.debug.go_to_point_remove()
        if program.debug.go_to_next_breakpoint():
            program.debug.go_to_next_breakpoint_remove()
        if program.debug.go_to_breakpoint():
            program.debug.go_to_breakpoint_remove()

        program.execute_command()
        program.add_step()

        output_current_program_info(program)

        state = debug_command_state.WAIT_NEW_ASK
        while state != debug_command_state.COMPLETE:
            answer = ask_new_debug_command(program)
            state = program.debug.check_answer(answer, program.IP)
            if state == debug_command_state.NOT_FATAL_INCORRECT_COMMAND:
                output_debug_command_mistake(
                    program.debug.last_mistake_message)

        program.move_IP()
