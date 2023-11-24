from litter_box import state, rotate, sense
from litter_box.settings import cycle_eating_time, cycle_overshoot_time


def do_cycle():
    if state.current_state == state.WAITING_TO_CYCLE and state.ok_to_move():
        state.current_state = state.SIFTING
    if state.current_state == state.SIFTING:
        rotate.counter_clock_wise()
        if sense.hall_sensor_triggered():
            state.current_state = state.EATING_SHIT
            rotate.stop()
            state.start_delay()
    if state.current_state == state.EATING_SHIT and state.delay_over(cycle_eating_time):
        state.current_state = state.MOVING_BACK
    if state.current_state == state.MOVING_BACK:
        rotate.clock_wise()
        if sense.hall_sensor_triggered():
            state.current_state = state.LEVELING_LITTER
            state.start_delay()
    if state.current_state == state.LEVELING_LITTER:
        rotate.clock_wise()
        if state.delay_over(cycle_overshoot_time):
            state.current_state = state.LEVELING_GLOBE
    if state.current_state == state.LEVELING_GLOBE:
        rotate.counter_clock_wise()
        if sense.hall_sensor_triggered():
            rotate.stop()
            state.current_state = state.IDLE
