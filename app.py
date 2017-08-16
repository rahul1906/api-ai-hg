#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


text = r"""
{
  "TotalRecordsFound": 109,
  "CurrentPage": 1,
  "RowsReturned": 20,
  "HealthgradesInfo": {
    "HealthgradesLogoUrl": "https://pbhportal.healthgrades.com/Partners/public/images/hg/hglogo.png",
    "PBHealthgradesLogoUrl": "https://pbhportal.healthgrades.com/Partners/public/images/hg/pbhglogo-130.png",
    "HealthgradesUrl": "http://www.healthgrades.com",
    "AboutHealthgrades": "Healthgrades is a third party vendor that allows patients to share feedback on their experience with a doctor.",
    "AboutPes": "Patient satisfaction ratings are personal opinions. So before you choose this doctor, take into account the number of surveys they have and all aspects of their background—education, training, and specialized experience—to ensure that they are the right fit for you.",
    "PesDisclaimer": "This information is based on other patient’s subjective view of their experience and may not reflect the actual quality of care the provider gave that patient. These are not official medical reviews.",
    "AboutExperienceMatch": "The Healthgrades Experience Match calculates how closely a provider may meet your needs based on your search criteria. It includes the provider's specialty, education, board certification, background check and number of patient's treated.",
    "AboutBoardCertification": "Board Certification should be one of your top considerations when choosing a doctor. Board certification is an official recognition given to doctors who have met specific requirements set by national medical specialty boards in the United States. Board certification indicates that a doctor is highly qualified in the medical field in which he or she practices. A board-certified doctor is more likely than a non-board-certified doctor to have the most current skills and knowledge about how to treat your medical condition."
  },
  "Results": [
    {
      "Id": "2P2ST",
      "DemographicInfo": {
        "DisplayName": "Dr. Raja S. Mehdi, MD",
        "DisplayLastName": "Dr. Mehdi",
        "FirstName": "Raja",
        "LastName": "Mehdi",
        "MiddleName": "S",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-raja-mehdi-2p2st?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/P/2/2P2ST_w60h80_v6933.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/P/2/2P2ST_w90h120_v6933.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/P/2/2P2ST_w120h160_v6933.jpg"
          }
        ],
        "Gender": "M",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nTreating the whole person. Not only is it our mi"
        },
        "Payors": [
          "AETNA",
          "AMERIB",
          "ANTHEA",
          "ASSURH",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "FIRSTB",
          "GOLDER",
          "GOVERA",
          "HUMANA",
          "MEDAID",
          "MULTIP",
          "UNITHC",
          "WELLPT"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1366441743"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.0983,
          "Longitude": -115.24113,
          "LatLon": "36.0983,-115.24113"
        },
        "Practices": [
          {
            "PracticeGuid": "B3A7F984-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FCKM4",
            "PracticeName": "Hope Cancer Care Of Nevada",
            "PracticeUrl": "hopecancercareofnevada.com",
            "Addresses": [
              {
                "Address1": "6827 W Tropicana Ave Ste 110",
                "OfficeCode": "OORH3KC",
                "OfficeGuid": "B6A97C8A-9AEC-4B75-A6D3-CEE9C59E57AB",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89103",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89103",
                    "Coordinates": {
                      "Latitude": 36.0983,
                      "Longitude": -115.24113,
                      "LatLon": "36.0983,-115.24113"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 508-9128"
                ],
                "Fax": [
                  "(702) 302-4125"
                ],
                "IsPrimary": true
              },
              {
                "Address1": "8530 W Sunset Rd Ste 330",
                "OfficeCode": "F8PXS",
                "OfficeGuid": "CE800688-8943-E111-B3AF-B499BAA4D952",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89113",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89113",
                    "Coordinates": {
                      "Latitude": 36.07131,
                      "Longitude": -115.27766,
                      "LatLon": "36.07131,-115.27766"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 508-9128"
                ],
                "Fax": [
                  "(702) 302-4125"
                ]
              },
              {
                "Address1": "3599 S Eastern Ave",
                "OfficeCode": "OOVLYNF",
                "OfficeGuid": "D3410BCC-8623-4699-94B1-581BE4B9F5F1",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89169",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89169",
                    "Coordinates": {
                      "Latitude": 36.12414,
                      "Longitude": -115.11916,
                      "LatLon": "36.12414,-115.11916"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 508-9128"
                ],
                "Fax": [
                  "(702) 302-4125"
                ]
              },
              {
                "Address1": "2340 E Calvada Blvd Ste 7",
                "OfficeCode": "YX63LL",
                "OfficeGuid": "438EB435-FF23-E211-AA81-B499BAA4D952",
                "Location": {
                  "CityName": "Pahrump",
                  "CityAndState": "Pahrump, NV",
                  "CityStateZipBestMatch": "Pahrump, NV 89048",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89048",
                    "Coordinates": {
                      "Latitude": 36.19209,
                      "Longitude": -115.97222,
                      "LatLon": "36.19209,-115.97222"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 508-9128"
                ],
                "Fax": [
                  "(702) 302-4125"
                ]
              }
            ]
          }
        ],
        "City": [
          "Pahrump",
          "Las Vegas"
        ],
        "CityState": [
          "Pahrump, NV",
          "Las Vegas, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "19",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Mehdi's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Medical Oncology",
          "Oncology",
          "Breast Oncology",
          "Neoplastic Diseases",
          "Gastrointestinal Oncology",
          "Geriatric Oncology",
          "Internal Medicine"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Medical Oncology",
          "PracticingSpecialityCode": "PS456",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Medical Oncology Specialist",
          "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS456",
          "Value": "Medical Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS412",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Breast Oncology",
            "PracticingSpecialityCode": "PS116",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Breast Oncology Specialist",
            "PracticingSpecialityNameIsts": "Breast Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Neoplastic Diseases",
            "PracticingSpecialityCode": "PS509",
            "PracticingSpecialityRank": 4,
            "PracticingSpecialityNameIst": "Neoplastic Disease Specialist",
            "PracticingSpecialityNameIsts": "Neoplastic Disease Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Gastrointestinal Oncology",
            "PracticingSpecialityCode": "PS1077",
            "PracticingSpecialityRank": 5,
            "PracticingSpecialityNameIst": "Gastrointestinal Oncology Specialist",
            "PracticingSpecialityNameIsts": "Gastrointestinal Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Geriatric Oncology",
            "PracticingSpecialityCode": "PS1078",
            "PracticingSpecialityRank": 6,
            "PracticingSpecialityNameIst": "Geriatric Oncology Specialist",
            "PracticingSpecialityNameIsts": "Geriatric Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Internal Medicine",
            "PracticingSpecialityCode": "PS412",
            "PracticingSpecialityRank": 7,
            "PracticingSpecialityNameIst": "Internist",
            "PracticingSpecialityNameIsts": "Internists",
            "RollupPracticingSpecialityCode": "PS412"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Breast Oncology",
          "Gastrointestinal Oncology",
          "Geriatric Oncology",
          "Internal Medicine",
          "Medical Oncology",
          "Neoplastic Diseases"
        ],
        "ProcedureIds": [
          229,
          1379,
          2145,
          2885,
          721,
          496,
          50998,
          1588
        ],
        "ConditionIds": [
          170,
          51067,
          14161,
          2286,
          51043,
          13000,
          163,
          51057,
          51091,
          19102,
          160,
          51106,
          51096,
          130,
          2454,
          18576,
          142,
          51116,
          150,
          75,
          17178,
          2406,
          1693,
          155,
          156,
          51055,
          51075,
          144,
          1395,
          11893,
          51089,
          2211,
          1765,
          2774,
          165,
          157,
          164,
          11414,
          1500,
          19830,
          17253,
          20066,
          50903,
          18366,
          4806,
          3759,
          11627,
          51122,
          52162,
          51941,
          126,
          4384,
          169,
          695,
          11392,
          1495,
          17191,
          52142,
          2904,
          8776,
          1410,
          15186,
          149,
          17704,
          120,
          4834,
          51340,
          52137,
          2800,
          1370,
          153
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 18,
        "SurveyOverallRatingPercent": 92,
        "SurveyOverallRatingScore": 4.6,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-raja-mehdi-2p2st/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "D6F15E",
          "F9D29F",
          "B2B744",
          "5FEB5C",
          "4D8ED7",
          "CBF7A2",
          "B5D7A6"
        ],
        "AffiliatedHospitalNames": [
          "Spring Valley Hospital Medical Center",
          "Summerlin Hospital Medical Center",
          "Desert Springs Hospital Medical Center",
          "Southern Hills Hospital and Medical Center",
          "Desert View Hospital",
          "St. Rose Dominican, San Martin Campus",
          "St. Rose Dominican, Siena Campus"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 97,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 11.3974733,
        "PesBoost": 0.21543,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.9775439,
        "HospitalQualityBoost": 9.532043,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 1,
      "Id": "XXRP5",
      "DemographicInfo": {
        "DisplayName": "Dr. Aaron T. Bowman, MD",
        "DisplayLastName": "Dr. Bowman",
        "FirstName": "Aaron",
        "LastName": "Bowman",
        "MiddleName": "Thomas",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-aaron-bowman-xxrp5?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w120h160_v1.jpg"
          }
        ],
        "Gender": "M",
        "Payors": [
          "AETNA",
          "AMERREP",
          "ANTHEA",
          "ASSURH",
          "BLUECG",
          "CHAMPV",
          "CIGNA",
          "COINCO",
          "DELTHS",
          "GOLDER",
          "GOVERA",
          "GRHECO",
          "HEALTA",
          "HUMANA",
          "MEDHEI",
          "MEDAID",
          "MEDICO",
          "MULTIP",
          "PRINLI",
          "TRICAR",
          "UNITHC"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1356430227"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 39.47085,
          "Longitude": -119.81025,
          "LatLon": "39.47085,-119.81025"
        },
        "Practices": [
          {
            "PracticeGuid": "81AFDDB9-9043-E111-B3AF-B499BAA4D952",
            "PracticeId": "FRTDR",
            "PracticeName": "Reno Oncology Consultants",
            "PracticeUrl": "renooncology.com",
            "Addresses": [
              {
                "Address1": "6130 Plumas St",
                "OfficeCode": "YBDDP5",
                "OfficeGuid": "97DB2C8F-E021-4BDA-9ED8-82E4A62369B2",
                "Location": {
                  "CityName": "Reno",
                  "CityAndState": "Reno, NV",
                  "CityStateZipBestMatch": "Reno, NV 89519",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89519",
                    "Coordinates": {
                      "Latitude": 39.47085,
                      "Longitude": -119.81025,
                      "LatLon": "39.47085,-119.81025"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 329-0222"
                ],
                "Fax": [
                  "(775) 329-3010"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Reno"
        ],
        "CityState": [
          "Reno, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "13",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Bowman's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Oncology",
          "Medical Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Oncology",
          "PracticingSpecialityCode": "PS592",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Oncology Specialist",
          "PracticingSpecialityNameIsts": "Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS592",
          "Value": "Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          50468,
          1379,
          50682
        ],
        "ConditionIds": [
          51043,
          157,
          144,
          155,
          51096,
          50553,
          150,
          19755,
          52042,
          14161,
          2286,
          2774,
          75,
          51968,
          142,
          2211,
          13000,
          51089,
          120,
          51106,
          2406,
          3264,
          837,
          172,
          2493,
          2710,
          1495,
          165,
          11893,
          2904,
          2841,
          51941,
          17253,
          51678,
          14671,
          163,
          52162,
          51188,
          1500,
          5128,
          10653,
          12070,
          170,
          841,
          52137,
          314,
          51067,
          160,
          51059,
          4737,
          152,
          2454,
          126,
          51921,
          2792,
          51116,
          12406,
          17191,
          162,
          15186,
          668,
          51127,
          164,
          11414,
          156,
          8776,
          2942,
          51122,
          18576,
          130,
          51075,
          51109,
          149,
          19102,
          169,
          51055,
          52015,
          51975,
          2423,
          4834,
          14889,
          51091,
          17178,
          4806,
          695,
          19830,
          1765,
          153,
          50903,
          51209,
          4384,
          52142,
          11392,
          51184,
          2404,
          18366,
          1410,
          3759,
          51340,
          17704,
          20066,
          51925,
          1370,
          11627,
          52169,
          2800
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 7,
        "SurveyOverallRatingPercent": 88,
        "SurveyOverallRatingScore": 4.4,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-aaron-bowman-xxrp5/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "30D73B",
          "7D4AEB",
          "C53DEB",
          "6B779D"
        ],
        "AffiliatedHospitalNames": [
          "Renown Regional Medical Center",
          "Renown South Meadows Medical Center",
          "Saint Mary's Regional Medical Center",
          "Banner Churchill Community Hospital"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 11.2868738,
        "PesBoost": 0.10483,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 9.532043,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 2,
      "Id": "XDJ2Q",
      "DemographicInfo": {
        "DisplayName": "Dr. Ayse Dincer, MD",
        "DisplayLastName": "Dr. Dincer",
        "FirstName": "Ayse",
        "LastName": "Dincer",
        "MiddleName": "Pinar",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-ayse-dincer-xdj2q?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w120h160_v1.jpg"
          }
        ],
        "Gender": "F",
        "Payors": [
          "AETNA",
          "CIGNA",
          "FIRSTB",
          "HUMANA",
          "MULTIP",
          "UNITHC"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1023111531"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.118406,
          "Longitude": -115.224784,
          "LatLon": "36.118406,-115.224784"
        },
        "Practices": [
          {
            "PracticeGuid": "3F50507D-09DF-4C66-8101-FBA9EAE5AE9B",
            "PracticeId": "PP3BJTT",
            "PracticeName": "VA Health System Spclty Clinic Southwest",
            "PracticeUrl": "",
            "Addresses": [
              {
                "Address1": "3880 S Jones Blvd",
                "OfficeCode": "OOSSNM6",
                "OfficeGuid": "85085C25-E197-4B93-8701-9A3923ACAD19",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89103",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89103",
                    "Coordinates": {
                      "Latitude": 36.118406,
                      "Longitude": -115.224784,
                      "LatLon": "36.118406,-115.224784"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 636-6390"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Las Vegas"
        ],
        "CityState": [
          "Las Vegas, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "24",
        "BoardCertificationSpecialties": [
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Dincer's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Oncology",
          "Medical Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Oncology",
          "PracticingSpecialityCode": "PS592",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Oncology Specialist",
          "PracticingSpecialityNameIsts": "Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS592",
          "Value": "Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Medical Oncology"
        ],
        "ProcedureIds": [],
        "ConditionIds": [
          170,
          120,
          19102,
          160,
          75,
          157,
          155,
          165,
          51089,
          2211,
          51055,
          1500,
          51075,
          18576,
          164,
          142,
          668,
          156,
          130,
          51116,
          17178,
          51067,
          153
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 1,
        "SurveyOverallRatingPercent": 100,
        "SurveyOverallRatingScore": 5,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-ayse-dincer-xdj2q/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "349902"
        ],
        "AffiliatedHospitalNames": [
          "St. Francis Regional Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 93,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 11.25532,
        "PesBoost": 0.073276,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.933333337,
        "HospitalQualityBoost": 9.532043,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 3,
      "Id": "Y872X",
      "DemographicInfo": {
        "DisplayName": "Dr. Dina Tack, MD",
        "DisplayLastName": "Dr. Tack",
        "FirstName": "Dina",
        "LastName": "Tack",
        "MiddleName": "Kristine",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-dina-tack-y872x?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w120h160_v1.jpg"
          }
        ],
        "Gender": "F",
        "Payors": [
          "AETNA",
          "ANTHEA",
          "BLUECG",
          "CIGNA",
          "UNITHC"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1730402025"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 39.203405,
          "Longitude": -119.786765,
          "LatLon": "39.203405,-119.786765"
        },
        "Practices": [
          {
            "PracticeGuid": "643D4658-AD6C-4792-BF43-3988B2DE66B0",
            "PracticeId": "PPP2BVD",
            "PracticeName": "Carson Tahoe Physician Clinic",
            "PracticeUrl": "carsontahoe.com",
            "Addresses": [
              {
                "Address1": "1535 Medical Pkwy Ste B",
                "OfficeCode": "OOO7C3S",
                "OfficeGuid": "11D99CAA-AD70-4196-83CD-9CF0A6002D23",
                "Location": {
                  "CityName": "Carson City",
                  "CityAndState": "Carson City, NV",
                  "CityStateZipBestMatch": "Carson City, NV 89703",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89703",
                    "Coordinates": {
                      "Latitude": 39.203405,
                      "Longitude": -119.786765,
                      "LatLon": "39.203405,-119.786765"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 445-7960"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Carson City"
        ],
        "CityState": [
          "Carson City, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "17",
        "BoardCertificationSpecialties": [
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Tack's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Oncology",
          "PracticingSpecialityCode": "PS592",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Oncology Specialist",
          "PracticingSpecialityNameIsts": "Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS592",
          "Value": "Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology"
        ],
        "ProcedureIds": [
          50468,
          50682,
          1379
        ],
        "ConditionIds": [
          150,
          52042,
          152,
          2286,
          14161,
          170,
          149,
          172,
          51043,
          142,
          3264,
          13000,
          157,
          164,
          2454,
          160,
          165,
          75,
          155,
          837,
          51091,
          19102,
          2792,
          144,
          2493,
          51055,
          1495,
          51089,
          51106,
          130,
          163,
          120,
          17178,
          51941,
          2406,
          51184,
          51087,
          3759,
          51116,
          1370,
          4384,
          169,
          51067,
          51340,
          153,
          11414,
          51122,
          52137,
          695,
          20066,
          51109,
          126,
          52142,
          50903,
          841,
          1410,
          17704,
          19830,
          2800,
          2904,
          51096,
          11392,
          4834,
          4806,
          156,
          18366,
          51075,
          12242,
          14671,
          51042,
          51209,
          1765,
          51188,
          52162,
          51911,
          18576
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 2,
        "SurveyOverallRatingPercent": 80,
        "SurveyOverallRatingScore": 4,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-dina-tack-y872x/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "8AF328",
          "762635",
          "4EF075"
        ],
        "AffiliatedHospitalNames": [
          "Carson Tahoe Sierra Surgery",
          "Carson Valley Medical Center",
          "Carson Tahoe Regional Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 98,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 11.2324743,
        "PesBoost": 0.050431,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.982090652,
        "HospitalQualityBoost": 9.532043,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 4,
      "Id": "26VYX",
      "DemographicInfo": {
        "DisplayName": "Dr. John Kelly, MD",
        "DisplayLastName": "Dr. Kelly",
        "FirstName": "John",
        "LastName": "Kelly",
        "MiddleName": "P",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-john-kelly-26vyx?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w120h160_v1.jpg"
          }
        ],
        "Gender": "M",
        "Payors": [
          "AETNA",
          "AMERREP",
          "ANTHEA",
          "ASSURH",
          "BLUECG",
          "BLUECF",
          "CIGNA",
          "COINCO",
          "CORESC",
          "COHECA",
          "DELTHS",
          "FIRSTB",
          "GRHECO",
          "HEALTA",
          "HUMANA",
          "MAILHA",
          "MEDHEI",
          "MEDAID",
          "MULTIP",
          "PACSRC",
          "PRINLI",
          "TRICAR",
          "UNITHC",
          "WEFAIN"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1477512234"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 39.203405,
          "Longitude": -119.786765,
          "LatLon": "39.203405,-119.786765"
        },
        "Practices": [
          {
            "PracticeGuid": "643D4658-AD6C-4792-BF43-3988B2DE66B0",
            "PracticeId": "PPP2BVD",
            "PracticeName": "Carson Tahoe Physician Clinic",
            "PracticeUrl": "carsontahoe.com",
            "Addresses": [
              {
                "Address1": "1535 Medical Pkwy Ste B",
                "OfficeCode": "OOO7C3S",
                "OfficeGuid": "11D99CAA-AD70-4196-83CD-9CF0A6002D23",
                "Location": {
                  "CityName": "Carson City",
                  "CityAndState": "Carson City, NV",
                  "CityStateZipBestMatch": "Carson City, NV 89703",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89703",
                    "Coordinates": {
                      "Latitude": 39.203405,
                      "Longitude": -119.786765,
                      "LatLon": "39.203405,-119.786765"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 445-7960"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Carson City"
        ],
        "CityState": [
          "Carson City, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "37",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Kelly's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Oncology",
          "PracticingSpecialityCode": "PS592",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Oncology Specialist",
          "PracticingSpecialityNameIsts": "Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS592",
          "Value": "Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology"
        ],
        "ProcedureIds": [
          1379,
          50682,
          50468
        ],
        "ConditionIds": [
          19755,
          51042,
          12406,
          52042,
          14161,
          2286,
          170,
          12070,
          149,
          12242,
          172,
          51921,
          1495,
          75,
          3264,
          2710,
          163,
          2774,
          155,
          17253,
          51091,
          157,
          51184,
          160,
          2493,
          19102,
          142,
          14671,
          2335,
          51043,
          2904,
          51106,
          13000,
          51968,
          51891,
          120,
          51941,
          164,
          51925,
          169,
          51678,
          51087,
          51111,
          51096,
          3767,
          2423,
          51122,
          51059,
          51055,
          144,
          51116,
          130,
          1693,
          51075,
          152,
          17178,
          165,
          2841,
          18576,
          51109,
          837,
          668,
          1765,
          52027,
          2211,
          51911,
          314,
          2406,
          150,
          5128,
          156,
          3759,
          11414,
          51089,
          162,
          2942,
          126,
          51975,
          10653,
          1500,
          2404,
          2454,
          51067,
          2800,
          15186,
          11893,
          8776,
          4384,
          50553,
          52169,
          20066,
          50903,
          18366,
          783,
          2792,
          1410,
          14889,
          51188,
          52137,
          51340,
          1370,
          10024,
          52162,
          19830,
          153,
          17704,
          51995,
          52142,
          11392,
          695,
          838,
          11627,
          4834,
          4737,
          4806,
          51209
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 22,
        "SurveyOverallRatingPercent": 50,
        "SurveyOverallRatingScore": 2.5,
        "IsRecommendedProvider": false,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-john-kelly-26vyx/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "1672C3",
          "762635",
          "CC4205",
          "4EF075",
          "8AF328"
        ],
        "AffiliatedHospitalNames": [
          "Barton Memorial Hospital",
          "Carson Valley Medical Center",
          "South Lyon Medical Center",
          "Carson Tahoe Regional Medical Center",
          "Carson Tahoe Sierra Surgery"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 11.1820431,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 9.532043,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 5,
      "Id": "Y4T2B",
      "DemographicInfo": {
        "DisplayName": "Dr. Don J. Park, MD",
        "DisplayLastName": "Dr. Park",
        "FirstName": "Don",
        "LastName": "Park",
        "MiddleName": "J",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-don-park-y4t2b?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w120h160_v1.jpg"
          }
        ],
        "Gender": "M",
        "Payors": [
          "AETNA",
          "BLUECG",
          "BLUECX",
          "CIGNA",
          "FIRSTB",
          "MULTIP",
          "PRIOHE",
          "UNITHC"
        ],
        "Languages": [],
        "Npi": "1285714352"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 39.526519,
          "Longitude": -119.79569,
          "LatLon": "39.526519,-119.79569"
        },
        "Practices": [
          {
            "PracticeGuid": "D84DB385-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FM2MW",
            "PracticeName": "Renown Medical Group - Ryland",
            "PracticeUrl": "http://www.renown.org",
            "Addresses": [
              {
                "Address1": "75 Pringle Way Ste 801",
                "OfficeCode": "YCCTKH",
                "OfficeGuid": "1419F045-3EC4-E311-8FD0-B499BAA4D952",
                "Location": {
                  "CityName": "Reno",
                  "CityAndState": "Reno, NV",
                  "CityStateZipBestMatch": "Reno, NV 89502",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89502",
                    "Coordinates": {
                      "Latitude": 39.526519,
                      "Longitude": -119.79569,
                      "LatLon": "39.526519,-119.79569"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 982-5000"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Reno"
        ],
        "CityState": [
          "Reno, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "24",
        "BoardCertificationSpecialties": [
          "Hematology",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CHMTL",
            "CertificationName": "Hematology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Park's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 1,
        "SpecialistDesc": [
          "Hematology Specialist",
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          1,
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Hematology",
          "Oncology",
          "Medical Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Hematology",
          "PracticingSpecialityCode": "PS361",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Hematology Specialist",
          "PracticingSpecialityNameIsts": "Hematology Specialists",
          "RollupPracticingSpecialityCode": "PS361"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS361",
          "Value": "Hematology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Hematology",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          50468,
          3125,
          50682,
          1379
        ],
        "ConditionIds": [
          130,
          14161,
          142,
          3264,
          51091,
          19102,
          75,
          51106,
          2406,
          51678,
          2211,
          51055,
          52137,
          314,
          155,
          51184,
          7536,
          51116,
          51122,
          17178,
          51075,
          18576,
          2454,
          51043,
          51230,
          152,
          150,
          156,
          149,
          2774,
          51340,
          13000,
          51089,
          160,
          52042,
          668,
          12070,
          695,
          18366,
          2904,
          51067,
          52142,
          51183,
          15186,
          51975,
          2710,
          14889,
          1410,
          170,
          1370,
          4384,
          165,
          1500,
          19830,
          126,
          172,
          3759,
          164,
          2404,
          4806,
          52015,
          17253,
          20066,
          17704,
          1765,
          157,
          10024,
          11893,
          51096,
          51109,
          169,
          120,
          2849,
          4834,
          163,
          1495,
          50903,
          11392,
          2800,
          11627,
          2841,
          52162,
          3997,
          51968,
          51042,
          5128,
          162,
          153,
          2792
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 11,
        "SurveyOverallRatingPercent": 70,
        "SurveyOverallRatingScore": 3.5,
        "IsRecommendedProvider": false,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-don-park-y4t2b/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "385C74",
          "93D959"
        ],
        "AffiliatedHospitalNames": [
          "Bronson Methodist Hospital",
          "Borgess Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Hematology",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Hematology and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 9.665783,
        "PesBoost": 0.072414,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 7.943369,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 6,
      "Id": "2RDDB",
      "DemographicInfo": {
        "DisplayName": "Dr. Regan Holdridge, MD",
        "DisplayLastName": "Dr. Holdridge",
        "FirstName": "Regan",
        "LastName": "Holdridge",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-regan-holdridge-2rddb?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/R/D/2RDDB_w60h80_v10004.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/R/D/2RDDB_w90h120_v10004.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/R/D/2RDDB_w120h160_v10004.jpg"
          }
        ],
        "Gender": "F",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nDr. Regan Holdridge is a medical oncologist and "
        },
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "CUHEFU",
          "FIRSTB",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL"
        ],
        "Languages": [
          "Spanish"
        ],
        "AcceptsNewPatients": true,
        "Npi": "1093937054"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.03183,
          "Longitude": -115.04945,
          "LatLon": "36.03183,-115.04945"
        },
        "Practices": [
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "1505 Wigwam Pkwy Ste 130",
                "OfficeCode": "OOVP6KP",
                "OfficeGuid": "A4738CE8-1776-48CF-A09C-D637F62922E4",
                "Location": {
                  "CityName": "Henderson",
                  "CityAndState": "Henderson, NV",
                  "CityStateZipBestMatch": "Henderson, NV 89074",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89074",
                    "Coordinates": {
                      "Latitude": 36.03183,
                      "Longitude": -115.04945,
                      "LatLon": "36.03183,-115.04945"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 856-1400"
                ],
                "Fax": [
                  "(702) 856-1407"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Henderson"
        ],
        "CityState": [
          "Henderson, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "14",
        "BoardCertificationSpecialties": [
          "Hematology",
          "Internal Medicine",
          "Medical Oncology",
          "Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CHMTL",
            "CertificationName": "Hematology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABMS",
            "CertifyingAuthorityBoardName": "American Board of Medical Specialties"
          },
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CONCG",
            "CertificationName": "Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABMS",
            "CertifyingAuthorityBoardName": "American Board of Medical Specialties"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Holdridge's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Hematology Specialist",
          "Researcher"
        ],
        "SpecialtiesIds": [
          67,
          1,
          990
        ],
        "SpecialtiesDescriptions": [
          "Medical Oncology",
          "Hematology",
          "Oncology",
          "Cancer Research"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Medical Oncology",
          "PracticingSpecialityCode": "PS456",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Medical Oncology Specialist",
          "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS456",
          "Value": "Medical Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS856",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Cancer Research",
            "PracticingSpecialityCode": "PS123",
            "PracticingSpecialityRank": 4,
            "PracticingSpecialityNameIst": "Cancer Researcher",
            "PracticingSpecialityNameIsts": "Cancer Researchers",
            "RollupPracticingSpecialityCode": "PS856"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Cancer Research",
          "Hematology",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          229,
          50998
        ],
        "ConditionIds": [
          51043,
          19755,
          2774,
          170,
          156,
          149,
          3264,
          13000,
          163,
          14671,
          120,
          19102,
          2841,
          2792,
          1500,
          144,
          51067,
          51122,
          17178,
          51116,
          155,
          75,
          1852,
          51106,
          164,
          172,
          668,
          17191,
          2904,
          160,
          2454,
          51096,
          142,
          165,
          1395,
          130,
          8776,
          126,
          12070,
          157,
          11627,
          17253,
          50903,
          3759,
          4834,
          4806,
          2849,
          51075,
          52142,
          51209,
          1765,
          18366,
          1370,
          153,
          52137,
          51340,
          51925,
          14889,
          1410
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 14,
        "SurveyOverallRatingPercent": 66,
        "SurveyOverallRatingScore": 3.3,
        "IsRecommendedProvider": false,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-regan-holdridge-2rddb/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "5FEB5C",
          "B2B744",
          "D6F15E",
          "B5D7A6",
          "A0C2A7",
          "CBF7A2",
          "4D8ED7",
          "A8F53E",
          "ADF464",
          "F9D29F"
        ],
        "AffiliatedHospitalNames": [
          "Southern Hills Hospital and Medical Center",
          "Desert Springs Hospital Medical Center",
          "Spring Valley Hospital Medical Center",
          "St. Rose Dominican, Siena Campus",
          "St. Rose Dominican, Rose de Lima Campus",
          "St. Rose Dominican, San Martin Campus",
          "Desert View Hospital",
          "Boulder City Hospital",
          "Valley Hospital Medical Center",
          "Summerlin Hospital Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 98,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Hematology",
              "Internal Medicine",
              "Medical Oncology",
              "Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Hematology, Internal Medicine, Medical Oncology and Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 9.661645,
        "PesBoost": 0.068276,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.9804386,
        "HospitalQualityBoost": 7.943369,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 7,
      "Id": "Y6PNP",
      "DemographicInfo": {
        "DisplayName": "Dr. Hamidreza Sanatinia, MD",
        "DisplayLastName": "Dr. Sanatinia",
        "FirstName": "Hamidreza",
        "LastName": "Sanatinia",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-hamidreza-sanatinia-y6pnp?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/6/P/Y6PNP_w60h80_v15620.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/6/P/Y6PNP_w90h120_v15620.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/6/P/Y6PNP_w120h160_v15620.jpg"
          }
        ],
        "Gender": "M",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nCancer affects every one of us. I believe in tre"
        },
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "CUHEFU",
          "FIRSTB",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL"
        ],
        "Languages": [
          "Spanish"
        ],
        "AcceptsNewPatients": true,
        "Npi": "1538178991"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.0718,
          "Longitude": -115.29489,
          "LatLon": "36.0718,-115.29489"
        },
        "Practices": [
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "9280 W Sunset Rd Ste 100",
                "OfficeCode": "YCD9XP",
                "OfficeGuid": "05C37E9F-08F5-4DA5-AF9D-F83315032E19",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89148",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89148",
                    "Coordinates": {
                      "Latitude": 36.0718,
                      "Longitude": -115.29489,
                      "LatLon": "36.0718,-115.29489"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 952-1251"
                ],
                "Fax": [
                  "(702) 952-1241"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Las Vegas"
        ],
        "CityState": [
          "Las Vegas, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "21",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology",
          "Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CONCG",
            "CertificationName": "Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABMS",
            "CertifyingAuthorityBoardName": "American Board of Medical Specialties"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Sanatinia's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Cardiology Specialist",
          "Hematology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          7,
          1,
          22
        ],
        "SpecialtiesDescriptions": [
          "Medical Oncology",
          "Cardiology",
          "Hematology",
          "Hematology & Oncology",
          "Oncology",
          "Internal Medicine"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Medical Oncology",
          "PracticingSpecialityCode": "PS456",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Medical Oncology Specialist",
          "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS456",
          "Value": "Medical Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS412",
          "PS127",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Cardiology",
            "PracticingSpecialityCode": "PS127",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Cardiology Specialist",
            "PracticingSpecialityNameIsts": "Cardiology Specialists",
            "RollupPracticingSpecialityCode": "PS127"
          },
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Hematology & Oncology",
            "PracticingSpecialityCode": "PS362",
            "PracticingSpecialityRank": 4,
            "PracticingSpecialityNameIst": "Hematology & Oncology Specialist",
            "PracticingSpecialityNameIsts": "Hematology & Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 5,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Internal Medicine",
            "PracticingSpecialityCode": "PS412",
            "PracticingSpecialityRank": 6,
            "PracticingSpecialityNameIst": "Internist",
            "PracticingSpecialityNameIsts": "Internists",
            "RollupPracticingSpecialityCode": "PS412"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Cardiology",
          "Hematology",
          "Hematology & Oncology",
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          229,
          50998,
          2287
        ],
        "ConditionIds": [
          51122,
          51042,
          841,
          170,
          2774,
          149,
          142,
          172,
          3264,
          163,
          13000,
          2406,
          130,
          1765,
          156,
          2493,
          157,
          51116,
          155,
          51096,
          17253,
          165,
          1500,
          164,
          4737,
          19102,
          2286,
          160,
          144,
          14671,
          1395,
          75,
          169,
          120,
          2904,
          51043,
          11627,
          12070,
          51075,
          51209,
          126,
          314,
          1495,
          52137,
          153,
          52142,
          10024,
          1370,
          150
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 10,
        "SurveyOverallRatingPercent": 100,
        "SurveyOverallRatingScore": 5,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-hamidreza-sanatinia-y6pnp/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "A8F53E",
          "D6F15E",
          "F9D29F",
          "B2B744",
          "5FEB5C",
          "F129D5",
          "4D8ED7",
          "7EA9BC",
          "ADF464",
          "CBF7A2",
          "B5D7A6"
        ],
        "AffiliatedHospitalNames": [
          "Boulder City Hospital",
          "Spring Valley Hospital Medical Center",
          "Summerlin Hospital Medical Center",
          "Desert Springs Hospital Medical Center",
          "Southern Hills Hospital and Medical Center",
          "North Vista Hospital",
          "Desert View Hospital",
          "Sunrise Hospital and Medical Center",
          "Valley Hospital Medical Center",
          "St. Rose Dominican, San Martin Campus",
          "St. Rose Dominican, Siena Campus"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 98,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology",
              "Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine, Medical Oncology and Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 8.174955,
        "PesBoost": 0.17026,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.9870062,
        "HospitalQualityBoost": 6.35469532,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 8,
      "Id": "XNV3J",
      "DemographicInfo": {
        "DisplayName": "Dr. James Forsythe, MD",
        "DisplayLastName": "Dr. Forsythe",
        "FirstName": "James",
        "LastName": "Forsythe",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-james-forsythe-xnv3j?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w120h160_v1.jpg"
          }
        ],
        "Gender": "M",
        "Payors": [
          "AETNA",
          "BLUECG",
          "COINCO",
          "CUHEFU",
          "GOVERA",
          "KAISER",
          "UNITHC"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1619983178"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 39.47327,
          "Longitude": -119.79351,
          "LatLon": "39.47327,-119.79351"
        },
        "Practices": [
          {
            "PracticeGuid": "3D28C241-74A1-4E90-86B3-463249C2FDA5",
            "PracticeId": "PPP2SJ8",
            "PracticeName": "Century Wellness Clinic",
            "PracticeUrl": "centurywellness.com",
            "Addresses": [
              {
                "Address1": "521 Hammill Ln",
                "OfficeCode": "OOO8XNB",
                "OfficeGuid": "0EB686D9-C22A-4F63-96A6-AA44395B166B",
                "Location": {
                  "CityName": "Reno",
                  "CityAndState": "Reno, NV",
                  "CityStateZipBestMatch": "Reno, NV 89511",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89511",
                    "Coordinates": {
                      "Latitude": 39.47327,
                      "Longitude": -119.79351,
                      "LatLon": "39.47327,-119.79351"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 827-0707"
                ]
              }
            ]
          },
          {
            "PracticeGuid": "811BD0CA-E8EA-E111-91C6-B499BAA4D952",
            "PracticeId": "WQ5F7",
            "PracticeName": "Century Wellness Clinic",
            "PracticeUrl": "",
            "Addresses": [
              {
                "Address1": "521 Hammill Ln # B",
                "OfficeCode": "WQ5F7",
                "OfficeGuid": "811BD0CA-E8EA-E111-91C6-B499BAA4D952",
                "Location": {
                  "CityName": "Reno",
                  "CityAndState": "Reno, NV",
                  "CityStateZipBestMatch": "Reno, NV 89511",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89511",
                    "Coordinates": {
                      "Latitude": 39.47327,
                      "Longitude": -119.79351,
                      "LatLon": "39.47327,-119.79351"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 827-0707"
                ],
                "Fax": [
                  "(775) 827-1006"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Reno"
        ],
        "CityState": [
          "Reno, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "52",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Forsythe's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Oncology",
          "Medical Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Oncology",
          "PracticingSpecialityCode": "PS592",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Oncology Specialist",
          "PracticingSpecialityNameIsts": "Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS592",
          "Value": "Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          50682
        ],
        "ConditionIds": [
          172,
          51043,
          120,
          19102,
          160,
          155,
          165,
          2454,
          18576,
          668,
          164,
          130,
          51921,
          2710,
          4384,
          51055,
          51340,
          75,
          52137,
          695,
          51122,
          3264,
          17253,
          1500,
          11392,
          163,
          2211,
          142,
          2774,
          4834,
          156,
          14161,
          2493,
          19755,
          51116,
          169,
          1410,
          19830,
          15186,
          126,
          17704,
          52142,
          50903,
          1370,
          1765,
          20066,
          18366,
          3759,
          149,
          153,
          841,
          51925,
          4806,
          2904
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 50,
        "SurveyOverallRatingPercent": 94,
        "SurveyOverallRatingScore": 4.7,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-james-forsythe-xnv3j/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "30D73B"
        ],
        "AffiliatedHospitalNames": [
          "Renown Regional Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 95,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 2.17914,
        "PesBoost": 0.52914,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.9518703,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 9,
      "Id": "2BJGP",
      "DemographicInfo": {
        "DisplayName": "Dr. Rupesh J. Parikh, MD",
        "DisplayLastName": "Dr. Parikh",
        "FirstName": "Rupesh",
        "LastName": "Parikh",
        "MiddleName": "Jayantilal",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-rupesh-parikh-2bjgp?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/B/J/2BJGP_w60h80_v10277.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/B/J/2BJGP_w90h120_v10277.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/B/J/2BJGP_w120h160_v10277.jpg"
          }
        ],
        "Gender": "M",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\n\"Treating the patient, not just the disease\" Tre"
        },
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "CUHEFU",
          "FIRSTB",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL",
          "WELLPT"
        ],
        "Languages": [
          "Spanish"
        ],
        "AcceptsNewPatients": true,
        "Npi": "1245249689"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.0054,
          "Longitude": -115.11438,
          "LatLon": "36.0054,-115.11438"
        },
        "Practices": [
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "10001 S Eastern Ave Ste 108",
                "OfficeCode": "YCD9KG",
                "OfficeGuid": "37778FFF-F9C9-4EF3-AC78-9AE7E3D634C7",
                "Location": {
                  "CityName": "Henderson",
                  "CityAndState": "Henderson, NV",
                  "CityStateZipBestMatch": "Henderson, NV 89052",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89052",
                    "Coordinates": {
                      "Latitude": 36.0054,
                      "Longitude": -115.11438,
                      "LatLon": "36.0054,-115.11438"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 952-3444"
                ],
                "Fax": [
                  "(702) 952-3494"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Henderson"
        ],
        "CityState": [
          "Henderson, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "20",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Parikh's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Hematology Specialist",
          "Gynecologic Oncology Specialist",
          "Internist",
          "Radiation Oncology Specialist"
        ],
        "SpecialtiesIds": [
          67,
          1,
          4,
          22,
          6
        ],
        "SpecialtiesDescriptions": [
          "Medical Oncology",
          "Hematology",
          "Oncology",
          "Gynecologic Oncology",
          "Internal Medicine",
          "Radiation Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Medical Oncology",
          "PracticingSpecialityCode": "PS456",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Medical Oncology Specialist",
          "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS456",
          "Value": "Medical Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS412",
          "PS345",
          "PS825",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Gynecologic Oncology",
            "PracticingSpecialityCode": "PS345",
            "PracticingSpecialityRank": 4,
            "PracticingSpecialityNameIst": "Gynecologic Oncology Specialist",
            "PracticingSpecialityNameIsts": "Gynecologic Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS345"
          },
          {
            "PracticingSpecialityName": "Internal Medicine",
            "PracticingSpecialityCode": "PS412",
            "PracticingSpecialityRank": 5,
            "PracticingSpecialityNameIst": "Internist",
            "PracticingSpecialityNameIsts": "Internists",
            "RollupPracticingSpecialityCode": "PS412"
          },
          {
            "PracticingSpecialityName": "Radiation Oncology",
            "PracticingSpecialityCode": "PS825",
            "PracticingSpecialityRank": 6,
            "PracticingSpecialityNameIst": "Radiation Oncology Specialist",
            "PracticingSpecialityNameIsts": "Radiation Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS825"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Gynecologic Oncology",
          "Hematology",
          "Internal Medicine",
          "Medical Oncology",
          "Radiation Oncology"
        ],
        "ProcedureIds": [
          229,
          50998,
          2287
        ],
        "ConditionIds": [
          19755,
          150,
          841,
          52042,
          62,
          2774,
          2286,
          170,
          142,
          3997,
          14671,
          51057,
          1852,
          2493,
          2406,
          163,
          144,
          155,
          51075,
          1495,
          1765,
          149,
          51043,
          75,
          160,
          17253,
          19102,
          4737,
          12070,
          13000,
          837,
          3264,
          2880,
          153,
          126,
          120,
          51096,
          51042,
          51188,
          18576,
          51911,
          11113,
          2904,
          51209,
          166,
          11627,
          156,
          1395,
          52142,
          51122,
          2792,
          165,
          8776,
          157,
          164,
          1500,
          51116,
          51975,
          130,
          52137,
          1370,
          51067,
          4832
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 47,
        "SurveyOverallRatingPercent": 96,
        "SurveyOverallRatingScore": 4.8,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-rupesh-parikh-2bjgp/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "A8F53E",
          "F9D29F",
          "D6F15E",
          "5FEB5C",
          "7EA9BC",
          "C0C277",
          "CBF7A2",
          "B5D7A6",
          "A0C2A7"
        ],
        "AffiliatedHospitalNames": [
          "Boulder City Hospital",
          "Summerlin Hospital Medical Center",
          "Spring Valley Hospital Medical Center",
          "Southern Hills Hospital and Medical Center",
          "Sunrise Hospital and Medical Center",
          "Mountainview Hospital",
          "St. Rose Dominican, San Martin Campus",
          "St. Rose Dominican, Siena Campus",
          "St. Rose Dominican, Rose de Lima Campus"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 2.17345,
        "PesBoost": 0.52345,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 10,
      "Id": "YKQPT",
      "DemographicInfo": {
        "DisplayName": "Dr. Jorge H. Perez-Cardona, MD",
        "DisplayLastName": "Dr. Perez-Cardona",
        "FirstName": "Jorge",
        "LastName": "Perez-Cardona",
        "MiddleName": "H",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-jorge-perez-ykqpt?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w120h160_v1.jpg"
          }
        ],
        "Gender": "M",
        "Payors": [
          "AETNA",
          "ASSURH",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "DELTHS",
          "GOVERA",
          "HENT",
          "HUMANA",
          "MEDICA",
          "MULTIP",
          "TRICAR",
          "UNITHC",
          "WELLPT"
        ],
        "Languages": [
          "Spanish"
        ],
        "AcceptsNewPatients": true,
        "Npi": "1801829635"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 39.15449,
          "Longitude": -119.76849,
          "LatLon": "39.15449,-119.76849"
        },
        "Practices": [
          {
            "PracticeGuid": "E1DEE4B9-9043-E111-B3AF-B499BAA4D952",
            "PracticeId": "FVC3P",
            "PracticeName": "Sierra Nevada Cancer Center",
            "PracticeUrl": "http://www.sierracancer.com",
            "Addresses": [
              {
                "Address1": "1460 S Curry St",
                "OfficeCode": "YDFYDF",
                "OfficeGuid": "6B617AB4-81DC-401E-A998-43CEB47D9278",
                "Location": {
                  "CityName": "Carson City",
                  "CityAndState": "Carson City, NV",
                  "CityStateZipBestMatch": "Carson City, NV 89703",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89703",
                    "Coordinates": {
                      "Latitude": 39.15449,
                      "Longitude": -119.76849,
                      "LatLon": "39.15449,-119.76849"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 883-3336"
                ],
                "IsPrimary": true
              },
              {
                "Address1": "1020 New River Pkwy",
                "OfficeCode": "YDFXSH",
                "OfficeGuid": "D379CD19-776C-4059-AAFD-D057F39D2199",
                "Location": {
                  "CityName": "Fallon",
                  "CityAndState": "Fallon, NV",
                  "CityStateZipBestMatch": "Fallon, NV 89406",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89406",
                    "Coordinates": {
                      "Latitude": 39.46476,
                      "Longitude": -118.76223,
                      "LatLon": "39.46476,-118.76223"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 883-3336"
                ]
              },
              {
                "Address1": "1107 US Highway 395 N",
                "OfficeCode": "YDFXVD",
                "OfficeGuid": "9D79873C-3342-4934-ADDC-B198AAC402A8",
                "Location": {
                  "CityName": "Gardnerville",
                  "CityAndState": "Gardnerville, NV",
                  "CityStateZipBestMatch": "Gardnerville, NV 89410",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89410",
                    "Coordinates": {
                      "Latitude": 38.919314,
                      "Longitude": -119.718668,
                      "LatLon": "38.919314,-119.718668"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 883-3336"
                ]
              }
            ]
          }
        ],
        "City": [
          "Fallon",
          "Gardnerville",
          "Carson City"
        ],
        "CityState": [
          "Fallon, NV",
          "Gardnerville, NV",
          "Carson City, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "40",
        "BoardCertificationSpecialties": [
          "Hematology",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CHMTL",
            "CertificationName": "Hematology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Perez-Cardona's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Hematology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          1,
          22
        ],
        "SpecialtiesDescriptions": [
          "Medical Oncology",
          "Hematology",
          "Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Medical Oncology",
          "PracticingSpecialityCode": "PS456",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Medical Oncology Specialist",
          "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS456",
          "Value": "Medical Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Hematology",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          229,
          50998,
          2287,
          1379
        ],
        "ConditionIds": [
          120,
          155,
          3264,
          163,
          19102,
          160,
          75,
          165,
          18576,
          1395,
          130,
          164,
          14161,
          51975,
          142,
          2454,
          51184,
          841,
          51096,
          2774,
          12070,
          156,
          668,
          51043,
          2792,
          149,
          150,
          2406,
          13000,
          52042,
          51067,
          51042,
          2493,
          2942,
          11893,
          2904,
          172,
          14889,
          12406,
          17704,
          51055,
          52137,
          19755,
          18366,
          52142,
          1370,
          51968,
          50698,
          17178,
          51111,
          1495,
          7536,
          1500,
          51911,
          4737,
          51122,
          51109,
          695,
          51075,
          126,
          51057,
          169,
          51188,
          5128,
          170,
          51089,
          2710,
          17253,
          51106,
          51230,
          157,
          52162,
          1765,
          2211,
          51183,
          51091,
          2849,
          51941,
          162,
          2286,
          152,
          51678,
          51116,
          4806,
          4834,
          52169,
          11627,
          153,
          15186,
          51209
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 78,
        "SurveyOverallRatingPercent": 88,
        "SurveyOverallRatingScore": 4.4,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-jorge-perez-ykqpt/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "4EF075"
        ],
        "AffiliatedHospitalNames": [
          "Carson Tahoe Regional Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Hematology",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Hematology and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 2.11313,
        "PesBoost": 0.46313,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 11,
      "Id": "XDC9T",
      "DemographicInfo": {
        "DisplayName": "Dr. Robert Strimling, MD",
        "DisplayLastName": "Dr. Strimling",
        "FirstName": "Robert",
        "LastName": "Strimling",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-robert-strimling-xdc9t?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/D/C/XDC9T_w60h80.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/D/C/XDC9T_w90h120.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/D/C/XDC9T_w120h160.jpg"
          }
        ],
        "Gender": "M",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nWe are the premier Dermatology, Mohs Skin Cancer"
        },
        "Payors": [
          "ACCEPA",
          "AETNA",
          "AMERIB",
          "ANTHEA",
          "ASSURH",
          "BLUECG",
          "CIGNA",
          "COINCO",
          "COHECA",
          "GOLDER",
          "GOVERA",
          "HUMANA",
          "MEMUOH",
          "MULTIP",
          "PRIFGR",
          "UNITHC",
          "WELLPT"
        ],
        "Languages": [
          "Spanish"
        ],
        "AcceptsNewPatients": true,
        "Npi": "1699746768"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.182827,
          "Longitude": -115.316365,
          "LatLon": "36.182827,-115.316365"
        },
        "Practices": [
          {
            "PracticeGuid": "1D16A585-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "DWTVB",
            "PracticeName": "Strimling Dermatology, Laser & Vein Institute",
            "PracticeUrl": "https://www.VegasDermatology.net",
            "Addresses": [
              {
                "Address1": "10105 Banburry Cross Dr Ste 350",
                "OfficeCode": "FLVNQ",
                "OfficeGuid": "884D1288-8943-E111-B3AF-B499BAA4D952",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89144",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89144",
                    "Coordinates": {
                      "Latitude": 36.182827,
                      "Longitude": -115.316365,
                      "LatLon": "36.182827,-115.316365"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 243-6400"
                ],
                "Fax": [
                  "(702) 243-4913"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Las Vegas"
        ],
        "CityState": [
          "Las Vegas, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "26",
        "BoardCertificationSpecialties": [
          "Dermatology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CDERM",
            "CertificationName": "Dermatology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABDERM",
            "CertifyingAuthorityBoardName": "American Board of Dermatology"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Strimling's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 63,
        "SpecialistDesc": [
          "Dermatologist",
          "Oncology Specialist",
          "Plastic Surgery Specialist",
          "Surgery Specialist",
          "Dermatopathology Specialist"
        ],
        "SpecialtiesIds": [
          63,
          67,
          41,
          44,
          87
        ],
        "SpecialtiesDescriptions": [
          "Dermatology",
          "Oncology",
          "Plastic Surgery",
          "Surgery",
          "Dermatologic Oncology",
          "Dermatologic Surgery",
          "Mohs Micrographic Surgery"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Dermatology",
          "PracticingSpecialityCode": "PS244",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Dermatologist",
          "PracticingSpecialityNameIsts": "Dermatologists",
          "RollupPracticingSpecialityCode": "PS244"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS244",
          "Value": "Dermatology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS244",
          "PS917",
          "PS773",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Dermatology",
            "PracticingSpecialityCode": "PS244",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Dermatologist",
            "PracticingSpecialityNameIsts": "Dermatologists",
            "RollupPracticingSpecialityCode": "PS244"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Plastic Surgery",
            "PracticingSpecialityCode": "PS773",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Plastic Surgery Specialist",
            "PracticingSpecialityNameIsts": "Plastic Surgery Specialists",
            "RollupPracticingSpecialityCode": "PS773"
          },
          {
            "PracticingSpecialityName": "Surgery",
            "PracticingSpecialityCode": "PS917",
            "PracticingSpecialityRank": 4,
            "PracticingSpecialityNameIst": "Surgery Specialist",
            "PracticingSpecialityNameIsts": "Surgery Specialists",
            "RollupPracticingSpecialityCode": "PS917"
          },
          {
            "PracticingSpecialityName": "Dermatologic Oncology",
            "PracticingSpecialityCode": "PS1009",
            "PracticingSpecialityRank": 5,
            "PracticingSpecialityNameIst": "Dermatologic Oncologist",
            "PracticingSpecialityNameIsts": "Dermatologic Oncologists",
            "RollupPracticingSpecialityCode": "PS244"
          },
          {
            "PracticingSpecialityName": "Dermatologic Surgery",
            "PracticingSpecialityCode": "PS242",
            "PracticingSpecialityRank": 6,
            "PracticingSpecialityNameIst": "Dermatologic Surgery Specialist",
            "PracticingSpecialityNameIsts": "Dermatologic Surgery Specialists",
            "RollupPracticingSpecialityCode": "PS244"
          },
          {
            "PracticingSpecialityName": "Mohs Micrographic Surgery",
            "PracticingSpecialityCode": "PS484",
            "PracticingSpecialityRank": 7,
            "PracticingSpecialityNameIst": "Mohs Micrographic Surgery Specialist",
            "PracticingSpecialityNameIsts": "Mohs Micrographic Surgery Specialists",
            "RollupPracticingSpecialityCode": "PS244"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Dermatologic Oncology",
          "Dermatologic Surgery",
          "Dermatology",
          "Mohs Micrographic Surgery",
          "Plastic Surgery",
          "Surgery"
        ],
        "ProcedureIds": [
          50985,
          445,
          87,
          50965,
          1990,
          840,
          904,
          2584,
          735,
          3022,
          396,
          131,
          50890,
          50047,
          51098,
          22,
          50723,
          51721,
          51726,
          52392,
          50879,
          2259,
          62,
          50587,
          2253,
          51722,
          51866,
          51724,
          50758,
          51718,
          142,
          50783,
          51719,
          51124
        ],
        "ConditionIds": [
          534,
          710,
          9855,
          18779,
          19448,
          555,
          11131,
          51446,
          11717,
          1495,
          157,
          1588,
          20096,
          2804,
          16438,
          2946,
          19798,
          1851,
          9443,
          2163,
          9543,
          8318,
          46,
          1551,
          19465,
          2699,
          2752,
          664,
          1664,
          1666,
          2172,
          1693,
          1922,
          35,
          51357,
          18652,
          51793,
          12755,
          51079,
          1556,
          9346,
          278,
          51721,
          51789,
          4656,
          5461,
          2792,
          577,
          51794,
          1765,
          1711
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 48,
        "SurveyOverallRatingPercent": 82,
        "SurveyOverallRatingScore": 4.1,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-robert-strimling-xdc9t/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "F9D29F"
        ],
        "AffiliatedHospitalNames": [
          "Summerlin Hospital Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 98,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Dermatology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Dermatology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 2.02103,
        "PesBoost": 0.37103,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.9854551,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 12,
      "Id": "Y9QQC",
      "DemographicInfo": {
        "DisplayName": "Dr. Russell Gollard, MD",
        "DisplayLastName": "Dr. Gollard",
        "FirstName": "Russell",
        "LastName": "Gollard",
        "MiddleName": "Patrick",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-russell-gollard-y9qqc?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/9/Q/Y9QQC_w60h80_v15620.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/9/Q/Y9QQC_w90h120_v15620.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/9/Q/Y9QQC_w120h160_v15620.jpg"
          }
        ],
        "Gender": "M",
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "FIRSTB",
          "HCAREP",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL"
        ],
        "Languages": [
          "Korean",
          "Spanish",
          "Tagalog"
        ],
        "AcceptsNewPatients": true,
        "Npi": "1699772210"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.152215,
          "Longitude": -115.206288,
          "LatLon": "36.152215,-115.206288"
        },
        "Practices": [
          {
            "PracticeGuid": "BF3B5B85-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "DQR7S",
            "PracticeName": "Urology Specialists Of Nevada",
            "PracticeUrl": "http://www.usonv.com/",
            "Addresses": [
              {
                "Address1": "4750 W Oakey Blvd Fl 2",
                "OfficeCode": "OOWQBHD",
                "OfficeGuid": "5D9DCE87-4013-42E4-B62E-3AF08B57F1F4",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89102",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89102",
                    "Coordinates": {
                      "Latitude": 36.152215,
                      "Longitude": -115.206288,
                      "LatLon": "36.152215,-115.206288"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 877-5199"
                ],
                "Fax": [
                  "(702) 352-2790"
                ],
                "IsPrimary": true
              }
            ]
          },
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "6190 S Fort Apache Rd",
                "OfficeCode": "OOJXWV5",
                "OfficeGuid": "32023E5A-D3F7-495E-863D-E2A18CEC2AAF",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89148",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89148",
                    "Coordinates": {
                      "Latitude": 36.075969,
                      "Longitude": -115.297028,
                      "LatLon": "36.075969,-115.297028"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 822-2000"
                ],
                "Fax": [
                  "(702) 938-2237"
                ]
              }
            ]
          }
        ],
        "City": [
          "Las Vegas"
        ],
        "CityState": [
          "Las Vegas, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "26",
        "BoardCertificationSpecialties": [
          "Hospice Care and Palliative Medicine",
          "Hematology",
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CHCPM",
            "CertificationName": "Hospice Care and Palliative Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CHMTL",
            "CertificationName": "Hematology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Gollard's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 1,
        "SpecialistDesc": [
          "Hematology Specialist",
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          1,
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Hematology",
          "Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Hematology",
          "PracticingSpecialityCode": "PS361",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Hematology Specialist",
          "PracticingSpecialityNameIsts": "Hematology Specialists",
          "RollupPracticingSpecialityCode": "PS361"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS361",
          "Value": "Hematology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Hematology"
        ],
        "ProcedureIds": [
          229,
          50998,
          50682
        ],
        "ConditionIds": [
          14161,
          4384,
          19755,
          3997,
          12070,
          2335,
          14889,
          51091,
          126,
          4806,
          160,
          3264,
          11893,
          5128,
          50698,
          2211,
          2406,
          11392,
          13000,
          51678,
          51941,
          2454,
          51968,
          2849,
          75,
          51184,
          51106,
          2942,
          1765,
          15186,
          51975,
          17178,
          51089,
          51230,
          7536,
          2841,
          2423,
          149,
          51183,
          2774,
          170,
          1410,
          51109,
          11627,
          172,
          51101,
          51077,
          17253,
          2792,
          17704,
          3759,
          12242,
          50553,
          51043,
          2493,
          142,
          14671,
          19830,
          120,
          19102,
          162,
          51340,
          695,
          163,
          2404,
          314,
          8776,
          1693,
          668,
          18576,
          50903,
          165,
          2800,
          10653,
          20066,
          152,
          2904,
          4834,
          157,
          52142,
          51096,
          1500,
          144,
          52162,
          1495,
          51122,
          51209,
          12406,
          155,
          52137,
          130,
          1370,
          51067,
          51188,
          51075,
          51116,
          51055,
          18366,
          17191,
          153,
          164,
          156,
          169,
          51042
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 30,
        "SurveyOverallRatingPercent": 84,
        "SurveyOverallRatingScore": 4.2,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-russell-gollard-y9qqc/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "B2B744",
          "5FEB5C",
          "D6F15E",
          "3C022D",
          "F129D5",
          "F9D29F",
          "7EA9BC",
          "ADF464",
          "F2A6B7",
          "C0C277",
          "B5D7A6",
          "A0C2A7",
          "CBF7A2"
        ],
        "AffiliatedHospitalNames": [
          "Desert Springs Hospital Medical Center",
          "Southern Hills Hospital and Medical Center",
          "Spring Valley Hospital Medical Center",
          "University Medical Center of Southern Nevada",
          "North Vista Hospital",
          "Summerlin Hospital Medical Center",
          "Sunrise Hospital and Medical Center",
          "Valley Hospital Medical Center",
          "Centennial Hills Hospital Medical Center",
          "Mountainview Hospital",
          "St. Rose Dominican, Siena Campus",
          "St. Rose Dominican, Rose de Lima Campus",
          "St. Rose Dominican, San Martin Campus"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 99,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Hematology",
              "Hospice Care and Palliative Medicine",
              "Internal Medicine",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Hematology, Hospice Care and Palliative Medicine, Internal Medicine and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 1.91233,
        "PesBoost": 0.26233,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.9932251,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 13,
      "Id": "XC3D4",
      "DemographicInfo": {
        "DisplayName": "Dr. Josette E. Spotts, MD",
        "DisplayLastName": "Dr. Spotts",
        "FirstName": "Josette",
        "LastName": "Spotts",
        "MiddleName": "Ellen",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-josette-spotts-xc3d4?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/C/3/XC3D4_w60h80_v21329.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/C/3/XC3D4_w90h120_v21329.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/C/3/XC3D4_w120h160_v21329.jpg"
          }
        ],
        "Gender": "F",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nI feel it is very important that the breast surg"
        },
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "CUHEFU",
          "FIRSTB",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1780787010"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.05507,
          "Longitude": -115.04991,
          "LatLon": "36.05507,-115.04991"
        },
        "Practices": [
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "1485 W Warm Springs Rd Ste 105",
                "OfficeCode": "YCCVCJ",
                "OfficeGuid": "707D5010-B99E-4603-86E2-D16E36FC9DB4",
                "Location": {
                  "CityName": "Henderson",
                  "CityAndState": "Henderson, NV",
                  "CityStateZipBestMatch": "Henderson, NV 89014",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89014",
                    "Coordinates": {
                      "Latitude": 36.05507,
                      "Longitude": -115.04991,
                      "LatLon": "36.05507,-115.04991"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 990-6360"
                ],
                "Fax": [
                  "(702) 990-6363"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Henderson"
        ],
        "CityState": [
          "Henderson, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "34",
        "BoardCertificationSpecialties": [
          "General Surgery"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CGSUR",
            "CertificationName": "General Surgery",
            "CertifyingAuthorityCode": "RCPSC",
            "CertifyingAuthorityName": "Royal College of Physicians and Surgeons of Canada",
            "CertifyingAuthorityBoardCode": "RCPSC",
            "CertifyingAuthorityBoardName": "Royal College of Physicians and Surgeons of Canada"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Spotts's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 38,
        "SpecialistDesc": [
          "General Surgery Specialist",
          "Oncology Specialist",
          "Surgery Specialist"
        ],
        "SpecialtiesIds": [
          38,
          67,
          44
        ],
        "SpecialtiesDescriptions": [
          "General Surgery",
          "Oncology",
          "Surgery"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "General Surgery",
          "PracticingSpecialityCode": "PS329",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "General Surgery Specialist",
          "PracticingSpecialityNameIsts": "General Surgery Specialists",
          "RollupPracticingSpecialityCode": "PS329"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS329",
          "Value": "General Surgery"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS329",
          "PS917",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "General Surgery",
            "PracticingSpecialityCode": "PS329",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "General Surgery Specialist",
            "PracticingSpecialityNameIsts": "General Surgery Specialists",
            "RollupPracticingSpecialityCode": "PS329"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Surgery",
            "PracticingSpecialityCode": "PS917",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Surgery Specialist",
            "PracticingSpecialityNameIsts": "Surgery Specialists",
            "RollupPracticingSpecialityCode": "PS917"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "General Surgery",
          "Surgery"
        ],
        "ProcedureIds": [
          50596,
          50661,
          50464,
          463,
          50502,
          35
        ],
        "ConditionIds": [
          130,
          51141,
          18366,
          1765
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 27,
        "SurveyOverallRatingPercent": 86,
        "SurveyOverallRatingScore": 4.3,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-josette-spotts-xc3d4/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "7EA9BC",
          "CBF7A2"
        ],
        "AffiliatedHospitalNames": [
          "Sunrise Hospital and Medical Center",
          "St. Rose Dominican, San Martin Campus"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "General Surgery"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in General Surgery"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 1.90448,
        "PesBoost": 0.25448,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 14,
      "Id": "2QWWY",
      "DemographicInfo": {
        "DisplayName": "Dr. Nicholas J. Vogelzang, MD",
        "DisplayLastName": "Dr. Vogelzang",
        "FirstName": "Nicholas",
        "LastName": "Vogelzang",
        "MiddleName": "John",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-nicholas-vogelzang-2qwwy?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/Q/W/2QWWY_w60h80_v10004.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/Q/W/2QWWY_w90h120_v10004.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/2/Q/W/2QWWY_w120h160_v10004.jpg"
          }
        ],
        "Gender": "M",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nIt's my job to continuously educate the patient "
        },
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "CUHEFU",
          "FIRSTB",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1558361154"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.12125,
          "Longitude": -115.11826,
          "LatLon": "36.12125,-115.11826"
        },
        "Practices": [
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "3730 S Eastern Ave",
                "OfficeCode": "YCD9F2",
                "OfficeGuid": "0E98AEBA-B7A8-4E2B-A65F-ED0123746F02",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89169",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89169",
                    "Coordinates": {
                      "Latitude": 36.12125,
                      "Longitude": -115.11826,
                      "LatLon": "36.12125,-115.11826"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 952-3400"
                ],
                "Fax": [
                  "(702) 952-3461"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Las Vegas"
        ],
        "CityState": [
          "Las Vegas, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "42",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology",
          "Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CONCG",
            "CertificationName": "Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABMS",
            "CertifyingAuthorityBoardName": "American Board of Medical Specialties"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Vogelzang's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Researcher"
        ],
        "SpecialtiesIds": [
          67,
          990
        ],
        "SpecialtiesDescriptions": [
          "Medical Oncology",
          "Oncology",
          "Cancer Research"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Medical Oncology",
          "PracticingSpecialityCode": "PS456",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Medical Oncology Specialist",
          "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS456",
          "Value": "Medical Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS856",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Cancer Research",
            "PracticingSpecialityCode": "PS123",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Cancer Researcher",
            "PracticingSpecialityNameIsts": "Cancer Researchers",
            "RollupPracticingSpecialityCode": "PS856"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Cancer Research",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          229,
          50998,
          10531
        ],
        "ConditionIds": [
          120,
          165,
          14361,
          1765,
          153
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 20,
        "SurveyOverallRatingPercent": 94,
        "SurveyOverallRatingScore": 4.7,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-nicholas-vogelzang-2qwwy/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "F9D29F",
          "B2B744",
          "7EA9BC"
        ],
        "AffiliatedHospitalNames": [
          "Summerlin Hospital Medical Center",
          "Desert Springs Hospital Medical Center",
          "Sunrise Hospital and Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 99,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology",
              "Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine, Medical Oncology and Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 1.89466,
        "PesBoost": 0.24466,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.990664363,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 15,
      "Id": "X2QQM",
      "DemographicInfo": {
        "DisplayName": "Dr. James Sanchez, MD",
        "DisplayLastName": "Dr. Sanchez",
        "FirstName": "James",
        "LastName": "Sanchez",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-james-sanchez-x2qqm?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/2/Q/X2QQM_w60h80_v4224.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/2/Q/X2QQM_w90h120_v4224.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/X/2/Q/X2QQM_w120h160_v4224.jpg"
          }
        ],
        "Gender": "M",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nDr. Sanchez's goal and patient philosophy is to "
        },
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "CUHEFU",
          "FIRSTB",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL"
        ],
        "Languages": [
          "Spanish"
        ],
        "AcceptsNewPatients": true,
        "Npi": "1669481024"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.2095,
          "Longitude": -115.25639,
          "LatLon": "36.2095,-115.25639"
        },
        "Practices": [
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "7445 Peak Dr",
                "OfficeCode": "OOVP6GG",
                "OfficeGuid": "748327B3-AEFB-4ABD-9F2B-71AB33F65F6E",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89128",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89128",
                    "Coordinates": {
                      "Latitude": 36.2095,
                      "Longitude": -115.25639,
                      "LatLon": "36.2095,-115.25639"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 952-2140"
                ],
                "Fax": [
                  "(702) 952-2147"
                ],
                "IsPrimary": true
              },
              {
                "Address1": "7445 Peak Dr",
                "OfficeCode": "YCD97D",
                "OfficeGuid": "E26A4D3D-2175-45CA-B574-3BFE23EFE281",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89128",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89128",
                    "Coordinates": {
                      "Latitude": 36.2095,
                      "Longitude": -115.25639,
                      "LatLon": "36.2095,-115.25639"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 952-2140"
                ],
                "Fax": [
                  "(702) 952-2147"
                ]
              }
            ]
          }
        ],
        "City": [
          "Las Vegas"
        ],
        "CityState": [
          "Las Vegas, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "37",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology",
          "Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CONCG",
            "CertificationName": "Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABMS",
            "CertifyingAuthorityBoardName": "American Board of Medical Specialties"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Sanchez's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 1,
        "SpecialistDesc": [
          "Hematology Specialist",
          "Oncology Specialist",
          "Obstetrics & Gynecology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          1,
          67,
          45,
          22
        ],
        "SpecialtiesDescriptions": [
          "Hematology & Oncology",
          "Oncology",
          "Hematology",
          "Obstetrics & Gynecology",
          "Internal Medicine"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Hematology & Oncology",
          "PracticingSpecialityCode": "PS362",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Hematology & Oncology Specialist",
          "PracticingSpecialityNameIsts": "Hematology & Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS361"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS362",
          "Value": "Hematology & Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS412",
          "PS574",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Hematology & Oncology",
            "PracticingSpecialityCode": "PS362",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Hematology & Oncology Specialist",
            "PracticingSpecialityNameIsts": "Hematology & Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Obstetrics & Gynecology",
            "PracticingSpecialityCode": "PS574",
            "PracticingSpecialityRank": 4,
            "PracticingSpecialityNameIst": "Obstetrics & Gynecology Specialist",
            "PracticingSpecialityNameIsts": "Obstetrics & Gynecology Specialists",
            "RollupPracticingSpecialityCode": "PS574"
          },
          {
            "PracticingSpecialityName": "Internal Medicine",
            "PracticingSpecialityCode": "PS412",
            "PracticingSpecialityRank": 5,
            "PracticingSpecialityNameIst": "Internist",
            "PracticingSpecialityNameIsts": "Internists",
            "RollupPracticingSpecialityCode": "PS412"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Hematology",
          "Hematology & Oncology",
          "Internal Medicine",
          "Obstetrics & Gynecology"
        ],
        "ProcedureIds": [
          229,
          50998,
          2287
        ],
        "ConditionIds": [
          51043,
          170,
          3997,
          17191,
          2774,
          172,
          142,
          13000,
          3264,
          163,
          14671,
          2493,
          2454,
          1395,
          2841,
          165,
          51059,
          51089,
          51678,
          2904,
          51091,
          51055,
          2406,
          160,
          17178,
          51106,
          51096,
          51184,
          51111,
          120,
          19102,
          2211,
          75,
          18576,
          144,
          155,
          51340,
          51975,
          51057,
          695,
          15186,
          12070,
          51122,
          2800,
          149,
          4806,
          130,
          51921,
          1500,
          12242,
          18366,
          162,
          51968,
          51188,
          2404,
          51109,
          2849,
          51127,
          19755,
          17253,
          164,
          50553,
          2792,
          51075,
          51067,
          156,
          157,
          2710,
          668,
          126,
          51116,
          52137,
          152,
          4384,
          14161,
          7536,
          1765,
          169,
          11392,
          1495,
          1693,
          51183,
          841,
          1410,
          20066,
          50903,
          1370,
          52162,
          3759,
          51050,
          17704,
          11627,
          4834,
          153,
          52142,
          51209,
          8776
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 18,
        "SurveyOverallRatingPercent": 96,
        "SurveyOverallRatingScore": 4.8,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-james-sanchez-x2qqm/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "7EA9BC",
          "C0C277",
          "B5D7A6",
          "CBF7A2",
          "A8F53E",
          "ADF464",
          "B2B744",
          "F2A6B7",
          "F9D29F"
        ],
        "AffiliatedHospitalNames": [
          "Sunrise Hospital and Medical Center",
          "Mountainview Hospital",
          "St. Rose Dominican, Siena Campus",
          "St. Rose Dominican, San Martin Campus",
          "Boulder City Hospital",
          "Valley Hospital Medical Center",
          "Desert Springs Hospital Medical Center",
          "Centennial Hills Hospital Medical Center",
          "Summerlin Hospital Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology",
              "Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine, Medical Oncology and Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 1.88595,
        "PesBoost": 0.23595,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 16,
      "Id": "YSYQY",
      "DemographicInfo": {
        "DisplayName": "Dr. Karen S. Jacks, MD",
        "DisplayLastName": "Dr. Jacks",
        "FirstName": "Karen",
        "LastName": "Jacks",
        "MiddleName": "Stewart",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-karen-jacks-ysyqy?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/S/Y/YSYQY_w60h80_v10004.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/S/Y/YSYQY_w90h120_v10004.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/Y/S/Y/YSYQY_w120h160_v10004.jpg"
          }
        ],
        "Gender": "F",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nMy philosophy is to care for each patient as a s"
        },
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "CUHEFU",
          "FIRSTB",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1457577470"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.0718,
          "Longitude": -115.29489,
          "LatLon": "36.0718,-115.29489"
        },
        "Practices": [
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "9280 W Sunset Rd Ste 100",
                "OfficeCode": "YCD9XP",
                "OfficeGuid": "05C37E9F-08F5-4DA5-AF9D-F83315032E19",
                "Location": {
                  "CityName": "Las Vegas",
                  "CityAndState": "Las Vegas, NV",
                  "CityStateZipBestMatch": "Las Vegas, NV 89148",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89148",
                    "Coordinates": {
                      "Latitude": 36.0718,
                      "Longitude": -115.29489,
                      "LatLon": "36.0718,-115.29489"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 952-1251"
                ],
                "Fax": [
                  "(702) 952-1241"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Las Vegas"
        ],
        "CityState": [
          "Las Vegas, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "16",
        "BoardCertificationSpecialties": [
          "Hematology",
          "Internal Medicine",
          "Medical Oncology",
          "Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CHMTL",
            "CertificationName": "Hematology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABMS",
            "CertifyingAuthorityBoardName": "American Board of Medical Specialties"
          },
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CONCG",
            "CertificationName": "Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABMS",
            "CertifyingAuthorityBoardName": "American Board of Medical Specialties"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Jacks's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Hematology Specialist",
          "Researcher"
        ],
        "SpecialtiesIds": [
          67,
          1,
          990
        ],
        "SpecialtiesDescriptions": [
          "Medical Oncology",
          "Hematology",
          "Oncology",
          "Clinical Research"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Medical Oncology",
          "PracticingSpecialityCode": "PS456",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Medical Oncology Specialist",
          "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS456",
          "Value": "Medical Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS856",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Clinical Research",
            "PracticingSpecialityCode": "PS186",
            "PracticingSpecialityRank": 4,
            "PracticingSpecialityNameIst": "Clinical Researcher",
            "PracticingSpecialityNameIsts": "Clinical Researchers",
            "RollupPracticingSpecialityCode": "PS856"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Clinical Research",
          "Hematology",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          50998,
          229
        ],
        "ConditionIds": [
          130,
          841,
          163,
          2904,
          1395,
          1765,
          172,
          126,
          52137,
          52142,
          1370,
          164
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 20,
        "SurveyOverallRatingPercent": 88,
        "SurveyOverallRatingScore": 4.4,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-karen-jacks-ysyqy/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "5FEB5C",
          "D6F15E",
          "F9D29F",
          "3C022D",
          "CBF7A2",
          "B5D7A6"
        ],
        "AffiliatedHospitalNames": [
          "Southern Hills Hospital and Medical Center",
          "Spring Valley Hospital Medical Center",
          "Summerlin Hospital Medical Center",
          "University Medical Center of Southern Nevada",
          "St. Rose Dominican, San Martin Campus",
          "St. Rose Dominican, Siena Campus"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 97,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Hematology",
              "Internal Medicine",
              "Medical Oncology",
              "Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Hematology, Internal Medicine, Medical Oncology and Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 1.86129,
        "PesBoost": 0.21129,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.9756141,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 17,
      "Id": "2HMVJ",
      "DemographicInfo": {
        "DisplayName": "Dr. Sowjanya Reganti, MD",
        "DisplayLastName": "Dr. Reganti",
        "FirstName": "Sowjanya",
        "LastName": "Reganti",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-sowjanya-reganti-2hmvj?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-female_w120h160_v1.jpg"
          }
        ],
        "Gender": "F",
        "Payors": [
          "AETNA",
          "ANTHEA",
          "CIGNA",
          "FIRSTB",
          "MULTIP",
          "UNITHC"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1356482020"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 39.53127,
          "Longitude": -119.81848,
          "LatLon": "39.53127,-119.81848"
        },
        "Practices": [
          {
            "PracticeGuid": "B4860CC5-5E6B-4C4B-9D50-E0B24393D38B",
            "PracticeId": "PPP8SYY",
            "PracticeName": "CANCER CARE SPECIALISTS",
            "PracticeUrl": "ccsreno.com",
            "Addresses": [
              {
                "Address1": "236 W 6th St Ste 400",
                "OfficeCode": "OOO3SJW",
                "OfficeGuid": "4D04422A-A459-4240-8929-518132C42099",
                "Location": {
                  "CityName": "Reno",
                  "CityAndState": "Reno, NV",
                  "CityStateZipBestMatch": "Reno, NV 89503",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89503",
                    "Coordinates": {
                      "Latitude": 39.53127,
                      "Longitude": -119.81848,
                      "LatLon": "39.53127,-119.81848"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 329-0873"
                ],
                "Fax": [
                  "(775) 329-1026"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Reno"
        ],
        "CityState": [
          "Reno, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "15",
        "BoardCertificationSpecialties": [
          "Hematology",
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CHMTL",
            "CertificationName": "Hematology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Reganti's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 1,
        "SpecialistDesc": [
          "Hematology Specialist",
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          1,
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Hematology",
          "Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Hematology",
          "PracticingSpecialityCode": "PS361",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Hematology Specialist",
          "PracticingSpecialityNameIsts": "Hematology Specialists",
          "RollupPracticingSpecialityCode": "PS361"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS361",
          "Value": "Hematology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS361",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Hematology",
            "PracticingSpecialityCode": "PS361",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Hematology Specialist",
            "PracticingSpecialityNameIsts": "Hematology Specialists",
            "RollupPracticingSpecialityCode": "PS361"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Hematology"
        ],
        "ProcedureIds": [
          50468,
          3125,
          1379,
          50682
        ],
        "ConditionIds": [
          2286,
          120,
          19755,
          52042,
          14161,
          17191,
          3997,
          12242,
          149,
          142,
          51043,
          3264,
          51968,
          51678,
          2454,
          2335,
          51184,
          51925,
          157,
          13000,
          2792,
          163,
          51091,
          160,
          165,
          4737,
          19102,
          155,
          51183,
          51096,
          2211,
          2841,
          2904,
          1495,
          144,
          17253,
          3759,
          51089,
          51116,
          52137,
          4806,
          164,
          51975,
          51067,
          19830,
          51122,
          2710,
          170,
          52162,
          51109,
          2404,
          169,
          10653,
          17178,
          11893,
          12070,
          2406,
          51106,
          51055,
          2493,
          668,
          1410,
          152,
          2774,
          156,
          51127,
          150,
          11113,
          51075,
          75,
          14671,
          52142,
          17704,
          12406,
          15186,
          51111,
          130,
          126,
          7536,
          51230,
          1500,
          51911,
          18576,
          51921,
          52169,
          51340,
          20066,
          51188,
          11414,
          18366,
          153,
          4384,
          51209,
          11627,
          50903,
          50698,
          51042,
          2800,
          1370,
          4834,
          14889,
          8776,
          1765,
          695,
          2849,
          2942,
          11392
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 16,
        "SurveyOverallRatingPercent": 90,
        "SurveyOverallRatingScore": 4.5,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-sowjanya-reganti-2hmvj/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "30D73B",
          "C53DEB"
        ],
        "AffiliatedHospitalNames": [
          "Renown Regional Medical Center",
          "Saint Mary's Regional Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Hematology",
              "Internal Medicine",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Hematology, Internal Medicine and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 1.83793,
        "PesBoost": 0.18793,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 18,
      "Id": "3FVSG",
      "DemographicInfo": {
        "DisplayName": "Dr. MaryAnn K. Allison, MD",
        "DisplayLastName": "Dr. Allison",
        "FirstName": "MaryAnn",
        "LastName": "Allison",
        "MiddleName": "Keeper",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-mary-ann-allison-3fvsg?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/3/F/V/3FVSG_w60h80_v1853.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/3/F/V/3FVSG_w90h120_v1853.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/prov/3/F/V/3FVSG_w120h160_v1853.jpg"
          }
        ],
        "Gender": "F",
        "CarePhilosophy": {
          "IsShortened": true,
          "Text": "\nI always try to assure the patient that I will o"
        },
        "Payors": [
          "AETNA",
          "AMERHC",
          "BEECHA",
          "BLUECG",
          "CIGNA",
          "COHECA",
          "CUHEFU",
          "FIRSTB",
          "HETHCH",
          "HUMANA",
          "MEDAID",
          "ONEHLT",
          "BU000031",
          "SIERRA",
          "TRICAR",
          "UNITHC",
          "USAHEA",
          "VEADPL"
        ],
        "Languages": [
          "Spanish"
        ],
        "AcceptsNewPatients": true,
        "Npi": "1952317794"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 36.03183,
          "Longitude": -115.04945,
          "LatLon": "36.03183,-115.04945"
        },
        "Practices": [
          {
            "PracticeGuid": "29CF7785-8943-E111-B3AF-B499BAA4D952",
            "PracticeId": "FLQ6B",
            "PracticeName": "Comprehensive Cancer Centers of Nevada",
            "PracticeUrl": "http://www.cccnevada.com",
            "Addresses": [
              {
                "Address1": "1505 Wigwam Pkwy Ste 130",
                "OfficeCode": "OOVP6KP",
                "OfficeGuid": "A4738CE8-1776-48CF-A09C-D637F62922E4",
                "Location": {
                  "CityName": "Henderson",
                  "CityAndState": "Henderson, NV",
                  "CityStateZipBestMatch": "Henderson, NV 89074",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89074",
                    "Coordinates": {
                      "Latitude": 36.03183,
                      "Longitude": -115.04945,
                      "LatLon": "36.03183,-115.04945"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(702) 856-1400"
                ],
                "Fax": [
                  "(702) 856-1407"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Henderson"
        ],
        "CityState": [
          "Henderson, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "34",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology",
          "Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CONCG",
            "CertificationName": "Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABMS",
            "CertifyingAuthorityBoardName": "American Board of Medical Specialties"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Allison's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Researcher"
        ],
        "SpecialtiesIds": [
          67,
          990
        ],
        "SpecialtiesDescriptions": [
          "Medical Oncology",
          "Oncology",
          "Cancer Research"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Medical Oncology",
          "PracticingSpecialityCode": "PS456",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Medical Oncology Specialist",
          "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS456",
          "Value": "Medical Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS856",
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Cancer Research",
            "PracticingSpecialityCode": "PS123",
            "PracticingSpecialityRank": 3,
            "PracticingSpecialityNameIst": "Cancer Researcher",
            "PracticingSpecialityNameIsts": "Cancer Researchers",
            "RollupPracticingSpecialityCode": "PS856"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Cancer Research",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          2885,
          51110,
          2145,
          229
        ],
        "ConditionIds": [
          130,
          1765
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 18,
        "SurveyOverallRatingPercent": 86,
        "SurveyOverallRatingScore": 4.3,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-mary-ann-allison-3fvsg/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "7EA9BC",
          "5FEB5C",
          "C0C277",
          "B5D7A6",
          "CBF7A2",
          "ADF464",
          "D6F15E",
          "B2B744",
          "A8F53E",
          "F9D29F"
        ],
        "AffiliatedHospitalNames": [
          "Sunrise Hospital and Medical Center",
          "Southern Hills Hospital and Medical Center",
          "Mountainview Hospital",
          "St. Rose Dominican, Siena Campus",
          "St. Rose Dominican, San Martin Campus",
          "Valley Hospital Medical Center",
          "Spring Valley Hospital Medical Center",
          "Desert Springs Hospital Medical Center",
          "Boulder City Hospital",
          "Summerlin Hospital Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 98,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology",
              "Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine, Medical Oncology and Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 1.83465993,
        "PesBoost": 0.18466,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 0.985586762,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    },
    {
      "ResultIndex": 19,
      "Id": "YMNM4",
      "DemographicInfo": {
        "DisplayName": "Dr. Forrest C. Conrath, MD",
        "DisplayLastName": "Dr. Conrath",
        "FirstName": "Forrest",
        "LastName": "Conrath",
        "MiddleName": "Craig",
        "ProfessionalType": "DOC",
        "ProviderUrl": "http://www.healthgrades.com/physician/dr-forrest-conrath-ymnm4?cid=PBHTEST_007",
        "ImagePaths": [
          {
            "Type": "small",
            "Description": "small image",
            "Width": 60,
            "Height": 80,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w60h80_v1.jpg"
          },
          {
            "Type": "medium",
            "Description": "medium image",
            "Width": 90,
            "Height": 120,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w90h120_v1.jpg"
          },
          {
            "Type": "large",
            "Description": "large image",
            "Width": 120,
            "Height": 160,
            "Url": "http://d1ffafozi03i4l.cloudfront.net/img/silhouettes/silhouette-male_w120h160_v1.jpg"
          }
        ],
        "Gender": "M",
        "Payors": [
          "AETNA",
          "ANTHEA",
          "ASSURH",
          "BLUECG",
          "CIGNA",
          "COINCO",
          "CORESC",
          "DELTHS",
          "FIRSTB",
          "GOLDER",
          "GOVERA",
          "GRHECO",
          "HEALTA",
          "HUMANA",
          "MEDHEI",
          "MEDAID",
          "MULTIP",
          "NATELE",
          "PRINLI",
          "TRICAR",
          "UNITHC"
        ],
        "Languages": [],
        "AcceptsNewPatients": true,
        "Npi": "1487694956"
      },
      "Offices": {
        "OfficeCoordinates": {
          "Latitude": 39.47085,
          "Longitude": -119.81025,
          "LatLon": "39.47085,-119.81025"
        },
        "Practices": [
          {
            "PracticeGuid": "81AFDDB9-9043-E111-B3AF-B499BAA4D952",
            "PracticeId": "FRTDR",
            "PracticeName": "Reno Oncology Consultants",
            "PracticeUrl": "renooncology.com",
            "Addresses": [
              {
                "Address1": "6130 Plumas St",
                "OfficeCode": "YBDDP5",
                "OfficeGuid": "97DB2C8F-E021-4BDA-9ED8-82E4A62369B2",
                "Location": {
                  "CityName": "Reno",
                  "CityAndState": "Reno, NV",
                  "CityStateZipBestMatch": "Reno, NV 89519",
                  "LocRegion": {
                    "RegionAbbreviation": "NV",
                    "RegionName": "Nevada",
                    "Zip": "89519",
                    "Coordinates": {
                      "Latitude": 39.47085,
                      "Longitude": -119.81025,
                      "LatLon": "39.47085,-119.81025"
                    },
                    "Nation": "USA"
                  }
                },
                "Phone": [
                  "(775) 329-0222"
                ],
                "Fax": [
                  "(775) 329-3010"
                ],
                "IsPrimary": true
              }
            ]
          }
        ],
        "City": [
          "Reno"
        ],
        "CityState": [
          "Reno, NV"
        ],
        "State": [
          "NV"
        ]
      },
      "Certifications": {
        "YearsSinceGraduation": "37",
        "BoardCertificationSpecialties": [
          "Internal Medicine",
          "Medical Oncology"
        ],
        "ProviderCertifications": [
          {
            "CertificationCode": "CITMD",
            "CertificationName": "Internal Medicine",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          },
          {
            "CertificationCode": "CMONC",
            "CertificationName": "Medical Oncology",
            "CertifyingAuthorityCode": "ABMS",
            "CertifyingAuthorityName": "American Board of Medical Specialties",
            "CertifyingAuthorityBoardCode": "ABIMMD",
            "CertifyingAuthorityBoardName": "American Board of Internal Medicine"
          }
        ],
        "HasPremiumDegree": true,
        "IsBoardCertified": true,
        "WhyItMatters": {
          "DisplayText": "Why It Matters: Dr. Conrath's Board Certifications"
        }
      },
      "SpecialtyProcedureConditions": {
        "PrimarySpecialtyId": 67,
        "SpecialistDesc": [
          "Oncology Specialist",
          "Internist"
        ],
        "SpecialtiesIds": [
          67,
          22
        ],
        "SpecialtiesDescriptions": [
          "Oncology",
          "Medical Oncology"
        ],
        "PrimaryPracticingSpecialty": {
          "PracticingSpecialityName": "Oncology",
          "PracticingSpecialityCode": "PS592",
          "PracticingSpecialityRank": 1,
          "PracticingSpecialityNameIst": "Oncology Specialist",
          "PracticingSpecialityNameIsts": "Oncology Specialists",
          "RollupPracticingSpecialityCode": "PS592"
        },
        "PrimaryPracticingSpecialtyCodeDescription": {
          "Key": "PS592",
          "Value": "Oncology"
        },
        "PracticingSpecialtyRollupCodes": [
          "PS592"
        ],
        "ProviderPracticingSpecialties": [
          {
            "PracticingSpecialityName": "Oncology",
            "PracticingSpecialityCode": "PS592",
            "PracticingSpecialityRank": 1,
            "PracticingSpecialityNameIst": "Oncology Specialist",
            "PracticingSpecialityNameIsts": "Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          },
          {
            "PracticingSpecialityName": "Medical Oncology",
            "PracticingSpecialityCode": "PS456",
            "PracticingSpecialityRank": 2,
            "PracticingSpecialityNameIst": "Medical Oncology Specialist",
            "PracticingSpecialityNameIsts": "Medical Oncology Specialists",
            "RollupPracticingSpecialityCode": "PS592"
          }
        ],
        "PracticingSpecialtiesDisplay": [
          "Oncology",
          "Medical Oncology"
        ],
        "ProcedureIds": [
          1379,
          50468,
          3125,
          50682
        ],
        "ConditionIds": [
          19755,
          150,
          12406,
          52042,
          17191,
          170,
          2774,
          149,
          172,
          142,
          3264,
          51043,
          51055,
          51184,
          51678,
          51077,
          157,
          51059,
          12070,
          51968,
          51925,
          17253,
          51941,
          163,
          19102,
          75,
          160,
          51096,
          2493,
          155,
          2841,
          837,
          11893,
          14671,
          11717,
          2211,
          51116,
          51042,
          156,
          1495,
          4384,
          14161,
          14889,
          4737,
          51921,
          51067,
          15186,
          1410,
          164,
          2406,
          51127,
          17178,
          51122,
          2800,
          51188,
          2286,
          2423,
          52015,
          668,
          3767,
          51089,
          2454,
          165,
          51106,
          120,
          1370,
          1500,
          51911,
          51075,
          51975,
          10653,
          51091,
          52137,
          51109,
          20066,
          2792,
          18576,
          169,
          2904,
          152,
          2710,
          13000,
          130,
          162,
          51340,
          3759,
          153,
          11627,
          126,
          19830,
          18366,
          52162,
          51209,
          52142,
          11392,
          50903,
          11414,
          8776,
          4834,
          17704,
          695,
          1765,
          4806,
          52169,
          11113
        ]
      },
      "PatientSatisfaction": {
        "SurveyUserCount": 14,
        "SurveyOverallRatingPercent": 92,
        "SurveyOverallRatingScore": 4.6,
        "IsRecommendedProvider": true,
        "SuppressSurveys": false,
        "TakeASurvey": {
          "DisplayText": "Take A Survey",
          "Url": "http://www.healthgrades.com/physician/dr-forrest-conrath-ymnm4/rate-doctor#QualitySurvey_anchor?cid=PBHTEST_007"
        }
      },
      "HospitalQuality": {
        "HasTopHospital": false,
        "HasSpecialtyExcellenceHospital": false,
        "HasTreatmentExcellenceHospital": false,
        "AffiliatedHospitalCodes": [
          "9698E8",
          "30D73B",
          "C53DEB"
        ],
        "AffiliatedHospitalNames": [
          "Northern Nevada Medical Center",
          "Renown Regional Medical Center",
          "Saint Mary's Regional Medical Center"
        ]
      },
      "MatchMessages": {
        "Messages": [
          {
            "category": "PracticingSpecialty",
            "message": "Oncology",
            "matchType": "Match"
          },
          {
            "category": "Distance",
            "message": "In ",
            "matchType": "Match"
          }
        ]
      },
      "Experience": {
        "ExperienceScore": 100,
        "ExperienceMatchMessages": [
          {
            "messageData": [
              "Oncology"
            ],
            "category": "PracticingSpecialty",
            "matchType": "Match",
            "message": "Specializes in Oncology"
          },
          {
            "messageData": [
              "Internal Medicine",
              "Medical Oncology"
            ],
            "category": "BoardCertification",
            "matchType": "Match",
            "message": "Board certified in Internal Medicine and Medical Oncology"
          },
          {
            "messageData": [],
            "category": "Degree",
            "matchType": "Match"
          },
          {
            "messageData": [],
            "category": "NoBoardAction",
            "matchType": "Match",
            "message": "No board actions found"
          },
          {
            "messageData": [],
            "category": "NoMalpractice",
            "matchType": "FuzzyMatch",
            "message": "Malpractice claims not available"
          },
          {
            "messageData": [],
            "category": "NoSanction",
            "matchType": "Match",
            "message": "No sanctions found"
          },
          {
            "messageData": [],
            "category": "TotalPatientVolume",
            "matchType": "Match",
            "message": "Based on total number of patients treated over the last 12 months"
          }
        ]
      },
      "BoardActions": {
        "HasBoardAction": false,
        "HasMalpractice": false,
        "HasMalpracticeState": false,
        "HasSanction": false
      },
      "BoostValues": {
        "ScoreBoost": 1.82921994,
        "PesBoost": 0.17922,
        "DegreeBoost": 0.4,
        "CertificationBoost": 0.25,
        "LegalBoost": 0,
        "SanctionBoost": 0.4,
        "ExperienceBoost": 1,
        "HospitalQualityBoost": 0,
        "BoardActionBoost": 0.4,
        "MalpracticeBoost": 0.1,
        "DistanceBoost": 0
      }
    }
  ],
  "Facets": [
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Female",
            "DisplayCount": "31",
            "Value": "F",
            "Data": "F",
            "Id": "F",
            "Content": {}
          },
          {
            "DisplayText": "Male",
            "DisplayCount": "78",
            "Value": "M",
            "Data": "M",
            "Id": "M",
            "Content": {}
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Male",
            "DisplayCount": "78",
            "Value": "M",
            "Data": "M",
            "Id": "M",
            "Content": {}
          },
          {
            "DisplayText": "Female",
            "DisplayCount": "31",
            "Value": "F",
            "Data": "F",
            "Id": "F",
            "Content": {}
          }
        ],
        "TopViewAllValues": []
      },
      "FacetKey": "gender"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Arabic",
            "DisplayCount": "3",
            "Value": "Arabic",
            "Data": "Arabic",
            "Id": "Arabic",
            "Content": {}
          },
          {
            "DisplayText": "Bengali",
            "DisplayCount": "1",
            "Value": "Bengali",
            "Data": "Bengali",
            "Id": "Bengali",
            "Content": {}
          },
          {
            "DisplayText": "Chinese",
            "DisplayCount": "7",
            "Value": "Chinese",
            "Data": "Chinese",
            "Id": "Chinese",
            "Content": {}
          },
          {
            "DisplayText": "French",
            "DisplayCount": "3",
            "Value": "French",
            "Data": "French",
            "Id": "French",
            "Content": {}
          },
          {
            "DisplayText": "German",
            "DisplayCount": "3",
            "Value": "German",
            "Data": "German",
            "Id": "German",
            "Content": {}
          },
          {
            "DisplayText": "Greek",
            "DisplayCount": "6",
            "Value": "Greek",
            "Data": "Greek",
            "Id": "Greek",
            "Content": {}
          },
          {
            "DisplayText": "Gujarati",
            "DisplayCount": "1",
            "Value": "Gujarati",
            "Data": "Gujarati",
            "Id": "Gujarati",
            "Content": {}
          },
          {
            "DisplayText": "Hindi",
            "DisplayCount": "3",
            "Value": "Hindi",
            "Data": "Hindi",
            "Id": "Hindi",
            "Content": {}
          },
          {
            "DisplayText": "Korean",
            "DisplayCount": "6",
            "Value": "Korean",
            "Data": "Korean",
            "Id": "Korean",
            "Content": {}
          },
          {
            "DisplayText": "Malay",
            "DisplayCount": "1",
            "Value": "Malay",
            "Data": "Malay",
            "Id": "Malay",
            "Content": {}
          },
          {
            "DisplayText": "Mandarin",
            "DisplayCount": "1",
            "Value": "Mandarin",
            "Data": "Mandarin",
            "Id": "Mandarin",
            "Content": {}
          },
          {
            "DisplayText": "Persian",
            "DisplayCount": "1",
            "Value": "Persian",
            "Data": "Persian",
            "Id": "Persian",
            "Content": {}
          },
          {
            "DisplayText": "Polish",
            "DisplayCount": "1",
            "Value": "Polish",
            "Data": "Polish",
            "Id": "Polish",
            "Content": {}
          },
          {
            "DisplayText": "Punjabi",
            "DisplayCount": "1",
            "Value": "Punjabi",
            "Data": "Punjabi",
            "Id": "Punjabi",
            "Content": {}
          },
          {
            "DisplayText": "Romanian",
            "DisplayCount": "1",
            "Value": "Romanian",
            "Data": "Romanian",
            "Id": "Romanian",
            "Content": {}
          },
          {
            "DisplayText": "Spanish",
            "DisplayCount": "49",
            "Value": "Spanish",
            "Data": "Spanish",
            "Id": "Spanish",
            "Content": {}
          },
          {
            "DisplayText": "Tagalog",
            "DisplayCount": "14",
            "Value": "Tagalog",
            "Data": "Tagalog",
            "Id": "Tagalog",
            "Content": {}
          },
          {
            "DisplayText": "Urdu",
            "DisplayCount": "1",
            "Value": "Urdu",
            "Data": "Urdu",
            "Id": "Urdu",
            "Content": {}
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Spanish",
            "DisplayCount": "49",
            "Value": "Spanish",
            "Data": "Spanish",
            "Id": "Spanish",
            "Content": {}
          },
          {
            "DisplayText": "Tagalog",
            "DisplayCount": "14",
            "Value": "Tagalog",
            "Data": "Tagalog",
            "Id": "Tagalog",
            "Content": {}
          },
          {
            "DisplayText": "Chinese",
            "DisplayCount": "7",
            "Value": "Chinese",
            "Data": "Chinese",
            "Id": "Chinese",
            "Content": {}
          }
        ],
        "TopViewAllValues": []
      },
      "FacetKey": "languages"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Aetna",
            "DisplayCount": "91",
            "Value": "Aetna|AETNA",
            "Id": "AETNA",
            "Content": {}
          },
          {
            "DisplayText": "Affiliated Health Funds",
            "DisplayCount": "1",
            "Value": "Affiliated Health Funds|AFHEFU",
            "Id": "AFHEFU",
            "Content": {}
          },
          {
            "DisplayText": "Altius Health Plans",
            "DisplayCount": "1",
            "Value": "Altius Health Plans|ALTIHP",
            "Id": "ALTIHP",
            "Content": {}
          },
          {
            "DisplayText": "Amalgamated Clothing & Textile Workers Union",
            "DisplayCount": "1",
            "Value": "Amalgamated Clothing & Textile Workers Union|AMCTWU",
            "Id": "AMCTWU",
            "Content": {}
          },
          {
            "DisplayText": "American Enterprise Group",
            "DisplayCount": "1",
            "Value": "American Enterprise Group|AMENGR",
            "Id": "AMENGR",
            "Content": {}
          },
          {
            "DisplayText": "American Republic",
            "DisplayCount": "5",
            "Value": "American Republic|AMERREP",
            "Id": "AMERREP",
            "Content": {}
          },
          {
            "DisplayText": "America's Health Choice",
            "DisplayCount": "32",
            "Value": "America's Health Choice|AMERHC",
            "Id": "AMERHC",
            "Content": {}
          },
          {
            "DisplayText": "Amerigroup (Wellpoint)",
            "DisplayCount": "11",
            "Value": "Amerigroup (Wellpoint)|AMERIB",
            "Id": "AMERIB",
            "Content": {}
          },
          {
            "DisplayText": "Anthem",
            "DisplayCount": "2",
            "Value": "Anthem|HPY0000768",
            "Id": "HPY0000768",
            "Content": {}
          },
          {
            "DisplayText": "Anthem Blue Cross Blue Shield",
            "DisplayCount": "35",
            "Value": "Anthem Blue Cross Blue Shield|ANTHEA",
            "Id": "ANTHEA",
            "Content": {}
          },
          {
            "DisplayText": "Arizona Health Care Cost Containment System (AHCCCS)",
            "DisplayCount": "1",
            "Value": "Arizona Health Care Cost Containment System (AHCCCS)|ARIZOA",
            "Id": "ARIZOA",
            "Content": {}
          },
          {
            "DisplayText": "Assurant Health",
            "DisplayCount": "9",
            "Value": "Assurant Health|ASSURH",
            "Id": "ASSURH",
            "Content": {}
          },
          {
            "DisplayText": "Beech Street (Multiplan)",
            "DisplayCount": "38",
            "Value": "Beech Street (Multiplan)|BEECHA",
            "Id": "BEECHA",
            "Content": {}
          },
          {
            "DisplayText": "Blue Cross Blue Shield",
            "DisplayCount": "89",
            "Value": "Blue Cross Blue Shield|BLUECG",
            "Id": "BLUECG",
            "Content": {}
          },
          {
            "DisplayText": "Blue Cross Blue Shield of California",
            "DisplayCount": "7",
            "Value": "Blue Cross Blue Shield of California|BLUECF",
            "Id": "BLUECF",
            "Content": {}
          },
          {
            "DisplayText": "Blue Cross Blue Shield of Louisiana",
            "DisplayCount": "1",
            "Value": "Blue Cross Blue Shield of Louisiana|BLUEEE",
            "Id": "BLUEEE",
            "Content": {}
          },
          {
            "DisplayText": "Blue Cross Blue Shield of Massachusetts",
            "DisplayCount": "1",
            "Value": "Blue Cross Blue Shield of Massachusetts|BLUECO",
            "Id": "BLUECO",
            "Content": {}
          },
          {
            "DisplayText": "Blue Cross Blue Shield of Michigan",
            "DisplayCount": "1",
            "Value": "Blue Cross Blue Shield of Michigan|BLUECX",
            "Id": "BLUECX",
            "Content": {}
          },
          {
            "DisplayText": "Blue Cross Blue Shield of Texas",
            "DisplayCount": "1",
            "Value": "Blue Cross Blue Shield of Texas|BLUECZ",
            "Id": "BLUECZ",
            "Content": {}
          },
          {
            "DisplayText": "Blue Shield of California",
            "DisplayCount": "1",
            "Value": "Blue Shield of California|BLSHCA",
            "Id": "BLSHCA",
            "Content": {}
          },
          {
            "DisplayText": "Capital District Physician's Health Plan (CDPHP)",
            "DisplayCount": "1",
            "Value": "Capital District Physician's Health Plan (CDPHP)|CAPITB",
            "Id": "CAPITB",
            "Content": {}
          },
          {
            "DisplayText": "Caremore Medical Group",
            "DisplayCount": "1",
            "Value": "Caremore Medical Group|CAREMR",
            "Id": "CAREMR",
            "Content": {}
          },
          {
            "DisplayText": "CareOregon",
            "DisplayCount": "1",
            "Value": "CareOregon|HPY0000788",
            "Id": "HPY0000788",
            "Content": {}
          },
          {
            "DisplayText": "CareSource",
            "DisplayCount": "3",
            "Value": "CareSource|CARESO",
            "Id": "CARESO",
            "Content": {}
          },
          {
            "DisplayText": "CHAMPVA",
            "DisplayCount": "5",
            "Value": "CHAMPVA|CHAMPV",
            "Id": "CHAMPV",
            "Content": {}
          },
          {
            "DisplayText": "Cigna",
            "DisplayCount": "93",
            "Value": "Cigna|CIGNA",
            "Id": "CIGNA",
            "Content": {}
          },
          {
            "DisplayText": "Commercial Insurance Company",
            "DisplayCount": "22",
            "Value": "Commercial Insurance Company|COINCO",
            "Id": "COINCO",
            "Content": {}
          },
          {
            "DisplayText": "Community Care Network",
            "DisplayCount": "1",
            "Value": "Community Care Network|COMCAN",
            "Id": "COMCAN",
            "Content": {}
          },
          {
            "DisplayText": "Community Health Choice",
            "DisplayCount": "3",
            "Value": "Community Health Choice|COMMHC",
            "Id": "COMMHC",
            "Content": {}
          },
          {
            "DisplayText": "CoreSource",
            "DisplayCount": "4",
            "Value": "CoreSource|CORESC",
            "Id": "CORESC",
            "Content": {}
          },
          {
            "DisplayText": "Coventry Health Care",
            "DisplayCount": "51",
            "Value": "Coventry Health Care|COHECA",
            "Id": "COHECA",
            "Content": {}
          },
          {
            "DisplayText": "Culinary Health Fund",
            "DisplayCount": "38",
            "Value": "Culinary Health Fund|CUHEFU",
            "Id": "CUHEFU",
            "Content": {}
          },
          {
            "DisplayText": "Delta Health System",
            "DisplayCount": "8",
            "Value": "Delta Health System|DELTHS",
            "Id": "DELTHS",
            "Content": {}
          },
          {
            "DisplayText": "Elderplan",
            "DisplayCount": "3",
            "Value": "Elderplan|ELDERA",
            "Id": "ELDERA",
            "Content": {}
          },
          {
            "DisplayText": "EmblemHealth",
            "DisplayCount": "5",
            "Value": "EmblemHealth|EMBLEA",
            "Id": "EMBLEA",
            "Content": {}
          },
          {
            "DisplayText": "Empire Blue Cross Blue Shield",
            "DisplayCount": "1",
            "Value": "Empire Blue Cross Blue Shield|EMPIRA",
            "Id": "EMPIRA",
            "Content": {}
          },
          {
            "DisplayText": "Fidelis Care",
            "DisplayCount": "1",
            "Value": "Fidelis Care|FIDELC",
            "Id": "FIDELC",
            "Content": {}
          },
          {
            "DisplayText": "First Health (Coventry Health Care)",
            "DisplayCount": "81",
            "Value": "First Health (Coventry Health Care)|FIRSTB",
            "Id": "FIRSTB",
            "Content": {}
          },
          {
            "DisplayText": "Golden Rule",
            "DisplayCount": "11",
            "Value": "Golden Rule|GOLDER",
            "Id": "GOLDER",
            "Content": {}
          },
          {
            "DisplayText": "Government Employees Health Association (GEHA)",
            "DisplayCount": "17",
            "Value": "Government Employees Health Association (GEHA)|GOVERA",
            "Id": "GOVERA",
            "Content": {}
          },
          {
            "DisplayText": "Group Health Cooperative",
            "DisplayCount": "9",
            "Value": "Group Health Cooperative|GRHECO",
            "Id": "GRHECO",
            "Content": {}
          },
          {
            "DisplayText": "Harvard Pilgrim Health Care",
            "DisplayCount": "2",
            "Value": "Harvard Pilgrim Health Care|HRPIHC",
            "Id": "HRPIHC",
            "Content": {}
          },
          {
            "DisplayText": "Health Net",
            "DisplayCount": "8",
            "Value": "Health Net|HENT",
            "Id": "HENT",
            "Content": {}
          },
          {
            "DisplayText": "Health Plan of Nevada",
            "DisplayCount": "2",
            "Value": "Health Plan of Nevada|HEPLNE",
            "Id": "HEPLNE",
            "Content": {}
          },
          {
            "DisplayText": "HealthCare Partners",
            "DisplayCount": "9",
            "Value": "HealthCare Partners|HCAREP",
            "Id": "HCAREP",
            "Content": {}
          },
          {
            "DisplayText": "HealthChoice",
            "DisplayCount": "33",
            "Value": "HealthChoice|HETHCH",
            "Id": "HETHCH",
            "Content": {}
          },
          {
            "DisplayText": "HealthFirst",
            "DisplayCount": "3",
            "Value": "HealthFirst|HLTHFI",
            "Id": "HLTHFI",
            "Content": {}
          },
          {
            "DisplayText": "HealthLink",
            "DisplayCount": "1",
            "Value": "HealthLink|HEALNK",
            "Id": "HEALNK",
            "Content": {}
          },
          {
            "DisplayText": "HealthPlus",
            "DisplayCount": "3",
            "Value": "HealthPlus|HEALPL",
            "Id": "HEALPL",
            "Content": {}
          },
          {
            "DisplayText": "HealthPlus Amerigroup",
            "DisplayCount": "3",
            "Value": "HealthPlus Amerigroup|HEALTN",
            "Id": "HEALTN",
            "Content": {}
          },
          {
            "DisplayText": "HealthSmart",
            "DisplayCount": "3",
            "Value": "HealthSmart|HEALTA",
            "Id": "HEALTA",
            "Content": {}
          },
          {
            "DisplayText": "Highmark Blue Cross Blue Shield",
            "DisplayCount": "1",
            "Value": "Highmark Blue Cross Blue Shield|HIGHMA",
            "Id": "HIGHMA",
            "Content": {}
          },
          {
            "DisplayText": "Homestate Health Plan",
            "DisplayCount": "1",
            "Value": "Homestate Health Plan|HPY0000770",
            "Id": "HPY0000770",
            "Content": {}
          },
          {
            "DisplayText": "Hometown Health Plan",
            "DisplayCount": "1",
            "Value": "Hometown Health Plan|HTHP",
            "Id": "HTHP",
            "Content": {}
          },
          {
            "DisplayText": "Horizon Blue Cross Blue Shield of New Jersey",
            "DisplayCount": "3",
            "Value": "Horizon Blue Cross Blue Shield of New Jersey|HORIZB",
            "Id": "HORIZB",
            "Content": {}
          },
          {
            "DisplayText": "Humana",
            "DisplayCount": "68",
            "Value": "Humana|HUMANA",
            "Id": "HUMANA",
            "Content": {}
          },
          {
            "DisplayText": "Husky Health",
            "DisplayCount": "3",
            "Value": "Husky Health|HUSKYA",
            "Id": "HUSKYA",
            "Content": {}
          },
          {
            "DisplayText": "inHealth",
            "DisplayCount": "3",
            "Value": "inHealth|INHEAA",
            "Id": "INHEAA",
            "Content": {}
          },
          {
            "DisplayText": "INTotal Health",
            "DisplayCount": "3",
            "Value": "INTotal Health|INTOTR",
            "Id": "INTOTR",
            "Content": {}
          },
          {
            "DisplayText": "Kaiser Permanente",
            "DisplayCount": "2",
            "Value": "Kaiser Permanente|KAISER",
            "Id": "KAISER",
            "Content": {}
          },
          {
            "DisplayText": "Locals (any local)",
            "DisplayCount": "1",
            "Value": "Locals (any local)|LOCALAL",
            "Id": "LOCALAL",
            "Content": {}
          },
          {
            "DisplayText": "Mail Handlers Benefit Plan (MHBP)",
            "DisplayCount": "3",
            "Value": "Mail Handlers Benefit Plan (MHBP)|MAILHA",
            "Id": "MAILHA",
            "Content": {}
          },
          {
            "DisplayText": "MedCare International",
            "DisplayCount": "1",
            "Value": "MedCare International|MEDCAI",
            "Id": "MEDCAI",
            "Content": {}
          },
          {
            "DisplayText": "MedHealthInsurance",
            "DisplayCount": "7",
            "Value": "MedHealthInsurance|MEDHEI",
            "Id": "MEDHEI",
            "Content": {}
          },
          {
            "DisplayText": "Medica",
            "DisplayCount": "1",
            "Value": "Medica|MDICA",
            "Id": "MDICA",
            "Content": {}
          },
          {
            "DisplayText": "Medicaid",
            "DisplayCount": "54",
            "Value": "Medicaid|MEDAID",
            "Id": "MEDAID",
            "Content": {}
          },
          {
            "DisplayText": "Medicaid of California",
            "DisplayCount": "1",
            "Value": "Medicaid of California|MEDICJ",
            "Id": "MEDICJ",
            "Content": {}
          },
          {
            "DisplayText": "Medical Mutual of Ohio",
            "DisplayCount": "2",
            "Value": "Medical Mutual of Ohio|MEMUOH",
            "Id": "MEMUOH",
            "Content": {}
          },
          {
            "DisplayText": "Medicare",
            "DisplayCount": "4",
            "Value": "Medicare|MEDICA",
            "Id": "MEDICA",
            "Content": {}
          },
          {
            "DisplayText": "Medico",
            "DisplayCount": "1",
            "Value": "Medico|MEDICO",
            "Id": "MEDICO",
            "Content": {}
          },
          {
            "DisplayText": "Meritain Health",
            "DisplayCount": "1",
            "Value": "Meritain Health|MERITA",
            "Id": "MERITA",
            "Content": {}
          },
          {
            "DisplayText": "Midwest Health Plan",
            "DisplayCount": "3",
            "Value": "Midwest Health Plan|MIDWEA",
            "Id": "MIDWEA",
            "Content": {}
          },
          {
            "DisplayText": "Molina Healthcare",
            "DisplayCount": "4",
            "Value": "Molina Healthcare|MLHC",
            "Id": "MLHC",
            "Content": {}
          },
          {
            "DisplayText": "MultiPlan",
            "DisplayCount": "43",
            "Value": "MultiPlan|MULTIP",
            "Id": "MULTIP",
            "Content": {}
          },
          {
            "DisplayText": "Mutual of Omaha",
            "DisplayCount": "2",
            "Value": "Mutual of Omaha|MUTUOM",
            "Id": "MUTUOM",
            "Content": {}
          },
          {
            "DisplayText": "MVP Health Care",
            "DisplayCount": "1",
            "Value": "MVP Health Care|MVPHEC",
            "Id": "MVPHEC",
            "Content": {}
          },
          {
            "DisplayText": "National Elevator",
            "DisplayCount": "3",
            "Value": "National Elevator|NATELE",
            "Id": "NATELE",
            "Content": {}
          },
          {
            "DisplayText": "One Health",
            "DisplayCount": "32",
            "Value": "One Health|ONEHLT",
            "Id": "ONEHLT",
            "Content": {}
          },
          {
            "DisplayText": "Oxford Health Plans",
            "DisplayCount": "1",
            "Value": "Oxford Health Plans|OXHEPL",
            "Id": "OXHEPL",
            "Content": {}
          },
          {
            "DisplayText": "PacificSource",
            "DisplayCount": "1",
            "Value": "PacificSource|PACSRC",
            "Id": "PACSRC",
            "Content": {}
          },
          {
            "DisplayText": "Peach State Health Plan",
            "DisplayCount": "3",
            "Value": "Peach State Health Plan|PESTHP",
            "Id": "PESTHP",
            "Content": {}
          },
          {
            "DisplayText": "PHCS",
            "DisplayCount": "37",
            "Value": "PHCS|BU000031",
            "Id": "BU000031",
            "Content": {}
          },
          {
            "DisplayText": "Planned Administration Inc",
            "DisplayCount": "2",
            "Value": "Planned Administration Inc|PLAADI",
            "Id": "PLAADI",
            "Content": {}
          },
          {
            "DisplayText": "Preferred Health Professionals",
            "DisplayCount": "1",
            "Value": "Preferred Health Professionals|PRHEPR",
            "Id": "PRHEPR",
            "Content": {}
          },
          {
            "DisplayText": "Preferred Health Systems",
            "DisplayCount": "2",
            "Value": "Preferred Health Systems|PRHESY",
            "Id": "PRHESY",
            "Content": {}
          },
          {
            "DisplayText": "Preferred Healthcare",
            "DisplayCount": "1",
            "Value": "Preferred Healthcare|PREFEE",
            "Id": "PREFEE",
            "Content": {}
          },
          {
            "DisplayText": "Principal Financial Group",
            "DisplayCount": "2",
            "Value": "Principal Financial Group|PRIFGR",
            "Id": "PRIFGR",
            "Content": {}
          },
          {
            "DisplayText": "Principal Life",
            "DisplayCount": "5",
            "Value": "Principal Life|PRINLI",
            "Id": "PRINLI",
            "Content": {}
          },
          {
            "DisplayText": "Priority Health",
            "DisplayCount": "1",
            "Value": "Priority Health|PRIOHE",
            "Id": "PRIOHE",
            "Content": {}
          },
          {
            "DisplayText": "Private HealthCare Systems",
            "DisplayCount": "1",
            "Value": "Private HealthCare Systems|PRIVAA",
            "Id": "PRIVAA",
            "Content": {}
          },
          {
            "DisplayText": "SelectHealth",
            "DisplayCount": "2",
            "Value": "SelectHealth|SELEHE",
            "Id": "SELEHE",
            "Content": {}
          },
          {
            "DisplayText": "Sierra Choice",
            "DisplayCount": "32",
            "Value": "Sierra Choice|SIERRA",
            "Id": "SIERRA",
            "Content": {}
          },
          {
            "DisplayText": "Simplifi",
            "DisplayCount": "1",
            "Value": "Simplifi|SIMPLI",
            "Id": "SIMPLI",
            "Content": {}
          },
          {
            "DisplayText": "Simply Healthcare Plans",
            "DisplayCount": "3",
            "Value": "Simply Healthcare Plans|SHCP",
            "Id": "SHCP",
            "Content": {}
          },
          {
            "DisplayText": "State Farm",
            "DisplayCount": "2",
            "Value": "State Farm|STATEF",
            "Id": "STATEF",
            "Content": {}
          },
          {
            "DisplayText": "Staywell (Wellcare)",
            "DisplayCount": "3",
            "Value": "Staywell (Wellcare)|STAYWA",
            "Id": "STAYWA",
            "Content": {}
          },
          {
            "DisplayText": "Tricare",
            "DisplayCount": "49",
            "Value": "Tricare|TRICAR",
            "Id": "TRICAR",
            "Content": {}
          },
          {
            "DisplayText": "Triwest",
            "DisplayCount": "1",
            "Value": "Triwest|TRIWES",
            "Id": "TRIWES",
            "Content": {}
          },
          {
            "DisplayText": "TriWest Champus",
            "DisplayCount": "1",
            "Value": "TriWest Champus|TRIWEC",
            "Id": "TRIWEC",
            "Content": {}
          },
          {
            "DisplayText": "Tufts Health Plan",
            "DisplayCount": "1",
            "Value": "Tufts Health Plan|TUFTSA",
            "Id": "TUFTSA",
            "Content": {}
          },
          {
            "DisplayText": "UnitedHealthCare",
            "DisplayCount": "94",
            "Value": "UnitedHealthCare|UNITHC",
            "Id": "UNITHC",
            "Content": {}
          },
          {
            "DisplayText": "USA Health Network",
            "DisplayCount": "32",
            "Value": "USA Health Network|USAHEA",
            "Id": "USAHEA",
            "Content": {}
          },
          {
            "DisplayText": "Veteran Administration Plan",
            "DisplayCount": "32",
            "Value": "Veteran Administration Plan|VEADPL",
            "Id": "VEADPL",
            "Content": {}
          },
          {
            "DisplayText": "WellCare",
            "DisplayCount": "1",
            "Value": "WellCare|WELLCB",
            "Id": "WELLCB",
            "Content": {}
          },
          {
            "DisplayText": "Wellcare of Georgia",
            "DisplayCount": "3",
            "Value": "Wellcare of Georgia|WELLCA",
            "Id": "WELLCA",
            "Content": {}
          },
          {
            "DisplayText": "WellPoint",
            "DisplayCount": "7",
            "Value": "WellPoint|WELLPT",
            "Id": "WELLPT",
            "Content": {}
          },
          {
            "DisplayText": "Wells Fargo Insurance",
            "DisplayCount": "1",
            "Value": "Wells Fargo Insurance|WEFAIN",
            "Id": "WEFAIN",
            "Content": {}
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "UnitedHealthCare",
            "DisplayCount": "94",
            "Value": "UnitedHealthCare|UNITHC",
            "Id": "UNITHC",
            "Content": {}
          },
          {
            "DisplayText": "Cigna",
            "DisplayCount": "93",
            "Value": "Cigna|CIGNA",
            "Id": "CIGNA",
            "Content": {}
          },
          {
            "DisplayText": "Aetna",
            "DisplayCount": "91",
            "Value": "Aetna|AETNA",
            "Id": "AETNA",
            "Content": {}
          }
        ],
        "TopViewAllValues": []
      },
      "FacetKey": "payors"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Banner Churchill Community Hospital",
            "DisplayCount": "1",
            "Value": "6B779D",
            "Data": "Banner Churchill Community Hospital|6B779D",
            "Id": "6B779D",
            "Content": {}
          },
          {
            "DisplayText": "Barton Memorial Hospital",
            "DisplayCount": "1",
            "Value": "1672C3",
            "Data": "Barton Memorial Hospital|1672C3",
            "Id": "1672C3",
            "Content": {}
          },
          {
            "DisplayText": "Borgess Medical Center",
            "DisplayCount": "1",
            "Value": "93D959",
            "Data": "Borgess Medical Center|93D959",
            "Id": "93D959",
            "Content": {}
          },
          {
            "DisplayText": "Boulder City Hospital",
            "DisplayCount": "12",
            "Value": "A8F53E",
            "Data": "Boulder City Hospital|A8F53E",
            "Id": "A8F53E",
            "Content": {}
          },
          {
            "DisplayText": "Bronson Methodist Hospital",
            "DisplayCount": "1",
            "Value": "385C74",
            "Data": "Bronson Methodist Hospital|385C74",
            "Id": "385C74",
            "Content": {}
          },
          {
            "DisplayText": "Carson Tahoe Regional Medical Center",
            "DisplayCount": "5",
            "Value": "4EF075",
            "Data": "Carson Tahoe Regional Medical Center|4EF075",
            "Id": "4EF075",
            "Content": {}
          },
          {
            "DisplayText": "Carson Tahoe Sierra Surgery",
            "DisplayCount": "2",
            "Value": "8AF328",
            "Data": "Carson Tahoe Sierra Surgery|8AF328",
            "Id": "8AF328",
            "Content": {}
          },
          {
            "DisplayText": "Carson Valley Medical Center",
            "DisplayCount": "3",
            "Value": "762635",
            "Data": "Carson Valley Medical Center|762635",
            "Id": "762635",
            "Content": {}
          },
          {
            "DisplayText": "Catholic Medical Center",
            "DisplayCount": "1",
            "Value": "AE8D1C",
            "Data": "Catholic Medical Center|AE8D1C",
            "Id": "AE8D1C",
            "Content": {}
          },
          {
            "DisplayText": "Centennial Hills Hospital Medical Center",
            "DisplayCount": "17",
            "Value": "F2A6B7",
            "Data": "Centennial Hills Hospital Medical Center|F2A6B7",
            "Id": "F2A6B7",
            "Content": {}
          },
          {
            "DisplayText": "Dartmouth - Hitchcock Medical Center",
            "DisplayCount": "1",
            "Value": "151BB5",
            "Data": "Dartmouth - Hitchcock Medical Center|151BB5",
            "Id": "151BB5",
            "Content": {}
          },
          {
            "DisplayText": "Desert Springs Hospital Medical Center",
            "DisplayCount": "22",
            "Value": "B2B744",
            "Data": "Desert Springs Hospital Medical Center|B2B744",
            "Id": "B2B744",
            "Content": {}
          },
          {
            "DisplayText": "Desert View Hospital",
            "DisplayCount": "3",
            "Value": "4D8ED7",
            "Data": "Desert View Hospital|4D8ED7",
            "Id": "4D8ED7",
            "Content": {}
          },
          {
            "DisplayText": "East Jefferson General Hospital",
            "DisplayCount": "1",
            "Value": "38AD8B",
            "Data": "East Jefferson General Hospital|38AD8B",
            "Id": "38AD8B",
            "Content": {}
          },
          {
            "DisplayText": "Mount Sinai Hospital",
            "DisplayCount": "1",
            "Value": "EAF80C",
            "Data": "Mount Sinai Hospital|EAF80C",
            "Id": "EAF80C",
            "Content": {}
          },
          {
            "DisplayText": "Mountainview Hospital",
            "DisplayCount": "33",
            "Value": "C0C277",
            "Data": "Mountainview Hospital|C0C277",
            "Id": "C0C277",
            "Content": {}
          },
          {
            "DisplayText": "North Vista Hospital",
            "DisplayCount": "15",
            "Value": "F129D5",
            "Data": "North Vista Hospital|F129D5",
            "Id": "F129D5",
            "Content": {}
          },
          {
            "DisplayText": "Northern Nevada Medical Center",
            "DisplayCount": "2",
            "Value": "9698E8",
            "Data": "Northern Nevada Medical Center|9698E8",
            "Id": "9698E8",
            "Content": {}
          },
          {
            "DisplayText": "Renown Regional Medical Center",
            "DisplayCount": "13",
            "Value": "30D73B",
            "Data": "Renown Regional Medical Center|30D73B",
            "Id": "30D73B",
            "Content": {}
          },
          {
            "DisplayText": "Renown South Meadows Medical Center",
            "DisplayCount": "1",
            "Value": "7D4AEB",
            "Data": "Renown South Meadows Medical Center|7D4AEB",
            "Id": "7D4AEB",
            "Content": {}
          },
          {
            "DisplayText": "Saint Joseph Hospital",
            "DisplayCount": "1",
            "Value": "9C91B8",
            "Data": "Saint Joseph Hospital|9C91B8",
            "Id": "9C91B8",
            "Content": {}
          },
          {
            "DisplayText": "Saint Mary's Regional Medical Center",
            "DisplayCount": "8",
            "Value": "C53DEB",
            "Data": "Saint Mary's Regional Medical Center|C53DEB",
            "Id": "C53DEB",
            "Content": {}
          },
          {
            "DisplayText": "South Lyon Medical Center",
            "DisplayCount": "1",
            "Value": "CC4205",
            "Data": "South Lyon Medical Center|CC4205",
            "Id": "CC4205",
            "Content": {}
          },
          {
            "DisplayText": "Southern Hills Hospital and Medical Center",
            "DisplayCount": "36",
            "Value": "5FEB5C",
            "Data": "Southern Hills Hospital and Medical Center|5FEB5C",
            "Id": "5FEB5C",
            "Content": {}
          },
          {
            "DisplayText": "Spring Valley Hospital Medical Center",
            "DisplayCount": "26",
            "Value": "D6F15E",
            "Data": "Spring Valley Hospital Medical Center|D6F15E",
            "Id": "D6F15E",
            "Content": {}
          },
          {
            "DisplayText": "St. Francis Regional Medical Center",
            "DisplayCount": "1",
            "Value": "349902",
            "Data": "St. Francis Regional Medical Center|349902",
            "Id": "349902",
            "Content": {}
          },
          {
            "DisplayText": "St. Rose Dominican, Rose de Lima Campus",
            "DisplayCount": "13",
            "Value": "A0C2A7",
            "Data": "St. Rose Dominican, Rose de Lima Campus|A0C2A7",
            "Id": "A0C2A7",
            "Content": {}
          },
          {
            "DisplayText": "St. Rose Dominican, San Martin Campus",
            "DisplayCount": "33",
            "Value": "CBF7A2",
            "Data": "St. Rose Dominican, San Martin Campus|CBF7A2",
            "Id": "CBF7A2",
            "Content": {}
          },
          {
            "DisplayText": "St. Rose Dominican, Siena Campus",
            "DisplayCount": "31",
            "Value": "B5D7A6",
            "Data": "St. Rose Dominican, Siena Campus|B5D7A6",
            "Id": "B5D7A6",
            "Content": {}
          },
          {
            "DisplayText": "Summerlin Hospital Medical Center",
            "DisplayCount": "38",
            "Value": "F9D29F",
            "Data": "Summerlin Hospital Medical Center|F9D29F",
            "Id": "F9D29F",
            "Content": {}
          },
          {
            "DisplayText": "Sunrise Children’s Hospital",
            "DisplayCount": "2",
            "Value": "4E76A3",
            "Data": "Sunrise Children’s Hospital|4E76A3",
            "Id": "4E76A3",
            "Content": {}
          },
          {
            "DisplayText": "Sunrise Hospital and Medical Center",
            "DisplayCount": "43",
            "Value": "7EA9BC",
            "Data": "Sunrise Hospital and Medical Center|7EA9BC",
            "Id": "7EA9BC",
            "Content": {}
          },
          {
            "DisplayText": "UC Irvine Medical Center",
            "DisplayCount": "1",
            "Value": "B7803B",
            "Data": "UC Irvine Medical Center|B7803B",
            "Id": "B7803B",
            "Content": {}
          },
          {
            "DisplayText": "University Medical Center of Southern Nevada",
            "DisplayCount": "17",
            "Value": "3C022D",
            "Data": "University Medical Center of Southern Nevada|3C022D",
            "Id": "3C022D",
            "Content": {}
          },
          {
            "DisplayText": "Valley Hospital Medical Center",
            "DisplayCount": "23",
            "Value": "ADF464",
            "Data": "Valley Hospital Medical Center|ADF464",
            "Id": "ADF464",
            "Content": {}
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Sunrise Hospital and Medical Center",
            "DisplayCount": "43",
            "Value": "7EA9BC",
            "Data": "Sunrise Hospital and Medical Center|7EA9BC",
            "Id": "7EA9BC",
            "Content": {}
          },
          {
            "DisplayText": "Summerlin Hospital Medical Center",
            "DisplayCount": "38",
            "Value": "F9D29F",
            "Data": "Summerlin Hospital Medical Center|F9D29F",
            "Id": "F9D29F",
            "Content": {}
          },
          {
            "DisplayText": "Southern Hills Hospital and Medical Center",
            "DisplayCount": "36",
            "Value": "5FEB5C",
            "Data": "Southern Hills Hospital and Medical Center|5FEB5C",
            "Id": "5FEB5C",
            "Content": {}
          }
        ],
        "TopViewAllValues": []
      },
      "FacetKey": "facilities"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "All American Surgical",
            "DisplayCount": "1",
            "Value": "PPP83J6",
            "Data": "All American Surgical|PPP83J6",
            "Id": "PPP83J6",
            "Content": {}
          },
          {
            "DisplayText": "Cancer & Blood Specialists of Nevada",
            "DisplayCount": "3",
            "Value": "PP3NW2M",
            "Data": "Cancer & Blood Specialists of Nevada|PP3NW2M",
            "Id": "PP3NW2M",
            "Content": {}
          },
          {
            "DisplayText": "Cancer and Blood Specialists NV",
            "DisplayCount": "1",
            "Value": "F99WM",
            "Data": "Cancer and Blood Specialists NV|F99WM",
            "Id": "F99WM",
            "Content": {}
          },
          {
            "DisplayText": "CANCER CARE SPECIALISTS",
            "DisplayCount": "3",
            "Value": "PPP8SYY",
            "Data": "CANCER CARE SPECIALISTS|PPP8SYY",
            "Id": "PPP8SYY",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Therapy",
            "DisplayCount": "1",
            "Value": "PP3Y6LW",
            "Data": "Cancer Therapy|PP3Y6LW",
            "Id": "PP3Y6LW",
            "Content": {}
          },
          {
            "DisplayText": "Cardiovascular Surgery of Southern Nevada",
            "DisplayCount": "1",
            "Value": "PP3Q37L",
            "Data": "Cardiovascular Surgery of Southern Nevada|PP3Q37L",
            "Id": "PP3Q37L",
            "Content": {}
          },
          {
            "DisplayText": "Carson Tahoe Physician Clinic",
            "DisplayCount": "2",
            "Value": "PPP2BVD",
            "Data": "Carson Tahoe Physician Clinic|PPP2BVD",
            "Id": "PPP2BVD",
            "Content": {}
          },
          {
            "DisplayText": "Century Wellness Clinic",
            "DisplayCount": "1",
            "Value": "WQ5F7",
            "Data": "Century Wellness Clinic|WQ5F7",
            "Id": "WQ5F7",
            "Content": {}
          },
          {
            "DisplayText": "Century Wellness Clinic",
            "DisplayCount": "1",
            "Value": "PPP2SJ8",
            "Data": "Century Wellness Clinic|PPP2SJ8",
            "Id": "PPP2SJ8",
            "Content": {}
          },
          {
            "DisplayText": "Children's Center for Cancer & Blood Diseases",
            "DisplayCount": "2",
            "Value": "FL73M",
            "Data": "Children's Center for Cancer & Blood Diseases|FL73M",
            "Id": "FL73M",
            "Content": {}
          },
          {
            "DisplayText": "Children's Specialty Center of Nevada",
            "DisplayCount": "1",
            "Value": "YBDL42",
            "Data": "Children's Specialty Center of Nevada|YBDL42",
            "Id": "YBDL42",
            "Content": {}
          },
          {
            "DisplayText": "Comprehensive Cancer Centers of Nevada",
            "DisplayCount": "29",
            "Value": "FLQ6B",
            "Data": "Comprehensive Cancer Centers of Nevada|FLQ6B",
            "Id": "FLQ6B",
            "Content": {}
          },
          {
            "DisplayText": "Comprehensive Cancer Centers Of NV",
            "DisplayCount": "1",
            "Value": "FJMGV",
            "Data": "Comprehensive Cancer Centers Of NV|FJMGV",
            "Id": "FJMGV",
            "Content": {}
          },
          {
            "DisplayText": "Comprehensive Cancer Ctrs Of NV",
            "DisplayCount": "2",
            "Value": "PP385CF",
            "Data": "Comprehensive Cancer Ctrs Of NV|PP385CF",
            "Id": "PP385CF",
            "Content": {}
          },
          {
            "DisplayText": "Health Insight",
            "DisplayCount": "1",
            "Value": "PP3SW58",
            "Data": "Health Insight|PP3SW58",
            "Id": "PP3SW58",
            "Content": {}
          },
          {
            "DisplayText": "HealthCare Partners Medical Group",
            "DisplayCount": "1",
            "Value": "PP336FB",
            "Data": "HealthCare Partners Medical Group|PP336FB",
            "Id": "PP336FB",
            "Content": {}
          },
          {
            "DisplayText": "Healthcare Partners Medical Group - Oncology",
            "DisplayCount": "1",
            "Value": "PP3QNQ4",
            "Data": "Healthcare Partners Medical Group - Oncology|PP3QNQ4",
            "Id": "PP3QNQ4",
            "Content": {}
          },
          {
            "DisplayText": "HealthCare Partners Medical Group Oncology/Hematology",
            "DisplayCount": "3",
            "Value": "PP3NPRD",
            "Data": "HealthCare Partners Medical Group Oncology/Hematology|PP3NPRD",
            "Id": "PP3NPRD",
            "Content": {}
          },
          {
            "DisplayText": "HealthCare Partners of Nevada - Oncology/Hematology",
            "DisplayCount": "1",
            "Value": "PP3NQJP",
            "Data": "HealthCare Partners of Nevada - Oncology/Hematology|PP3NQJP",
            "Id": "PP3NQJP",
            "Content": {}
          },
          {
            "DisplayText": "Hope Cancer Care Of Nevada",
            "DisplayCount": "1",
            "Value": "FCKM4",
            "Data": "Hope Cancer Care Of Nevada|FCKM4",
            "Id": "FCKM4",
            "Content": {}
          },
          {
            "DisplayText": "Hope Cancer Center of Nevada",
            "DisplayCount": "1",
            "Value": "PP3R6VL",
            "Data": "Hope Cancer Center of Nevada|PP3R6VL",
            "Id": "PP3R6VL",
            "Content": {}
          },
          {
            "DisplayText": "Inpatient Consultants Of Nevada",
            "DisplayCount": "1",
            "Value": "FFC8P",
            "Data": "Inpatient Consultants Of Nevada|FFC8P",
            "Id": "FFC8P",
            "Content": {}
          },
          {
            "DisplayText": "Internal Medicine Associates",
            "DisplayCount": "1",
            "Value": "FYQCD",
            "Data": "Internal Medicine Associates|FYQCD",
            "Id": "FYQCD",
            "Content": {}
          },
          {
            "DisplayText": "Las Vegas Cancer Center",
            "DisplayCount": "3",
            "Value": "F6XW6",
            "Data": "Las Vegas Cancer Center|F6XW6",
            "Id": "F6XW6",
            "Content": {}
          },
          {
            "DisplayText": "LIMITED TO OFFICIAL STATE DUTIES ONLY",
            "DisplayCount": "1",
            "Value": "PP343KQ",
            "Data": "LIMITED TO OFFICIAL STATE DUTIES ONLY|PP343KQ",
            "Id": "PP343KQ",
            "Content": {}
          },
          {
            "DisplayText": "Maryland Pkwy Oncology/Hematology",
            "DisplayCount": "2",
            "Value": "FCWTJ",
            "Data": "Maryland Pkwy Oncology/Hematology|FCWTJ",
            "Id": "FCWTJ",
            "Content": {}
          },
          {
            "DisplayText": "MIKE OCALLAGHAN FEDERAL HOSPITAL",
            "DisplayCount": "1",
            "Value": "YX2QPX",
            "Data": "MIKE OCALLAGHAN FEDERAL HOSPITAL|YX2QPX",
            "Id": "YX2QPX",
            "Content": {}
          },
          {
            "DisplayText": "Nevada Cancer Center",
            "DisplayCount": "6",
            "Value": "PP3S7TX",
            "Data": "Nevada Cancer Center|PP3S7TX",
            "Id": "PP3S7TX",
            "Content": {}
          },
          {
            "DisplayText": "Nevada Orthopedic & Spine Center",
            "DisplayCount": "1",
            "Value": "PP3NQBP",
            "Data": "Nevada Orthopedic & Spine Center|PP3NQBP",
            "Id": "PP3NQBP",
            "Content": {}
          },
          {
            "DisplayText": "Reno Oncology Consultants",
            "DisplayCount": "4",
            "Value": "FRTDR",
            "Data": "Reno Oncology Consultants|FRTDR",
            "Id": "FRTDR",
            "Content": {}
          },
          {
            "DisplayText": "Reno VA Medical Center ONC",
            "DisplayCount": "1",
            "Value": "PP3YYRW",
            "Data": "Reno VA Medical Center ONC|PP3YYRW",
            "Id": "PP3YYRW",
            "Content": {}
          },
          {
            "DisplayText": "Renown Institute For Cancer",
            "DisplayCount": "1",
            "Value": "PP3Y2DT",
            "Data": "Renown Institute For Cancer|PP3Y2DT",
            "Id": "PP3Y2DT",
            "Content": {}
          },
          {
            "DisplayText": "Renown Medical Group - Center C",
            "DisplayCount": "1",
            "Value": "PP34NKX",
            "Data": "Renown Medical Group - Center C|PP34NKX",
            "Id": "PP34NKX",
            "Content": {}
          },
          {
            "DisplayText": "Renown Medical Group - Oncology/Hematology",
            "DisplayCount": "2",
            "Value": "PP3GHGY",
            "Data": "Renown Medical Group - Oncology/Hematology|PP3GHGY",
            "Id": "PP3GHGY",
            "Content": {}
          },
          {
            "DisplayText": "Renown Medical Group - Ryland",
            "DisplayCount": "1",
            "Value": "FM2MW",
            "Data": "Renown Medical Group - Ryland|FM2MW",
            "Id": "FM2MW",
            "Content": {}
          },
          {
            "DisplayText": "Saint Mary's Medical Group",
            "DisplayCount": "1",
            "Value": "YCWN39",
            "Data": "Saint Mary's Medical Group|YCWN39",
            "Id": "YCWN39",
            "Content": {}
          },
          {
            "DisplayText": "Sierra Nevada Cancer Center",
            "DisplayCount": "1",
            "Value": "FVC3P",
            "Data": "Sierra Nevada Cancer Center|FVC3P",
            "Id": "FVC3P",
            "Content": {}
          },
          {
            "DisplayText": "Sierra Pediatric Bld/Cncr Spec",
            "DisplayCount": "1",
            "Value": "PP3JB9J",
            "Data": "Sierra Pediatric Bld/Cncr Spec|PP3JB9J",
            "Id": "PP3JB9J",
            "Content": {}
          },
          {
            "DisplayText": "Strimling Dermatology, Laser & Vein Institute",
            "DisplayCount": "1",
            "Value": "DWTVB",
            "Data": "Strimling Dermatology, Laser & Vein Institute|DWTVB",
            "Id": "DWTVB",
            "Content": {}
          },
          {
            "DisplayText": "Surgical Dermatology and Laser Center",
            "DisplayCount": "1",
            "Value": "PP3FVCV",
            "Data": "Surgical Dermatology and Laser Center|PP3FVCV",
            "Id": "PP3FVCV",
            "Content": {}
          },
          {
            "DisplayText": "Swallowing and Voice Solutions, LLC",
            "DisplayCount": "1",
            "Value": "PP3FYPB",
            "Data": "Swallowing and Voice Solutions, LLC|PP3FYPB",
            "Id": "PP3FYPB",
            "Content": {}
          },
          {
            "DisplayText": "Synergy Cancer Center of Nevada",
            "DisplayCount": "1",
            "Value": "YCWWHK",
            "Data": "Synergy Cancer Center of Nevada|YCWWHK",
            "Id": "YCWWHK",
            "Content": {}
          },
          {
            "DisplayText": "Tenaya Oncology/Hematology",
            "DisplayCount": "1",
            "Value": "PP3S86F",
            "Data": "Tenaya Oncology/Hematology|PP3S86F",
            "Id": "PP3S86F",
            "Content": {}
          },
          {
            "DisplayText": "Univ Nevada Scl Medcn Pediatric",
            "DisplayCount": "1",
            "Value": "PP35TK2",
            "Data": "Univ Nevada Scl Medcn Pediatric|PP35TK2",
            "Id": "PP35TK2",
            "Content": {}
          },
          {
            "DisplayText": "University Health System",
            "DisplayCount": "2",
            "Value": "PP34YBS",
            "Data": "University Health System|PP34YBS",
            "Id": "PP34YBS",
            "Content": {}
          },
          {
            "DisplayText": "UNIVERSITY OF NEVADA SCHOOL OF MEDICINE",
            "DisplayCount": "1",
            "Value": "PPPDJC3",
            "Data": "UNIVERSITY OF NEVADA SCHOOL OF MEDICINE|PPPDJC3",
            "Id": "PPPDJC3",
            "Content": {}
          },
          {
            "DisplayText": "University of Nevada School of Medicine-Department of General Surgery",
            "DisplayCount": "1",
            "Value": "YX2VVK",
            "Data": "University of Nevada School of Medicine-Department of General Surgery|YX2VVK",
            "Id": "YX2VVK",
            "Content": {}
          },
          {
            "DisplayText": "University of Nevada School of Medicine-Division of Plastic Surgery",
            "DisplayCount": "1",
            "Value": "YXY35T",
            "Data": "University of Nevada School of Medicine-Division of Plastic Surgery|YXY35T",
            "Id": "YXY35T",
            "Content": {}
          },
          {
            "DisplayText": "University of Nevada, School of Medicine",
            "DisplayCount": "1",
            "Value": "PP3NRNP",
            "Data": "University of Nevada, School of Medicine|PP3NRNP",
            "Id": "PP3NRNP",
            "Content": {}
          },
          {
            "DisplayText": "Urology Specialists Of Nevada",
            "DisplayCount": "3",
            "Value": "DQR7S",
            "Data": "Urology Specialists Of Nevada|DQR7S",
            "Id": "DQR7S",
            "Content": {}
          },
          {
            "DisplayText": "VA Health System Spclty Clinic Southwest",
            "DisplayCount": "1",
            "Value": "PP3BJTT",
            "Data": "VA Health System Spclty Clinic Southwest|PP3BJTT",
            "Id": "PP3BJTT",
            "Content": {}
          },
          {
            "DisplayText": "VA Medical Center",
            "DisplayCount": "1",
            "Value": "DSV4M",
            "Data": "VA Medical Center|DSV4M",
            "Id": "DSV4M",
            "Content": {}
          },
          {
            "DisplayText": "Va Sierra Nevada Health Care System",
            "DisplayCount": "1",
            "Value": "DWGGQ",
            "Data": "Va Sierra Nevada Health Care System|DWGGQ",
            "Id": "DWGGQ",
            "Content": {}
          },
          {
            "DisplayText": "VA Southern Nevada Hlthcr Systm",
            "DisplayCount": "1",
            "Value": "PPP5BYX",
            "Data": "VA Southern Nevada Hlthcr Systm|PPP5BYX",
            "Id": "PPP5BYX",
            "Content": {}
          },
          {
            "DisplayText": "VISHAL GANDOTRA, MD INC",
            "DisplayCount": "1",
            "Value": "YCCKMJ",
            "Data": "VISHAL GANDOTRA, MD INC|YCCKMJ",
            "Id": "YCCKMJ",
            "Content": {}
          },
          {
            "DisplayText": "Women's Cancer Center of Nevada",
            "DisplayCount": "1",
            "Value": "Y3YAB6",
            "Data": "Women's Cancer Center of Nevada|Y3YAB6",
            "Id": "Y3YAB6",
            "Content": {}
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Comprehensive Cancer Centers of Nevada",
            "DisplayCount": "29",
            "Value": "FLQ6B",
            "Data": "Comprehensive Cancer Centers of Nevada|FLQ6B",
            "Id": "FLQ6B",
            "Content": {}
          },
          {
            "DisplayText": "Nevada Cancer Center",
            "DisplayCount": "6",
            "Value": "PP3S7TX",
            "Data": "Nevada Cancer Center|PP3S7TX",
            "Id": "PP3S7TX",
            "Content": {}
          },
          {
            "DisplayText": "Reno Oncology Consultants",
            "DisplayCount": "4",
            "Value": "FRTDR",
            "Data": "Reno Oncology Consultants|FRTDR",
            "Id": "FRTDR",
            "Content": {}
          }
        ],
        "TopViewAllValues": []
      },
      "FacetKey": "practices"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Oncology",
            "DisplayCount": "81",
            "Value": "PS592",
            "Data": "PS592/Oncology|PS592",
            "Id": "PS592",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps592"
            }
          },
          {
            "DisplayText": "Medical Oncology",
            "DisplayCount": "59",
            "Value": "PS456",
            "Data": "PS592/Medical Oncology|PS456",
            "Id": "PS456",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps456"
            }
          },
          {
            "DisplayText": "Pediatric Hematology & Oncology",
            "DisplayCount": "15",
            "Value": "PS692",
            "Data": "PS592/Pediatric Hematology & Oncology|PS692",
            "Id": "PS692",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps692"
            }
          },
          {
            "DisplayText": "Breast Surgical Oncology",
            "DisplayCount": "4",
            "Value": "PS118",
            "Data": "PS592/Breast Surgical Oncology|PS118",
            "Id": "PS118",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps118"
            }
          },
          {
            "DisplayText": "Dermatologic Oncology",
            "DisplayCount": "3",
            "Value": "PS1009",
            "Data": "PS592/Dermatologic Oncology|PS1009",
            "Id": "PS1009",
            "Content": {}
          },
          {
            "DisplayText": "Musculoskeletal Oncology",
            "DisplayCount": "2",
            "Value": "PS492",
            "Data": "PS592/Musculoskeletal Oncology|PS492",
            "Id": "PS492",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps492"
            }
          },
          {
            "DisplayText": "Surgical Oncology",
            "DisplayCount": "2",
            "Value": "PS1054",
            "Data": "PS592/Surgical Oncology|PS1054",
            "Id": "PS1054",
            "Content": {}
          },
          {
            "DisplayText": "Breast Oncology",
            "DisplayCount": "1",
            "Value": "PS116",
            "Data": "PS592/Breast Oncology|PS116",
            "Id": "PS116",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps116"
            }
          },
          {
            "DisplayText": "Complex General Surgical Oncology",
            "DisplayCount": "1",
            "Value": "PS197",
            "Data": "PS592/Complex General Surgical Oncology|PS197",
            "Id": "PS197",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps197"
            }
          },
          {
            "DisplayText": "Gastrointestinal Oncology",
            "DisplayCount": "1",
            "Value": "PS1077",
            "Data": "PS592/Gastrointestinal Oncology|PS1077",
            "Id": "PS1077",
            "Content": {}
          },
          {
            "DisplayText": "Geriatric Oncology",
            "DisplayCount": "1",
            "Value": "PS1078",
            "Data": "PS592/Geriatric Oncology|PS1078",
            "Id": "PS1078",
            "Content": {}
          },
          {
            "DisplayText": "Head & Neck Surgical Oncology",
            "DisplayCount": "1",
            "Value": "PS1150",
            "Data": "PS592/Head & Neck Surgical Oncology|PS1150",
            "Id": "PS1150",
            "Content": {}
          },
          {
            "DisplayText": "Neoplastic Diseases",
            "DisplayCount": "1",
            "Value": "PS509",
            "Data": "PS592/Neoplastic Diseases|PS509",
            "Id": "PS509",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps509"
            }
          },
          {
            "DisplayText": "Oncoplastic Surgery",
            "DisplayCount": "1",
            "Value": "PS1195",
            "Data": "PS592/Oncoplastic Surgery|PS1195",
            "Id": "PS1195",
            "Content": {}
          },
          {
            "DisplayText": "Urologic Oncology",
            "DisplayCount": "1",
            "Value": "PS959",
            "Data": "PS592/Urologic Oncology|PS959",
            "Id": "PS959",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps959"
            }
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Oncology",
            "DisplayCount": "81",
            "Value": "PS592",
            "Data": "PS592/Oncology|PS592",
            "Id": "PS592",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps592"
            }
          },
          {
            "DisplayText": "Medical Oncology",
            "DisplayCount": "59",
            "Value": "PS456",
            "Data": "PS592/Medical Oncology|PS456",
            "Id": "PS456",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps456"
            }
          },
          {
            "DisplayText": "Pediatric Hematology & Oncology",
            "DisplayCount": "15",
            "Value": "PS692",
            "Data": "PS592/Pediatric Hematology & Oncology|PS692",
            "Id": "PS692",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/pracspec/ps692"
            }
          }
        ],
        "TopViewAllValues": []
      },
      "FacetKey": "practicing_specialties"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Acne",
            "DisplayCount": "1",
            "Value": "PS592/A/Acne|1551",
            "Data": "PS592/A/Acne|1551",
            "Id": "1551",
            "Content": {}
          },
          {
            "DisplayText": "Actinic Keratosis",
            "DisplayCount": "1",
            "Value": "PS592/A/Actinic Keratosis|1556",
            "Data": "PS592/A/Actinic Keratosis|1556",
            "Id": "1556",
            "Content": {}
          },
          {
            "DisplayText": "Acute Leukemia",
            "DisplayCount": "81",
            "Value": "PS592/A/Acute Leukemia|3264",
            "Data": "PS592/A/Acute Leukemia|3264",
            "Id": "3264",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/3264"
            }
          },
          {
            "DisplayText": "Acute Lymphoid Leukemia",
            "DisplayCount": "25",
            "Value": "PS592/A/Acute Lymphoid Leukemia|52169",
            "Data": "PS592/A/Acute Lymphoid Leukemia|52169",
            "Id": "52169",
            "Content": {}
          },
          {
            "DisplayText": "Acute Myeloid Leukemia",
            "DisplayCount": "37",
            "Value": "PS592/A/Acute Myeloid Leukemia|11627",
            "Data": "PS592/A/Acute Myeloid Leukemia|11627",
            "Id": "11627",
            "Content": {}
          },
          {
            "DisplayText": "Adrenal Cortical Carcinoma",
            "DisplayCount": "81",
            "Value": "PS592/A/Adrenal Cortical Carcinoma|3384",
            "Data": "PS592/A/Adrenal Cortical Carcinoma|3384",
            "Id": "3384",
            "Content": {}
          },
          {
            "DisplayText": "Adrenal Gland Cancer",
            "DisplayCount": "81",
            "Value": "PS592/A/Adrenal Gland Cancer|51042",
            "Data": "PS592/A/Adrenal Gland Cancer|51042",
            "Id": "51042",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51042"
            }
          },
          {
            "DisplayText": "All Lymphoma",
            "DisplayCount": "53",
            "Value": "PS592/A/All Lymphoma|52142",
            "Data": "PS592/A/All Lymphoma|52142",
            "Id": "52142",
            "Content": {}
          },
          {
            "DisplayText": "Anal and Rectal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/A/Anal and Rectal Cancer|51043",
            "Data": "PS592/A/Anal and Rectal Cancer|51043",
            "Id": "51043",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51043"
            }
          },
          {
            "DisplayText": "Anal Disorders",
            "DisplayCount": "35",
            "Value": "PS592/A/Anal Disorders|3759",
            "Data": "PS592/A/Anal Disorders|3759",
            "Id": "3759",
            "Content": {}
          },
          {
            "DisplayText": "Anaplastic Oligodendroglioma",
            "DisplayCount": "81",
            "Value": "PS592/A/Anaplastic Oligodendroglioma|50887",
            "Data": "PS592/A/Anaplastic Oligodendroglioma|50887",
            "Id": "50887",
            "Content": {}
          },
          {
            "DisplayText": "Anemia",
            "DisplayCount": "61",
            "Value": "PS592/A/Anemia|75",
            "Data": "PS592/A/Anemia|75",
            "Id": "75",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/75"
            }
          },
          {
            "DisplayText": "Aneurysm",
            "DisplayCount": "1",
            "Value": "PS592/A/Aneurysm|1611",
            "Data": "PS592/A/Aneurysm|1611",
            "Id": "1611",
            "Content": {}
          },
          {
            "DisplayText": "Antiphospholipid Syndrome (APS)",
            "DisplayCount": "26",
            "Value": "PS592/A/Antiphospholipid Syndrome (APS)|3997",
            "Data": "PS592/A/Antiphospholipid Syndrome (APS)|3997",
            "Id": "3997",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/3997"
            }
          },
          {
            "DisplayText": "Aortic Embolism and Thrombosis",
            "DisplayCount": "1",
            "Value": "PS592/A/Aortic Embolism and Thrombosis|51050",
            "Data": "PS592/A/Aortic Embolism and Thrombosis|51050",
            "Id": "51050",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51050"
            }
          },
          {
            "DisplayText": "Arrhythmias",
            "DisplayCount": "1",
            "Value": "PS592/A/Arrhythmias|51051",
            "Data": "PS592/A/Arrhythmias|51051",
            "Id": "51051",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51051"
            }
          },
          {
            "DisplayText": "Astrocytoma",
            "DisplayCount": "81",
            "Value": "PS592/A/Astrocytoma|1658",
            "Data": "PS592/A/Astrocytoma|1658",
            "Id": "1658",
            "Content": {}
          },
          {
            "DisplayText": "Athlete's Foot",
            "DisplayCount": "1",
            "Value": "PS592/A/Athlete's Foot|1664",
            "Data": "PS592/A/Athlete's Foot|1664",
            "Id": "1664",
            "Content": {}
          },
          {
            "DisplayText": "Atopic Dermatitis (Eczema)",
            "DisplayCount": "1",
            "Value": "PS592/A/Atopic Dermatitis (Eczema)|1666",
            "Data": "PS592/A/Atopic Dermatitis (Eczema)|1666",
            "Id": "1666",
            "Content": {}
          },
          {
            "DisplayText": "Atrial Fibrillation",
            "DisplayCount": "1",
            "Value": "PS592/A/Atrial Fibrillation|4",
            "Data": "PS592/A/Atrial Fibrillation|4",
            "Id": "4",
            "Content": {}
          },
          {
            "DisplayText": "Autoimmune Diseases",
            "DisplayCount": "40",
            "Value": "PS592/A/Autoimmune Diseases|4384",
            "Data": "PS592/A/Autoimmune Diseases|4384",
            "Id": "4384",
            "Content": {}
          },
          {
            "DisplayText": "Basal Cell Carcinoma",
            "DisplayCount": "42",
            "Value": "PS592/B/Basal Cell Carcinoma |1693",
            "Data": "PS592/B/Basal Cell Carcinoma |1693",
            "Id": "1693",
            "Content": {}
          },
          {
            "DisplayText": "Basal Cell Carcinoma",
            "DisplayCount": "53",
            "Value": "PS592/B/Basal Cell Carcinoma|1693",
            "Data": "PS592/B/Basal Cell Carcinoma|1693",
            "Id": "1693",
            "Content": {}
          },
          {
            "DisplayText": "Benign Tumor",
            "DisplayCount": "3",
            "Value": "PS592/B/Benign Tumor|4656",
            "Data": "PS592/B/Benign Tumor|4656",
            "Id": "4656",
            "Content": {}
          },
          {
            "DisplayText": "Bile Duct Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Bile Duct Cancer|4737",
            "Data": "PS592/B/Bile Duct Cancer|4737",
            "Id": "4737",
            "Content": {}
          },
          {
            "DisplayText": "Biliary Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Biliary Cancer|1703",
            "Data": "PS592/B/Biliary Cancer|1703",
            "Id": "1703",
            "Content": {}
          },
          {
            "DisplayText": "Birthmark",
            "DisplayCount": "1",
            "Value": "PS592/B/Birthmark|1711",
            "Data": "PS592/B/Birthmark|1711",
            "Id": "1711",
            "Content": {}
          },
          {
            "DisplayText": "Bladder Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Bladder Cancer|120",
            "Data": "PS592/B/Bladder Cancer|120",
            "Id": "120",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/120"
            }
          },
          {
            "DisplayText": "Bleeding Disorders",
            "DisplayCount": "43",
            "Value": "PS592/B/Bleeding Disorders|4806",
            "Data": "PS592/B/Bleeding Disorders|4806",
            "Id": "4806",
            "Content": {}
          },
          {
            "DisplayText": "Blood Cancer",
            "DisplayCount": "1",
            "Value": "PS592/B/Blood Cancer|4832",
            "Data": "PS592/B/Blood Cancer|4832",
            "Id": "4832",
            "Content": {}
          },
          {
            "DisplayText": "Blood Disorders",
            "DisplayCount": "50",
            "Value": "PS592/B/Blood Disorders|4834",
            "Data": "PS592/B/Blood Disorders|4834",
            "Id": "4834",
            "Content": {}
          },
          {
            "DisplayText": "Bone Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Cancer|126",
            "Data": "PS592/B/Bone Cancer|126",
            "Id": "126",
            "Content": {}
          },
          {
            "DisplayText": "Bone Disorders",
            "DisplayCount": "46",
            "Value": "PS592/B/Bone Disorders|50903",
            "Data": "PS592/B/Bone Disorders|50903",
            "Id": "50903",
            "Content": {}
          },
          {
            "DisplayText": "Bone Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Sarcoma|51017",
            "Data": "PS592/B/Bone Sarcoma|51017",
            "Id": "51017",
            "Content": {}
          },
          {
            "DisplayText": "Brain and Nervous System Cancer (incl. Gliomas, Astrocytoma, Schwannoma, Medulloblastoma, Chordoma)",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain and Nervous System Cancer (incl. Gliomas, Astrocytoma, Schwannoma, Medulloblastoma, Chordoma)|51055",
            "Data": "PS592/B/Brain and Nervous System Cancer (incl. Gliomas, Astrocytoma, Schwannoma, Medulloblastoma, Chordoma)|51055",
            "Id": "51055",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51055"
            }
          },
          {
            "DisplayText": "Brain Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain Cancer|142",
            "Data": "PS592/B/Brain Cancer|142",
            "Id": "142",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/142"
            }
          },
          {
            "DisplayText": "Brain Disorders",
            "DisplayCount": "40",
            "Value": "PS592/B/Brain Disorders|1410",
            "Data": "PS592/B/Brain Disorders|1410",
            "Id": "1410",
            "Content": {}
          },
          {
            "DisplayText": "Brain Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain Sarcoma|50908",
            "Data": "PS592/B/Brain Sarcoma|50908",
            "Id": "50908",
            "Content": {}
          },
          {
            "DisplayText": "Brain Tumor",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain Tumor|1437",
            "Data": "PS592/B/Brain Tumor|1437",
            "Id": "1437",
            "Content": {}
          },
          {
            "DisplayText": "Breast Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Cancer|130",
            "Data": "PS592/B/Breast Cancer|130",
            "Id": "130",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/130"
            }
          },
          {
            "DisplayText": "Breast Cancer Recurrence",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Cancer Recurrence|50909",
            "Data": "PS592/B/Breast Cancer Recurrence|50909",
            "Id": "50909",
            "Content": {}
          },
          {
            "DisplayText": "Breast Diseases",
            "DisplayCount": "43",
            "Value": "PS592/B/Breast Diseases|18366",
            "Data": "PS592/B/Breast Diseases|18366",
            "Id": "18366",
            "Content": {}
          },
          {
            "DisplayText": "Breast Lump",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Lump|51141",
            "Data": "PS592/B/Breast Lump|51141",
            "Id": "51141",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51141"
            }
          },
          {
            "DisplayText": "Breast Tumor",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Tumor|18734",
            "Data": "PS592/B/Breast Tumor|18734",
            "Id": "18734",
            "Content": {}
          },
          {
            "DisplayText": "Burkitt's Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/B/Burkitt's Lymphoma|5128",
            "Data": "PS592/B/Burkitt's Lymphoma|5128",
            "Id": "5128",
            "Content": {}
          },
          {
            "DisplayText": "Cancer",
            "DisplayCount": "81",
            "Value": "PS592/C/Cancer|1765",
            "Data": "PS592/C/Cancer|1765",
            "Id": "1765",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Treatment Complications",
            "DisplayCount": "2",
            "Value": "PS592/C/Cancer Treatment Complications|70",
            "Data": "PS592/C/Cancer Treatment Complications|70",
            "Id": "70",
            "Content": {}
          },
          {
            "DisplayText": "Carcinoma in Situ",
            "DisplayCount": "81",
            "Value": "PS592/C/Carcinoma in Situ|51057",
            "Data": "PS592/C/Carcinoma in Situ|51057",
            "Id": "51057",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51057"
            }
          },
          {
            "DisplayText": "Cardiomyopathy",
            "DisplayCount": "1",
            "Value": "PS592/C/Cardiomyopathy|1440",
            "Data": "PS592/C/Cardiomyopathy|1440",
            "Id": "1440",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/1440"
            }
          },
          {
            "DisplayText": "Cellulitis",
            "DisplayCount": "1",
            "Value": "PS592/C/Cellulitis|5461",
            "Data": "PS592/C/Cellulitis|5461",
            "Id": "5461",
            "Content": {}
          },
          {
            "DisplayText": "Central Nervous System Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/C/Central Nervous System Lymphoma|19755",
            "Data": "PS592/C/Central Nervous System Lymphoma|19755",
            "Id": "19755",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/19755"
            }
          },
          {
            "DisplayText": "Cervical Cancer",
            "DisplayCount": "81",
            "Value": "PS592/C/Cervical Cancer|144",
            "Data": "PS592/C/Cervical Cancer|144",
            "Id": "144",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/144"
            }
          },
          {
            "DisplayText": "Chondrosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/C/Chondrosarcoma|6331",
            "Data": "PS592/C/Chondrosarcoma|6331",
            "Id": "6331",
            "Content": {}
          },
          {
            "DisplayText": "Chordoma",
            "DisplayCount": "81",
            "Value": "PS592/C/Chordoma|6334",
            "Data": "PS592/C/Chordoma|6334",
            "Id": "6334",
            "Content": {}
          },
          {
            "DisplayText": "Chronic Myeloid Leukemia (CML)",
            "DisplayCount": "81",
            "Value": "PS592/C/Chronic Myeloid Leukemia (CML)|668",
            "Data": "PS592/C/Chronic Myeloid Leukemia (CML)|668",
            "Id": "668",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/668"
            }
          },
          {
            "DisplayText": "Clival Tumor",
            "DisplayCount": "81",
            "Value": "PS592/C/Clival Tumor|50921",
            "Data": "PS592/C/Clival Tumor|50921",
            "Id": "50921",
            "Content": {}
          },
          {
            "DisplayText": "Coagulation Defects in Pregnancy and Postpartum",
            "DisplayCount": "81",
            "Value": "PS592/C/Coagulation Defects in Pregnancy and Postpartum|51977",
            "Data": "PS592/C/Coagulation Defects in Pregnancy and Postpartum|51977",
            "Id": "51977",
            "Content": {}
          },
          {
            "DisplayText": "Coagulation Disorders (incl. Hemophilia)",
            "DisplayCount": "81",
            "Value": "PS592/C/Coagulation Disorders (incl. Hemophilia)|51678",
            "Data": "PS592/C/Coagulation Disorders (incl. Hemophilia)|51678",
            "Id": "51678",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51678"
            }
          },
          {
            "DisplayText": "Cold Sore",
            "DisplayCount": "1",
            "Value": "PS592/C/Cold Sore|1851",
            "Data": "PS592/C/Cold Sore|1851",
            "Id": "1851",
            "Content": {}
          },
          {
            "DisplayText": "Colon Cancer",
            "DisplayCount": "3",
            "Value": "PS592/C/Colon Cancer|1852",
            "Data": "PS592/C/Colon Cancer|1852",
            "Id": "1852",
            "Content": {}
          },
          {
            "DisplayText": "Colorectal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/C/Colorectal Cancer|19102",
            "Data": "PS592/C/Colorectal Cancer|19102",
            "Id": "19102",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/19102"
            }
          },
          {
            "DisplayText": "COPD (Chronic Obstructive Pulmonary Disease)",
            "DisplayCount": "1",
            "Value": "PS592/C/COPD (Chronic Obstructive Pulmonary Disease)|1827",
            "Data": "PS592/C/COPD (Chronic Obstructive Pulmonary Disease)|1827",
            "Id": "1827",
            "Content": {}
          },
          {
            "DisplayText": "Coronary Artery Disease (CAD)",
            "DisplayCount": "1",
            "Value": "PS592/C/Coronary Artery Disease (CAD)|19699",
            "Data": "PS592/C/Coronary Artery Disease (CAD)|19699",
            "Id": "19699",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/19699"
            }
          },
          {
            "DisplayText": "Cryoglobulinemia",
            "DisplayCount": "12",
            "Value": "PS592/C/Cryoglobulinemia|50698",
            "Data": "PS592/C/Cryoglobulinemia|50698",
            "Id": "50698",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/50698"
            }
          },
          {
            "DisplayText": "Deep Vein Thrombosis (DVT)",
            "DisplayCount": "28",
            "Value": "PS592/D/Deep Vein Thrombosis (DVT)|7536",
            "Data": "PS592/D/Deep Vein Thrombosis (DVT)|7536",
            "Id": "7536",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/7536"
            }
          },
          {
            "DisplayText": "Dermatitis",
            "DisplayCount": "1",
            "Value": "PS592/D/Dermatitis|1922",
            "Data": "PS592/D/Dermatitis|1922",
            "Id": "1922",
            "Content": {}
          },
          {
            "DisplayText": "Dermatological Disorders",
            "DisplayCount": "1",
            "Value": "PS592/D/Dermatological Disorders|19798",
            "Data": "PS592/D/Dermatological Disorders|19798",
            "Id": "19798",
            "Content": {}
          },
          {
            "DisplayText": "ENT Cancer",
            "DisplayCount": "81",
            "Value": "PS592/E/ENT Cancer|51067",
            "Data": "PS592/E/ENT Cancer|51067",
            "Id": "51067",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51067"
            }
          },
          {
            "DisplayText": "Eosinophilia",
            "DisplayCount": "1",
            "Value": "PS592/E/Eosinophilia|51664",
            "Data": "PS592/E/Eosinophilia|51664",
            "Id": "51664",
            "Content": {}
          },
          {
            "DisplayText": "Ependymoma",
            "DisplayCount": "81",
            "Value": "PS592/E/Ependymoma|2002",
            "Data": "PS592/E/Ependymoma|2002",
            "Id": "2002",
            "Content": {}
          },
          {
            "DisplayText": "Esophageal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/E/Esophageal Cancer|149",
            "Data": "PS592/E/Esophageal Cancer|149",
            "Id": "149",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/149"
            }
          },
          {
            "DisplayText": "Esophageal Diseases",
            "DisplayCount": "28",
            "Value": "PS592/E/Esophageal Diseases|19830",
            "Data": "PS592/E/Esophageal Diseases|19830",
            "Id": "19830",
            "Content": {}
          },
          {
            "DisplayText": "Ewing's Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/E/Ewing's Sarcoma|2016",
            "Data": "PS592/E/Ewing's Sarcoma|2016",
            "Id": "2016",
            "Content": {}
          },
          {
            "DisplayText": "Exposure to Synthetic Estrogen Diethylstilbestrol",
            "DisplayCount": "81",
            "Value": "PS592/E/Exposure to Synthetic Estrogen Diethylstilbestrol|50941",
            "Data": "PS592/E/Exposure to Synthetic Estrogen Diethylstilbestrol|50941",
            "Id": "50941",
            "Content": {}
          },
          {
            "DisplayText": "External Ear Disorders",
            "DisplayCount": "1",
            "Value": "PS592/E/External Ear Disorders|8318",
            "Data": "PS592/E/External Ear Disorders|8318",
            "Id": "8318",
            "Content": {}
          },
          {
            "DisplayText": "Eye Cancer",
            "DisplayCount": "26",
            "Value": "PS592/E/Eye Cancer|8776",
            "Data": "PS592/E/Eye Cancer|8776",
            "Id": "8776",
            "Content": {}
          },
          {
            "DisplayText": "Eyelid Growth",
            "DisplayCount": "1",
            "Value": "PS592/E/Eyelid Growth|710",
            "Data": "PS592/E/Eyelid Growth|710",
            "Id": "710",
            "Content": {}
          },
          {
            "DisplayText": "Eyelid Lesions",
            "DisplayCount": "1",
            "Value": "PS592/E/Eyelid Lesions|19448",
            "Data": "PS592/E/Eyelid Lesions|19448",
            "Id": "19448",
            "Content": {}
          },
          {
            "DisplayText": "Fallopian Tube Cancer",
            "DisplayCount": "81",
            "Value": "PS592/F/Fallopian Tube Cancer|841",
            "Data": "PS592/F/Fallopian Tube Cancer|841",
            "Id": "841",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/841"
            }
          },
          {
            "DisplayText": "Fibrosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/F/Fibrosarcoma|9084",
            "Data": "PS592/F/Fibrosarcoma|9084",
            "Id": "9084",
            "Content": {}
          },
          {
            "DisplayText": "Follicular Lymphoma, Large-Cell",
            "DisplayCount": "1",
            "Value": "PS592/F/Follicular Lymphoma, Large-Cell|11894",
            "Data": "PS592/F/Follicular Lymphoma, Large-Cell|11894",
            "Id": "11894",
            "Content": {}
          },
          {
            "DisplayText": "Folliculitis",
            "DisplayCount": "1",
            "Value": "PS592/F/Folliculitis|278",
            "Data": "PS592/F/Folliculitis|278",
            "Id": "278",
            "Content": {}
          },
          {
            "DisplayText": "Foot Conditions",
            "DisplayCount": "1",
            "Value": "PS592/F/Foot Conditions|9346",
            "Data": "PS592/F/Foot Conditions|9346",
            "Id": "9346",
            "Content": {}
          },
          {
            "DisplayText": "Fungal Nail Infection",
            "DisplayCount": "1",
            "Value": "PS592/F/Fungal Nail Infection|9443",
            "Data": "PS592/F/Fungal Nail Infection|9443",
            "Id": "9443",
            "Content": {}
          },
          {
            "DisplayText": "Gallbladder and Biliary Tract Cancer",
            "DisplayCount": "81",
            "Value": "PS592/G/Gallbladder and Biliary Tract Cancer|51075",
            "Data": "PS592/G/Gallbladder and Biliary Tract Cancer|51075",
            "Id": "51075",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51075"
            }
          },
          {
            "DisplayText": "Gallbladder Cancer",
            "DisplayCount": "81",
            "Value": "PS592/G/Gallbladder Cancer|150",
            "Data": "PS592/G/Gallbladder Cancer|150",
            "Id": "150",
            "Content": {}
          },
          {
            "DisplayText": "Gastrointestinal Diseases",
            "DisplayCount": "47",
            "Value": "PS592/G/Gastrointestinal Diseases|51340",
            "Data": "PS592/G/Gastrointestinal Diseases|51340",
            "Id": "51340",
            "Content": {}
          },
          {
            "DisplayText": "Genital Warts",
            "DisplayCount": "1",
            "Value": "PS592/G/Genital Warts|9543",
            "Data": "PS592/G/Genital Warts|9543",
            "Id": "9543",
            "Content": {}
          },
          {
            "DisplayText": "Glioblastoma",
            "DisplayCount": "81",
            "Value": "PS592/G/Glioblastoma|9628",
            "Data": "PS592/G/Glioblastoma|9628",
            "Id": "9628",
            "Content": {}
          },
          {
            "DisplayText": "Glioma",
            "DisplayCount": "81",
            "Value": "PS592/G/Glioma|2105",
            "Data": "PS592/G/Glioma|2105",
            "Id": "2105",
            "Content": {}
          },
          {
            "DisplayText": "Graft vs Host Disease",
            "DisplayCount": "81",
            "Value": "PS592/G/Graft vs Host Disease|51077",
            "Data": "PS592/G/Graft vs Host Disease|51077",
            "Id": "51077",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51077"
            }
          },
          {
            "DisplayText": "Gum Cancer",
            "DisplayCount": "81",
            "Value": "PS592/G/Gum Cancer|51891",
            "Data": "PS592/G/Gum Cancer|51891",
            "Id": "51891",
            "Content": {}
          },
          {
            "DisplayText": "Gynecologic Cancer",
            "DisplayCount": "50",
            "Value": "PS592/G/Gynecologic Cancer|1370",
            "Data": "PS592/G/Gynecologic Cancer|1370",
            "Id": "1370",
            "Content": {}
          },
          {
            "DisplayText": "Hair Conditions",
            "DisplayCount": "1",
            "Value": "PS592/H/Hair Conditions|9855",
            "Data": "PS592/H/Hair Conditions|9855",
            "Id": "9855",
            "Content": {}
          },
          {
            "DisplayText": "Hair Loss",
            "DisplayCount": "1",
            "Value": "PS592/H/Hair Loss|1588",
            "Data": "PS592/H/Hair Loss|1588",
            "Id": "1588",
            "Content": {}
          },
          {
            "DisplayText": "Head and Neck Cancer",
            "DisplayCount": "53",
            "Value": "PS592/H/Head and Neck Cancer|52137",
            "Data": "PS592/H/Head and Neck Cancer|52137",
            "Id": "52137",
            "Content": {}
          },
          {
            "DisplayText": "Head and Neck Tumor",
            "DisplayCount": "81",
            "Value": "PS592/H/Head and Neck Tumor|18765",
            "Data": "PS592/H/Head and Neck Tumor|18765",
            "Id": "18765",
            "Content": {}
          },
          {
            "DisplayText": "Heart Disease",
            "DisplayCount": "1",
            "Value": "PS592/H/Heart Disease|1468",
            "Data": "PS592/H/Heart Disease|1468",
            "Id": "1468",
            "Content": {}
          },
          {
            "DisplayText": "Heart Tumors, Malignant",
            "DisplayCount": "81",
            "Value": "PS592/H/Heart Tumors, Malignant|51059",
            "Data": "PS592/H/Heart Tumors, Malignant|51059",
            "Id": "51059",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51059"
            }
          },
          {
            "DisplayText": "Hemophilia",
            "DisplayCount": "81",
            "Value": "PS592/H/Hemophilia|314",
            "Data": "PS592/H/Hemophilia|314",
            "Id": "314",
            "Content": {}
          },
          {
            "DisplayText": "Hemophilia A",
            "DisplayCount": "81",
            "Value": "PS592/H/Hemophilia A|10024",
            "Data": "PS592/H/Hemophilia A|10024",
            "Id": "10024",
            "Content": {}
          },
          {
            "DisplayText": "Hemorrhage from Placenta Previa",
            "DisplayCount": "81",
            "Value": "PS592/H/Hemorrhage from Placenta Previa|51934",
            "Data": "PS592/H/Hemorrhage from Placenta Previa|51934",
            "Id": "51934",
            "Content": {}
          },
          {
            "DisplayText": "Herpes Simplex Infection",
            "DisplayCount": "1",
            "Value": "PS592/H/Herpes Simplex Infection|2163",
            "Data": "PS592/H/Herpes Simplex Infection|2163",
            "Id": "2163",
            "Content": {}
          },
          {
            "DisplayText": "Hidradenitis",
            "DisplayCount": "1",
            "Value": "PS592/H/Hidradenitis|51079",
            "Data": "PS592/H/Hidradenitis|51079",
            "Id": "51079",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51079"
            }
          },
          {
            "DisplayText": "Hives",
            "DisplayCount": "1",
            "Value": "PS592/H/Hives|2172",
            "Data": "PS592/H/Hives|2172",
            "Id": "2172",
            "Content": {}
          },
          {
            "DisplayText": "Hodgkin's Disease",
            "DisplayCount": "81",
            "Value": "PS592/H/Hodgkin's Disease|152",
            "Data": "PS592/H/Hodgkin's Disease|152",
            "Id": "152",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/152"
            }
          },
          {
            "DisplayText": "Hypercoagulable State",
            "DisplayCount": "34",
            "Value": "PS592/H/Hypercoagulable State|52162",
            "Data": "PS592/H/Hypercoagulable State|52162",
            "Id": "52162",
            "Content": {}
          },
          {
            "DisplayText": "Hyperthrophic Scar",
            "DisplayCount": "1",
            "Value": "PS592/H/Hyperthrophic Scar|51357",
            "Data": "PS592/H/Hyperthrophic Scar|51357",
            "Id": "51357",
            "Content": {}
          },
          {
            "DisplayText": "Immune Thrombocytopenic Purpura (ITP)",
            "DisplayCount": "81",
            "Value": "PS592/I/Immune Thrombocytopenic Purpura (ITP)|2211",
            "Data": "PS592/I/Immune Thrombocytopenic Purpura (ITP)|2211",
            "Id": "2211",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2211"
            }
          },
          {
            "DisplayText": "Kaposi's Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/K/Kaposi's Sarcoma|11113",
            "Data": "PS592/K/Kaposi's Sarcoma|11113",
            "Id": "11113",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/11113"
            }
          },
          {
            "DisplayText": "Keloid Scar",
            "DisplayCount": "1",
            "Value": "PS592/K/Keloid Scar|11131",
            "Data": "PS592/K/Keloid Scar|11131",
            "Id": "11131",
            "Content": {}
          },
          {
            "DisplayText": "Kidney Cancer",
            "DisplayCount": "81",
            "Value": "PS592/K/Kidney Cancer|153",
            "Data": "PS592/K/Kidney Cancer|153",
            "Id": "153",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/153"
            }
          },
          {
            "DisplayText": "Lambert-Eaton Syndrome",
            "DisplayCount": "81",
            "Value": "PS592/L/Lambert-Eaton Syndrome|51087",
            "Data": "PS592/L/Lambert-Eaton Syndrome|51087",
            "Id": "51087",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51087"
            }
          },
          {
            "DisplayText": "Laryngeal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/L/Laryngeal Cancer|2286",
            "Data": "PS592/L/Laryngeal Cancer|2286",
            "Id": "2286",
            "Content": {}
          },
          {
            "DisplayText": "Larynx Conditions",
            "DisplayCount": "15",
            "Value": "PS592/L/Larynx Conditions|11414",
            "Data": "PS592/L/Larynx Conditions|11414",
            "Id": "11414",
            "Content": {}
          },
          {
            "DisplayText": "Leg and Foot Ulcers",
            "DisplayCount": "1",
            "Value": "PS592/L/Leg and Foot Ulcers|51789",
            "Data": "PS592/L/Leg and Foot Ulcers|51789",
            "Id": "51789",
            "Content": {}
          },
          {
            "DisplayText": "Leukemia",
            "DisplayCount": "81",
            "Value": "PS592/L/Leukemia|62",
            "Data": "PS592/L/Leukemia|62",
            "Id": "62",
            "Content": {}
          },
          {
            "DisplayText": "Leukocytosis",
            "DisplayCount": "49",
            "Value": "PS592/L/Leukocytosis|51089",
            "Data": "PS592/L/Leukocytosis|51089",
            "Id": "51089",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51089"
            }
          },
          {
            "DisplayText": "Lip Cancer",
            "DisplayCount": "81",
            "Value": "PS592/L/Lip Cancer|11717",
            "Data": "PS592/L/Lip Cancer|11717",
            "Id": "11717",
            "Content": {}
          },
          {
            "DisplayText": "Liposarcoma",
            "DisplayCount": "81",
            "Value": "PS592/L/Liposarcoma|11741",
            "Data": "PS592/L/Liposarcoma|11741",
            "Id": "11741",
            "Content": {}
          },
          {
            "DisplayText": "Liver Cancer",
            "DisplayCount": "81",
            "Value": "PS592/L/Liver Cancer|155",
            "Data": "PS592/L/Liver Cancer|155",
            "Id": "155",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/155"
            }
          },
          {
            "DisplayText": "Liver Tumor",
            "DisplayCount": "81",
            "Value": "PS592/L/Liver Tumor|1413",
            "Data": "PS592/L/Liver Tumor|1413",
            "Id": "1413",
            "Content": {}
          },
          {
            "DisplayText": "Lung Cancer",
            "DisplayCount": "81",
            "Value": "PS592/L/Lung Cancer|156",
            "Data": "PS592/L/Lung Cancer|156",
            "Id": "156",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/156"
            }
          },
          {
            "DisplayText": "Lung Neoplasms, Not Specified as Malignant",
            "DisplayCount": "18",
            "Value": "PS592/L/Lung Neoplasms, Not Specified as Malignant|51183",
            "Data": "PS592/L/Lung Neoplasms, Not Specified as Malignant|51183",
            "Id": "51183",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51183"
            }
          },
          {
            "DisplayText": "Lymphocytosis",
            "DisplayCount": "32",
            "Value": "PS592/L/Lymphocytosis|51091",
            "Data": "PS592/L/Lymphocytosis|51091",
            "Id": "51091",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51091"
            }
          },
          {
            "DisplayText": "Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphoma|1395",
            "Data": "PS592/L/Lymphoma|1395",
            "Id": "1395",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/1395"
            }
          },
          {
            "DisplayText": "Lymphoma of the Bone",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphoma of the Bone|50904",
            "Data": "PS592/L/Lymphoma of the Bone|50904",
            "Id": "50904",
            "Content": {}
          },
          {
            "DisplayText": "Lymphoma of the Brain",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphoma of the Brain|50907",
            "Data": "PS592/L/Lymphoma of the Brain|50907",
            "Id": "50907",
            "Content": {}
          },
          {
            "DisplayText": "Lymphoma, Large Cell, Anaplastic",
            "DisplayCount": "39",
            "Value": "PS592/L/Lymphoma, Large Cell, Anaplastic|3767",
            "Data": "PS592/L/Lymphoma, Large Cell, Anaplastic|3767",
            "Id": "3767",
            "Content": {}
          },
          {
            "DisplayText": "Lymphoma, Large Cell, Anaplastic",
            "DisplayCount": "42",
            "Value": "PS592/L/Lymphoma, Large Cell, Anaplastic |3767",
            "Data": "PS592/L/Lymphoma, Large Cell, Anaplastic |3767",
            "Id": "3767",
            "Content": {}
          },
          {
            "DisplayText": "Lymphoma, Large-Cell",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphoma, Large-Cell|11893",
            "Data": "PS592/L/Lymphoma, Large-Cell|11893",
            "Id": "11893",
            "Content": {}
          },
          {
            "DisplayText": "Lymphosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphosarcoma|51941",
            "Data": "PS592/L/Lymphosarcoma|51941",
            "Id": "51941",
            "Content": {}
          },
          {
            "DisplayText": "Macroglobulinemia (incl. Waldenstrom's )",
            "DisplayCount": "81",
            "Value": "PS592/M/Macroglobulinemia (incl. Waldenstrom's )|51184",
            "Data": "PS592/M/Macroglobulinemia (incl. Waldenstrom's )|51184",
            "Id": "51184",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51184"
            }
          },
          {
            "DisplayText": "Male Breast Cancer",
            "DisplayCount": "81",
            "Value": "PS592/M/Male Breast Cancer|11989",
            "Data": "PS592/M/Male Breast Cancer|11989",
            "Id": "11989",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Bone Cancer of the Skull, Face, and Jaw",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Bone Cancer of the Skull, Face, and Jaw|51902",
            "Data": "PS592/M/Malignant Bone Cancer of the Skull, Face, and Jaw|51902",
            "Id": "51902",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Brain Tumor",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Brain Tumor|50973",
            "Data": "PS592/M/Malignant Brain Tumor|50973",
            "Id": "50973",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Breast Tumor",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Breast Tumor|50974",
            "Data": "PS592/M/Malignant Breast Tumor|50974",
            "Id": "50974",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Glioma",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Glioma|50975",
            "Data": "PS592/M/Malignant Glioma|50975",
            "Id": "50975",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Histiocytosis",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Histiocytosis|52027",
            "Data": "PS592/M/Malignant Histiocytosis|52027",
            "Id": "52027",
            "Content": {}
          },
          {
            "DisplayText": "Mantle Cell Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/M/Mantle Cell Lymphoma|12070",
            "Data": "PS592/M/Mantle Cell Lymphoma|12070",
            "Id": "12070",
            "Content": {}
          },
          {
            "DisplayText": "Marginal Zone Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/M/Marginal Zone Lymphoma|51968",
            "Data": "PS592/M/Marginal Zone Lymphoma|51968",
            "Id": "51968",
            "Content": {}
          },
          {
            "DisplayText": "Mast Cell Diseases",
            "DisplayCount": "6",
            "Value": "PS592/M/Mast Cell Diseases|2335",
            "Data": "PS592/M/Mast Cell Diseases|2335",
            "Id": "2335",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2335"
            }
          },
          {
            "DisplayText": "Maternal Anemia",
            "DisplayCount": "81",
            "Value": "PS592/M/Maternal Anemia|51995",
            "Data": "PS592/M/Maternal Anemia|51995",
            "Id": "51995",
            "Content": {}
          },
          {
            "DisplayText": "Mediastinal Tumors, Malignant",
            "DisplayCount": "25",
            "Value": "PS592/M/Mediastinal Tumors, Malignant|51188",
            "Data": "PS592/M/Mediastinal Tumors, Malignant|51188",
            "Id": "51188",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51188"
            }
          },
          {
            "DisplayText": "Mediastinal Tumors, Not Specified as Malignant",
            "DisplayCount": "1",
            "Value": "PS592/M/Mediastinal Tumors, Not Specified as Malignant|51189",
            "Data": "PS592/M/Mediastinal Tumors, Not Specified as Malignant|51189",
            "Id": "51189",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51189"
            }
          },
          {
            "DisplayText": "Melanoma",
            "DisplayCount": "81",
            "Value": "PS592/M/Melanoma|1495",
            "Data": "PS592/M/Melanoma|1495",
            "Id": "1495",
            "Content": {}
          },
          {
            "DisplayText": "Meningiomas",
            "DisplayCount": "14",
            "Value": "PS592/M/Meningiomas|12242",
            "Data": "PS592/M/Meningiomas|12242",
            "Id": "12242",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/12242"
            }
          },
          {
            "DisplayText": "Merkel Cell Carcinoma",
            "DisplayCount": "81",
            "Value": "PS592/M/Merkel Cell Carcinoma|12406",
            "Data": "PS592/M/Merkel Cell Carcinoma|12406",
            "Id": "12406",
            "Content": {}
          },
          {
            "DisplayText": "Mesothelioma",
            "DisplayCount": "81",
            "Value": "PS592/M/Mesothelioma|2353",
            "Data": "PS592/M/Mesothelioma|2353",
            "Id": "2353",
            "Content": {}
          },
          {
            "DisplayText": "Metastatic Bone Cancer",
            "DisplayCount": "81",
            "Value": "PS592/M/Metastatic Bone Cancer|12463",
            "Data": "PS592/M/Metastatic Bone Cancer|12463",
            "Id": "12463",
            "Content": {}
          },
          {
            "DisplayText": "Metastatic Respiratory System Cancer",
            "DisplayCount": "81",
            "Value": "PS592/M/Metastatic Respiratory System Cancer|51821",
            "Data": "PS592/M/Metastatic Respiratory System Cancer|51821",
            "Id": "51821",
            "Content": {}
          },
          {
            "DisplayText": "Moles (Benign Skin Lesions)",
            "DisplayCount": "1",
            "Value": "PS592/M/Moles (Benign Skin Lesions)|51793",
            "Data": "PS592/M/Moles (Benign Skin Lesions)|51793",
            "Id": "51793",
            "Content": {}
          },
          {
            "DisplayText": "Molluscum Contagiosum Infection",
            "DisplayCount": "1",
            "Value": "PS592/M/Molluscum Contagiosum Infection|12755",
            "Data": "PS592/M/Molluscum Contagiosum Infection|12755",
            "Id": "12755",
            "Content": {}
          },
          {
            "DisplayText": "Multiple Endocrine Neoplasia",
            "DisplayCount": "81",
            "Value": "PS592/M/Multiple Endocrine Neoplasia|12899",
            "Data": "PS592/M/Multiple Endocrine Neoplasia|12899",
            "Id": "12899",
            "Content": {}
          },
          {
            "DisplayText": "Multiple Myeloma",
            "DisplayCount": "81",
            "Value": "PS592/M/Multiple Myeloma|159",
            "Data": "PS592/M/Multiple Myeloma|159",
            "Id": "159",
            "Content": {}
          },
          {
            "DisplayText": "Musculoskeletal Sarcomas",
            "DisplayCount": "81",
            "Value": "PS592/M/Musculoskeletal Sarcomas|50980",
            "Data": "PS592/M/Musculoskeletal Sarcomas|50980",
            "Id": "50980",
            "Content": {}
          },
          {
            "DisplayText": "Musculoskeletal Tumor",
            "DisplayCount": "81",
            "Value": "PS592/M/Musculoskeletal Tumor|50981",
            "Data": "PS592/M/Musculoskeletal Tumor|50981",
            "Id": "50981",
            "Content": {}
          },
          {
            "DisplayText": "Mycosis Fungoides",
            "DisplayCount": "81",
            "Value": "PS592/M/Mycosis Fungoides|2404",
            "Data": "PS592/M/Mycosis Fungoides|2404",
            "Id": "2404",
            "Content": {}
          },
          {
            "DisplayText": "Myelodysplastic Syndromes",
            "DisplayCount": "50",
            "Value": "PS592/M/Myelodysplastic Syndromes|2406",
            "Data": "PS592/M/Myelodysplastic Syndromes|2406",
            "Id": "2406",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2406"
            }
          },
          {
            "DisplayText": "Myeloma",
            "DisplayCount": "81",
            "Value": "PS592/M/Myeloma|13000",
            "Data": "PS592/M/Myeloma|13000",
            "Id": "13000",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/13000"
            }
          },
          {
            "DisplayText": "Myeloproliferative Disorders",
            "DisplayCount": "81",
            "Value": "PS592/M/Myeloproliferative Disorders|18576",
            "Data": "PS592/M/Myeloproliferative Disorders|18576",
            "Id": "18576",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/18576"
            }
          },
          {
            "DisplayText": "Nasal Cavity Cancer",
            "DisplayCount": "81",
            "Value": "PS592/N/Nasal Cavity Cancer|50814",
            "Data": "PS592/N/Nasal Cavity Cancer|50814",
            "Id": "50814",
            "Content": {}
          },
          {
            "DisplayText": "Neck Tumor",
            "DisplayCount": "81",
            "Value": "PS592/N/Neck Tumor|19985",
            "Data": "PS592/N/Neck Tumor|19985",
            "Id": "19985",
            "Content": {}
          },
          {
            "DisplayText": "Neuroendocrine Cancer",
            "DisplayCount": "81",
            "Value": "PS592/N/Neuroendocrine Cancer|50986",
            "Data": "PS592/N/Neuroendocrine Cancer|50986",
            "Id": "50986",
            "Content": {}
          },
          {
            "DisplayText": "Neuroendocrine Tumors",
            "DisplayCount": "81",
            "Value": "PS592/N/Neuroendocrine Tumors|51096",
            "Data": "PS592/N/Neuroendocrine Tumors|51096",
            "Id": "51096",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51096"
            }
          },
          {
            "DisplayText": "Neutropenia",
            "DisplayCount": "52",
            "Value": "PS592/N/Neutropenia|2454",
            "Data": "PS592/N/Neutropenia|2454",
            "Id": "2454",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2454"
            }
          },
          {
            "DisplayText": "Nodular Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/N/Nodular Lymphoma|51975",
            "Data": "PS592/N/Nodular Lymphoma|51975",
            "Id": "51975",
            "Content": {}
          },
          {
            "DisplayText": "Non-Hodgkin's Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/N/Non-Hodgkin's Lymphoma|160",
            "Data": "PS592/N/Non-Hodgkin's Lymphoma|160",
            "Id": "160",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/160"
            }
          },
          {
            "DisplayText": "Non-Small Cell Lung Cancer",
            "DisplayCount": "81",
            "Value": "PS592/N/Non-Small Cell Lung Cancer|50990",
            "Data": "PS592/N/Non-Small Cell Lung Cancer|50990",
            "Id": "50990",
            "Content": {}
          },
          {
            "DisplayText": "Oral Cancer",
            "DisplayCount": "81",
            "Value": "PS592/O/Oral Cancer|1500",
            "Data": "PS592/O/Oral Cancer|1500",
            "Id": "1500",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/1500"
            }
          },
          {
            "DisplayText": "Osteosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/O/Osteosarcoma|2493",
            "Data": "PS592/O/Osteosarcoma|2493",
            "Id": "2493",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2493"
            }
          },
          {
            "DisplayText": "Ovarian Cancer",
            "DisplayCount": "81",
            "Value": "PS592/O/Ovarian Cancer|163",
            "Data": "PS592/O/Ovarian Cancer|163",
            "Id": "163",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/163"
            }
          },
          {
            "DisplayText": "Pancreatic Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Pancreatic Cancer|164",
            "Data": "PS592/P/Pancreatic Cancer|164",
            "Id": "164",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/164"
            }
          },
          {
            "DisplayText": "Pancytopenia",
            "DisplayCount": "44",
            "Value": "PS592/P/Pancytopenia|14161",
            "Data": "PS592/P/Pancytopenia|14161",
            "Id": "14161",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/14161"
            }
          },
          {
            "DisplayText": "Parathyroid Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Parathyroid Cancer|14220",
            "Data": "PS592/P/Parathyroid Cancer|14220",
            "Id": "14220",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/14220"
            }
          },
          {
            "DisplayText": "Paroxysmal Nocturnal Hemoglobinuria",
            "DisplayCount": "8",
            "Value": "PS592/P/Paroxysmal Nocturnal Hemoglobinuria|51101",
            "Data": "PS592/P/Paroxysmal Nocturnal Hemoglobinuria|51101",
            "Id": "51101",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51101"
            }
          },
          {
            "DisplayText": "Penile Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Penile Cancer|14361",
            "Data": "PS592/P/Penile Cancer|14361",
            "Id": "14361",
            "Content": {}
          },
          {
            "DisplayText": "Peripheral Arterial Aneurysm",
            "DisplayCount": "1",
            "Value": "PS592/P/Peripheral Arterial Aneurysm|52155",
            "Data": "PS592/P/Peripheral Arterial Aneurysm|52155",
            "Id": "52155",
            "Content": {}
          },
          {
            "DisplayText": "Peripheral Arterial Aneurysm and Dissection",
            "DisplayCount": "1",
            "Value": "PS592/P/Peripheral Arterial Aneurysm and Dissection|51205",
            "Data": "PS592/P/Peripheral Arterial Aneurysm and Dissection|51205",
            "Id": "51205",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51205"
            }
          },
          {
            "DisplayText": "Peripheral T-Cell Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/P/Peripheral T-Cell Lymphoma|52015",
            "Data": "PS592/P/Peripheral T-Cell Lymphoma|52015",
            "Id": "52015",
            "Content": {}
          },
          {
            "DisplayText": "Pheochromocytoma",
            "DisplayCount": "81",
            "Value": "PS592/P/Pheochromocytoma|14485",
            "Data": "PS592/P/Pheochromocytoma|14485",
            "Id": "14485",
            "Content": {}
          },
          {
            "DisplayText": "Pituitary Gland Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Pituitary Gland Cancer|51105",
            "Data": "PS592/P/Pituitary Gland Cancer|51105",
            "Id": "51105",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51105"
            }
          },
          {
            "DisplayText": "Pituitary Tumor",
            "DisplayCount": "81",
            "Value": "PS592/P/Pituitary Tumor|51000",
            "Data": "PS592/P/Pituitary Tumor|51000",
            "Id": "51000",
            "Content": {}
          },
          {
            "DisplayText": "Pleura Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Pleura Cancer|14671",
            "Data": "PS592/P/Pleura Cancer|14671",
            "Id": "14671",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/14671"
            }
          },
          {
            "DisplayText": "Pleural Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Pleural Cancer|51209",
            "Data": "PS592/P/Pleural Cancer|51209",
            "Id": "51209",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51209"
            }
          },
          {
            "DisplayText": "Pleural Mesothelioma",
            "DisplayCount": "81",
            "Value": "PS592/P/Pleural Mesothelioma|51001",
            "Data": "PS592/P/Pleural Mesothelioma|51001",
            "Id": "51001",
            "Content": {}
          },
          {
            "DisplayText": "Polycythemia Rubra Vera",
            "DisplayCount": "43",
            "Value": "PS592/P/Polycythemia Rubra Vera|51106",
            "Data": "PS592/P/Polycythemia Rubra Vera|51106",
            "Id": "51106",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51106"
            }
          },
          {
            "DisplayText": "Pregnancy-Related Disorders",
            "DisplayCount": "27",
            "Value": "PS592/P/Pregnancy-Related Disorders|14889",
            "Data": "PS592/P/Pregnancy-Related Disorders|14889",
            "Id": "14889",
            "Content": {}
          },
          {
            "DisplayText": "Primary Central Nervous System Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/P/Primary Central Nervous System Lymphoma|51921",
            "Data": "PS592/P/Primary Central Nervous System Lymphoma|51921",
            "Id": "51921",
            "Content": {}
          },
          {
            "DisplayText": "Primary Hypercoagulable State (incl. Factor V Leiden Disease)",
            "DisplayCount": "38",
            "Value": "PS592/P/Primary Hypercoagulable State (incl. Factor V Leiden Disease)|51109",
            "Data": "PS592/P/Primary Hypercoagulable State (incl. Factor V Leiden Disease)|51109",
            "Id": "51109",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51109"
            }
          },
          {
            "DisplayText": "Prostate Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Prostate Cancer|165",
            "Data": "PS592/P/Prostate Cancer|165",
            "Id": "165",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/165"
            }
          },
          {
            "DisplayText": "Psoriasis",
            "DisplayCount": "1",
            "Value": "PS592/P/Psoriasis|534",
            "Data": "PS592/P/Psoriasis|534",
            "Id": "534",
            "Content": {}
          },
          {
            "DisplayText": "Pulmonary Disease",
            "DisplayCount": "43",
            "Value": "PS592/P/Pulmonary Disease|20066",
            "Data": "PS592/P/Pulmonary Disease|20066",
            "Id": "20066",
            "Content": {}
          },
          {
            "DisplayText": "Pulmonary Embolism",
            "DisplayCount": "1",
            "Value": "PS592/P/Pulmonary Embolism|2636",
            "Data": "PS592/P/Pulmonary Embolism|2636",
            "Id": "2636",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2636"
            }
          },
          {
            "DisplayText": "Purpura",
            "DisplayCount": "29",
            "Value": "PS592/P/Purpura|15186",
            "Data": "PS592/P/Purpura|15186",
            "Id": "15186",
            "Content": {}
          },
          {
            "DisplayText": "Qualitative Platelet Defects (incl. Glanzmann's Thrombasthenia)",
            "DisplayCount": "8",
            "Value": "PS592/Q/Qualitative Platelet Defects (incl. Glanzmann's Thrombasthenia)|51111",
            "Data": "PS592/Q/Qualitative Platelet Defects (incl. Glanzmann's Thrombasthenia)|51111",
            "Id": "51111",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51111"
            }
          },
          {
            "DisplayText": "Rash",
            "DisplayCount": "1",
            "Value": "PS592/R/Rash|18652",
            "Data": "PS592/R/Rash|18652",
            "Id": "18652",
            "Content": {}
          },
          {
            "DisplayText": "Reticulosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/R/Reticulosarcoma|51925",
            "Data": "PS592/R/Reticulosarcoma|51925",
            "Id": "51925",
            "Content": {}
          },
          {
            "DisplayText": "Retina Diseases",
            "DisplayCount": "5",
            "Value": "PS592/R/Retina Diseases|783",
            "Data": "PS592/R/Retina Diseases|783",
            "Id": "783",
            "Content": {}
          },
          {
            "DisplayText": "Retinoblastoma",
            "DisplayCount": "81",
            "Value": "PS592/R/Retinoblastoma|2683",
            "Data": "PS592/R/Retinoblastoma|2683",
            "Id": "2683",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2683"
            }
          },
          {
            "DisplayText": "Rhabdomyosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/R/Rhabdomyosarcoma|2689",
            "Data": "PS592/R/Rhabdomyosarcoma|2689",
            "Id": "2689",
            "Content": {}
          },
          {
            "DisplayText": "Ringworm",
            "DisplayCount": "1",
            "Value": "PS592/R/Ringworm|2699",
            "Data": "PS592/R/Ringworm|2699",
            "Id": "2699",
            "Content": {}
          },
          {
            "DisplayText": "Rosacea",
            "DisplayCount": "1",
            "Value": "PS592/R/Rosacea|555",
            "Data": "PS592/R/Rosacea|555",
            "Id": "555",
            "Content": {}
          },
          {
            "DisplayText": "Salivary Gland Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Salivary Gland Cancer|2710",
            "Data": "PS592/S/Salivary Gland Cancer|2710",
            "Id": "2710",
            "Content": {}
          },
          {
            "DisplayText": "Salivary Gland Tumors",
            "DisplayCount": "81",
            "Value": "PS592/S/Salivary Gland Tumors|50842",
            "Data": "PS592/S/Salivary Gland Tumors|50842",
            "Id": "50842",
            "Content": {}
          },
          {
            "DisplayText": "Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/S/Sarcoma|166",
            "Data": "PS592/S/Sarcoma|166",
            "Id": "166",
            "Content": {}
          },
          {
            "DisplayText": "Seborrheic Dermatitis",
            "DisplayCount": "1",
            "Value": "PS592/S/Seborrheic Dermatitis|51794",
            "Data": "PS592/S/Seborrheic Dermatitis|51794",
            "Id": "51794",
            "Content": {}
          },
          {
            "DisplayText": "Secondary Hypertension",
            "DisplayCount": "81",
            "Value": "PS592/S/Secondary Hypertension|16146",
            "Data": "PS592/S/Secondary Hypertension|16146",
            "Id": "16146",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/16146"
            }
          },
          {
            "DisplayText": "Secondary Malignancies",
            "DisplayCount": "81",
            "Value": "PS592/S/Secondary Malignancies|51116",
            "Data": "PS592/S/Secondary Malignancies|51116",
            "Id": "51116",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51116"
            }
          },
          {
            "DisplayText": "Sezary's Disease",
            "DisplayCount": "81",
            "Value": "PS592/S/Sezary's Disease|51978",
            "Data": "PS592/S/Sezary's Disease|51978",
            "Id": "51978",
            "Content": {}
          },
          {
            "DisplayText": "Shingles",
            "DisplayCount": "1",
            "Value": "PS592/S/Shingles|577",
            "Data": "PS592/S/Shingles|577",
            "Id": "577",
            "Content": {}
          },
          {
            "DisplayText": "Sickle Cell Disease",
            "DisplayCount": "31",
            "Value": "PS592/S/Sickle Cell Disease|50553",
            "Data": "PS592/S/Sickle Cell Disease|50553",
            "Id": "50553",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/50553"
            }
          },
          {
            "DisplayText": "Skin Aging",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Aging|2752",
            "Data": "PS592/S/Skin Aging|2752",
            "Id": "2752",
            "Content": {}
          },
          {
            "DisplayText": "Skin Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Skin Cancer|157",
            "Data": "PS592/S/Skin Cancer|157",
            "Id": "157",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/157"
            }
          },
          {
            "DisplayText": "Skin Discoloration",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Discoloration|51721",
            "Data": "PS592/S/Skin Discoloration|51721",
            "Id": "51721",
            "Content": {}
          },
          {
            "DisplayText": "Skin Diseases",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Diseases|46",
            "Data": "PS592/S/Skin Diseases|46",
            "Id": "46",
            "Content": {}
          },
          {
            "DisplayText": "Skin Disorders",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Disorders|16438",
            "Data": "PS592/S/Skin Disorders|16438",
            "Id": "16438",
            "Content": {}
          },
          {
            "DisplayText": "Skin Infections",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Infections|20096",
            "Data": "PS592/S/Skin Infections|20096",
            "Id": "20096",
            "Content": {}
          },
          {
            "DisplayText": "Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Lesion|18779",
            "Data": "PS592/S/Skin Lesion|18779",
            "Id": "18779",
            "Content": {}
          },
          {
            "DisplayText": "Small Cell Lung Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Small Cell Lung Cancer|51019",
            "Data": "PS592/S/Small Cell Lung Cancer|51019",
            "Id": "51019",
            "Content": {}
          },
          {
            "DisplayText": "Small Intestine Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Small Intestine Cancer|52042",
            "Data": "PS592/S/Small Intestine Cancer|52042",
            "Id": "52042",
            "Content": {}
          },
          {
            "DisplayText": "Soft Tissue Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/S/Soft Tissue Sarcoma|2774",
            "Data": "PS592/S/Soft Tissue Sarcoma|2774",
            "Id": "2774",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2774"
            }
          },
          {
            "DisplayText": "Soft Tissue Sarcoma of Head, Face, and Neck",
            "DisplayCount": "81",
            "Value": "PS592/S/Soft Tissue Sarcoma of Head, Face, and Neck|51907",
            "Data": "PS592/S/Soft Tissue Sarcoma of Head, Face, and Neck|51907",
            "Id": "51907",
            "Content": {}
          },
          {
            "DisplayText": "Soft Tissue Tumors of Head and Neck",
            "DisplayCount": "81",
            "Value": "PS592/S/Soft Tissue Tumors of Head and Neck|51021",
            "Data": "PS592/S/Soft Tissue Tumors of Head and Neck|51021",
            "Id": "51021",
            "Content": {}
          },
          {
            "DisplayText": "Spider Veins",
            "DisplayCount": "1",
            "Value": "PS592/S/Spider Veins|19465",
            "Data": "PS592/S/Spider Veins|19465",
            "Id": "19465",
            "Content": {}
          },
          {
            "DisplayText": "Spinal Cord Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Spinal Cord Cancer|51023",
            "Data": "PS592/S/Spinal Cord Cancer|51023",
            "Id": "51023",
            "Content": {}
          },
          {
            "DisplayText": "Spinal Cord Tumor",
            "DisplayCount": "81",
            "Value": "PS592/S/Spinal Cord Tumor|1511",
            "Data": "PS592/S/Spinal Cord Tumor|1511",
            "Id": "1511",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/1511"
            }
          },
          {
            "DisplayText": "Squamous Cell Carcinoma",
            "DisplayCount": "81",
            "Value": "PS592/S/Squamous Cell Carcinoma|2792",
            "Data": "PS592/S/Squamous Cell Carcinoma|2792",
            "Id": "2792",
            "Content": {}
          },
          {
            "DisplayText": "Stomach and Small Intestine Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Stomach and Small Intestine Cancer|51122",
            "Data": "PS592/S/Stomach and Small Intestine Cancer|51122",
            "Id": "51122",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51122"
            }
          },
          {
            "DisplayText": "Stomach Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Stomach Cancer|169",
            "Data": "PS592/S/Stomach Cancer|169",
            "Id": "169",
            "Content": {}
          },
          {
            "DisplayText": "Stomach Diseases",
            "DisplayCount": "44",
            "Value": "PS592/S/Stomach Diseases|2800",
            "Data": "PS592/S/Stomach Diseases|2800",
            "Id": "2800",
            "Content": {}
          },
          {
            "DisplayText": "Stretch Marks",
            "DisplayCount": "1",
            "Value": "PS592/S/Stretch Marks|2804",
            "Data": "PS592/S/Stretch Marks|2804",
            "Id": "2804",
            "Content": {}
          },
          {
            "DisplayText": "Synovial Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/S/Synovial Sarcoma|17002",
            "Data": "PS592/S/Synovial Sarcoma|17002",
            "Id": "17002",
            "Content": {}
          },
          {
            "DisplayText": "Testicular Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Testicular Cancer|170",
            "Data": "PS592/T/Testicular Cancer|170",
            "Id": "170",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/170"
            }
          },
          {
            "DisplayText": "Thalassemia",
            "DisplayCount": "28",
            "Value": "PS592/T/Thalassemia|2841",
            "Data": "PS592/T/Thalassemia|2841",
            "Id": "2841",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2841"
            }
          },
          {
            "DisplayText": "Throat Cancer (Hypopharyngeal)",
            "DisplayCount": "81",
            "Value": "PS592/T/Throat Cancer (Hypopharyngeal)|10653",
            "Data": "PS592/T/Throat Cancer (Hypopharyngeal)|10653",
            "Id": "10653",
            "Content": {}
          },
          {
            "DisplayText": "Throat Cancer (Nasopharyngeal)",
            "DisplayCount": "81",
            "Value": "PS592/T/Throat Cancer (Nasopharyngeal)|2423",
            "Data": "PS592/T/Throat Cancer (Nasopharyngeal)|2423",
            "Id": "2423",
            "Content": {}
          },
          {
            "DisplayText": "Throat Cancer (Oropharyngeal)",
            "DisplayCount": "81",
            "Value": "PS592/T/Throat Cancer (Oropharyngeal)|162",
            "Data": "PS592/T/Throat Cancer (Oropharyngeal)|162",
            "Id": "162",
            "Content": {}
          },
          {
            "DisplayText": "Thrombocytosis",
            "DisplayCount": "42",
            "Value": "PS592/T/Thrombocytosis|17178",
            "Data": "PS592/T/Thrombocytosis|17178",
            "Id": "17178",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/17178"
            }
          },
          {
            "DisplayText": "Thrombosis",
            "DisplayCount": "29",
            "Value": "PS592/T/Thrombosis|2849",
            "Data": "PS592/T/Thrombosis|2849",
            "Id": "2849",
            "Content": {}
          },
          {
            "DisplayText": "Thymomas",
            "DisplayCount": "81",
            "Value": "PS592/T/Thymomas|17191",
            "Data": "PS592/T/Thymomas|17191",
            "Id": "17191",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/17191"
            }
          },
          {
            "DisplayText": "Thyroid Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Thyroid Cancer|172",
            "Data": "PS592/T/Thyroid Cancer|172",
            "Id": "172",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/172"
            }
          },
          {
            "DisplayText": "Tongue Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Tongue Cancer|17253",
            "Data": "PS592/T/Tongue Cancer|17253",
            "Id": "17253",
            "Content": {}
          },
          {
            "DisplayText": "Tonsil Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Tonsil Cancer|51911",
            "Data": "PS592/T/Tonsil Cancer|51911",
            "Id": "51911",
            "Content": {}
          },
          {
            "DisplayText": "Transitional Cell Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Transitional Cell Cancer|2866",
            "Data": "PS592/T/Transitional Cell Cancer|2866",
            "Id": "2866",
            "Content": {}
          },
          {
            "DisplayText": "Tuberous Sclerosis",
            "DisplayCount": "81",
            "Value": "PS592/T/Tuberous Sclerosis|2878",
            "Data": "PS592/T/Tuberous Sclerosis|2878",
            "Id": "2878",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2878"
            }
          },
          {
            "DisplayText": "Tumor",
            "DisplayCount": "1",
            "Value": "PS592/T/Tumor|2880",
            "Data": "PS592/T/Tumor|2880",
            "Id": "2880",
            "Content": {}
          },
          {
            "DisplayText": "Ulcer",
            "DisplayCount": "1",
            "Value": "PS592/U/Ulcer|35",
            "Data": "PS592/U/Ulcer|35",
            "Id": "35",
            "Content": {}
          },
          {
            "DisplayText": "Upper Urinary Tract Tumor",
            "DisplayCount": "81",
            "Value": "PS592/U/Upper Urinary Tract Tumor|50866",
            "Data": "PS592/U/Upper Urinary Tract Tumor|50866",
            "Id": "50866",
            "Content": {}
          },
          {
            "DisplayText": "Ureteral Cancer",
            "DisplayCount": "81",
            "Value": "PS592/U/Ureteral Cancer|51035",
            "Data": "PS592/U/Ureteral Cancer|51035",
            "Id": "51035",
            "Content": {}
          },
          {
            "DisplayText": "Urinary Disorders",
            "DisplayCount": "42",
            "Value": "PS592/U/Urinary Disorders|17704",
            "Data": "PS592/U/Urinary Disorders|17704",
            "Id": "17704",
            "Content": {}
          },
          {
            "DisplayText": "Uterine Cancer",
            "DisplayCount": "81",
            "Value": "PS592/U/Uterine Cancer|2904",
            "Data": "PS592/U/Uterine Cancer|2904",
            "Id": "2904",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2904"
            }
          },
          {
            "DisplayText": "Uterine Diseases",
            "DisplayCount": "27",
            "Value": "PS592/U/Uterine Diseases|695",
            "Data": "PS592/U/Uterine Diseases|695",
            "Id": "695",
            "Content": {}
          },
          {
            "DisplayText": "Uterine Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/U/Uterine Sarcoma|17747",
            "Data": "PS592/U/Uterine Sarcoma|17747",
            "Id": "17747",
            "Content": {}
          },
          {
            "DisplayText": "Vaginal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/V/Vaginal Cancer|837",
            "Data": "PS592/V/Vaginal Cancer|837",
            "Id": "837",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/837"
            }
          },
          {
            "DisplayText": "Varicose Veins",
            "DisplayCount": "1",
            "Value": "PS592/V/Varicose Veins|664",
            "Data": "PS592/V/Varicose Veins|664",
            "Id": "664",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/664"
            }
          },
          {
            "DisplayText": "Vascular Disease",
            "DisplayCount": "45",
            "Value": "PS592/V/Vascular Disease|11392",
            "Data": "PS592/V/Vascular Disease|11392",
            "Id": "11392",
            "Content": {}
          },
          {
            "DisplayText": "Venous Embolism and Thrombosis",
            "DisplayCount": "24",
            "Value": "PS592/V/Venous Embolism and Thrombosis|51230",
            "Data": "PS592/V/Venous Embolism and Thrombosis|51230",
            "Id": "51230",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51230"
            }
          },
          {
            "DisplayText": "Vertebral Column Tumors",
            "DisplayCount": "9",
            "Value": "PS592/V/Vertebral Column Tumors|51127",
            "Data": "PS592/V/Vertebral Column Tumors|51127",
            "Id": "51127",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51127"
            }
          },
          {
            "DisplayText": "von Willebrand Disease",
            "DisplayCount": "81",
            "Value": "PS592/V/von Willebrand Disease|2942",
            "Data": "PS592/V/von Willebrand Disease|2942",
            "Id": "2942",
            "Content": {}
          },
          {
            "DisplayText": "Vulvar Cancer",
            "DisplayCount": "81",
            "Value": "PS592/V/Vulvar Cancer|838",
            "Data": "PS592/V/Vulvar Cancer|838",
            "Id": "838",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/838"
            }
          },
          {
            "DisplayText": "Warts",
            "DisplayCount": "1",
            "Value": "PS592/W/Warts|2946",
            "Data": "PS592/W/Warts|2946",
            "Id": "2946",
            "Content": {}
          },
          {
            "DisplayText": "Wrinkles",
            "DisplayCount": "1",
            "Value": "PS592/W/Wrinkles|51446",
            "Data": "PS592/W/Wrinkles|51446",
            "Id": "51446",
            "Content": {}
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Acute Leukemia",
            "DisplayCount": "81",
            "Value": "PS592/A/Acute Leukemia|3264",
            "Data": "PS592/A/Acute Leukemia|3264",
            "Id": "3264",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/3264"
            }
          },
          {
            "DisplayText": "Adrenal Cortical Carcinoma",
            "DisplayCount": "81",
            "Value": "PS592/A/Adrenal Cortical Carcinoma|3384",
            "Data": "PS592/A/Adrenal Cortical Carcinoma|3384",
            "Id": "3384",
            "Content": {}
          },
          {
            "DisplayText": "Adrenal Gland Cancer",
            "DisplayCount": "81",
            "Value": "PS592/A/Adrenal Gland Cancer|51042",
            "Data": "PS592/A/Adrenal Gland Cancer|51042",
            "Id": "51042",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51042"
            }
          }
        ],
        "TopViewAllValues": [
          {
            "DisplayText": "Acute Leukemia",
            "DisplayCount": "81",
            "Value": "PS592/A/Acute Leukemia|3264",
            "Data": "PS592/A/Acute Leukemia|3264",
            "Id": "3264",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/3264"
            }
          },
          {
            "DisplayText": "Adrenal Cortical Carcinoma",
            "DisplayCount": "81",
            "Value": "PS592/A/Adrenal Cortical Carcinoma|3384",
            "Data": "PS592/A/Adrenal Cortical Carcinoma|3384",
            "Id": "3384",
            "Content": {}
          },
          {
            "DisplayText": "Adrenal Gland Cancer",
            "DisplayCount": "81",
            "Value": "PS592/A/Adrenal Gland Cancer|51042",
            "Data": "PS592/A/Adrenal Gland Cancer|51042",
            "Id": "51042",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51042"
            }
          },
          {
            "DisplayText": "Anal and Rectal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/A/Anal and Rectal Cancer|51043",
            "Data": "PS592/A/Anal and Rectal Cancer|51043",
            "Id": "51043",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51043"
            }
          },
          {
            "DisplayText": "Anaplastic Oligodendroglioma",
            "DisplayCount": "81",
            "Value": "PS592/A/Anaplastic Oligodendroglioma|50887",
            "Data": "PS592/A/Anaplastic Oligodendroglioma|50887",
            "Id": "50887",
            "Content": {}
          },
          {
            "DisplayText": "Astrocytoma",
            "DisplayCount": "81",
            "Value": "PS592/A/Astrocytoma|1658",
            "Data": "PS592/A/Astrocytoma|1658",
            "Id": "1658",
            "Content": {}
          },
          {
            "DisplayText": "Bile Duct Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Bile Duct Cancer|4737",
            "Data": "PS592/B/Bile Duct Cancer|4737",
            "Id": "4737",
            "Content": {}
          },
          {
            "DisplayText": "Biliary Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Biliary Cancer|1703",
            "Data": "PS592/B/Biliary Cancer|1703",
            "Id": "1703",
            "Content": {}
          },
          {
            "DisplayText": "Bladder Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Bladder Cancer|120",
            "Data": "PS592/B/Bladder Cancer|120",
            "Id": "120",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/120"
            }
          },
          {
            "DisplayText": "Bone Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Cancer|126",
            "Data": "PS592/B/Bone Cancer|126",
            "Id": "126",
            "Content": {}
          },
          {
            "DisplayText": "Bone Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Sarcoma|51017",
            "Data": "PS592/B/Bone Sarcoma|51017",
            "Id": "51017",
            "Content": {}
          },
          {
            "DisplayText": "Brain and Nervous System Cancer (incl. Gliomas, Astrocytoma, Schwannoma, Medulloblastoma, Chordoma)",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain and Nervous System Cancer (incl. Gliomas, Astrocytoma, Schwannoma, Medulloblastoma, Chordoma)|51055",
            "Data": "PS592/B/Brain and Nervous System Cancer (incl. Gliomas, Astrocytoma, Schwannoma, Medulloblastoma, Chordoma)|51055",
            "Id": "51055",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51055"
            }
          },
          {
            "DisplayText": "Brain Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain Cancer|142",
            "Data": "PS592/B/Brain Cancer|142",
            "Id": "142",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/142"
            }
          },
          {
            "DisplayText": "Brain Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain Sarcoma|50908",
            "Data": "PS592/B/Brain Sarcoma|50908",
            "Id": "50908",
            "Content": {}
          },
          {
            "DisplayText": "Brain Tumor",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain Tumor|1437",
            "Data": "PS592/B/Brain Tumor|1437",
            "Id": "1437",
            "Content": {}
          },
          {
            "DisplayText": "Breast Cancer",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Cancer|130",
            "Data": "PS592/B/Breast Cancer|130",
            "Id": "130",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/130"
            }
          },
          {
            "DisplayText": "Breast Cancer Recurrence",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Cancer Recurrence|50909",
            "Data": "PS592/B/Breast Cancer Recurrence|50909",
            "Id": "50909",
            "Content": {}
          },
          {
            "DisplayText": "Breast Lump",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Lump|51141",
            "Data": "PS592/B/Breast Lump|51141",
            "Id": "51141",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51141"
            }
          },
          {
            "DisplayText": "Breast Tumor",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Tumor|18734",
            "Data": "PS592/B/Breast Tumor|18734",
            "Id": "18734",
            "Content": {}
          },
          {
            "DisplayText": "Burkitt's Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/B/Burkitt's Lymphoma|5128",
            "Data": "PS592/B/Burkitt's Lymphoma|5128",
            "Id": "5128",
            "Content": {}
          },
          {
            "DisplayText": "Cancer",
            "DisplayCount": "81",
            "Value": "PS592/C/Cancer|1765",
            "Data": "PS592/C/Cancer|1765",
            "Id": "1765",
            "Content": {}
          },
          {
            "DisplayText": "Carcinoma in Situ",
            "DisplayCount": "81",
            "Value": "PS592/C/Carcinoma in Situ|51057",
            "Data": "PS592/C/Carcinoma in Situ|51057",
            "Id": "51057",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51057"
            }
          },
          {
            "DisplayText": "Central Nervous System Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/C/Central Nervous System Lymphoma|19755",
            "Data": "PS592/C/Central Nervous System Lymphoma|19755",
            "Id": "19755",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/19755"
            }
          },
          {
            "DisplayText": "Cervical Cancer",
            "DisplayCount": "81",
            "Value": "PS592/C/Cervical Cancer|144",
            "Data": "PS592/C/Cervical Cancer|144",
            "Id": "144",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/144"
            }
          },
          {
            "DisplayText": "Chondrosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/C/Chondrosarcoma|6331",
            "Data": "PS592/C/Chondrosarcoma|6331",
            "Id": "6331",
            "Content": {}
          },
          {
            "DisplayText": "Chordoma",
            "DisplayCount": "81",
            "Value": "PS592/C/Chordoma|6334",
            "Data": "PS592/C/Chordoma|6334",
            "Id": "6334",
            "Content": {}
          },
          {
            "DisplayText": "Chronic Myeloid Leukemia (CML)",
            "DisplayCount": "81",
            "Value": "PS592/C/Chronic Myeloid Leukemia (CML)|668",
            "Data": "PS592/C/Chronic Myeloid Leukemia (CML)|668",
            "Id": "668",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/668"
            }
          },
          {
            "DisplayText": "Clival Tumor",
            "DisplayCount": "81",
            "Value": "PS592/C/Clival Tumor|50921",
            "Data": "PS592/C/Clival Tumor|50921",
            "Id": "50921",
            "Content": {}
          },
          {
            "DisplayText": "Coagulation Defects in Pregnancy and Postpartum",
            "DisplayCount": "81",
            "Value": "PS592/C/Coagulation Defects in Pregnancy and Postpartum|51977",
            "Data": "PS592/C/Coagulation Defects in Pregnancy and Postpartum|51977",
            "Id": "51977",
            "Content": {}
          },
          {
            "DisplayText": "Coagulation Disorders (incl. Hemophilia)",
            "DisplayCount": "81",
            "Value": "PS592/C/Coagulation Disorders (incl. Hemophilia)|51678",
            "Data": "PS592/C/Coagulation Disorders (incl. Hemophilia)|51678",
            "Id": "51678",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51678"
            }
          },
          {
            "DisplayText": "Colorectal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/C/Colorectal Cancer|19102",
            "Data": "PS592/C/Colorectal Cancer|19102",
            "Id": "19102",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/19102"
            }
          },
          {
            "DisplayText": "ENT Cancer",
            "DisplayCount": "81",
            "Value": "PS592/E/ENT Cancer|51067",
            "Data": "PS592/E/ENT Cancer|51067",
            "Id": "51067",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51067"
            }
          },
          {
            "DisplayText": "Ependymoma",
            "DisplayCount": "81",
            "Value": "PS592/E/Ependymoma|2002",
            "Data": "PS592/E/Ependymoma|2002",
            "Id": "2002",
            "Content": {}
          },
          {
            "DisplayText": "Esophageal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/E/Esophageal Cancer|149",
            "Data": "PS592/E/Esophageal Cancer|149",
            "Id": "149",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/149"
            }
          },
          {
            "DisplayText": "Ewing's Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/E/Ewing's Sarcoma|2016",
            "Data": "PS592/E/Ewing's Sarcoma|2016",
            "Id": "2016",
            "Content": {}
          },
          {
            "DisplayText": "Exposure to Synthetic Estrogen Diethylstilbestrol",
            "DisplayCount": "81",
            "Value": "PS592/E/Exposure to Synthetic Estrogen Diethylstilbestrol|50941",
            "Data": "PS592/E/Exposure to Synthetic Estrogen Diethylstilbestrol|50941",
            "Id": "50941",
            "Content": {}
          },
          {
            "DisplayText": "Fallopian Tube Cancer",
            "DisplayCount": "81",
            "Value": "PS592/F/Fallopian Tube Cancer|841",
            "Data": "PS592/F/Fallopian Tube Cancer|841",
            "Id": "841",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/841"
            }
          },
          {
            "DisplayText": "Fibrosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/F/Fibrosarcoma|9084",
            "Data": "PS592/F/Fibrosarcoma|9084",
            "Id": "9084",
            "Content": {}
          },
          {
            "DisplayText": "Gallbladder and Biliary Tract Cancer",
            "DisplayCount": "81",
            "Value": "PS592/G/Gallbladder and Biliary Tract Cancer|51075",
            "Data": "PS592/G/Gallbladder and Biliary Tract Cancer|51075",
            "Id": "51075",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51075"
            }
          },
          {
            "DisplayText": "Gallbladder Cancer",
            "DisplayCount": "81",
            "Value": "PS592/G/Gallbladder Cancer|150",
            "Data": "PS592/G/Gallbladder Cancer|150",
            "Id": "150",
            "Content": {}
          },
          {
            "DisplayText": "Glioblastoma",
            "DisplayCount": "81",
            "Value": "PS592/G/Glioblastoma|9628",
            "Data": "PS592/G/Glioblastoma|9628",
            "Id": "9628",
            "Content": {}
          },
          {
            "DisplayText": "Glioma",
            "DisplayCount": "81",
            "Value": "PS592/G/Glioma|2105",
            "Data": "PS592/G/Glioma|2105",
            "Id": "2105",
            "Content": {}
          },
          {
            "DisplayText": "Graft vs Host Disease",
            "DisplayCount": "81",
            "Value": "PS592/G/Graft vs Host Disease|51077",
            "Data": "PS592/G/Graft vs Host Disease|51077",
            "Id": "51077",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51077"
            }
          },
          {
            "DisplayText": "Gum Cancer",
            "DisplayCount": "81",
            "Value": "PS592/G/Gum Cancer|51891",
            "Data": "PS592/G/Gum Cancer|51891",
            "Id": "51891",
            "Content": {}
          },
          {
            "DisplayText": "Head and Neck Tumor",
            "DisplayCount": "81",
            "Value": "PS592/H/Head and Neck Tumor|18765",
            "Data": "PS592/H/Head and Neck Tumor|18765",
            "Id": "18765",
            "Content": {}
          },
          {
            "DisplayText": "Heart Tumors, Malignant",
            "DisplayCount": "81",
            "Value": "PS592/H/Heart Tumors, Malignant|51059",
            "Data": "PS592/H/Heart Tumors, Malignant|51059",
            "Id": "51059",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51059"
            }
          },
          {
            "DisplayText": "Hemophilia",
            "DisplayCount": "81",
            "Value": "PS592/H/Hemophilia|314",
            "Data": "PS592/H/Hemophilia|314",
            "Id": "314",
            "Content": {}
          },
          {
            "DisplayText": "Hemophilia A",
            "DisplayCount": "81",
            "Value": "PS592/H/Hemophilia A|10024",
            "Data": "PS592/H/Hemophilia A|10024",
            "Id": "10024",
            "Content": {}
          },
          {
            "DisplayText": "Hemorrhage from Placenta Previa",
            "DisplayCount": "81",
            "Value": "PS592/H/Hemorrhage from Placenta Previa|51934",
            "Data": "PS592/H/Hemorrhage from Placenta Previa|51934",
            "Id": "51934",
            "Content": {}
          },
          {
            "DisplayText": "Hodgkin's Disease",
            "DisplayCount": "81",
            "Value": "PS592/H/Hodgkin's Disease|152",
            "Data": "PS592/H/Hodgkin's Disease|152",
            "Id": "152",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/152"
            }
          },
          {
            "DisplayText": "Immune Thrombocytopenic Purpura (ITP)",
            "DisplayCount": "81",
            "Value": "PS592/I/Immune Thrombocytopenic Purpura (ITP)|2211",
            "Data": "PS592/I/Immune Thrombocytopenic Purpura (ITP)|2211",
            "Id": "2211",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2211"
            }
          },
          {
            "DisplayText": "Kaposi's Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/K/Kaposi's Sarcoma|11113",
            "Data": "PS592/K/Kaposi's Sarcoma|11113",
            "Id": "11113",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/11113"
            }
          },
          {
            "DisplayText": "Kidney Cancer",
            "DisplayCount": "81",
            "Value": "PS592/K/Kidney Cancer|153",
            "Data": "PS592/K/Kidney Cancer|153",
            "Id": "153",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/153"
            }
          },
          {
            "DisplayText": "Lambert-Eaton Syndrome",
            "DisplayCount": "81",
            "Value": "PS592/L/Lambert-Eaton Syndrome|51087",
            "Data": "PS592/L/Lambert-Eaton Syndrome|51087",
            "Id": "51087",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51087"
            }
          },
          {
            "DisplayText": "Laryngeal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/L/Laryngeal Cancer|2286",
            "Data": "PS592/L/Laryngeal Cancer|2286",
            "Id": "2286",
            "Content": {}
          },
          {
            "DisplayText": "Leukemia",
            "DisplayCount": "81",
            "Value": "PS592/L/Leukemia|62",
            "Data": "PS592/L/Leukemia|62",
            "Id": "62",
            "Content": {}
          },
          {
            "DisplayText": "Lip Cancer",
            "DisplayCount": "81",
            "Value": "PS592/L/Lip Cancer|11717",
            "Data": "PS592/L/Lip Cancer|11717",
            "Id": "11717",
            "Content": {}
          },
          {
            "DisplayText": "Liposarcoma",
            "DisplayCount": "81",
            "Value": "PS592/L/Liposarcoma|11741",
            "Data": "PS592/L/Liposarcoma|11741",
            "Id": "11741",
            "Content": {}
          },
          {
            "DisplayText": "Liver Cancer",
            "DisplayCount": "81",
            "Value": "PS592/L/Liver Cancer|155",
            "Data": "PS592/L/Liver Cancer|155",
            "Id": "155",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/155"
            }
          },
          {
            "DisplayText": "Liver Tumor",
            "DisplayCount": "81",
            "Value": "PS592/L/Liver Tumor|1413",
            "Data": "PS592/L/Liver Tumor|1413",
            "Id": "1413",
            "Content": {}
          },
          {
            "DisplayText": "Lung Cancer",
            "DisplayCount": "81",
            "Value": "PS592/L/Lung Cancer|156",
            "Data": "PS592/L/Lung Cancer|156",
            "Id": "156",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/156"
            }
          },
          {
            "DisplayText": "Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphoma|1395",
            "Data": "PS592/L/Lymphoma|1395",
            "Id": "1395",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/1395"
            }
          },
          {
            "DisplayText": "Lymphoma of the Bone",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphoma of the Bone|50904",
            "Data": "PS592/L/Lymphoma of the Bone|50904",
            "Id": "50904",
            "Content": {}
          },
          {
            "DisplayText": "Lymphoma of the Brain",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphoma of the Brain|50907",
            "Data": "PS592/L/Lymphoma of the Brain|50907",
            "Id": "50907",
            "Content": {}
          },
          {
            "DisplayText": "Lymphoma, Large-Cell",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphoma, Large-Cell|11893",
            "Data": "PS592/L/Lymphoma, Large-Cell|11893",
            "Id": "11893",
            "Content": {}
          },
          {
            "DisplayText": "Lymphosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/L/Lymphosarcoma|51941",
            "Data": "PS592/L/Lymphosarcoma|51941",
            "Id": "51941",
            "Content": {}
          },
          {
            "DisplayText": "Macroglobulinemia (incl. Waldenstrom's )",
            "DisplayCount": "81",
            "Value": "PS592/M/Macroglobulinemia (incl. Waldenstrom's )|51184",
            "Data": "PS592/M/Macroglobulinemia (incl. Waldenstrom's )|51184",
            "Id": "51184",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51184"
            }
          },
          {
            "DisplayText": "Male Breast Cancer",
            "DisplayCount": "81",
            "Value": "PS592/M/Male Breast Cancer|11989",
            "Data": "PS592/M/Male Breast Cancer|11989",
            "Id": "11989",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Bone Cancer of the Skull, Face, and Jaw",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Bone Cancer of the Skull, Face, and Jaw|51902",
            "Data": "PS592/M/Malignant Bone Cancer of the Skull, Face, and Jaw|51902",
            "Id": "51902",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Brain Tumor",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Brain Tumor|50973",
            "Data": "PS592/M/Malignant Brain Tumor|50973",
            "Id": "50973",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Breast Tumor",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Breast Tumor|50974",
            "Data": "PS592/M/Malignant Breast Tumor|50974",
            "Id": "50974",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Glioma",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Glioma|50975",
            "Data": "PS592/M/Malignant Glioma|50975",
            "Id": "50975",
            "Content": {}
          },
          {
            "DisplayText": "Malignant Histiocytosis",
            "DisplayCount": "81",
            "Value": "PS592/M/Malignant Histiocytosis|52027",
            "Data": "PS592/M/Malignant Histiocytosis|52027",
            "Id": "52027",
            "Content": {}
          },
          {
            "DisplayText": "Mantle Cell Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/M/Mantle Cell Lymphoma|12070",
            "Data": "PS592/M/Mantle Cell Lymphoma|12070",
            "Id": "12070",
            "Content": {}
          },
          {
            "DisplayText": "Marginal Zone Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/M/Marginal Zone Lymphoma|51968",
            "Data": "PS592/M/Marginal Zone Lymphoma|51968",
            "Id": "51968",
            "Content": {}
          },
          {
            "DisplayText": "Maternal Anemia",
            "DisplayCount": "81",
            "Value": "PS592/M/Maternal Anemia|51995",
            "Data": "PS592/M/Maternal Anemia|51995",
            "Id": "51995",
            "Content": {}
          },
          {
            "DisplayText": "Melanoma",
            "DisplayCount": "81",
            "Value": "PS592/M/Melanoma|1495",
            "Data": "PS592/M/Melanoma|1495",
            "Id": "1495",
            "Content": {}
          },
          {
            "DisplayText": "Merkel Cell Carcinoma",
            "DisplayCount": "81",
            "Value": "PS592/M/Merkel Cell Carcinoma|12406",
            "Data": "PS592/M/Merkel Cell Carcinoma|12406",
            "Id": "12406",
            "Content": {}
          },
          {
            "DisplayText": "Mesothelioma",
            "DisplayCount": "81",
            "Value": "PS592/M/Mesothelioma|2353",
            "Data": "PS592/M/Mesothelioma|2353",
            "Id": "2353",
            "Content": {}
          },
          {
            "DisplayText": "Metastatic Bone Cancer",
            "DisplayCount": "81",
            "Value": "PS592/M/Metastatic Bone Cancer|12463",
            "Data": "PS592/M/Metastatic Bone Cancer|12463",
            "Id": "12463",
            "Content": {}
          },
          {
            "DisplayText": "Metastatic Respiratory System Cancer",
            "DisplayCount": "81",
            "Value": "PS592/M/Metastatic Respiratory System Cancer|51821",
            "Data": "PS592/M/Metastatic Respiratory System Cancer|51821",
            "Id": "51821",
            "Content": {}
          },
          {
            "DisplayText": "Multiple Endocrine Neoplasia",
            "DisplayCount": "81",
            "Value": "PS592/M/Multiple Endocrine Neoplasia|12899",
            "Data": "PS592/M/Multiple Endocrine Neoplasia|12899",
            "Id": "12899",
            "Content": {}
          },
          {
            "DisplayText": "Multiple Myeloma",
            "DisplayCount": "81",
            "Value": "PS592/M/Multiple Myeloma|159",
            "Data": "PS592/M/Multiple Myeloma|159",
            "Id": "159",
            "Content": {}
          },
          {
            "DisplayText": "Musculoskeletal Sarcomas",
            "DisplayCount": "81",
            "Value": "PS592/M/Musculoskeletal Sarcomas|50980",
            "Data": "PS592/M/Musculoskeletal Sarcomas|50980",
            "Id": "50980",
            "Content": {}
          },
          {
            "DisplayText": "Musculoskeletal Tumor",
            "DisplayCount": "81",
            "Value": "PS592/M/Musculoskeletal Tumor|50981",
            "Data": "PS592/M/Musculoskeletal Tumor|50981",
            "Id": "50981",
            "Content": {}
          },
          {
            "DisplayText": "Mycosis Fungoides",
            "DisplayCount": "81",
            "Value": "PS592/M/Mycosis Fungoides|2404",
            "Data": "PS592/M/Mycosis Fungoides|2404",
            "Id": "2404",
            "Content": {}
          },
          {
            "DisplayText": "Myeloma",
            "DisplayCount": "81",
            "Value": "PS592/M/Myeloma|13000",
            "Data": "PS592/M/Myeloma|13000",
            "Id": "13000",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/13000"
            }
          },
          {
            "DisplayText": "Myeloproliferative Disorders",
            "DisplayCount": "81",
            "Value": "PS592/M/Myeloproliferative Disorders|18576",
            "Data": "PS592/M/Myeloproliferative Disorders|18576",
            "Id": "18576",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/18576"
            }
          },
          {
            "DisplayText": "Nasal Cavity Cancer",
            "DisplayCount": "81",
            "Value": "PS592/N/Nasal Cavity Cancer|50814",
            "Data": "PS592/N/Nasal Cavity Cancer|50814",
            "Id": "50814",
            "Content": {}
          },
          {
            "DisplayText": "Neck Tumor",
            "DisplayCount": "81",
            "Value": "PS592/N/Neck Tumor|19985",
            "Data": "PS592/N/Neck Tumor|19985",
            "Id": "19985",
            "Content": {}
          },
          {
            "DisplayText": "Neuroendocrine Cancer",
            "DisplayCount": "81",
            "Value": "PS592/N/Neuroendocrine Cancer|50986",
            "Data": "PS592/N/Neuroendocrine Cancer|50986",
            "Id": "50986",
            "Content": {}
          },
          {
            "DisplayText": "Neuroendocrine Tumors",
            "DisplayCount": "81",
            "Value": "PS592/N/Neuroendocrine Tumors|51096",
            "Data": "PS592/N/Neuroendocrine Tumors|51096",
            "Id": "51096",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51096"
            }
          },
          {
            "DisplayText": "Nodular Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/N/Nodular Lymphoma|51975",
            "Data": "PS592/N/Nodular Lymphoma|51975",
            "Id": "51975",
            "Content": {}
          },
          {
            "DisplayText": "Non-Hodgkin's Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/N/Non-Hodgkin's Lymphoma|160",
            "Data": "PS592/N/Non-Hodgkin's Lymphoma|160",
            "Id": "160",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/160"
            }
          },
          {
            "DisplayText": "Non-Small Cell Lung Cancer",
            "DisplayCount": "81",
            "Value": "PS592/N/Non-Small Cell Lung Cancer|50990",
            "Data": "PS592/N/Non-Small Cell Lung Cancer|50990",
            "Id": "50990",
            "Content": {}
          },
          {
            "DisplayText": "Oral Cancer",
            "DisplayCount": "81",
            "Value": "PS592/O/Oral Cancer|1500",
            "Data": "PS592/O/Oral Cancer|1500",
            "Id": "1500",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/1500"
            }
          },
          {
            "DisplayText": "Osteosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/O/Osteosarcoma|2493",
            "Data": "PS592/O/Osteosarcoma|2493",
            "Id": "2493",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2493"
            }
          },
          {
            "DisplayText": "Ovarian Cancer",
            "DisplayCount": "81",
            "Value": "PS592/O/Ovarian Cancer|163",
            "Data": "PS592/O/Ovarian Cancer|163",
            "Id": "163",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/163"
            }
          },
          {
            "DisplayText": "Pancreatic Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Pancreatic Cancer|164",
            "Data": "PS592/P/Pancreatic Cancer|164",
            "Id": "164",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/164"
            }
          },
          {
            "DisplayText": "Parathyroid Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Parathyroid Cancer|14220",
            "Data": "PS592/P/Parathyroid Cancer|14220",
            "Id": "14220",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/14220"
            }
          },
          {
            "DisplayText": "Penile Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Penile Cancer|14361",
            "Data": "PS592/P/Penile Cancer|14361",
            "Id": "14361",
            "Content": {}
          },
          {
            "DisplayText": "Peripheral T-Cell Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/P/Peripheral T-Cell Lymphoma|52015",
            "Data": "PS592/P/Peripheral T-Cell Lymphoma|52015",
            "Id": "52015",
            "Content": {}
          },
          {
            "DisplayText": "Pheochromocytoma",
            "DisplayCount": "81",
            "Value": "PS592/P/Pheochromocytoma|14485",
            "Data": "PS592/P/Pheochromocytoma|14485",
            "Id": "14485",
            "Content": {}
          },
          {
            "DisplayText": "Pituitary Gland Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Pituitary Gland Cancer|51105",
            "Data": "PS592/P/Pituitary Gland Cancer|51105",
            "Id": "51105",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51105"
            }
          },
          {
            "DisplayText": "Pituitary Tumor",
            "DisplayCount": "81",
            "Value": "PS592/P/Pituitary Tumor|51000",
            "Data": "PS592/P/Pituitary Tumor|51000",
            "Id": "51000",
            "Content": {}
          },
          {
            "DisplayText": "Pleura Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Pleura Cancer|14671",
            "Data": "PS592/P/Pleura Cancer|14671",
            "Id": "14671",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/14671"
            }
          },
          {
            "DisplayText": "Pleural Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Pleural Cancer|51209",
            "Data": "PS592/P/Pleural Cancer|51209",
            "Id": "51209",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51209"
            }
          },
          {
            "DisplayText": "Pleural Mesothelioma",
            "DisplayCount": "81",
            "Value": "PS592/P/Pleural Mesothelioma|51001",
            "Data": "PS592/P/Pleural Mesothelioma|51001",
            "Id": "51001",
            "Content": {}
          },
          {
            "DisplayText": "Primary Central Nervous System Lymphoma",
            "DisplayCount": "81",
            "Value": "PS592/P/Primary Central Nervous System Lymphoma|51921",
            "Data": "PS592/P/Primary Central Nervous System Lymphoma|51921",
            "Id": "51921",
            "Content": {}
          },
          {
            "DisplayText": "Prostate Cancer",
            "DisplayCount": "81",
            "Value": "PS592/P/Prostate Cancer|165",
            "Data": "PS592/P/Prostate Cancer|165",
            "Id": "165",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/165"
            }
          },
          {
            "DisplayText": "Reticulosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/R/Reticulosarcoma|51925",
            "Data": "PS592/R/Reticulosarcoma|51925",
            "Id": "51925",
            "Content": {}
          },
          {
            "DisplayText": "Retinoblastoma",
            "DisplayCount": "81",
            "Value": "PS592/R/Retinoblastoma|2683",
            "Data": "PS592/R/Retinoblastoma|2683",
            "Id": "2683",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2683"
            }
          },
          {
            "DisplayText": "Rhabdomyosarcoma",
            "DisplayCount": "81",
            "Value": "PS592/R/Rhabdomyosarcoma|2689",
            "Data": "PS592/R/Rhabdomyosarcoma|2689",
            "Id": "2689",
            "Content": {}
          },
          {
            "DisplayText": "Salivary Gland Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Salivary Gland Cancer|2710",
            "Data": "PS592/S/Salivary Gland Cancer|2710",
            "Id": "2710",
            "Content": {}
          },
          {
            "DisplayText": "Salivary Gland Tumors",
            "DisplayCount": "81",
            "Value": "PS592/S/Salivary Gland Tumors|50842",
            "Data": "PS592/S/Salivary Gland Tumors|50842",
            "Id": "50842",
            "Content": {}
          },
          {
            "DisplayText": "Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/S/Sarcoma|166",
            "Data": "PS592/S/Sarcoma|166",
            "Id": "166",
            "Content": {}
          },
          {
            "DisplayText": "Secondary Hypertension",
            "DisplayCount": "81",
            "Value": "PS592/S/Secondary Hypertension|16146",
            "Data": "PS592/S/Secondary Hypertension|16146",
            "Id": "16146",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/16146"
            }
          },
          {
            "DisplayText": "Secondary Malignancies",
            "DisplayCount": "81",
            "Value": "PS592/S/Secondary Malignancies|51116",
            "Data": "PS592/S/Secondary Malignancies|51116",
            "Id": "51116",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51116"
            }
          },
          {
            "DisplayText": "Sezary's Disease",
            "DisplayCount": "81",
            "Value": "PS592/S/Sezary's Disease|51978",
            "Data": "PS592/S/Sezary's Disease|51978",
            "Id": "51978",
            "Content": {}
          },
          {
            "DisplayText": "Skin Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Skin Cancer|157",
            "Data": "PS592/S/Skin Cancer|157",
            "Id": "157",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/157"
            }
          },
          {
            "DisplayText": "Small Cell Lung Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Small Cell Lung Cancer|51019",
            "Data": "PS592/S/Small Cell Lung Cancer|51019",
            "Id": "51019",
            "Content": {}
          },
          {
            "DisplayText": "Small Intestine Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Small Intestine Cancer|52042",
            "Data": "PS592/S/Small Intestine Cancer|52042",
            "Id": "52042",
            "Content": {}
          },
          {
            "DisplayText": "Soft Tissue Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/S/Soft Tissue Sarcoma|2774",
            "Data": "PS592/S/Soft Tissue Sarcoma|2774",
            "Id": "2774",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2774"
            }
          },
          {
            "DisplayText": "Soft Tissue Sarcoma of Head, Face, and Neck",
            "DisplayCount": "81",
            "Value": "PS592/S/Soft Tissue Sarcoma of Head, Face, and Neck|51907",
            "Data": "PS592/S/Soft Tissue Sarcoma of Head, Face, and Neck|51907",
            "Id": "51907",
            "Content": {}
          },
          {
            "DisplayText": "Soft Tissue Tumors of Head and Neck",
            "DisplayCount": "81",
            "Value": "PS592/S/Soft Tissue Tumors of Head and Neck|51021",
            "Data": "PS592/S/Soft Tissue Tumors of Head and Neck|51021",
            "Id": "51021",
            "Content": {}
          },
          {
            "DisplayText": "Spinal Cord Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Spinal Cord Cancer|51023",
            "Data": "PS592/S/Spinal Cord Cancer|51023",
            "Id": "51023",
            "Content": {}
          },
          {
            "DisplayText": "Spinal Cord Tumor",
            "DisplayCount": "81",
            "Value": "PS592/S/Spinal Cord Tumor|1511",
            "Data": "PS592/S/Spinal Cord Tumor|1511",
            "Id": "1511",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/1511"
            }
          },
          {
            "DisplayText": "Squamous Cell Carcinoma",
            "DisplayCount": "81",
            "Value": "PS592/S/Squamous Cell Carcinoma|2792",
            "Data": "PS592/S/Squamous Cell Carcinoma|2792",
            "Id": "2792",
            "Content": {}
          },
          {
            "DisplayText": "Stomach and Small Intestine Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Stomach and Small Intestine Cancer|51122",
            "Data": "PS592/S/Stomach and Small Intestine Cancer|51122",
            "Id": "51122",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51122"
            }
          },
          {
            "DisplayText": "Stomach Cancer",
            "DisplayCount": "81",
            "Value": "PS592/S/Stomach Cancer|169",
            "Data": "PS592/S/Stomach Cancer|169",
            "Id": "169",
            "Content": {}
          },
          {
            "DisplayText": "Synovial Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/S/Synovial Sarcoma|17002",
            "Data": "PS592/S/Synovial Sarcoma|17002",
            "Id": "17002",
            "Content": {}
          },
          {
            "DisplayText": "Testicular Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Testicular Cancer|170",
            "Data": "PS592/T/Testicular Cancer|170",
            "Id": "170",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/170"
            }
          },
          {
            "DisplayText": "Throat Cancer (Hypopharyngeal)",
            "DisplayCount": "81",
            "Value": "PS592/T/Throat Cancer (Hypopharyngeal)|10653",
            "Data": "PS592/T/Throat Cancer (Hypopharyngeal)|10653",
            "Id": "10653",
            "Content": {}
          },
          {
            "DisplayText": "Throat Cancer (Nasopharyngeal)",
            "DisplayCount": "81",
            "Value": "PS592/T/Throat Cancer (Nasopharyngeal)|2423",
            "Data": "PS592/T/Throat Cancer (Nasopharyngeal)|2423",
            "Id": "2423",
            "Content": {}
          },
          {
            "DisplayText": "Throat Cancer (Oropharyngeal)",
            "DisplayCount": "81",
            "Value": "PS592/T/Throat Cancer (Oropharyngeal)|162",
            "Data": "PS592/T/Throat Cancer (Oropharyngeal)|162",
            "Id": "162",
            "Content": {}
          },
          {
            "DisplayText": "Thymomas",
            "DisplayCount": "81",
            "Value": "PS592/T/Thymomas|17191",
            "Data": "PS592/T/Thymomas|17191",
            "Id": "17191",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/17191"
            }
          },
          {
            "DisplayText": "Thyroid Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Thyroid Cancer|172",
            "Data": "PS592/T/Thyroid Cancer|172",
            "Id": "172",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/172"
            }
          },
          {
            "DisplayText": "Tongue Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Tongue Cancer|17253",
            "Data": "PS592/T/Tongue Cancer|17253",
            "Id": "17253",
            "Content": {}
          },
          {
            "DisplayText": "Tonsil Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Tonsil Cancer|51911",
            "Data": "PS592/T/Tonsil Cancer|51911",
            "Id": "51911",
            "Content": {}
          },
          {
            "DisplayText": "Transitional Cell Cancer",
            "DisplayCount": "81",
            "Value": "PS592/T/Transitional Cell Cancer|2866",
            "Data": "PS592/T/Transitional Cell Cancer|2866",
            "Id": "2866",
            "Content": {}
          },
          {
            "DisplayText": "Tuberous Sclerosis",
            "DisplayCount": "81",
            "Value": "PS592/T/Tuberous Sclerosis|2878",
            "Data": "PS592/T/Tuberous Sclerosis|2878",
            "Id": "2878",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2878"
            }
          },
          {
            "DisplayText": "Upper Urinary Tract Tumor",
            "DisplayCount": "81",
            "Value": "PS592/U/Upper Urinary Tract Tumor|50866",
            "Data": "PS592/U/Upper Urinary Tract Tumor|50866",
            "Id": "50866",
            "Content": {}
          },
          {
            "DisplayText": "Ureteral Cancer",
            "DisplayCount": "81",
            "Value": "PS592/U/Ureteral Cancer|51035",
            "Data": "PS592/U/Ureteral Cancer|51035",
            "Id": "51035",
            "Content": {}
          },
          {
            "DisplayText": "Uterine Cancer",
            "DisplayCount": "81",
            "Value": "PS592/U/Uterine Cancer|2904",
            "Data": "PS592/U/Uterine Cancer|2904",
            "Id": "2904",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2904"
            }
          },
          {
            "DisplayText": "Uterine Sarcoma",
            "DisplayCount": "81",
            "Value": "PS592/U/Uterine Sarcoma|17747",
            "Data": "PS592/U/Uterine Sarcoma|17747",
            "Id": "17747",
            "Content": {}
          },
          {
            "DisplayText": "Vaginal Cancer",
            "DisplayCount": "81",
            "Value": "PS592/V/Vaginal Cancer|837",
            "Data": "PS592/V/Vaginal Cancer|837",
            "Id": "837",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/837"
            }
          },
          {
            "DisplayText": "von Willebrand Disease",
            "DisplayCount": "81",
            "Value": "PS592/V/von Willebrand Disease|2942",
            "Data": "PS592/V/von Willebrand Disease|2942",
            "Id": "2942",
            "Content": {}
          },
          {
            "DisplayText": "Vulvar Cancer",
            "DisplayCount": "81",
            "Value": "PS592/V/Vulvar Cancer|838",
            "Data": "PS592/V/Vulvar Cancer|838",
            "Id": "838",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/838"
            }
          },
          {
            "DisplayText": "Anemia",
            "DisplayCount": "61",
            "Value": "PS592/A/Anemia|75",
            "Data": "PS592/A/Anemia|75",
            "Id": "75",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/75"
            }
          },
          {
            "DisplayText": "All Lymphoma",
            "DisplayCount": "53",
            "Value": "PS592/A/All Lymphoma|52142",
            "Data": "PS592/A/All Lymphoma|52142",
            "Id": "52142",
            "Content": {}
          },
          {
            "DisplayText": "Basal Cell Carcinoma",
            "DisplayCount": "53",
            "Value": "PS592/B/Basal Cell Carcinoma|1693",
            "Data": "PS592/B/Basal Cell Carcinoma|1693",
            "Id": "1693",
            "Content": {}
          },
          {
            "DisplayText": "Head and Neck Cancer",
            "DisplayCount": "53",
            "Value": "PS592/H/Head and Neck Cancer|52137",
            "Data": "PS592/H/Head and Neck Cancer|52137",
            "Id": "52137",
            "Content": {}
          },
          {
            "DisplayText": "Neutropenia",
            "DisplayCount": "52",
            "Value": "PS592/N/Neutropenia|2454",
            "Data": "PS592/N/Neutropenia|2454",
            "Id": "2454",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2454"
            }
          },
          {
            "DisplayText": "Blood Disorders",
            "DisplayCount": "50",
            "Value": "PS592/B/Blood Disorders|4834",
            "Data": "PS592/B/Blood Disorders|4834",
            "Id": "4834",
            "Content": {}
          },
          {
            "DisplayText": "Gynecologic Cancer",
            "DisplayCount": "50",
            "Value": "PS592/G/Gynecologic Cancer|1370",
            "Data": "PS592/G/Gynecologic Cancer|1370",
            "Id": "1370",
            "Content": {}
          },
          {
            "DisplayText": "Myelodysplastic Syndromes",
            "DisplayCount": "50",
            "Value": "PS592/M/Myelodysplastic Syndromes|2406",
            "Data": "PS592/M/Myelodysplastic Syndromes|2406",
            "Id": "2406",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2406"
            }
          },
          {
            "DisplayText": "Leukocytosis",
            "DisplayCount": "49",
            "Value": "PS592/L/Leukocytosis|51089",
            "Data": "PS592/L/Leukocytosis|51089",
            "Id": "51089",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51089"
            }
          },
          {
            "DisplayText": "Gastrointestinal Diseases",
            "DisplayCount": "47",
            "Value": "PS592/G/Gastrointestinal Diseases|51340",
            "Data": "PS592/G/Gastrointestinal Diseases|51340",
            "Id": "51340",
            "Content": {}
          },
          {
            "DisplayText": "Bone Disorders",
            "DisplayCount": "46",
            "Value": "PS592/B/Bone Disorders|50903",
            "Data": "PS592/B/Bone Disorders|50903",
            "Id": "50903",
            "Content": {}
          },
          {
            "DisplayText": "Vascular Disease",
            "DisplayCount": "45",
            "Value": "PS592/V/Vascular Disease|11392",
            "Data": "PS592/V/Vascular Disease|11392",
            "Id": "11392",
            "Content": {}
          },
          {
            "DisplayText": "Pancytopenia",
            "DisplayCount": "44",
            "Value": "PS592/P/Pancytopenia|14161",
            "Data": "PS592/P/Pancytopenia|14161",
            "Id": "14161",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/14161"
            }
          },
          {
            "DisplayText": "Stomach Diseases",
            "DisplayCount": "44",
            "Value": "PS592/S/Stomach Diseases|2800",
            "Data": "PS592/S/Stomach Diseases|2800",
            "Id": "2800",
            "Content": {}
          },
          {
            "DisplayText": "Bleeding Disorders",
            "DisplayCount": "43",
            "Value": "PS592/B/Bleeding Disorders|4806",
            "Data": "PS592/B/Bleeding Disorders|4806",
            "Id": "4806",
            "Content": {}
          },
          {
            "DisplayText": "Breast Diseases",
            "DisplayCount": "43",
            "Value": "PS592/B/Breast Diseases|18366",
            "Data": "PS592/B/Breast Diseases|18366",
            "Id": "18366",
            "Content": {}
          },
          {
            "DisplayText": "Polycythemia Rubra Vera",
            "DisplayCount": "43",
            "Value": "PS592/P/Polycythemia Rubra Vera|51106",
            "Data": "PS592/P/Polycythemia Rubra Vera|51106",
            "Id": "51106",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51106"
            }
          },
          {
            "DisplayText": "Pulmonary Disease",
            "DisplayCount": "43",
            "Value": "PS592/P/Pulmonary Disease|20066",
            "Data": "PS592/P/Pulmonary Disease|20066",
            "Id": "20066",
            "Content": {}
          },
          {
            "DisplayText": "Basal Cell Carcinoma",
            "DisplayCount": "42",
            "Value": "PS592/B/Basal Cell Carcinoma |1693",
            "Data": "PS592/B/Basal Cell Carcinoma |1693",
            "Id": "1693",
            "Content": {}
          },
          {
            "DisplayText": "Lymphoma, Large Cell, Anaplastic",
            "DisplayCount": "42",
            "Value": "PS592/L/Lymphoma, Large Cell, Anaplastic |3767",
            "Data": "PS592/L/Lymphoma, Large Cell, Anaplastic |3767",
            "Id": "3767",
            "Content": {}
          },
          {
            "DisplayText": "Thrombocytosis",
            "DisplayCount": "42",
            "Value": "PS592/T/Thrombocytosis|17178",
            "Data": "PS592/T/Thrombocytosis|17178",
            "Id": "17178",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/17178"
            }
          },
          {
            "DisplayText": "Urinary Disorders",
            "DisplayCount": "42",
            "Value": "PS592/U/Urinary Disorders|17704",
            "Data": "PS592/U/Urinary Disorders|17704",
            "Id": "17704",
            "Content": {}
          },
          {
            "DisplayText": "Autoimmune Diseases",
            "DisplayCount": "40",
            "Value": "PS592/A/Autoimmune Diseases|4384",
            "Data": "PS592/A/Autoimmune Diseases|4384",
            "Id": "4384",
            "Content": {}
          },
          {
            "DisplayText": "Brain Disorders",
            "DisplayCount": "40",
            "Value": "PS592/B/Brain Disorders|1410",
            "Data": "PS592/B/Brain Disorders|1410",
            "Id": "1410",
            "Content": {}
          },
          {
            "DisplayText": "Lymphoma, Large Cell, Anaplastic",
            "DisplayCount": "39",
            "Value": "PS592/L/Lymphoma, Large Cell, Anaplastic|3767",
            "Data": "PS592/L/Lymphoma, Large Cell, Anaplastic|3767",
            "Id": "3767",
            "Content": {}
          },
          {
            "DisplayText": "Primary Hypercoagulable State (incl. Factor V Leiden Disease)",
            "DisplayCount": "38",
            "Value": "PS592/P/Primary Hypercoagulable State (incl. Factor V Leiden Disease)|51109",
            "Data": "PS592/P/Primary Hypercoagulable State (incl. Factor V Leiden Disease)|51109",
            "Id": "51109",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51109"
            }
          },
          {
            "DisplayText": "Acute Myeloid Leukemia",
            "DisplayCount": "37",
            "Value": "PS592/A/Acute Myeloid Leukemia|11627",
            "Data": "PS592/A/Acute Myeloid Leukemia|11627",
            "Id": "11627",
            "Content": {}
          },
          {
            "DisplayText": "Anal Disorders",
            "DisplayCount": "35",
            "Value": "PS592/A/Anal Disorders|3759",
            "Data": "PS592/A/Anal Disorders|3759",
            "Id": "3759",
            "Content": {}
          },
          {
            "DisplayText": "Hypercoagulable State",
            "DisplayCount": "34",
            "Value": "PS592/H/Hypercoagulable State|52162",
            "Data": "PS592/H/Hypercoagulable State|52162",
            "Id": "52162",
            "Content": {}
          },
          {
            "DisplayText": "Lymphocytosis",
            "DisplayCount": "32",
            "Value": "PS592/L/Lymphocytosis|51091",
            "Data": "PS592/L/Lymphocytosis|51091",
            "Id": "51091",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51091"
            }
          },
          {
            "DisplayText": "Sickle Cell Disease",
            "DisplayCount": "31",
            "Value": "PS592/S/Sickle Cell Disease|50553",
            "Data": "PS592/S/Sickle Cell Disease|50553",
            "Id": "50553",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/50553"
            }
          },
          {
            "DisplayText": "Purpura",
            "DisplayCount": "29",
            "Value": "PS592/P/Purpura|15186",
            "Data": "PS592/P/Purpura|15186",
            "Id": "15186",
            "Content": {}
          },
          {
            "DisplayText": "Thrombosis",
            "DisplayCount": "29",
            "Value": "PS592/T/Thrombosis|2849",
            "Data": "PS592/T/Thrombosis|2849",
            "Id": "2849",
            "Content": {}
          },
          {
            "DisplayText": "Deep Vein Thrombosis (DVT)",
            "DisplayCount": "28",
            "Value": "PS592/D/Deep Vein Thrombosis (DVT)|7536",
            "Data": "PS592/D/Deep Vein Thrombosis (DVT)|7536",
            "Id": "7536",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/7536"
            }
          },
          {
            "DisplayText": "Esophageal Diseases",
            "DisplayCount": "28",
            "Value": "PS592/E/Esophageal Diseases|19830",
            "Data": "PS592/E/Esophageal Diseases|19830",
            "Id": "19830",
            "Content": {}
          },
          {
            "DisplayText": "Thalassemia",
            "DisplayCount": "28",
            "Value": "PS592/T/Thalassemia|2841",
            "Data": "PS592/T/Thalassemia|2841",
            "Id": "2841",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2841"
            }
          },
          {
            "DisplayText": "Pregnancy-Related Disorders",
            "DisplayCount": "27",
            "Value": "PS592/P/Pregnancy-Related Disorders|14889",
            "Data": "PS592/P/Pregnancy-Related Disorders|14889",
            "Id": "14889",
            "Content": {}
          },
          {
            "DisplayText": "Uterine Diseases",
            "DisplayCount": "27",
            "Value": "PS592/U/Uterine Diseases|695",
            "Data": "PS592/U/Uterine Diseases|695",
            "Id": "695",
            "Content": {}
          },
          {
            "DisplayText": "Antiphospholipid Syndrome (APS)",
            "DisplayCount": "26",
            "Value": "PS592/A/Antiphospholipid Syndrome (APS)|3997",
            "Data": "PS592/A/Antiphospholipid Syndrome (APS)|3997",
            "Id": "3997",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/3997"
            }
          },
          {
            "DisplayText": "Eye Cancer",
            "DisplayCount": "26",
            "Value": "PS592/E/Eye Cancer|8776",
            "Data": "PS592/E/Eye Cancer|8776",
            "Id": "8776",
            "Content": {}
          },
          {
            "DisplayText": "Acute Lymphoid Leukemia",
            "DisplayCount": "25",
            "Value": "PS592/A/Acute Lymphoid Leukemia|52169",
            "Data": "PS592/A/Acute Lymphoid Leukemia|52169",
            "Id": "52169",
            "Content": {}
          },
          {
            "DisplayText": "Mediastinal Tumors, Malignant",
            "DisplayCount": "25",
            "Value": "PS592/M/Mediastinal Tumors, Malignant|51188",
            "Data": "PS592/M/Mediastinal Tumors, Malignant|51188",
            "Id": "51188",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51188"
            }
          },
          {
            "DisplayText": "Venous Embolism and Thrombosis",
            "DisplayCount": "24",
            "Value": "PS592/V/Venous Embolism and Thrombosis|51230",
            "Data": "PS592/V/Venous Embolism and Thrombosis|51230",
            "Id": "51230",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51230"
            }
          },
          {
            "DisplayText": "Lung Neoplasms, Not Specified as Malignant",
            "DisplayCount": "18",
            "Value": "PS592/L/Lung Neoplasms, Not Specified as Malignant|51183",
            "Data": "PS592/L/Lung Neoplasms, Not Specified as Malignant|51183",
            "Id": "51183",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51183"
            }
          },
          {
            "DisplayText": "Larynx Conditions",
            "DisplayCount": "15",
            "Value": "PS592/L/Larynx Conditions|11414",
            "Data": "PS592/L/Larynx Conditions|11414",
            "Id": "11414",
            "Content": {}
          },
          {
            "DisplayText": "Meningiomas",
            "DisplayCount": "14",
            "Value": "PS592/M/Meningiomas|12242",
            "Data": "PS592/M/Meningiomas|12242",
            "Id": "12242",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/12242"
            }
          },
          {
            "DisplayText": "Cryoglobulinemia",
            "DisplayCount": "12",
            "Value": "PS592/C/Cryoglobulinemia|50698",
            "Data": "PS592/C/Cryoglobulinemia|50698",
            "Id": "50698",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/50698"
            }
          },
          {
            "DisplayText": "Vertebral Column Tumors",
            "DisplayCount": "9",
            "Value": "PS592/V/Vertebral Column Tumors|51127",
            "Data": "PS592/V/Vertebral Column Tumors|51127",
            "Id": "51127",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51127"
            }
          },
          {
            "DisplayText": "Paroxysmal Nocturnal Hemoglobinuria",
            "DisplayCount": "8",
            "Value": "PS592/P/Paroxysmal Nocturnal Hemoglobinuria|51101",
            "Data": "PS592/P/Paroxysmal Nocturnal Hemoglobinuria|51101",
            "Id": "51101",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51101"
            }
          },
          {
            "DisplayText": "Qualitative Platelet Defects (incl. Glanzmann's Thrombasthenia)",
            "DisplayCount": "8",
            "Value": "PS592/Q/Qualitative Platelet Defects (incl. Glanzmann's Thrombasthenia)|51111",
            "Data": "PS592/Q/Qualitative Platelet Defects (incl. Glanzmann's Thrombasthenia)|51111",
            "Id": "51111",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51111"
            }
          },
          {
            "DisplayText": "Mast Cell Diseases",
            "DisplayCount": "6",
            "Value": "PS592/M/Mast Cell Diseases|2335",
            "Data": "PS592/M/Mast Cell Diseases|2335",
            "Id": "2335",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2335"
            }
          },
          {
            "DisplayText": "Retina Diseases",
            "DisplayCount": "5",
            "Value": "PS592/R/Retina Diseases|783",
            "Data": "PS592/R/Retina Diseases|783",
            "Id": "783",
            "Content": {}
          },
          {
            "DisplayText": "Benign Tumor",
            "DisplayCount": "3",
            "Value": "PS592/B/Benign Tumor|4656",
            "Data": "PS592/B/Benign Tumor|4656",
            "Id": "4656",
            "Content": {}
          },
          {
            "DisplayText": "Colon Cancer",
            "DisplayCount": "3",
            "Value": "PS592/C/Colon Cancer|1852",
            "Data": "PS592/C/Colon Cancer|1852",
            "Id": "1852",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Treatment Complications",
            "DisplayCount": "2",
            "Value": "PS592/C/Cancer Treatment Complications|70",
            "Data": "PS592/C/Cancer Treatment Complications|70",
            "Id": "70",
            "Content": {}
          },
          {
            "DisplayText": "Acne",
            "DisplayCount": "1",
            "Value": "PS592/A/Acne|1551",
            "Data": "PS592/A/Acne|1551",
            "Id": "1551",
            "Content": {}
          },
          {
            "DisplayText": "Actinic Keratosis",
            "DisplayCount": "1",
            "Value": "PS592/A/Actinic Keratosis|1556",
            "Data": "PS592/A/Actinic Keratosis|1556",
            "Id": "1556",
            "Content": {}
          },
          {
            "DisplayText": "Aneurysm",
            "DisplayCount": "1",
            "Value": "PS592/A/Aneurysm|1611",
            "Data": "PS592/A/Aneurysm|1611",
            "Id": "1611",
            "Content": {}
          },
          {
            "DisplayText": "Aortic Embolism and Thrombosis",
            "DisplayCount": "1",
            "Value": "PS592/A/Aortic Embolism and Thrombosis|51050",
            "Data": "PS592/A/Aortic Embolism and Thrombosis|51050",
            "Id": "51050",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51050"
            }
          },
          {
            "DisplayText": "Arrhythmias",
            "DisplayCount": "1",
            "Value": "PS592/A/Arrhythmias|51051",
            "Data": "PS592/A/Arrhythmias|51051",
            "Id": "51051",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51051"
            }
          },
          {
            "DisplayText": "Athlete's Foot",
            "DisplayCount": "1",
            "Value": "PS592/A/Athlete's Foot|1664",
            "Data": "PS592/A/Athlete's Foot|1664",
            "Id": "1664",
            "Content": {}
          },
          {
            "DisplayText": "Atopic Dermatitis (Eczema)",
            "DisplayCount": "1",
            "Value": "PS592/A/Atopic Dermatitis (Eczema)|1666",
            "Data": "PS592/A/Atopic Dermatitis (Eczema)|1666",
            "Id": "1666",
            "Content": {}
          },
          {
            "DisplayText": "Atrial Fibrillation",
            "DisplayCount": "1",
            "Value": "PS592/A/Atrial Fibrillation|4",
            "Data": "PS592/A/Atrial Fibrillation|4",
            "Id": "4",
            "Content": {}
          },
          {
            "DisplayText": "Birthmark",
            "DisplayCount": "1",
            "Value": "PS592/B/Birthmark|1711",
            "Data": "PS592/B/Birthmark|1711",
            "Id": "1711",
            "Content": {}
          },
          {
            "DisplayText": "Blood Cancer",
            "DisplayCount": "1",
            "Value": "PS592/B/Blood Cancer|4832",
            "Data": "PS592/B/Blood Cancer|4832",
            "Id": "4832",
            "Content": {}
          },
          {
            "DisplayText": "Cardiomyopathy",
            "DisplayCount": "1",
            "Value": "PS592/C/Cardiomyopathy|1440",
            "Data": "PS592/C/Cardiomyopathy|1440",
            "Id": "1440",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/1440"
            }
          },
          {
            "DisplayText": "Cellulitis",
            "DisplayCount": "1",
            "Value": "PS592/C/Cellulitis|5461",
            "Data": "PS592/C/Cellulitis|5461",
            "Id": "5461",
            "Content": {}
          },
          {
            "DisplayText": "Cold Sore",
            "DisplayCount": "1",
            "Value": "PS592/C/Cold Sore|1851",
            "Data": "PS592/C/Cold Sore|1851",
            "Id": "1851",
            "Content": {}
          },
          {
            "DisplayText": "COPD (Chronic Obstructive Pulmonary Disease)",
            "DisplayCount": "1",
            "Value": "PS592/C/COPD (Chronic Obstructive Pulmonary Disease)|1827",
            "Data": "PS592/C/COPD (Chronic Obstructive Pulmonary Disease)|1827",
            "Id": "1827",
            "Content": {}
          },
          {
            "DisplayText": "Coronary Artery Disease (CAD)",
            "DisplayCount": "1",
            "Value": "PS592/C/Coronary Artery Disease (CAD)|19699",
            "Data": "PS592/C/Coronary Artery Disease (CAD)|19699",
            "Id": "19699",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/19699"
            }
          },
          {
            "DisplayText": "Dermatitis",
            "DisplayCount": "1",
            "Value": "PS592/D/Dermatitis|1922",
            "Data": "PS592/D/Dermatitis|1922",
            "Id": "1922",
            "Content": {}
          },
          {
            "DisplayText": "Dermatological Disorders",
            "DisplayCount": "1",
            "Value": "PS592/D/Dermatological Disorders|19798",
            "Data": "PS592/D/Dermatological Disorders|19798",
            "Id": "19798",
            "Content": {}
          },
          {
            "DisplayText": "Eosinophilia",
            "DisplayCount": "1",
            "Value": "PS592/E/Eosinophilia|51664",
            "Data": "PS592/E/Eosinophilia|51664",
            "Id": "51664",
            "Content": {}
          },
          {
            "DisplayText": "External Ear Disorders",
            "DisplayCount": "1",
            "Value": "PS592/E/External Ear Disorders|8318",
            "Data": "PS592/E/External Ear Disorders|8318",
            "Id": "8318",
            "Content": {}
          },
          {
            "DisplayText": "Eyelid Growth",
            "DisplayCount": "1",
            "Value": "PS592/E/Eyelid Growth|710",
            "Data": "PS592/E/Eyelid Growth|710",
            "Id": "710",
            "Content": {}
          },
          {
            "DisplayText": "Eyelid Lesions",
            "DisplayCount": "1",
            "Value": "PS592/E/Eyelid Lesions|19448",
            "Data": "PS592/E/Eyelid Lesions|19448",
            "Id": "19448",
            "Content": {}
          },
          {
            "DisplayText": "Follicular Lymphoma, Large-Cell",
            "DisplayCount": "1",
            "Value": "PS592/F/Follicular Lymphoma, Large-Cell|11894",
            "Data": "PS592/F/Follicular Lymphoma, Large-Cell|11894",
            "Id": "11894",
            "Content": {}
          },
          {
            "DisplayText": "Folliculitis",
            "DisplayCount": "1",
            "Value": "PS592/F/Folliculitis|278",
            "Data": "PS592/F/Folliculitis|278",
            "Id": "278",
            "Content": {}
          },
          {
            "DisplayText": "Foot Conditions",
            "DisplayCount": "1",
            "Value": "PS592/F/Foot Conditions|9346",
            "Data": "PS592/F/Foot Conditions|9346",
            "Id": "9346",
            "Content": {}
          },
          {
            "DisplayText": "Fungal Nail Infection",
            "DisplayCount": "1",
            "Value": "PS592/F/Fungal Nail Infection|9443",
            "Data": "PS592/F/Fungal Nail Infection|9443",
            "Id": "9443",
            "Content": {}
          },
          {
            "DisplayText": "Genital Warts",
            "DisplayCount": "1",
            "Value": "PS592/G/Genital Warts|9543",
            "Data": "PS592/G/Genital Warts|9543",
            "Id": "9543",
            "Content": {}
          },
          {
            "DisplayText": "Hair Conditions",
            "DisplayCount": "1",
            "Value": "PS592/H/Hair Conditions|9855",
            "Data": "PS592/H/Hair Conditions|9855",
            "Id": "9855",
            "Content": {}
          },
          {
            "DisplayText": "Hair Loss",
            "DisplayCount": "1",
            "Value": "PS592/H/Hair Loss|1588",
            "Data": "PS592/H/Hair Loss|1588",
            "Id": "1588",
            "Content": {}
          },
          {
            "DisplayText": "Heart Disease",
            "DisplayCount": "1",
            "Value": "PS592/H/Heart Disease|1468",
            "Data": "PS592/H/Heart Disease|1468",
            "Id": "1468",
            "Content": {}
          },
          {
            "DisplayText": "Herpes Simplex Infection",
            "DisplayCount": "1",
            "Value": "PS592/H/Herpes Simplex Infection|2163",
            "Data": "PS592/H/Herpes Simplex Infection|2163",
            "Id": "2163",
            "Content": {}
          },
          {
            "DisplayText": "Hidradenitis",
            "DisplayCount": "1",
            "Value": "PS592/H/Hidradenitis|51079",
            "Data": "PS592/H/Hidradenitis|51079",
            "Id": "51079",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51079"
            }
          },
          {
            "DisplayText": "Hives",
            "DisplayCount": "1",
            "Value": "PS592/H/Hives|2172",
            "Data": "PS592/H/Hives|2172",
            "Id": "2172",
            "Content": {}
          },
          {
            "DisplayText": "Hyperthrophic Scar",
            "DisplayCount": "1",
            "Value": "PS592/H/Hyperthrophic Scar|51357",
            "Data": "PS592/H/Hyperthrophic Scar|51357",
            "Id": "51357",
            "Content": {}
          },
          {
            "DisplayText": "Keloid Scar",
            "DisplayCount": "1",
            "Value": "PS592/K/Keloid Scar|11131",
            "Data": "PS592/K/Keloid Scar|11131",
            "Id": "11131",
            "Content": {}
          },
          {
            "DisplayText": "Leg and Foot Ulcers",
            "DisplayCount": "1",
            "Value": "PS592/L/Leg and Foot Ulcers|51789",
            "Data": "PS592/L/Leg and Foot Ulcers|51789",
            "Id": "51789",
            "Content": {}
          },
          {
            "DisplayText": "Mediastinal Tumors, Not Specified as Malignant",
            "DisplayCount": "1",
            "Value": "PS592/M/Mediastinal Tumors, Not Specified as Malignant|51189",
            "Data": "PS592/M/Mediastinal Tumors, Not Specified as Malignant|51189",
            "Id": "51189",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51189"
            }
          },
          {
            "DisplayText": "Moles (Benign Skin Lesions)",
            "DisplayCount": "1",
            "Value": "PS592/M/Moles (Benign Skin Lesions)|51793",
            "Data": "PS592/M/Moles (Benign Skin Lesions)|51793",
            "Id": "51793",
            "Content": {}
          },
          {
            "DisplayText": "Molluscum Contagiosum Infection",
            "DisplayCount": "1",
            "Value": "PS592/M/Molluscum Contagiosum Infection|12755",
            "Data": "PS592/M/Molluscum Contagiosum Infection|12755",
            "Id": "12755",
            "Content": {}
          },
          {
            "DisplayText": "Peripheral Arterial Aneurysm",
            "DisplayCount": "1",
            "Value": "PS592/P/Peripheral Arterial Aneurysm|52155",
            "Data": "PS592/P/Peripheral Arterial Aneurysm|52155",
            "Id": "52155",
            "Content": {}
          },
          {
            "DisplayText": "Peripheral Arterial Aneurysm and Dissection",
            "DisplayCount": "1",
            "Value": "PS592/P/Peripheral Arterial Aneurysm and Dissection|51205",
            "Data": "PS592/P/Peripheral Arterial Aneurysm and Dissection|51205",
            "Id": "51205",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/51205"
            }
          },
          {
            "DisplayText": "Psoriasis",
            "DisplayCount": "1",
            "Value": "PS592/P/Psoriasis|534",
            "Data": "PS592/P/Psoriasis|534",
            "Id": "534",
            "Content": {}
          },
          {
            "DisplayText": "Pulmonary Embolism",
            "DisplayCount": "1",
            "Value": "PS592/P/Pulmonary Embolism|2636",
            "Data": "PS592/P/Pulmonary Embolism|2636",
            "Id": "2636",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/2636"
            }
          },
          {
            "DisplayText": "Rash",
            "DisplayCount": "1",
            "Value": "PS592/R/Rash|18652",
            "Data": "PS592/R/Rash|18652",
            "Id": "18652",
            "Content": {}
          },
          {
            "DisplayText": "Ringworm",
            "DisplayCount": "1",
            "Value": "PS592/R/Ringworm|2699",
            "Data": "PS592/R/Ringworm|2699",
            "Id": "2699",
            "Content": {}
          },
          {
            "DisplayText": "Rosacea",
            "DisplayCount": "1",
            "Value": "PS592/R/Rosacea|555",
            "Data": "PS592/R/Rosacea|555",
            "Id": "555",
            "Content": {}
          },
          {
            "DisplayText": "Seborrheic Dermatitis",
            "DisplayCount": "1",
            "Value": "PS592/S/Seborrheic Dermatitis|51794",
            "Data": "PS592/S/Seborrheic Dermatitis|51794",
            "Id": "51794",
            "Content": {}
          },
          {
            "DisplayText": "Shingles",
            "DisplayCount": "1",
            "Value": "PS592/S/Shingles|577",
            "Data": "PS592/S/Shingles|577",
            "Id": "577",
            "Content": {}
          },
          {
            "DisplayText": "Skin Aging",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Aging|2752",
            "Data": "PS592/S/Skin Aging|2752",
            "Id": "2752",
            "Content": {}
          },
          {
            "DisplayText": "Skin Discoloration",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Discoloration|51721",
            "Data": "PS592/S/Skin Discoloration|51721",
            "Id": "51721",
            "Content": {}
          },
          {
            "DisplayText": "Skin Diseases",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Diseases|46",
            "Data": "PS592/S/Skin Diseases|46",
            "Id": "46",
            "Content": {}
          },
          {
            "DisplayText": "Skin Disorders",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Disorders|16438",
            "Data": "PS592/S/Skin Disorders|16438",
            "Id": "16438",
            "Content": {}
          },
          {
            "DisplayText": "Skin Infections",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Infections|20096",
            "Data": "PS592/S/Skin Infections|20096",
            "Id": "20096",
            "Content": {}
          },
          {
            "DisplayText": "Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Lesion|18779",
            "Data": "PS592/S/Skin Lesion|18779",
            "Id": "18779",
            "Content": {}
          },
          {
            "DisplayText": "Spider Veins",
            "DisplayCount": "1",
            "Value": "PS592/S/Spider Veins|19465",
            "Data": "PS592/S/Spider Veins|19465",
            "Id": "19465",
            "Content": {}
          },
          {
            "DisplayText": "Stretch Marks",
            "DisplayCount": "1",
            "Value": "PS592/S/Stretch Marks|2804",
            "Data": "PS592/S/Stretch Marks|2804",
            "Id": "2804",
            "Content": {}
          },
          {
            "DisplayText": "Tumor",
            "DisplayCount": "1",
            "Value": "PS592/T/Tumor|2880",
            "Data": "PS592/T/Tumor|2880",
            "Id": "2880",
            "Content": {}
          },
          {
            "DisplayText": "Ulcer",
            "DisplayCount": "1",
            "Value": "PS592/U/Ulcer|35",
            "Data": "PS592/U/Ulcer|35",
            "Id": "35",
            "Content": {}
          },
          {
            "DisplayText": "Varicose Veins",
            "DisplayCount": "1",
            "Value": "PS592/V/Varicose Veins|664",
            "Data": "PS592/V/Varicose Veins|664",
            "Id": "664",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/cond/664"
            }
          },
          {
            "DisplayText": "Warts",
            "DisplayCount": "1",
            "Value": "PS592/W/Warts|2946",
            "Data": "PS592/W/Warts|2946",
            "Id": "2946",
            "Content": {}
          },
          {
            "DisplayText": "Wrinkles",
            "DisplayCount": "1",
            "Value": "PS592/W/Wrinkles|51446",
            "Data": "PS592/W/Wrinkles|51446",
            "Id": "51446",
            "Content": {}
          }
        ]
      },
      "FacetKey": "conditions"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Abscess or Fluid Incision and Drainage",
            "DisplayCount": "1",
            "Value": "PS592/A/Abscess or Fluid Incision and Drainage|52392",
            "Data": "PS592/A/Abscess or Fluid Incision and Drainage|52392",
            "Id": "52392",
            "Content": {}
          },
          {
            "DisplayText": "Acne Surgery",
            "DisplayCount": "1",
            "Value": "PS592/A/Acne Surgery|735",
            "Data": "PS592/A/Acne Surgery|735",
            "Id": "735",
            "Content": {}
          },
          {
            "DisplayText": "Adjacent Tissue Transfer",
            "DisplayCount": "1",
            "Value": "PS592/A/Adjacent Tissue Transfer|51718",
            "Data": "PS592/A/Adjacent Tissue Transfer|51718",
            "Id": "51718",
            "Content": {}
          },
          {
            "DisplayText": "Aesthetic Hand Rejuvenation",
            "DisplayCount": "1",
            "Value": "PS592/A/Aesthetic Hand Rejuvenation|50985",
            "Data": "PS592/A/Aesthetic Hand Rejuvenation|50985",
            "Id": "50985",
            "Content": {}
          },
          {
            "DisplayText": "Biological Therapy",
            "DisplayCount": "81",
            "Value": "PS592/B/Biological Therapy|496",
            "Data": "PS592/B/Biological Therapy|496",
            "Id": "496",
            "Content": {}
          },
          {
            "DisplayText": "Biopsy",
            "DisplayCount": "81",
            "Value": "PS592/B/Biopsy|87",
            "Data": "PS592/B/Biopsy|87",
            "Id": "87",
            "Content": {}
          },
          {
            "DisplayText": "Biopsy of Breast",
            "DisplayCount": "81",
            "Value": "PS592/B/Biopsy of Breast|50464",
            "Data": "PS592/B/Biopsy of Breast|50464",
            "Id": "50464",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50464"
            }
          },
          {
            "DisplayText": "Bone Marrow Aspiration",
            "DisplayCount": "4",
            "Value": "PS592/B/Bone Marrow Aspiration|1378",
            "Data": "PS592/B/Bone Marrow Aspiration|1378",
            "Id": "1378",
            "Content": {}
          },
          {
            "DisplayText": "Bone Marrow Biopsy",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Marrow Biopsy|1379",
            "Data": "PS592/B/Bone Marrow Biopsy|1379",
            "Id": "1379",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/1379"
            }
          },
          {
            "DisplayText": "Bone Marrow Transplant",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Marrow Transplant|1576",
            "Data": "PS592/B/Bone Marrow Transplant|1576",
            "Id": "1576",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/1576"
            }
          },
          {
            "DisplayText": "Bone Scan",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Scan|50279",
            "Data": "PS592/B/Bone Scan|50279",
            "Id": "50279",
            "Content": {}
          },
          {
            "DisplayText": "Botox® Injection",
            "DisplayCount": "1",
            "Value": "PS592/B/Botox® Injection|50047",
            "Data": "PS592/B/Botox® Injection|50047",
            "Id": "50047",
            "Content": {}
          },
          {
            "DisplayText": "Brachytherapy",
            "DisplayCount": "81",
            "Value": "PS592/B/Brachytherapy|1579",
            "Data": "PS592/B/Brachytherapy|1579",
            "Id": "1579",
            "Content": {}
          },
          {
            "DisplayText": "Brain Radiation Treatment",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain Radiation Treatment|50281",
            "Data": "PS592/B/Brain Radiation Treatment|50281",
            "Id": "50281",
            "Content": {}
          },
          {
            "DisplayText": "Breast Cancer Screening",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Cancer Screening|50284",
            "Data": "PS592/B/Breast Cancer Screening|50284",
            "Id": "50284",
            "Content": {}
          },
          {
            "DisplayText": "Breast Cancer Treatment",
            "DisplayCount": "3",
            "Value": "PS592/B/Breast Cancer Treatment|2145",
            "Data": "PS592/B/Breast Cancer Treatment|2145",
            "Id": "2145",
            "Content": {}
          },
          {
            "DisplayText": "Breast Reconstruction",
            "DisplayCount": "1",
            "Value": "PS592/B/Breast Reconstruction|50596",
            "Data": "PS592/B/Breast Reconstruction|50596",
            "Id": "50596",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50596"
            }
          },
          {
            "DisplayText": "Breast Surgical Procedure",
            "DisplayCount": "1",
            "Value": "PS592/B/Breast Surgical Procedure|35",
            "Data": "PS592/B/Breast Surgical Procedure|35",
            "Id": "35",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Counseling",
            "DisplayCount": "2",
            "Value": "PS592/C/Cancer Counseling|721",
            "Data": "PS592/C/Cancer Counseling|721",
            "Id": "721",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Pain Management",
            "DisplayCount": "2",
            "Value": "PS592/C/Cancer Pain Management|1588",
            "Data": "PS592/C/Cancer Pain Management|1588",
            "Id": "1588",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Treatment",
            "DisplayCount": "27",
            "Value": "PS592/C/Cancer Treatment|50998",
            "Data": "PS592/C/Cancer Treatment|50998",
            "Id": "50998",
            "Content": {}
          },
          {
            "DisplayText": "Captique™ Injection",
            "DisplayCount": "1",
            "Value": "PS592/C/Captique™ Injection|50723",
            "Data": "PS592/C/Captique™ Injection|50723",
            "Id": "50723",
            "Content": {}
          },
          {
            "DisplayText": "Cardiac MRI (Magnetic Resonance Imaging) of Heart or Chest",
            "DisplayCount": "8",
            "Value": "PS592/C/Cardiac MRI (Magnetic Resonance Imaging) of Heart or Chest|50468",
            "Data": "PS592/C/Cardiac MRI (Magnetic Resonance Imaging) of Heart or Chest|50468",
            "Id": "50468",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50468"
            }
          },
          {
            "DisplayText": "Chemotherapy",
            "DisplayCount": "81",
            "Value": "PS592/C/Chemotherapy|229",
            "Data": "PS592/C/Chemotherapy|229",
            "Id": "229",
            "Content": {}
          },
          {
            "DisplayText": "Chest CT (incl. Heart and Lungs)",
            "DisplayCount": "1",
            "Value": "PS592/C/Chest CT (incl. Heart and Lungs)|50466",
            "Data": "PS592/C/Chest CT (incl. Heart and Lungs)|50466",
            "Id": "50466",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50466"
            }
          },
          {
            "DisplayText": "Collagen Injection",
            "DisplayCount": "1",
            "Value": "PS592/C/Collagen Injection|62",
            "Data": "PS592/C/Collagen Injection|62",
            "Id": "62",
            "Content": {}
          },
          {
            "DisplayText": "Cryoablation",
            "DisplayCount": "81",
            "Value": "PS592/C/Cryoablation|1412",
            "Data": "PS592/C/Cryoablation|1412",
            "Id": "1412",
            "Content": {}
          },
          {
            "DisplayText": "Destruction of Benign Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/D/Destruction of Benign Skin Lesion|51719",
            "Data": "PS592/D/Destruction of Benign Skin Lesion|51719",
            "Id": "51719",
            "Content": {}
          },
          {
            "DisplayText": "Destruction of Penile Lesion",
            "DisplayCount": "1",
            "Value": "PS592/D/Destruction of Penile Lesion|51721",
            "Data": "PS592/D/Destruction of Penile Lesion|51721",
            "Id": "51721",
            "Content": {}
          },
          {
            "DisplayText": "Electrocoagulation",
            "DisplayCount": "81",
            "Value": "PS592/E/Electrocoagulation|50312",
            "Data": "PS592/E/Electrocoagulation|50312",
            "Id": "50312",
            "Content": {}
          },
          {
            "DisplayText": "Endoscopy",
            "DisplayCount": "81",
            "Value": "PS592/E/Endoscopy|767",
            "Data": "PS592/E/Endoscopy|767",
            "Id": "767",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Benign Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/E/Excision of Benign Skin Lesion|2253",
            "Data": "PS592/E/Excision of Benign Skin Lesion|2253",
            "Id": "2253",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Breast Tumor",
            "DisplayCount": "1",
            "Value": "PS592/E/Excision of Breast Tumor|50502",
            "Data": "PS592/E/Excision of Breast Tumor|50502",
            "Id": "50502",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50502"
            }
          },
          {
            "DisplayText": "Excision of Facial Bone",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Facial Bone|51864",
            "Data": "PS592/E/Excision of Facial Bone|51864",
            "Id": "51864",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Femur or Knee",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Femur or Knee|51870",
            "Data": "PS592/E/Excision of Femur or Knee|51870",
            "Id": "51870",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Humerus",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Humerus|51871",
            "Data": "PS592/E/Excision of Humerus|51871",
            "Id": "51871",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Metacarpal and Carpal",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Metacarpal and Carpal|51888",
            "Data": "PS592/E/Excision of Metacarpal and Carpal|51888",
            "Id": "51888",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Radius or Ulna",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Radius or Ulna|51909",
            "Data": "PS592/E/Excision of Radius or Ulna|51909",
            "Id": "51909",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Scapula, Clavicle, Rib, or Sternum",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Scapula, Clavicle, Rib, or Sternum|51879",
            "Data": "PS592/E/Excision of Scapula, Clavicle, Rib, or Sternum|51879",
            "Id": "51879",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Skin Cancer",
            "DisplayCount": "1",
            "Value": "PS592/E/Excision of Skin Cancer|51722",
            "Data": "PS592/E/Excision of Skin Cancer|51722",
            "Id": "51722",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/E/Excision of Skin Lesion|50758",
            "Data": "PS592/E/Excision of Skin Lesion|50758",
            "Id": "50758",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Tarsal or Metatarsal",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Tarsal or Metatarsal|51883",
            "Data": "PS592/E/Excision of Tarsal or Metatarsal|51883",
            "Id": "51883",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Tibia or Fibula",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Tibia or Fibula|51876",
            "Data": "PS592/E/Excision of Tibia or Fibula|51876",
            "Id": "51876",
            "Content": {}
          },
          {
            "DisplayText": "Eyelid Surgery",
            "DisplayCount": "1",
            "Value": "PS592/E/Eyelid Surgery|2259",
            "Data": "PS592/E/Eyelid Surgery|2259",
            "Id": "2259",
            "Content": {}
          },
          {
            "DisplayText": "Facial Peel",
            "DisplayCount": "1",
            "Value": "PS592/F/Facial Peel|396",
            "Data": "PS592/F/Facial Peel|396",
            "Id": "396",
            "Content": {}
          },
          {
            "DisplayText": "Facial Rejuvenation",
            "DisplayCount": "1",
            "Value": "PS592/F/Facial Rejuvenation|50890",
            "Data": "PS592/F/Facial Rejuvenation|50890",
            "Id": "50890",
            "Content": {}
          },
          {
            "DisplayText": "Genetic Screening for Breast Cancer",
            "DisplayCount": "2",
            "Value": "PS592/G/Genetic Screening for Breast Cancer|51110",
            "Data": "PS592/G/Genetic Screening for Breast Cancer|51110",
            "Id": "51110",
            "Content": {}
          },
          {
            "DisplayText": "Genetic Testing",
            "DisplayCount": "3",
            "Value": "PS592/G/Genetic Testing|2885",
            "Data": "PS592/G/Genetic Testing|2885",
            "Id": "2885",
            "Content": {}
          },
          {
            "DisplayText": "Glycolic Acid Skin Care Treatment",
            "DisplayCount": "1",
            "Value": "PS592/G/Glycolic Acid Skin Care Treatment|51124",
            "Data": "PS592/G/Glycolic Acid Skin Care Treatment|51124",
            "Id": "51124",
            "Content": {}
          },
          {
            "DisplayText": "Hair Removal",
            "DisplayCount": "1",
            "Value": "PS592/H/Hair Removal|142",
            "Data": "PS592/H/Hair Removal|142",
            "Id": "142",
            "Content": {}
          },
          {
            "DisplayText": "Head and Neck Surgery",
            "DisplayCount": "1",
            "Value": "PS592/H/Head and Neck Surgery|22",
            "Data": "PS592/H/Head and Neck Surgery|22",
            "Id": "22",
            "Content": {}
          },
          {
            "DisplayText": "Hematologic Disorder Treatment",
            "DisplayCount": "13",
            "Value": "PS592/H/Hematologic Disorder Treatment|2287",
            "Data": "PS592/H/Hematologic Disorder Treatment|2287",
            "Id": "2287",
            "Content": {}
          },
          {
            "DisplayText": "HPC Transplantation (Stem Cell Transplant)",
            "DisplayCount": "81",
            "Value": "PS592/H/HPC Transplantation (Stem Cell Transplant)|50650",
            "Data": "PS592/H/HPC Transplantation (Stem Cell Transplant)|50650",
            "Id": "50650",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50650"
            }
          },
          {
            "DisplayText": "Hylaform Injection",
            "DisplayCount": "1",
            "Value": "PS592/H/Hylaform Injection|50783",
            "Data": "PS592/H/Hylaform Injection|50783",
            "Id": "50783",
            "Content": {}
          },
          {
            "DisplayText": "Immunotherapy",
            "DisplayCount": "81",
            "Value": "PS592/I/Immunotherapy|10531",
            "Data": "PS592/I/Immunotherapy|10531",
            "Id": "10531",
            "Content": {}
          },
          {
            "DisplayText": "Induction Chemotherapy",
            "DisplayCount": "81",
            "Value": "PS592/I/Induction Chemotherapy|50343",
            "Data": "PS592/I/Induction Chemotherapy|50343",
            "Id": "50343",
            "Content": {}
          },
          {
            "DisplayText": "Interstitial Brachytherapy",
            "DisplayCount": "81",
            "Value": "PS592/I/Interstitial Brachytherapy|50346",
            "Data": "PS592/I/Interstitial Brachytherapy|50346",
            "Id": "50346",
            "Content": {}
          },
          {
            "DisplayText": "Intraoperative Radiation Therapy (IORT)",
            "DisplayCount": "81",
            "Value": "PS592/I/Intraoperative Radiation Therapy (IORT)|2320",
            "Data": "PS592/I/Intraoperative Radiation Therapy (IORT)|2320",
            "Id": "2320",
            "Content": {}
          },
          {
            "DisplayText": "Intravesical Therapy",
            "DisplayCount": "81",
            "Value": "PS592/I/Intravesical Therapy|50351",
            "Data": "PS592/I/Intravesical Therapy|50351",
            "Id": "50351",
            "Content": {}
          },
          {
            "DisplayText": "Laser Nail Treatment",
            "DisplayCount": "1",
            "Value": "PS592/L/Laser Nail Treatment|50965",
            "Data": "PS592/L/Laser Nail Treatment|50965",
            "Id": "50965",
            "Content": {}
          },
          {
            "DisplayText": "Laser Spider Vein Treatment",
            "DisplayCount": "1",
            "Value": "PS592/L/Laser Spider Vein Treatment|51098",
            "Data": "PS592/L/Laser Spider Vein Treatment|51098",
            "Id": "51098",
            "Content": {}
          },
          {
            "DisplayText": "Lung Surgery",
            "DisplayCount": "1",
            "Value": "PS592/L/Lung Surgery|1455",
            "Data": "PS592/L/Lung Surgery|1455",
            "Id": "1455",
            "Content": {}
          },
          {
            "DisplayText": "Lymph Node Biopsy or Excision",
            "DisplayCount": "1",
            "Value": "PS592/L/Lymph Node Biopsy or Excision|50661",
            "Data": "PS592/L/Lymph Node Biopsy or Excision|50661",
            "Id": "50661",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50661"
            }
          },
          {
            "DisplayText": "Mastectomy",
            "DisplayCount": "1",
            "Value": "PS592/M/Mastectomy|463",
            "Data": "PS592/M/Mastectomy|463",
            "Id": "463",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/463"
            }
          },
          {
            "DisplayText": "Mohs Surgery",
            "DisplayCount": "1",
            "Value": "PS592/M/Mohs Surgery|3022",
            "Data": "PS592/M/Mohs Surgery|3022",
            "Id": "3022",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/3022"
            }
          },
          {
            "DisplayText": "Mole Removal",
            "DisplayCount": "1",
            "Value": "PS592/M/Mole Removal|840",
            "Data": "PS592/M/Mole Removal|840",
            "Id": "840",
            "Content": {}
          },
          {
            "DisplayText": "PET Scan",
            "DisplayCount": "81",
            "Value": "PS592/P/PET Scan|944",
            "Data": "PS592/P/PET Scan|944",
            "Id": "944",
            "Content": {}
          },
          {
            "DisplayText": "Photodynamic Therapy (PDT)",
            "DisplayCount": "81",
            "Value": "PS592/P/Photodynamic Therapy (PDT)|10900",
            "Data": "PS592/P/Photodynamic Therapy (PDT)|10900",
            "Id": "10900",
            "Content": {}
          },
          {
            "DisplayText": "Plasmapheresis",
            "DisplayCount": "11",
            "Value": "PS592/P/Plasmapheresis|3125",
            "Data": "PS592/P/Plasmapheresis|3125",
            "Id": "3125",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/3125"
            }
          },
          {
            "DisplayText": "Platelet-Rich Plasma Injection (PRP)",
            "DisplayCount": "81",
            "Value": "PS592/P/Platelet-Rich Plasma Injection (PRP)|50110",
            "Data": "PS592/P/Platelet-Rich Plasma Injection (PRP)|50110",
            "Id": "50110",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50110"
            }
          },
          {
            "DisplayText": "Radiation Therapy",
            "DisplayCount": "81",
            "Value": "PS592/R/Radiation Therapy|1953",
            "Data": "PS592/R/Radiation Therapy|1953",
            "Id": "1953",
            "Content": {}
          },
          {
            "DisplayText": "Radioactive Iodine Treatment",
            "DisplayCount": "81",
            "Value": "PS592/R/Radioactive Iodine Treatment|50226",
            "Data": "PS592/R/Radioactive Iodine Treatment|50226",
            "Id": "50226",
            "Content": {}
          },
          {
            "DisplayText": "Radiofrequency Ablation",
            "DisplayCount": "81",
            "Value": "PS592/R/Radiofrequency Ablation|2599",
            "Data": "PS592/R/Radiofrequency Ablation|2599",
            "Id": "2599",
            "Content": {}
          },
          {
            "DisplayText": "Radiosensitizers",
            "DisplayCount": "81",
            "Value": "PS592/R/Radiosensitizers|50416",
            "Data": "PS592/R/Radiosensitizers|50416",
            "Id": "50416",
            "Content": {}
          },
          {
            "DisplayText": "Restylane® Injections",
            "DisplayCount": "1",
            "Value": "PS592/R/Restylane® Injections|131",
            "Data": "PS592/R/Restylane® Injections|131",
            "Id": "131",
            "Content": {}
          },
          {
            "DisplayText": "Shaving of Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/S/Shaving of Skin Lesion|51726",
            "Data": "PS592/S/Shaving of Skin Lesion|51726",
            "Id": "51726",
            "Content": {}
          },
          {
            "DisplayText": "Skin Biopsy",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Biopsy|1990",
            "Data": "PS592/S/Skin Biopsy|1990",
            "Id": "1990",
            "Content": {}
          },
          {
            "DisplayText": "Skin Cancer Removal",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Cancer Removal|445",
            "Data": "PS592/S/Skin Cancer Removal|445",
            "Id": "445",
            "Content": {}
          },
          {
            "DisplayText": "Skin Surgery",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Surgery|904",
            "Data": "PS592/S/Skin Surgery|904",
            "Id": "904",
            "Content": {}
          },
          {
            "DisplayText": "Soft Tissue Tumor Removal",
            "DisplayCount": "1",
            "Value": "PS592/S/Soft Tissue Tumor Removal|51724",
            "Data": "PS592/S/Soft Tissue Tumor Removal|51724",
            "Id": "51724",
            "Content": {}
          },
          {
            "DisplayText": "Stereotactic Body Radiotherapy (SBRT)",
            "DisplayCount": "81",
            "Value": "PS592/S/Stereotactic Body Radiotherapy (SBRT)|3201",
            "Data": "PS592/S/Stereotactic Body Radiotherapy (SBRT)|3201",
            "Id": "3201",
            "Content": {}
          },
          {
            "DisplayText": "Stereotactic Radiosurgery",
            "DisplayCount": "81",
            "Value": "PS592/S/Stereotactic Radiosurgery|3202",
            "Data": "PS592/S/Stereotactic Radiosurgery|3202",
            "Id": "3202",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/3202"
            }
          },
          {
            "DisplayText": "Tattoo Removal",
            "DisplayCount": "1",
            "Value": "PS592/T/Tattoo Removal|50879",
            "Data": "PS592/T/Tattoo Removal|50879",
            "Id": "50879",
            "Content": {}
          },
          {
            "DisplayText": "Thoracentesis",
            "DisplayCount": "19",
            "Value": "PS592/T/Thoracentesis|50682",
            "Data": "PS592/T/Thoracentesis|50682",
            "Id": "50682",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50682"
            }
          },
          {
            "DisplayText": "Thyroid Lobectomy",
            "DisplayCount": "81",
            "Value": "PS592/T/Thyroid Lobectomy|51913",
            "Data": "PS592/T/Thyroid Lobectomy|51913",
            "Id": "51913",
            "Content": {}
          },
          {
            "DisplayText": "Thyroidectomy",
            "DisplayCount": "81",
            "Value": "PS592/T/Thyroidectomy|2522",
            "Data": "PS592/T/Thyroidectomy|2522",
            "Id": "2522",
            "Content": {}
          },
          {
            "DisplayText": "Tumor Ablation",
            "DisplayCount": "81",
            "Value": "PS592/T/Tumor Ablation|1507",
            "Data": "PS592/T/Tumor Ablation|1507",
            "Id": "1507",
            "Content": {}
          },
          {
            "DisplayText": "Venous Sclerotherapy",
            "DisplayCount": "1",
            "Value": "PS592/V/Venous Sclerotherapy|51866",
            "Data": "PS592/V/Venous Sclerotherapy|51866",
            "Id": "51866",
            "Content": {}
          },
          {
            "DisplayText": "Wart Removal",
            "DisplayCount": "1",
            "Value": "PS592/W/Wart Removal|2584",
            "Data": "PS592/W/Wart Removal|2584",
            "Id": "2584",
            "Content": {}
          },
          {
            "DisplayText": "Wound Repair",
            "DisplayCount": "1",
            "Value": "PS592/W/Wound Repair|50587",
            "Data": "PS592/W/Wound Repair|50587",
            "Id": "50587",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50587"
            }
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Biological Therapy",
            "DisplayCount": "81",
            "Value": "PS592/B/Biological Therapy|496",
            "Data": "PS592/B/Biological Therapy|496",
            "Id": "496",
            "Content": {}
          },
          {
            "DisplayText": "Biopsy",
            "DisplayCount": "81",
            "Value": "PS592/B/Biopsy|87",
            "Data": "PS592/B/Biopsy|87",
            "Id": "87",
            "Content": {}
          },
          {
            "DisplayText": "Biopsy of Breast",
            "DisplayCount": "81",
            "Value": "PS592/B/Biopsy of Breast|50464",
            "Data": "PS592/B/Biopsy of Breast|50464",
            "Id": "50464",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50464"
            }
          }
        ],
        "TopViewAllValues": [
          {
            "DisplayText": "Biological Therapy",
            "DisplayCount": "81",
            "Value": "PS592/B/Biological Therapy|496",
            "Data": "PS592/B/Biological Therapy|496",
            "Id": "496",
            "Content": {}
          },
          {
            "DisplayText": "Biopsy",
            "DisplayCount": "81",
            "Value": "PS592/B/Biopsy|87",
            "Data": "PS592/B/Biopsy|87",
            "Id": "87",
            "Content": {}
          },
          {
            "DisplayText": "Biopsy of Breast",
            "DisplayCount": "81",
            "Value": "PS592/B/Biopsy of Breast|50464",
            "Data": "PS592/B/Biopsy of Breast|50464",
            "Id": "50464",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50464"
            }
          },
          {
            "DisplayText": "Bone Marrow Biopsy",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Marrow Biopsy|1379",
            "Data": "PS592/B/Bone Marrow Biopsy|1379",
            "Id": "1379",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/1379"
            }
          },
          {
            "DisplayText": "Bone Marrow Transplant",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Marrow Transplant|1576",
            "Data": "PS592/B/Bone Marrow Transplant|1576",
            "Id": "1576",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/1576"
            }
          },
          {
            "DisplayText": "Bone Scan",
            "DisplayCount": "81",
            "Value": "PS592/B/Bone Scan|50279",
            "Data": "PS592/B/Bone Scan|50279",
            "Id": "50279",
            "Content": {}
          },
          {
            "DisplayText": "Brachytherapy",
            "DisplayCount": "81",
            "Value": "PS592/B/Brachytherapy|1579",
            "Data": "PS592/B/Brachytherapy|1579",
            "Id": "1579",
            "Content": {}
          },
          {
            "DisplayText": "Brain Radiation Treatment",
            "DisplayCount": "81",
            "Value": "PS592/B/Brain Radiation Treatment|50281",
            "Data": "PS592/B/Brain Radiation Treatment|50281",
            "Id": "50281",
            "Content": {}
          },
          {
            "DisplayText": "Breast Cancer Screening",
            "DisplayCount": "81",
            "Value": "PS592/B/Breast Cancer Screening|50284",
            "Data": "PS592/B/Breast Cancer Screening|50284",
            "Id": "50284",
            "Content": {}
          },
          {
            "DisplayText": "Chemotherapy",
            "DisplayCount": "81",
            "Value": "PS592/C/Chemotherapy|229",
            "Data": "PS592/C/Chemotherapy|229",
            "Id": "229",
            "Content": {}
          },
          {
            "DisplayText": "Cryoablation",
            "DisplayCount": "81",
            "Value": "PS592/C/Cryoablation|1412",
            "Data": "PS592/C/Cryoablation|1412",
            "Id": "1412",
            "Content": {}
          },
          {
            "DisplayText": "Electrocoagulation",
            "DisplayCount": "81",
            "Value": "PS592/E/Electrocoagulation|50312",
            "Data": "PS592/E/Electrocoagulation|50312",
            "Id": "50312",
            "Content": {}
          },
          {
            "DisplayText": "Endoscopy",
            "DisplayCount": "81",
            "Value": "PS592/E/Endoscopy|767",
            "Data": "PS592/E/Endoscopy|767",
            "Id": "767",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Facial Bone",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Facial Bone|51864",
            "Data": "PS592/E/Excision of Facial Bone|51864",
            "Id": "51864",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Femur or Knee",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Femur or Knee|51870",
            "Data": "PS592/E/Excision of Femur or Knee|51870",
            "Id": "51870",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Humerus",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Humerus|51871",
            "Data": "PS592/E/Excision of Humerus|51871",
            "Id": "51871",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Metacarpal and Carpal",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Metacarpal and Carpal|51888",
            "Data": "PS592/E/Excision of Metacarpal and Carpal|51888",
            "Id": "51888",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Radius or Ulna",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Radius or Ulna|51909",
            "Data": "PS592/E/Excision of Radius or Ulna|51909",
            "Id": "51909",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Scapula, Clavicle, Rib, or Sternum",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Scapula, Clavicle, Rib, or Sternum|51879",
            "Data": "PS592/E/Excision of Scapula, Clavicle, Rib, or Sternum|51879",
            "Id": "51879",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Tarsal or Metatarsal",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Tarsal or Metatarsal|51883",
            "Data": "PS592/E/Excision of Tarsal or Metatarsal|51883",
            "Id": "51883",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Tibia or Fibula",
            "DisplayCount": "81",
            "Value": "PS592/E/Excision of Tibia or Fibula|51876",
            "Data": "PS592/E/Excision of Tibia or Fibula|51876",
            "Id": "51876",
            "Content": {}
          },
          {
            "DisplayText": "HPC Transplantation (Stem Cell Transplant)",
            "DisplayCount": "81",
            "Value": "PS592/H/HPC Transplantation (Stem Cell Transplant)|50650",
            "Data": "PS592/H/HPC Transplantation (Stem Cell Transplant)|50650",
            "Id": "50650",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50650"
            }
          },
          {
            "DisplayText": "Immunotherapy",
            "DisplayCount": "81",
            "Value": "PS592/I/Immunotherapy|10531",
            "Data": "PS592/I/Immunotherapy|10531",
            "Id": "10531",
            "Content": {}
          },
          {
            "DisplayText": "Induction Chemotherapy",
            "DisplayCount": "81",
            "Value": "PS592/I/Induction Chemotherapy|50343",
            "Data": "PS592/I/Induction Chemotherapy|50343",
            "Id": "50343",
            "Content": {}
          },
          {
            "DisplayText": "Interstitial Brachytherapy",
            "DisplayCount": "81",
            "Value": "PS592/I/Interstitial Brachytherapy|50346",
            "Data": "PS592/I/Interstitial Brachytherapy|50346",
            "Id": "50346",
            "Content": {}
          },
          {
            "DisplayText": "Intraoperative Radiation Therapy (IORT)",
            "DisplayCount": "81",
            "Value": "PS592/I/Intraoperative Radiation Therapy (IORT)|2320",
            "Data": "PS592/I/Intraoperative Radiation Therapy (IORT)|2320",
            "Id": "2320",
            "Content": {}
          },
          {
            "DisplayText": "Intravesical Therapy",
            "DisplayCount": "81",
            "Value": "PS592/I/Intravesical Therapy|50351",
            "Data": "PS592/I/Intravesical Therapy|50351",
            "Id": "50351",
            "Content": {}
          },
          {
            "DisplayText": "PET Scan",
            "DisplayCount": "81",
            "Value": "PS592/P/PET Scan|944",
            "Data": "PS592/P/PET Scan|944",
            "Id": "944",
            "Content": {}
          },
          {
            "DisplayText": "Photodynamic Therapy (PDT)",
            "DisplayCount": "81",
            "Value": "PS592/P/Photodynamic Therapy (PDT)|10900",
            "Data": "PS592/P/Photodynamic Therapy (PDT)|10900",
            "Id": "10900",
            "Content": {}
          },
          {
            "DisplayText": "Platelet-Rich Plasma Injection (PRP)",
            "DisplayCount": "81",
            "Value": "PS592/P/Platelet-Rich Plasma Injection (PRP)|50110",
            "Data": "PS592/P/Platelet-Rich Plasma Injection (PRP)|50110",
            "Id": "50110",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50110"
            }
          },
          {
            "DisplayText": "Radiation Therapy",
            "DisplayCount": "81",
            "Value": "PS592/R/Radiation Therapy|1953",
            "Data": "PS592/R/Radiation Therapy|1953",
            "Id": "1953",
            "Content": {}
          },
          {
            "DisplayText": "Radioactive Iodine Treatment",
            "DisplayCount": "81",
            "Value": "PS592/R/Radioactive Iodine Treatment|50226",
            "Data": "PS592/R/Radioactive Iodine Treatment|50226",
            "Id": "50226",
            "Content": {}
          },
          {
            "DisplayText": "Radiofrequency Ablation",
            "DisplayCount": "81",
            "Value": "PS592/R/Radiofrequency Ablation|2599",
            "Data": "PS592/R/Radiofrequency Ablation|2599",
            "Id": "2599",
            "Content": {}
          },
          {
            "DisplayText": "Radiosensitizers",
            "DisplayCount": "81",
            "Value": "PS592/R/Radiosensitizers|50416",
            "Data": "PS592/R/Radiosensitizers|50416",
            "Id": "50416",
            "Content": {}
          },
          {
            "DisplayText": "Stereotactic Body Radiotherapy (SBRT)",
            "DisplayCount": "81",
            "Value": "PS592/S/Stereotactic Body Radiotherapy (SBRT)|3201",
            "Data": "PS592/S/Stereotactic Body Radiotherapy (SBRT)|3201",
            "Id": "3201",
            "Content": {}
          },
          {
            "DisplayText": "Stereotactic Radiosurgery",
            "DisplayCount": "81",
            "Value": "PS592/S/Stereotactic Radiosurgery|3202",
            "Data": "PS592/S/Stereotactic Radiosurgery|3202",
            "Id": "3202",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/3202"
            }
          },
          {
            "DisplayText": "Thyroid Lobectomy",
            "DisplayCount": "81",
            "Value": "PS592/T/Thyroid Lobectomy|51913",
            "Data": "PS592/T/Thyroid Lobectomy|51913",
            "Id": "51913",
            "Content": {}
          },
          {
            "DisplayText": "Thyroidectomy",
            "DisplayCount": "81",
            "Value": "PS592/T/Thyroidectomy|2522",
            "Data": "PS592/T/Thyroidectomy|2522",
            "Id": "2522",
            "Content": {}
          },
          {
            "DisplayText": "Tumor Ablation",
            "DisplayCount": "81",
            "Value": "PS592/T/Tumor Ablation|1507",
            "Data": "PS592/T/Tumor Ablation|1507",
            "Id": "1507",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Treatment",
            "DisplayCount": "27",
            "Value": "PS592/C/Cancer Treatment|50998",
            "Data": "PS592/C/Cancer Treatment|50998",
            "Id": "50998",
            "Content": {}
          },
          {
            "DisplayText": "Thoracentesis",
            "DisplayCount": "19",
            "Value": "PS592/T/Thoracentesis|50682",
            "Data": "PS592/T/Thoracentesis|50682",
            "Id": "50682",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50682"
            }
          },
          {
            "DisplayText": "Hematologic Disorder Treatment",
            "DisplayCount": "13",
            "Value": "PS592/H/Hematologic Disorder Treatment|2287",
            "Data": "PS592/H/Hematologic Disorder Treatment|2287",
            "Id": "2287",
            "Content": {}
          },
          {
            "DisplayText": "Plasmapheresis",
            "DisplayCount": "11",
            "Value": "PS592/P/Plasmapheresis|3125",
            "Data": "PS592/P/Plasmapheresis|3125",
            "Id": "3125",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/3125"
            }
          },
          {
            "DisplayText": "Cardiac MRI (Magnetic Resonance Imaging) of Heart or Chest",
            "DisplayCount": "8",
            "Value": "PS592/C/Cardiac MRI (Magnetic Resonance Imaging) of Heart or Chest|50468",
            "Data": "PS592/C/Cardiac MRI (Magnetic Resonance Imaging) of Heart or Chest|50468",
            "Id": "50468",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50468"
            }
          },
          {
            "DisplayText": "Bone Marrow Aspiration",
            "DisplayCount": "4",
            "Value": "PS592/B/Bone Marrow Aspiration|1378",
            "Data": "PS592/B/Bone Marrow Aspiration|1378",
            "Id": "1378",
            "Content": {}
          },
          {
            "DisplayText": "Breast Cancer Treatment",
            "DisplayCount": "3",
            "Value": "PS592/B/Breast Cancer Treatment|2145",
            "Data": "PS592/B/Breast Cancer Treatment|2145",
            "Id": "2145",
            "Content": {}
          },
          {
            "DisplayText": "Genetic Testing",
            "DisplayCount": "3",
            "Value": "PS592/G/Genetic Testing|2885",
            "Data": "PS592/G/Genetic Testing|2885",
            "Id": "2885",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Counseling",
            "DisplayCount": "2",
            "Value": "PS592/C/Cancer Counseling|721",
            "Data": "PS592/C/Cancer Counseling|721",
            "Id": "721",
            "Content": {}
          },
          {
            "DisplayText": "Cancer Pain Management",
            "DisplayCount": "2",
            "Value": "PS592/C/Cancer Pain Management|1588",
            "Data": "PS592/C/Cancer Pain Management|1588",
            "Id": "1588",
            "Content": {}
          },
          {
            "DisplayText": "Genetic Screening for Breast Cancer",
            "DisplayCount": "2",
            "Value": "PS592/G/Genetic Screening for Breast Cancer|51110",
            "Data": "PS592/G/Genetic Screening for Breast Cancer|51110",
            "Id": "51110",
            "Content": {}
          },
          {
            "DisplayText": "Abscess or Fluid Incision and Drainage",
            "DisplayCount": "1",
            "Value": "PS592/A/Abscess or Fluid Incision and Drainage|52392",
            "Data": "PS592/A/Abscess or Fluid Incision and Drainage|52392",
            "Id": "52392",
            "Content": {}
          },
          {
            "DisplayText": "Acne Surgery",
            "DisplayCount": "1",
            "Value": "PS592/A/Acne Surgery|735",
            "Data": "PS592/A/Acne Surgery|735",
            "Id": "735",
            "Content": {}
          },
          {
            "DisplayText": "Adjacent Tissue Transfer",
            "DisplayCount": "1",
            "Value": "PS592/A/Adjacent Tissue Transfer|51718",
            "Data": "PS592/A/Adjacent Tissue Transfer|51718",
            "Id": "51718",
            "Content": {}
          },
          {
            "DisplayText": "Aesthetic Hand Rejuvenation",
            "DisplayCount": "1",
            "Value": "PS592/A/Aesthetic Hand Rejuvenation|50985",
            "Data": "PS592/A/Aesthetic Hand Rejuvenation|50985",
            "Id": "50985",
            "Content": {}
          },
          {
            "DisplayText": "Botox® Injection",
            "DisplayCount": "1",
            "Value": "PS592/B/Botox® Injection|50047",
            "Data": "PS592/B/Botox® Injection|50047",
            "Id": "50047",
            "Content": {}
          },
          {
            "DisplayText": "Breast Reconstruction",
            "DisplayCount": "1",
            "Value": "PS592/B/Breast Reconstruction|50596",
            "Data": "PS592/B/Breast Reconstruction|50596",
            "Id": "50596",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50596"
            }
          },
          {
            "DisplayText": "Breast Surgical Procedure",
            "DisplayCount": "1",
            "Value": "PS592/B/Breast Surgical Procedure|35",
            "Data": "PS592/B/Breast Surgical Procedure|35",
            "Id": "35",
            "Content": {}
          },
          {
            "DisplayText": "Captique™ Injection",
            "DisplayCount": "1",
            "Value": "PS592/C/Captique™ Injection|50723",
            "Data": "PS592/C/Captique™ Injection|50723",
            "Id": "50723",
            "Content": {}
          },
          {
            "DisplayText": "Chest CT (incl. Heart and Lungs)",
            "DisplayCount": "1",
            "Value": "PS592/C/Chest CT (incl. Heart and Lungs)|50466",
            "Data": "PS592/C/Chest CT (incl. Heart and Lungs)|50466",
            "Id": "50466",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50466"
            }
          },
          {
            "DisplayText": "Collagen Injection",
            "DisplayCount": "1",
            "Value": "PS592/C/Collagen Injection|62",
            "Data": "PS592/C/Collagen Injection|62",
            "Id": "62",
            "Content": {}
          },
          {
            "DisplayText": "Destruction of Benign Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/D/Destruction of Benign Skin Lesion|51719",
            "Data": "PS592/D/Destruction of Benign Skin Lesion|51719",
            "Id": "51719",
            "Content": {}
          },
          {
            "DisplayText": "Destruction of Penile Lesion",
            "DisplayCount": "1",
            "Value": "PS592/D/Destruction of Penile Lesion|51721",
            "Data": "PS592/D/Destruction of Penile Lesion|51721",
            "Id": "51721",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Benign Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/E/Excision of Benign Skin Lesion|2253",
            "Data": "PS592/E/Excision of Benign Skin Lesion|2253",
            "Id": "2253",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Breast Tumor",
            "DisplayCount": "1",
            "Value": "PS592/E/Excision of Breast Tumor|50502",
            "Data": "PS592/E/Excision of Breast Tumor|50502",
            "Id": "50502",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50502"
            }
          },
          {
            "DisplayText": "Excision of Skin Cancer",
            "DisplayCount": "1",
            "Value": "PS592/E/Excision of Skin Cancer|51722",
            "Data": "PS592/E/Excision of Skin Cancer|51722",
            "Id": "51722",
            "Content": {}
          },
          {
            "DisplayText": "Excision of Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/E/Excision of Skin Lesion|50758",
            "Data": "PS592/E/Excision of Skin Lesion|50758",
            "Id": "50758",
            "Content": {}
          },
          {
            "DisplayText": "Eyelid Surgery",
            "DisplayCount": "1",
            "Value": "PS592/E/Eyelid Surgery|2259",
            "Data": "PS592/E/Eyelid Surgery|2259",
            "Id": "2259",
            "Content": {}
          },
          {
            "DisplayText": "Facial Peel",
            "DisplayCount": "1",
            "Value": "PS592/F/Facial Peel|396",
            "Data": "PS592/F/Facial Peel|396",
            "Id": "396",
            "Content": {}
          },
          {
            "DisplayText": "Facial Rejuvenation",
            "DisplayCount": "1",
            "Value": "PS592/F/Facial Rejuvenation|50890",
            "Data": "PS592/F/Facial Rejuvenation|50890",
            "Id": "50890",
            "Content": {}
          },
          {
            "DisplayText": "Glycolic Acid Skin Care Treatment",
            "DisplayCount": "1",
            "Value": "PS592/G/Glycolic Acid Skin Care Treatment|51124",
            "Data": "PS592/G/Glycolic Acid Skin Care Treatment|51124",
            "Id": "51124",
            "Content": {}
          },
          {
            "DisplayText": "Hair Removal",
            "DisplayCount": "1",
            "Value": "PS592/H/Hair Removal|142",
            "Data": "PS592/H/Hair Removal|142",
            "Id": "142",
            "Content": {}
          },
          {
            "DisplayText": "Head and Neck Surgery",
            "DisplayCount": "1",
            "Value": "PS592/H/Head and Neck Surgery|22",
            "Data": "PS592/H/Head and Neck Surgery|22",
            "Id": "22",
            "Content": {}
          },
          {
            "DisplayText": "Hylaform Injection",
            "DisplayCount": "1",
            "Value": "PS592/H/Hylaform Injection|50783",
            "Data": "PS592/H/Hylaform Injection|50783",
            "Id": "50783",
            "Content": {}
          },
          {
            "DisplayText": "Laser Nail Treatment",
            "DisplayCount": "1",
            "Value": "PS592/L/Laser Nail Treatment|50965",
            "Data": "PS592/L/Laser Nail Treatment|50965",
            "Id": "50965",
            "Content": {}
          },
          {
            "DisplayText": "Laser Spider Vein Treatment",
            "DisplayCount": "1",
            "Value": "PS592/L/Laser Spider Vein Treatment|51098",
            "Data": "PS592/L/Laser Spider Vein Treatment|51098",
            "Id": "51098",
            "Content": {}
          },
          {
            "DisplayText": "Lung Surgery",
            "DisplayCount": "1",
            "Value": "PS592/L/Lung Surgery|1455",
            "Data": "PS592/L/Lung Surgery|1455",
            "Id": "1455",
            "Content": {}
          },
          {
            "DisplayText": "Lymph Node Biopsy or Excision",
            "DisplayCount": "1",
            "Value": "PS592/L/Lymph Node Biopsy or Excision|50661",
            "Data": "PS592/L/Lymph Node Biopsy or Excision|50661",
            "Id": "50661",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50661"
            }
          },
          {
            "DisplayText": "Mastectomy",
            "DisplayCount": "1",
            "Value": "PS592/M/Mastectomy|463",
            "Data": "PS592/M/Mastectomy|463",
            "Id": "463",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/463"
            }
          },
          {
            "DisplayText": "Mohs Surgery",
            "DisplayCount": "1",
            "Value": "PS592/M/Mohs Surgery|3022",
            "Data": "PS592/M/Mohs Surgery|3022",
            "Id": "3022",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/3022"
            }
          },
          {
            "DisplayText": "Mole Removal",
            "DisplayCount": "1",
            "Value": "PS592/M/Mole Removal|840",
            "Data": "PS592/M/Mole Removal|840",
            "Id": "840",
            "Content": {}
          },
          {
            "DisplayText": "Restylane® Injections",
            "DisplayCount": "1",
            "Value": "PS592/R/Restylane® Injections|131",
            "Data": "PS592/R/Restylane® Injections|131",
            "Id": "131",
            "Content": {}
          },
          {
            "DisplayText": "Shaving of Skin Lesion",
            "DisplayCount": "1",
            "Value": "PS592/S/Shaving of Skin Lesion|51726",
            "Data": "PS592/S/Shaving of Skin Lesion|51726",
            "Id": "51726",
            "Content": {}
          },
          {
            "DisplayText": "Skin Biopsy",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Biopsy|1990",
            "Data": "PS592/S/Skin Biopsy|1990",
            "Id": "1990",
            "Content": {}
          },
          {
            "DisplayText": "Skin Cancer Removal",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Cancer Removal|445",
            "Data": "PS592/S/Skin Cancer Removal|445",
            "Id": "445",
            "Content": {}
          },
          {
            "DisplayText": "Skin Surgery",
            "DisplayCount": "1",
            "Value": "PS592/S/Skin Surgery|904",
            "Data": "PS592/S/Skin Surgery|904",
            "Id": "904",
            "Content": {}
          },
          {
            "DisplayText": "Soft Tissue Tumor Removal",
            "DisplayCount": "1",
            "Value": "PS592/S/Soft Tissue Tumor Removal|51724",
            "Data": "PS592/S/Soft Tissue Tumor Removal|51724",
            "Id": "51724",
            "Content": {}
          },
          {
            "DisplayText": "Tattoo Removal",
            "DisplayCount": "1",
            "Value": "PS592/T/Tattoo Removal|50879",
            "Data": "PS592/T/Tattoo Removal|50879",
            "Id": "50879",
            "Content": {}
          },
          {
            "DisplayText": "Venous Sclerotherapy",
            "DisplayCount": "1",
            "Value": "PS592/V/Venous Sclerotherapy|51866",
            "Data": "PS592/V/Venous Sclerotherapy|51866",
            "Id": "51866",
            "Content": {}
          },
          {
            "DisplayText": "Wart Removal",
            "DisplayCount": "1",
            "Value": "PS592/W/Wart Removal|2584",
            "Data": "PS592/W/Wart Removal|2584",
            "Id": "2584",
            "Content": {}
          },
          {
            "DisplayText": "Wound Repair",
            "DisplayCount": "1",
            "Value": "PS592/W/Wound Repair|50587",
            "Data": "PS592/W/Wound Repair|50587",
            "Id": "50587",
            "Content": {
              "HasContent": true,
              "ContentUrl": "/autosuggest/proc/50587"
            }
          }
        ]
      },
      "FacetKey": "procedures"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Recommended By Patients",
            "DisplayCount": "67",
            "Value": "recommendedByPatients",
            "Content": {}
          },
          {
            "DisplayText": "Board Certified",
            "DisplayCount": "95",
            "Value": "boardCertified",
            "Content": {}
          },
          {
            "DisplayText": "Accepting New Patients",
            "DisplayCount": "85",
            "Value": "newPatients",
            "Content": {}
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Recommended By Patients",
            "DisplayCount": "67",
            "Value": "recommendedByPatients",
            "Content": {}
          },
          {
            "DisplayText": "Board Certified",
            "DisplayCount": "95",
            "Value": "boardCertified",
            "Content": {}
          },
          {
            "DisplayText": "Has No Sanctions",
            "DisplayCount": "107",
            "Value": "noSanctions",
            "Content": {}
          }
        ],
        "TopViewAllValues": []
      },
      "FacetKey": "feedback"
    },
    {
      "Info": {
        "AllValues": [
          {
            "DisplayText": "Accepts New Patients",
            "DisplayCount": "85",
            "Value": "newPatients",
            "Content": {}
          }
        ],
        "SelectedValues": [],
        "TopValues": [
          {
            "DisplayText": "Accepts New Patients",
            "DisplayCount": "85",
            "Value": "newPatients",
            "Content": {}
          }
        ],
        "TopViewAllValues": []
      },
      "FacetKey": "newPatients"
    }
  ],
  "SearchType": "PracticingSpecialty",
  "CID": "PBHTEST_007"
}


"""

@app.route('/chat', methods=['GET'])
def web():    
    return "WELCOME :)"


@app.route('/webhook', methods=['POST'])
def webhook():
    # req = request.get_json(silent=True, force=True)
    req = json.loads(text, strict=False)

    print("Request:")
    # print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    names = create_namelist(req)
    return create_messages(names)


def create_namelist(data):
    l = []
    for i in range(0, 5):
        l.append(data['Results'][i]['DemographicInfo']['DisplayName'])
    return l


def create_messages(l):
    l1 = [{'type':0,'speech':'these are the top 5 results that matched your search...'}]
    for i in l:
        a = {"type":0,
        "speech":i}
        l1.append(a)
    return {"messages":l1}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')