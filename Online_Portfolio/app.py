from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    certificate_folders = [
        {
            'name': 'AI Bootcamp',
            'images': [
                'AI Essentials.jpg',
                'AI For Everyone.jpg',
                'AI Foundations Prompt Engineering with ChatGPT.jpg',
                'AI and Climate Change.jpg',
                'AI and Disaster Management.jpg',
                'AI and Public Health.jpg',
                'Artificial Intelligence on Microsoft Azure.jpg',
                'Building AI Powered Chatbots Without Programming.jpg',
                'Generative AI with Large Language Models.jpg',
                'Human Factors in AI.jpg',
                'Introduction to Artificial Intelligence (AI).jpg',
                'Introduction to Generative AI.jpg',
                'Introduction to Responsible AI.jpg',
                'Machine Learning Foundations for Product Managers.jpg',
                'Managing Machine Learning Projects.jpg',
                'Python for Data Science, AI & Development.jpg',
                'Supervised Machine Learning Regression and Classification.jpg',
                'Trustworthy AI Managing Bias, Ethics, and Accountability.jpg',
                'Unsupervised Learning, Recommenders, Reinforcement Learning.jpg'
            ],
            'badge': 'AI bootcamp completion badge.png'
        },
        {
            'name': 'Professional Development',
            'images': [
                'Active Listening Enhancing Communication Skills.jpg',
                'ChatGPT + Zapier Easy Inbox Intelligence for Smarter Email.jpg',
                'Customer Service Fundamentals.jpg',
                'Developing Interpersonal Skills.jpg',
                'Emotional Intelligence.jpg',
                'Grit and Growth Mindset.jpg',
                'Leading with Impact Team Dynamics, Strategy and Ethics.jpg',
                'Managing Conflicts with Cultural and Emotional Intelligence.jpg',
                'Negotiation skills Negotiate and resolve conflict.jpg',
                'Positive Psychology Resilience Skills.jpg',
                'Preparation for Job Interviews.jpg',
                'Psychology of the Self.jpg',
                'Solving Problems with Creative and Critical Thinking.jpg',
                'Verbal Communications and Presentation Skills.jpg',
                'Work Smarter, Not Harder Time Management for Personal & Professional Productivity.jpg',
                'Write Professional Emails in English.jpg'
            ],
            'badge': 'Professional Development completion badge.png'
        },
        {
            'name': 'Technical Support',
            'images': [
                'IT Security Defense against the digital dark arts.jpg',
                'Introduction to Hardware and Operating Systems.jpg',
                'Operating Systems and You Becoming a Power User.jpg',
                'Sound the Alarm Detection and Response.jpg',
                'System Administration and IT Infrastructure Services.jpg',
                'Technical Support (IT) Case Studies and Capstone.jpg',
                'Technical Support Fundamentals.jpg',
                'The Bits and Bytes of Computer Networking.jpg'
            ],
            'badge': 'Technical support completion badge.png'
        }
    ]
    
    return render_template('index.html', certificate_folders=certificate_folders, theme='cyberpunk-neon')

if __name__ == '__main__':
    app.run(debug=True)

