-- Ensure that the warehouse is dropped if it exists
DROP WAREHOUSE IF EXISTS CompanyTask;

-- Create a warehouse instance
CREATE WAREHOUSE CompanyTask
  WITH WAREHOUSE_SIZE = 'SMALL'
  WAREHOUSE_TYPE = 'STANDARD'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

-- Use the warehouse
USE WAREHOUSE CompanyTask;

-- Ensure that the database is dropped if it exists
DROP DATABASE IF EXISTS SnowLeadDB;

-- Create a database
CREATE DATABASE SnowLeadDB;

-- Use the database
USE DATABASE SnowLeadDB;

-- Ensure that the schema is dropped if it exists
DROP SCHEMA IF EXISTS SnowLeadDB.LeadSchema;

-- Create a schema
CREATE SCHEMA SnowLeadDB.LeadSchema;

-- Create the company leads table
CREATE TABLE IF NOT EXISTS SnowLeadDB.LeadSchema.CompanyLeads (
    Id STRING DEFAULT UUID_STRING(),
    State INT NOT NULL,
    CreatedDateUtc TIMESTAMP_NTZ NOT NULL,
    CancellationRequestDateUtc TIMESTAMP_NTZ NULL,
    CancellationDateUtc TIMESTAMP_NTZ NULL,
    CancellationRejectionDateUtc TIMESTAMP_NTZ NULL,
    SoldEmployee STRING(255) NOT NULL,
    CancelledEmployee STRING(255) NULL,
    UpdatedDateUtc TIMESTAMP_NTZ NOT NULL
);

-- Create the lead events table
CREATE TABLE IF NOT EXISTS SnowLeadDB.LeadSchema.LeadEvents (
    Id STRING DEFAULT UUID_STRING(),
    EventType STRING(255) NOT NULL,
    EventEmployee STRING(255) NOT NULL,
    EventDate TIMESTAMP_NTZ NOT NULL,
    LeadId STRING NOT NULL,
    UpdatedDateUtc TIMESTAMP_NTZ NOT NULL
);