from enum import Enum


class AssessmentStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PARTIAL = "PARTIAL"


class RiskLevel(str, Enum):
    EXCELLENT = "EXCELLENT"
    LOW = "LOW RISK"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class IndustryType(str, Enum):
    MANUFACTURING = "MANUFACTURING"


class LoanType(str, Enum):
    WORKING_CAPITAL = "WORKING_CAPITAL"
    TERM_LOAN = "TERM_LOAN"
    MACHINERY = "MACHINERY"
    EXPANSION = "EXPANSION"
    OTHER = "OTHER"


class CollateralType(str, Enum):
    LAND = "LAND"
    BUILDING = "BUILDING"
    MACHINERY = "MACHINERY"
    VEHICLE = "VEHICLE"
    INVENTORY = "INVENTORY"
    NONE = "NONE"

class AlternateDataStatus(str, Enum):
    """
    Qualitative status for alternate data cards.
    """
    EXCELLENT = "Excellent"
    GOOD = "Good"
    AVERAGE = "Average"
    NEEDS_IMPROVEMENT = "Needs Improvement"