import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Load Data
file_name = "EduPro_Data.xlsx" 

try:
    users_df = pd.read_excel(file_name, sheet_name="Users")
    courses_df = pd.read_excel(file_name, sheet_name="Courses")
    transactions_df = pd.read_excel(file_name, sheet_name="Transactions")
    print("Data loaded successfully! Engineering features...")
except Exception as e:
    print(f"Error loading data. Make sure {file_name} is an Excel file in this folder. Error: {e}")
    exit()

# Fix dates
transactions_df['TransactionDate'] = pd.to_datetime(transactions_df['TransactionDate'])

# 2. Feature Engineering
tx_course_df = pd.merge(transactions_df, courses_df, on="CourseID", how="left")
learner_features = []

for user_id, group in tx_course_df.groupby("UserID"):
    total_courses = group['CourseID'].nunique()
    
    if len(group) > 1:
        days_between = group['TransactionDate'].sort_values().diff().dt.days.dropna()
        enrollment_frequency = days_between.mean() if len(days_between) > 0 else 0
    else:
        enrollment_frequency = 0  
        
    preferred_category = group['CourseCategory'].mode()[0] if not group['CourseCategory'].empty else "Unknown"
    preferred_level = group['CourseLevel'].mode()[0] if not group['CourseLevel'].empty else "Unknown"
    
    learner_features.append({
        "UserID": user_id,
        "Total_Courses_Enrolled": total_courses,
        "Enrollment_Frequency_Days": enrollment_frequency,
        "Preferred_Category": preferred_category,
        "Preferred_Level": preferred_level,
        "Avg_Spending_Per_Learner": group['Amount'].mean(),
        "Diversity_Score": group['CourseCategory'].nunique(),
        "Learning_Depth_Index": group[group['CourseLevel'] == 'Beginner'].shape[0] / total_courses if total_courses > 0 else 0
    })

features_df = pd.DataFrame(learner_features)
final_profile_df = pd.merge(users_df, features_df, on="UserID", how="inner")

# 3. Clustering
print("Applying K-Means Clustering...")
numerical_cols = ['Age', 'Total_Courses_Enrolled', 'Enrollment_Frequency_Days', 'Avg_Spending_Per_Learner', 'Diversity_Score', 'Learning_Depth_Index']
encoded_df = pd.get_dummies(final_profile_df[numerical_cols + ['Gender', 'Preferred_Category', 'Preferred_Level']])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(encoded_df)

kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
final_profile_df['Assigned_Segment'] = kmeans.fit_transform(scaled_features).argmin(axis=1)

# 4. Save Output
final_profile_df.to_csv("edupro_segments.csv", index=False)
print("Pipeline complete! Saved segmented profiles to edupro_segments.csv")