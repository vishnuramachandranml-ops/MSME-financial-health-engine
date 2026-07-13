from enum import Enum


class MonitoringFrequency(str, Enum):
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    HALF_YEARLY = "HALF YEARLY"
    YEARLY = "YEARLY"