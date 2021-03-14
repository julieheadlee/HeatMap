--Drop existing tables
DROP TABLE "AirQuality";
DROP TABLE "CensusPopulation";
DROP TABLE "Sites";
DROP TABLE "DateYear";
DROP TABLE "year";
DROP TABLE "Defining_Parameter";
DROP TABLE "County";

-- AirQuality_DB

CREATE TABLE "County" (
    "county_code" int   NOT NULL,
    "county_name" varchar   NOT NULL,
    CONSTRAINT "pk_County" PRIMARY KEY (
        "county_code"
     )
);

CREATE TABLE "Sites" (
    "site_no" varchar   NOT NULL,
    "Latitude" float   NOT NULL,
    "Longitude" float   NOT NULL,
    "Elevation" float   , -- remove NOT NULL
    "Land_Use" varchar   , -- remove NOT NULL
    "Location_Setting" varchar   , -- remove NOT NULL
    "State_Name" varchar   NOT NULL,
    "County_Code" int   NOT NULL,
    "City_Name" varchar   NOT NULL,
    "CBSA_Name" varchar   , -- remove NOT NULL
    CONSTRAINT "pk_Sites" PRIMARY KEY (
        "site_no"
     )
);

CREATE TABLE "Defining_Parameter" (
    "Defining_Parameter" varchar   NOT NULL,
    CONSTRAINT "pk_Defining_Parameter" PRIMARY KEY (
        "Defining_Parameter"
     )
);

CREATE TABLE "year" (
    "year" int   NOT NULL,
    CONSTRAINT "pk_year" PRIMARY KEY (
        "year"
     )
);

CREATE TABLE "DateYear" (
    "Date" date   NOT NULL,
    "year" int   NOT NULL,
    CONSTRAINT "pk_DateYear" PRIMARY KEY (
        "Date"
     )
);

CREATE TABLE "AirQuality" (
    "aq_unique_no" int   NOT NULL,
    "State_Name" varchar   NOT NULL,
    "county_code" int   NOT NULL,
    "Date" date   NOT NULL,
    "AQI" int   NOT NULL,
    "Category" varchar   NOT NULL,
    "site_no" varchar   NOT NULL,
    "Defining_Parameter" varchar   NOT NULL,
    CONSTRAINT "pk_AirQuality" PRIMARY KEY (
        "aq_unique_no"
     )
);

CREATE TABLE "CensusPopulation" (
    "census_unique_no" int   NOT NULL,
    "county_code" int   NOT NULL,
    "year" int   NOT NULL,
    "population" int   NOT NULL,
    CONSTRAINT "pk_CensusPopulation" PRIMARY KEY (
        "census_unique_no"
     )
);

ALTER TABLE "Sites" ADD CONSTRAINT "fk_Sites_County_Code" FOREIGN KEY("County_Code")
REFERENCES "County" ("county_code");

ALTER TABLE "DateYear" ADD CONSTRAINT "fk_DateYear_year" FOREIGN KEY("year")
REFERENCES "year" ("year");

ALTER TABLE "AirQuality" ADD CONSTRAINT "fk_AirQuality_county_code" FOREIGN KEY("county_code")
REFERENCES "County" ("county_code");

ALTER TABLE "AirQuality" ADD CONSTRAINT "fk_AirQuality_Date" FOREIGN KEY("Date")
REFERENCES "DateYear" ("Date");

ALTER TABLE "AirQuality" ADD CONSTRAINT "fk_AirQuality_site_no" FOREIGN KEY("site_no")
REFERENCES "Sites" ("site_no");

ALTER TABLE "AirQuality" ADD CONSTRAINT "fk_AirQuality_Defining_Parameter" FOREIGN KEY("Defining_Parameter")
REFERENCES "Defining_Parameter" ("Defining_Parameter");

ALTER TABLE "CensusPopulation" ADD CONSTRAINT "fk_CensusPopulation_county_code" FOREIGN KEY("county_code")
REFERENCES "County" ("county_code");

ALTER TABLE "CensusPopulation" ADD CONSTRAINT "fk_CensusPopulation_year" FOREIGN KEY("year")
REFERENCES "year" ("year");
