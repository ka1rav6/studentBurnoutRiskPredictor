from pymongo import MongoClient
import pprint
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
db = client["student_burnout"]
collection = db["studentDetails"]

"""
'_id': ObjectId('69d2540a14b1b2bed9b8bdae'),
  'academic_performance': 69.1419153525,
  'academic_year': 4,
  'age': 24,
  'anxiety_score': 1.1025582818,
  'burnout_score': 0.0,
  'depression_score': 0.0,
  'dropout_risk': 0.0,
  'exam_pressure': 4.0109450566,
  'family_expectation': 5.9347794488,
  'financial_stress': 4.3828198246,
  'gender': 'Male',
  'internet_usage': 5.1349028034,
  'mental_health_index': 8.927394423,
  'physical_activity': 4.0265036126,
  'risk_level': 'Low',
  'screen_time': 4.9031463065,
  'sleep_hours': 5.9893242425,
  'social_support': 4.5129207754,
  'stress_level': 1.8545952311,
  'study_hours_per_day': 2.1865693152}

"""
collection.update_many(
    {},
    [
        {
            "$set": {
                "risk_level": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$risk_level", "Low"]}, "then": 0},
                            {"case": {"$eq": ["$risk_level", "Medium"]}, "then": 1},
                            {"case": {"$eq": ["$risk_level", "High"]}, "then": 2},
                        ],
                        "default": "$risk_level"
                    }
                }
            }
        }
    ]
)

pprint.pprint(list(collection.find())[:5])