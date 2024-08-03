# TechShop Web Scraping and ETL Pipeline Project

### Project Overview

TechShop, a prominent online laptop vendor on Jumia, sought to enhance its strategic business decisions by leveraging detailed sales data. This project involved the development of an advanced Python ETL (Extract, Transform, Load) pipeline designed to scrape, clean, and transform data from Jumia’s website into a PostgreSQL database. The resulting solution empowered TechShop with real-time insights, enabling data-driven decisions to optimize inventory, pricing strategies, and marketing efforts.

### Business Problem

TechShop required comprehensive and up-to-date data from Jumia's e-commerce platform to make informed decisions regarding its laptop sales strategies. The primary challenge was the lack of readily accessible data, necessitating the implementation of a robust web scraping and ETL pipeline to automate data extraction, transformation, and loading processes. The goal was to ensure accurate, timely, and structured data availability for analysis.

### Objectives

- **Develop a Python script** to efficiently scrape laptop data from Jumia’s website.
- **Clean and transform the scraped data** to fit a structured database schema.
- **Load the processed data** into a PostgreSQL database.
- **Automate the ETL process** to run periodically, ensuring data remains current.

### Key Accomplishments

- **Automated Data Extraction:** Successfully developed a Python script utilizing Requests and BeautifulSoup to scrape data from multiple pages on Jumia’s website, capturing key product details such as names, new prices, old prices, and discounts.
- **Data Cleaning and Transformation:** Implemented data cleaning functions to strip unwanted characters and format price fields, ensuring data integrity and consistency before database insertion.
- **Database Integration:** Utilized SQLAlchemy to seamlessly load the cleaned data into a PostgreSQL database, enabling efficient querying and analysis.
- **Periodic Automation:** Scheduled the ETL pipeline to run at regular intervals, ensuring that TechShop always has access to the latest sales data for strategic decision-making.

### Benefits

- **Real-time Data Access:** Provided TechShop with up-to-date sales data, enhancing their ability to make timely and informed business decisions.
- **Resource Efficiency:** Automated the data collection and processing workflow, significantly reducing manual effort and operational costs.
- **Enhanced Business Insights:** Equipped TechShop with comprehensive data analytics capabilities, leading to improved inventory management, pricing optimization, and targeted marketing strategies.

### Tech Stack

- **Python:** Leveraged libraries such as Requests for web scraping, BeautifulSoup for HTML parsing, and SQLAlchemy for database interactions.
- **SQL:** Utilized for writing queries to manipulate and manage data within the PostgreSQL database.
- **PostgreSQL:** Employed as the relational database to store and manage the transformed data, enabling efficient data retrieval and analysis.

### Conclusion

The TechShop Web Scraping and ETL Pipeline Project exemplifies the power of automated data engineering solutions in transforming raw web data into actionable business insights. By developing a robust and automated ETL pipeline, TechShop was able to unlock the potential of its sales data, driving better business decisions and achieving greater operational efficiency.
