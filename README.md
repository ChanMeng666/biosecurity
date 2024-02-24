# biosecurity
COMP639 Studio Project – Semester 1 2024  Individual Assignment

1. [Database Design and Data Insertion](#database-design-and-data-insertion) 
## Database Design and Data Insertion 
### Database Design 
#### Concept Our database design includes the following features: 
- **Role Differentiation (Roles)**: The 'roles' table uses 'role_id' and 'role_name' to define different system roles like Agronomist, Staff, and Administrator. This design supports permission management, ensuring users access to the system at the appropriate level based on their role. 
- **User Table (Users)**: The 'users' table contains basic user information including username, hashed password, and contact information. The 'role_id' field acts as a foreign key, linking to the 'roles' table. This signifies that each user is assigned a specific role. 
- **Differentiating User Type**: The 'agronomists', 'staff', and 'administrators' tables further breakdown the user types. They each have a foreign key pointing to 'user_id' in the 'users' table, designating them as specific subsets of 'users'. This scheme allows for different user types to have additional specific information - for example, 'agronomists' can have 'address' information. 
- **Agriculture Project Table (Agriculture Items)**: The 'agriculture_items' table catalogues detailed information on agriculture projects such as the project type, common name, scientific name and descriptions of the biology, impacts, and control methods. 
- **Image Table (Images)**: The 'images' table is used to store images related to agriculture projects. It is connected to the 'agriculture_items' table via a foreign key, 'agriculture_id'. The 'is_primary' field is used to mark the main image, representing an important feature for front-end display. 
- **Data Integrity & Normalization**: The database uses foreign keys to assure reference integrity, ensuring that the logical relationship between the data is strictly maintained. By normalizing the information, we reduce data redundancy and improve data consistency. 
- **Scalability and Modularity**: The database design allows for the flexible addition of new roles and user types.
#### Software: I use Navicat database management software to create the database and tables and generate an ER diagram in "Database\Database.png". 
### Data Insertion 
I utilize Navicat database management software's data generation function to insert 'agronomists.address' data and all data for the 'users' table. 
To insert data in the 'agriculture_items' table and 'images' table, we employed the technique of "view page source code" on the data source website (https://agpest.co.nz/pest-directory/) to filter the needed text information and image paths and insert them into our created database.
