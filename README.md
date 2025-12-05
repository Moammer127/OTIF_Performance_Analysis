# OTIF_Performance_Analysis

### Project Overview


This project evaluates employee performance in this order delivery process and identifies factors affecting timely and accurate delivery.This project is target on objectives sach as assess employee performance in order delivery, identify factors impacting delivery speed and efficiency, analyze common delivery errors, and provide recommendations for improvemenr.

### Data Sources

- Orders Table: stores information about customer orders. It typically includes fields like Order ID, Customer ID, Order Date, Salesperson ID, Returns, ScheduleDeleveryDate, EBL_IssuedDate, and ActualDelevery Date.This table helps analysts track order processing, monitor customer activity, and analyze overall sales performance.
  
- Salesperson Table: stores key information about each sales representative. It typically includes fields like Salesperson ID, SalespersonName, and Team.This table helps analysts track salesperson performance, assign sales activities, and analyze sales results by representative or region.
  
- Date Table: is a foundational reference table used in data analysis and reporting. It typically includes fields like Date, Year, Quarter, and Month.This table helps analysts perform accurate time-based analysis, filtering, and trend reporting across all datasets.
  
- Customers Table: stores key information about each customer. It usually includes fields like Customer ID, Name, City ID, CityName, and ServiceChannel.This table helps analysts understand customer demographics, behavior, and purchasing patterns to improve sales and marketing strategies.

### Tools
- Excel - Exploration Data Analysis(EDA).
- Python - Data Cleaning.
- Power Bi - Data Modelling, Data Analysis, and Creating Dashboard.
  
### Exploratory Data Analysis(EDA)
- Overall performance
    - What is the overall OTIF percentage for a given period monthly?
    - How does OTIF vary across different customers or cities?
- On-Time aspect
    - What percentage of orders were delivered on or before the promised date?
    - Which teams or suppliers have the highest late deliveries?
    - What are the most common reasons for late delivery (transport delays,warehouse issues, supplier shortage?
- In-Full aspect
    - What percentage of orders were delivered with the correct quantity and items?


### Data Cleaning/Preparation

In the initial data cleaning phase, I performed the following tasks:
- Extract data from Csv Files. 
- Data cleaning and formatting. 
- Join tables.
- Union tables.
- Renamed same columns name.
- Join Columns in one Column.
- Convert between data type.
- Data Loading and inspection. 
  

### Data Analysis
#### Write same DAX functions to calculate KPIs 
Calculate number of customers:
Number of Customers = DISTINCTCOUNT('F-Orders'[CustomerID])

Calculate number of orders:

Number of Orders = COUNT('F-Orders'[OrderID])

Calculate number of orders delevered:

Number of Orders Delevered = CALCULATE([# Orders],'F-Orders'[ActualDeliveryDate]<> BLANK())

Calculate in full%:

In Full % = DIVIDE(
                   CALCULATE([# Orders Delevered],'F-Orders'[Returns]=0),[# Orders Delevered])

Calculate on time%:

On time % = DIVIDE(CALCULATE([# Orders Delevered],'F-Orders'[On time]= "Yes"),[# Orders Delevered])

Calculate order cycle time:

Order Cycle Time = AVERAGEX('F-Orders',DATEDIFF('F-Orders'[OrderDate],'F-Orders'[ActualDeliveryDate],DAY))

Calculate Order Fill Rate:

Order Fill Rate = AVERAGEX('F-Orders',DATEDIFF('F-Orders'[OrderDate],'F-Orders'[e-BL_IssuedDate],DAY))

Calculate OTIF%:

OTIF = [In Full %]*[On time %]

Calculate outstanding:

Outstanding = CALCULATE([# Orders]-[# Orders Delevered],ALL('Calendar'),'Calendar'[Date]<=MAX('Calendar'[Date]))

Calculate prevous month OTIF:

Prevous month otif = CALCULATE([OTIF],DATEADD('Calendar'[Date],-1,MONTH))


### Results

- The OTIF percentage is approximately 78%, and the main reason for the failure is related to On Time performance.
- The best OTIF performance was recorded in January 2019, because all teams during that period performed well. This is also due to the fact that delivery companies usually operate at high efficiency at the beginning of    each year.
- The worst OTIF performance was in April 2020, because some teams caused delays in delivering the products. This negatively affected the On Time %, and consequently impacted customer satisfaction.
- The best team is Coast, based on its performance in On Time %, Number of Orders, In Full %, and Number of Delivered Orders.
- The worst-performing team in terms of OTIF is South MC/KA, because it is a team dedicated only to packaging. Therefore, we find that its In Full % is 100%, but this does not improve its OTIF performance.
- The team that contributed the most to Outstanding orders is Coast, due to being assigned more tasks than the other teams, although the number of orders it successfully delivered is significantly higher compared to      the other teams.

### Recommendations

- Improve planning and demand forecasting
    - Review the accuracy of demand forecasting to reduce shortages or overstock.
    - Ensure early coordination between sales, production, and procurement teams to avoid supply gaps.
- Enhance inventory management
   - Set appropriate safety stock levels for high-demand products.
   - Use smart inventory management systems to track real quantities.
   - Monitor products with frequent “Not In Full” cases and address the root causes.
- Improve logistics performance (On-Time)
   - Review the performance of carriers and suppliers by comparing actual vs planned delivery times.
   - Use backup carriers to reduce the risk of delays.
   - Improve warehouse packing and shipping processes to minimize errors.
