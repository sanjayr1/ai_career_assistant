import os
from crewai import Crew
from agents import researcher, profiler, resume_strategist, interview_preparer
from tasks import research_task, profile_task, resume_strategy_task, interview_preparation_task
from utils import get_openai_api_key, get_serper_api_key

# Warning control
import warnings
warnings.filterwarnings('ignore')

# Setting up environment variables for OpenAI and Serper API keys
openai_api_key = get_openai_api_key()

# TODO need to use free llama 11B model since i've downloaded it, or pass in model separately

#os.environ["OPENAI_MODEL_NAME"] = 'o1-preview'
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

# Create the Crew
job_application_crew = Crew(
    agents=[researcher, profiler, resume_strategist, interview_preparer],
    tasks=[research_task, profile_task, resume_strategy_task, interview_preparation_task],
    verbose=True
)

#TODO: pass in inputs separately
# Define inputs
job_application_inputs = {
    'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
    'github_url': 'https://github.com/joaomdmoura',
    'personal_writeup': """Noah is an accomplished Software Engineering Leader with 18 years of experience..."""
}

# Run the crew
result = job_application_crew.kickoff(inputs=job_application_inputs)