import pandas as pd

# Load all the CSV files
certifications_df = pd.read_csv('./data/linkedin_data/Certifications.csv')
education_df = pd.read_csv('./data/linkedin_data/Education.csv')
positions_df = pd.read_csv('./data/linkedin_data/Positions.csv')
profile_df = pd.read_csv('./data/linkedin_data/Profile.csv')
courses_df = pd.read_csv('./data/linkedin_data/Courses.csv')
projects_df = pd.read_csv('./data/linkedin_data/Projects.csv')
skills_df = pd.read_csv('./data/linkedin_data/Skills.csv')


# Function to write to a markdown file
def write_to_markdown():
    with open('profile_summary.md', 'w') as file:
        # Writing Profile Section
        file.write("# Profile Information\n")
        for first_name, last_name, summary, location, website in zip(profile_df['First Name'],
                                                                     profile_df['Last Name'],
                                                                     profile_df['Summary'],
                                                                     profile_df['Geo Location'],
                                                                     profile_df['Websites']):
            file.write(f"First Name: {profile_df['First Name'].values[0]}\n"
                       f"Last Name: {profile_df['Last Name'].values[0]}\n"
                       f"Location: {profile_df['Geo Location'].values[0]}\n"
                       f"Summary: {profile_df['Summary'].values[0]}\n"
                       f"Websites: {profile_df['Websites'].values[0]}\n"
                       
                       )
        
        # Writing Certifications Section
        file.write("\n## Certifications\n")
        for cert_name, institution, date in zip(certifications_df['Name'], 
                                                certifications_df['Authority'], 
                                                certifications_df['Started On']):
            file.write(f"- {cert_name} from {institution} (Issued on: {date})\n")
        
        # Writing Education Section
        file.write("\n## Education\n")
        for school, degree, field, start_date, grad_date in zip(education_df['School Name'], 
                                                    education_df['Degree Name'], 
                                                    education_df['Notes'], 
                                                    education_df['Start Date'],
                                                    education_df['End Date']):
            file.write(f"- {degree} in {field} from {school} (Start: {start_date}, Graduated: {grad_date})\n")
        
        # Writing Positions Section
        file.write("\n## Work Experience\n")
        for title, company, start, end, description in zip(positions_df['Title'], 
                                              positions_df['Company Name'], 
                                              positions_df['Started On'], 
                                              positions_df['Finished On'],
                                              positions_df['Description']):
            file.write(f"- {title} at {company} (From: {start} to {end} -- role info: {description})\n")
        
        # Writing Courses Section
        file.write("\n## Courses\n")
        for course in courses_df['Name']:
            file.write(f"- {course}\n")
        
        # Writing Projects Section
        file.write("\n## Projects\n")
        for project, description in zip(projects_df['Title'], projects_df['Description']):
            file.write(f"- {project}: {description}\n")
        
        # Writing Skills Section
        file.write("\n## Skills\n")
        for skill in skills_df['Name']:
            file.write(f"- {skill}\n")

# Call the function to write the markdown file
write_to_markdown()

print("Markdown file 'profile_summary.md' created successfully.")