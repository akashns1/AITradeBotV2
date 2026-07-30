from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConfirmationAnalysis:
    confirmed: bool