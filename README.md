EduPro: Student Segmentation & Personalization Engine

🚀 Project OverviewThis project delivers a data-driven personalization engine for the EduPro online learning platform. By transitioning from a legacy, one-size-fits-all recommendation model to a student-centric intelligence framework, this system enables EduPro to deliver adaptive, meaningful, and engaging learning experiences.  The project was developed as part of a collaboration with Unified Mentor and Toronto Government Parks, Forestry & Recreation.  

🛠️ Key CapabilitiesIntelligent Segmentation: Utilizes unsupervised machine learning (K-Means Clustering) to group learners based on behavioral patterns rather than just raw demographic data.  Advanced Feature Engineering: Extracts deep insights from transactional data, including:Learning Depth Index: Categorizes users based on their progression from beginner to advanced content.  Diversity Score: Measures the breadth of domains explored by each learner.  Enrollment Frequency: Tracks behavioral loyalty and engagement cadence.  Interactive Analytics: A fully functional dashboard built with Streamlit, providing real-time segment visualization and path recommendations. 

🏗️ MethodologyLearner-Level Aggregation: Merged multi-dimensional datasets (Users, Courses, Transactions) to build holistic learner profiles.  Preprocessing: Standardized numerical features and encoded categorical data to ensure high-quality input for clustering.  Clustering: Implemented K-Means clustering, validated by the Silhouette Score to ensure optimal segment separation.  Personalized Logic: Applied rating-weighted relevance and cluster-based filtering to provide actionable course recommendations. 

📦 How to RunEnsure you have Python installed and the required libraries:Bash
# Install dependencies
pip install pandas numpy scikit-learn openpyxl streamlit plotly

# Run the ML pipeline to generate segments
python pipeline.py

# Launch the dashboard
streamlit run app.py

📊 Technical Stack
Languages: Python
ML Libraries: Scikit-learn (K-Means, StandardScaler)
Data Processing: Pandas, NumPy
Visualization: Streamlit, Plotly
Version Control: Git/GitHub

🎯 ImpactBy shifting focus from predicting course demand to understanding the unique learner journey, this engine helps EduPro improve learner engagement, increase course completion rates, and build long-term platform loyalty.  
Developed by Tanishq Ganesh Gawade
