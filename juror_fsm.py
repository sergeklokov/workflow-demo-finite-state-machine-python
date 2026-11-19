from enum import Enum


class JurorState(Enum):
    SUMMONED = "Summoned"
    VOIR_DIRE = "Voir Dire"
    SELECTED = "Selected"
    SWORN_IN = "Sworn In"
    HEARING_EVIDENCE = "Hearing Evidence"
    DELIBERATING = "Deliberating"
    VERDICT_REACHED = "Verdict Reached"
    DISCHARGED = "Discharged"


class JurorFSM:
    TRANSITIONS = {
        (JurorState.SUMMONED, "begin_voir_dire"): JurorState.VOIR_DIRE,
        (JurorState.VOIR_DIRE, "selected"): JurorState.SELECTED,
        (JurorState.SELECTED, "swear_in"): JurorState.SWORN_IN,
        (JurorState.SWORN_IN, "trial_begins"): JurorState.HEARING_EVIDENCE,
        (JurorState.HEARING_EVIDENCE, "begin_deliberation"): JurorState.DELIBERATING,
        (JurorState.DELIBERATING, "reach_verdict"): JurorState.VERDICT_REACHED,
        (JurorState.VERDICT_REACHED, "discharge"): JurorState.DISCHARGED,

        # Allows a juror to be summoned again in the future
        (JurorState.DISCHARGED, "summon_again"): JurorState.SUMMONED,
    }

    def __init__(self):
        self.state = JurorState.SUMMONED

    def process_event(self, event: str):
        transition = (self.state, event)

        if transition not in self.TRANSITIONS:
            raise ValueError(
                f"Invalid transition: {self.state.value} -> {event}"
            )

        previous_state = self.state
        self.state = self.TRANSITIONS[transition]

        print(
            f"[EVENT] {event:<20} | {previous_state.value:>20} "
            f"-> {self.state.value}"
        )

    def current_state(self):
        return self.state.value


def main():
    juror = JurorFSM()

    print(f"Initial State: {juror.current_state()}\n")

    events = [
        "begin_voir_dire",
        "selected",
        "swear_in",
        "trial_begins",
        "begin_deliberation",
        "reach_verdict",
        "discharge",
        "summon_again"
    ]

    for event in events:
        juror.process_event(event)

    print(f"Current State: {juror.current_state()}")


if __name__ == "__main__":
    main()