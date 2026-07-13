
"""
Swagger example payloads for AssessmentRequest.
These examples are intentionally realistic and can be reused by:
- Swagger/OpenAPI
- Postman
- UI Demo
- Unit Tests
"""

def _base():
    return {
        "metadata": {
            "request_id": "REQ-001",
            "source_system": "Swagger",
            "model_version": "1.0",
        },
        "business_profile": {
            "business_id": "MSME001",
            "business_name": "",
            "industry": "MANUFACTURING",
            "business_type": "Private Limited",
            "msme_registered": True,
            "udyam_registration_number": "UDYAM-XX-1234567",
            "business_age_years": 10,
            "employee_count": 50,
            "annual_turnover": 25000000,
            "location": "Coimbatore",
        },
        "cashflow": {
            "monthly_revenue": {"values": [1000000,1050000,1100000,1150000,1200000,1250000]},
            "monthly_expenses": {"values": [750000,780000,800000,820000,850000,870000]},
            "average_collection_days": 45,
            "average_supplier_payment_days": 40,
        },
        "operations": {
            "monthly_sales_orders":{"values":[950000,1000000,1050000,1100000,1150000,1200000]},
            "monthly_purchase_orders":{"values":[700000,720000,740000,760000,780000,800000]},
            "vendor_count":40,
            "customer_count":150,
            "repeat_customer_ratio":0.82,
            "capacity_utilization":0.88,
            "inventory_turnover":8,
            "order_fulfillment_rate":0.98,
            "employee_productivity":400000,
        },
        "alternate_data":{
            "gst_registered":True,
            "gst_filing_rate":1.0,
            "gst_turnover":24500000,
            "upi_transaction_count":6500,
            "upi_transaction_volume":9000000,
            "average_bank_balance":2500000,
            "digital_payment_ratio":0.85,
            "positive_bank_statement_months":12,
            "online_rating":4.7,
            "electricity_units":{"values":[10000,10100,10200,10400,10500,10700]},
            "fuel_expense":{"values":[150000,152000,154000,156000,158000,160000]},
        },
        "compliance":{
            "gst_registered":True,
            "gst_return_filing_rate":1.0,
            "itr_filed_last_3_years":True,
            "epfo_registered":True,
            "epfo_compliance_rate":1.0,
            "tax_payment_delay_days":0,
            "statutory_dues_pending":False,
            "regulatory_notices":0,
        },
        "financial_position":{
            "total_assets":18000000,
            "current_assets":9000000,
            "fixed_assets":9000000,
            "cash_and_bank":2500000,
            "inventory":2800000,
            "accounts_receivable":1800000,
            "total_liabilities":7000000,
            "current_liabilities":4000000,
            "long_term_debt":2000000,
            "net_worth":11000000,
            "book_value":11000000,
            "working_capital":5000000,
        },
        "loan_request":{
            "loan_type":"WORKING_CAPITAL",
            "requested_amount":3000000,
            "loan_tenure_months":36,
            "loan_purpose":"Working capital expansion",
            "existing_loan_amount":1000000,
            "existing_emi":45000,
            "collateral":{
                "available":True,
                "collateral_type":"LAND",
                "estimated_value":10000000,
            },
        },
    }

HEALTHY_MANUFACTURING=_base()
HEALTHY_MANUFACTURING["business_profile"]["business_name"]="ABC Precision Components"

MEDIUM_RISK_MANUFACTURING=_base()
MEDIUM_RISK_MANUFACTURING["metadata"]["request_id"]="REQ-002"
MEDIUM_RISK_MANUFACTURING["business_profile"]["business_name"]="Metro Engineering"
MEDIUM_RISK_MANUFACTURING["cashflow"]["average_collection_days"]=90
MEDIUM_RISK_MANUFACTURING["cashflow"]["monthly_expenses"]["values"]=[850000,880000,910000,940000,980000,1020000]
MEDIUM_RISK_MANUFACTURING["financial_position"]["current_assets"]=5000000
MEDIUM_RISK_MANUFACTURING["financial_position"]["current_liabilities"]=4500000

NEW_TO_CREDIT=_base()
NEW_TO_CREDIT["metadata"]["request_id"]="REQ-003"
NEW_TO_CREDIT["business_profile"]["business_name"]="NextGen Fabrication"
NEW_TO_CREDIT["business_profile"]["business_age_years"]=2
NEW_TO_CREDIT["loan_request"]["existing_loan_amount"]=0
NEW_TO_CREDIT["loan_request"]["existing_emi"]=0
NEW_TO_CREDIT["alternate_data"]["digital_payment_ratio"]=0.94

HIGH_RISK_MANUFACTURING=_base()
HIGH_RISK_MANUFACTURING["metadata"]["request_id"]="REQ-004"
HIGH_RISK_MANUFACTURING["business_profile"]["business_name"]="XYZ Castings"
HIGH_RISK_MANUFACTURING["cashflow"]["monthly_revenue"]["values"]=[1200000,1150000,1100000,1050000,1000000,950000]
HIGH_RISK_MANUFACTURING["cashflow"]["monthly_expenses"]["values"]=[1300000,1280000,1260000,1240000,1220000,1200000]
HIGH_RISK_MANUFACTURING["cashflow"]["average_collection_days"]=165
HIGH_RISK_MANUFACTURING["compliance"]["gst_return_filing_rate"]=0.72
HIGH_RISK_MANUFACTURING["compliance"]["epfo_compliance_rate"]=0.68
HIGH_RISK_MANUFACTURING["compliance"]["tax_payment_delay_days"]=48
HIGH_RISK_MANUFACTURING["compliance"]["regulatory_notices"]=3
HIGH_RISK_MANUFACTURING["financial_position"]["current_assets"]=2500000
HIGH_RISK_MANUFACTURING["financial_position"]["current_liabilities"]=5000000
HIGH_RISK_MANUFACTURING["alternate_data"]["average_bank_balance"]=80000
HIGH_RISK_MANUFACTURING["alternate_data"]["positive_bank_statement_months"]=4


WHAT_IF_CASHFLOW = {
    "original_request": HEALTHY_MANUFACTURING,
    "scenario": {
        "cashflow": {
            "revenue_growth": 35,
            "collection_days": 45,
        }
    },
}

WHAT_IF_FINANCIAL_POSITION = {
    "original_request": HEALTHY_MANUFACTURING,
    "scenario": {
        "financial_position": {
            "current_ratio": 2.0,
            "working_capital": 7500000,
        }
    },
}

WHAT_IF_COMPLIANCE = {
    "original_request": MEDIUM_RISK_MANUFACTURING,
    "scenario": {
        "compliance": {
            "gst_filing_rate": 100,
            "epfo_compliance_rate": 100,
            "tax_delay_days": 0,
        }
    },
}

WHAT_IF_ALL = {
    "original_request": MEDIUM_RISK_MANUFACTURING,
    "scenario": {
        "cashflow": {
            "revenue_growth": 35,
            "collection_days": 45,
        },
        "financial_position": {
            "current_ratio": 2.0,
            "working_capital": 7500000,
        },
        "operations": {
            "capacity_utilization": 95,
        },
        "compliance": {
            "gst_filing_rate": 100,
            "epfo_compliance_rate": 100,
        },
        "alternate_data": {
            "digital_payment_ratio": 95,
            "average_bank_balance": 5000000,
        },
    },
}