Shaun's Interactive Terminal Portfolio
A comprehensive terminal-based portfolio
"""

import random
import sys
import time
from typing import List, Dict
import argparse
from datetime import datetime

class ShaunPortfolio:
    def __init__(self):
        self.commands = {
            'intro': self.intro,
            'about': self.about,
            'timeline': self.timeline,
            'skills': self.skills,
            'projects': self.projects,
            'design': self.design_showcase,
            'investments': self.investments,
            'hobbies': self.hobbies,
            'contact': self.contact,
            'jokes': self.jokes,
            'philosophy': self.philosophy,
            'help': self.help,
            'exit': self.exit_app
        }
        
        self.jokes_db = {
            'dark': [
                "My investment portfolio is like my neural networks - promising backtests, questionable live performance.",
                "I built an AI that predicts market crashes... it's been predicting one every day for 2 years. One day it'll be right.",
                "My code debugging skills are like my stock picks - eventually I find the bug, but not before losing sleep.",
                "Why do I love XAI? Because unlike my investment decisions, at least I can explain why the AI is wrong."
            ],
            'dad': [
                "Why don't data scientists invest in crypto? Because they know the difference between correlation and causation!",
                "I told my YOLO model a joke about object detection... it saw right through it!",
                "What's the difference between my Python code and my investment returns? My code actually executes properly.",
                "Why did the data scientist become a day trader? He wanted his losses to be statistically significant!"
            ],
            'tech': [
                "My multi-modal AI is like a good investment portfolio - diversified, occasionally brilliant, and requires constant monitoring.",
                "I built a social automation bot so advanced, it started giving me investment advice. I'm still debugging that feature.",
                "Why use YOLO for object detection? Because YOLO is also my investment strategy!",
                "My XAI classifier is so explainable, it writes better documentation than I do."
            ],
            'personal': [
                "I analyze penny stocks like Kendrick analyzes beats - looking for patterns others miss.",
                "My design process is like Travis Scott's production - layer everything until it sounds (looks) perfect.",
                "I debug code to NF, trade stocks to Drake, and design UI to Eminem. Productivity through mood matching.",
                "Asked my AI debate platform about MX5 vs R15. It's been arguing for 3 hours. Some questions have no right answers."
            ]
        }

    def ascii_art_header(self):
        return """
╔═══════════════════════════════════════════════════════════════════╗
║  ███████╗██╗  ██╗ █████╗ ██╗   ██╗███╗   ██╗                    ║
║  ██╔════╝██║  ██║██╔══██╗██║   ██║████╗  ██║                    ║
║  ███████╗███████║███████║██║   ██║██╔██╗ ██║                    ║
║  ╚════██║██╔══██║██╔══██║██║   ██║██║╚██╗██║                    ║
║  ███████║██║  ██║██║  ██║╚██████╔╝██║ ╚████║                    ║
║  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                    ║
║                                                                   ║
║         Data Scientist • AI Builder • Strategic Investor         ║
╚═══════════════════════════════════════════════════════════════════╝
        """

    def intro(self):
        """Enhanced introduction with ASCII art"""
        print(self.ascii_art_header())
        intro_text = """
🎯 THE ELEVATOR PITCH:
Data Science graduate who self-taught everything from Python to portfolio management
during college (2nd semester → graduation). I build AI solutions, run SAAS ventures, 
and strategically invest - all while designing the UI/UX for my own products.

⚡ CURRENT PROJECTS:
• Multi-Modal AI Debate Platform (Reinforcement Learning visualization)
• This terminal portfolio package (you're experiencing it!)
• Active investment portfolio management

💡 THE UNIQUE MIX:
Technical depth + Business strategy + Design sensibility + Financial literacy
= Solutions that actually ship AND make money

🎵 POWERED BY: Kendrick for strategy, NF for focus, Eminem for precision

Type 'timeline' for the full journey or 'help' to explore specific areas!
        """
        print(intro_text)

    def timeline(self):
        """Visual timeline of journey"""
        timeline_text = """
📈 THE JOURNEY TIMELINE:

🎓 COLLEGE ERA (Self-taught Revolution):
├─ 2nd Semester: Started Python, fell down the rabbit hole
├─ Mid-College: Data Analysis mastery (SQL, Power BI, SPSS)
├─ Final Year: Built CSR Scholarship Aggregator (first SAAS)
└─ Graduation: Data Science degree + arsenal of self-taught skills

🚀 PROJECT EVOLUTION:
├─ XAI Object Classifier (YOLO-based, no model training)
├─ Social Interactivity Automation Bot  
├─ Market Basket Analysis & Inventory Systems
├─ Multi-Modal AI Assistant
├─ Bulk Email Automation (SMTP mastery)
└─ Game Development experiments (GDevelop)

💼 BUSINESS VENTURES:
├─ Ed-tech SAAS platform
├─ Gaming industry solutions  
├─ Product businesses: Sanitaryware, Skincare, Board Games, Clothing
└─ Supply chain & logistics management experience

🎨 DESIGN MASTERY:
├─ Graphic Design & 2D Animation
├─ UI/UX for own products
├─ Motion Design (currently learning)
└─ Frontend development

📊 CURRENT FOCUS (2024-2025):
├─ Multi-Modal AI Debate Platform (4 models, @ chat interface)
├─ Investment Portfolio (Penny stocks + SIPs + Index funds)
├─ This Terminal Portfolio Package
└─ Next venture planning

The pattern? Start curious, learn obsessively, build relentlessly, profit strategically.
        """
        print(timeline_text)

    def skills(self):
        """Comprehensive skills breakdown"""
        skills_text = """
🛠️ TECHNICAL STACK:

💻 Programming & AI/ML:
├── Python (Expert) - 4+ years, production-level
├── Data Analysis: Power BI, Excel, SPSS, SQL
├── AI/ML: Multi-modal systems, XAI, YOLO integration  
├── Automation: Social bots, Email systems (SMTP)
└── Game Dev: GDevelop (hobby level)

📊 Data Specializations:
├── Finance Analytics (market analysis, portfolio optimization)
├── Health-tech Data (compliance, outcome prediction)
├── Market Basket Analysis & Customer Segmentation
└── Inventory & Supply Chain Analytics

🎨 Design & Frontend:
├── Graphic Design (Brand identity, marketing materials)
├── 2D Animation (Product demos, explainer content)
├── UI/UX Design (Mobile & web applications)
├── Motion Design (Learning - After Effects workflow)
└── Frontend Development (React, responsive design)

💰 Business & Finance:
├── SAAS Development & Go-to-market
├── Investment Analysis (Technical + Fundamental)
├── Supply Chain Management (Physical products)
├── Organizational Management (Team coordination)
└── Strategic Planning (Market entry, scaling)

🔧 SPECIALITY: Building complete solutions - from initial data analysis 
             through AI implementation, UI design, and business deployment.
        """
        print(skills_text)

    def projects(self):
        """Detailed project showcase"""
        projects_text = """
🚀 PROJECT PORTFOLIO:

🤖 Multi-Modal AI Debate Platform [ACTIVE]
   • 4 AI models collaborating via @ chat interface
   • Reinforcement Learning visualization layer
   • Multi-domain brainstorming through model debate
   • Tech: Python, OpenAI API, Custom UI, Whiteboard interface
   • Status: 2-model capacity, scaling to 4

🔍 XAI Object Classifier [COMPLETED]
   • Explainable AI without custom model training
   • YOLO integration for transparent detection
   • Built for interpretability from day one
   • Impact: Deployed in health-tech compliance system

🎯 Social Interactivity Automation Bot [COMPLETED]
   • Multi-platform engagement automation
   • Intelligent content scheduling and responses
   • Custom analytics dashboard
   • Results: 3x engagement rates across client accounts

📊 SAAS Portfolio:
   ├── CSR Scholarship Aggregator (Ed-tech)
   ├── Inventory Analysis System (Manufacturing)
   ├── Market Basket Analyzer (Retail optimization)
   └── Current: Multi-modal AI platform

🛠️ Automation Suite:
   ├── Bulk Email System (SMTP optimization)
   ├── Social Media Management
   └── Data Pipeline Automation

🎮 Creative Projects:
   ├── Game Development (GDevelop experiments)
   ├── 2D Animation for product demos
   └── UI/UX for all personal ventures

💡 BUILD PHILOSOPHY: "Start with real problems, build elegant solutions, 
                     ship fast, scale smart, profit sustainably."
        """
        print(projects_text)

    def design_showcase(self):
        """Showcase design work through ASCII and descriptions"""
        design_text = """
🎨 DESIGN PORTFOLIO:

┌─────────────────────────────────────────────────────────────────┐
│  GRAPHIC DESIGN SHOWCASE                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ██████╗ ██████╗  █████╗ ███╗   ██╗██████╗                     │
│  ██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗                    │  
│  ██████╔╝██████╔╝███████║██╔██╗ ██║██║  ██║                    │
│  ██╔══██╗██╔══██╗██╔══██║██║╚██╗██║██║  ██║                    │
│  ██████╔╝██║  ██║██║  ██║██║ ╚████║██████╔╝                    │
│  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝                     │
│                                                                 │
│  Identity Design • Marketing Materials • Product Visuals       │
└─────────────────────────────────────────────────────────────────┘

🎯 UI/UX PROJECTS:
┌──────────┬──────────┬──────────┬──────────┐
│ [ Home ] │ [  Data  ] │ [ AI Hub ] │ [Contact]│  ← Multi-Modal AI Interface
├──────────┴──────────┴──────────┴──────────┤
│  ┌─────────────────────────────────────┐   │
│  │ @GPT4: Analyze this dataset         │   │
│  │ @Claude: Counter-argument needed    │   │  ← Chat Interface Design
│  │ @Gemini: Visual representation?     │   │
│  │ @Local: Privacy-first analysis     │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘

📱 MOBILE-FIRST APPROACH:
• Responsive design across all projects
• Touch-optimized interactions
• Progressive enhancement strategy

🎬 ANIMATION & MOTION:
• 2D explainer videos for SAAS products  
• Micro-interactions in UI elements
• Loading animations and transitions
• Currently learning After Effects workflow

🎨 DESIGN PHILOSOPHY:
"Form follows function, but personality makes it memorable. 
 Every pixel should serve the user's goal while reflecting the brand's soul."

💡 TOOLS: Figma, Adobe Creative Suite, Canva Pro, Custom CSS animations
        """
        print(design_text)

    def investments(self):
        """Investment portfolio showcase (humble approach)"""
        investments_text = """
📊 INVESTMENT STRATEGY:

💡 PHILOSOPHY:
"Diversified learning portfolio - each investment teaches something new
while building long-term wealth. Data-driven decisions, emotion-controlled execution."

🎯 CURRENT ALLOCATION:

├── 📈 Growth Stocks (35%)
│   • Penny stocks (high-risk research plays)
│   • Small-cap tech companies
│   • Emerging market opportunities
│   
├── 💰 Income Generation (25%)
│   • Dividend-paying blue chips
│   • REIT exposure for real estate
│   • Utility stocks for stability
│   
├── 🔄 Systematic Investment (25%)
│   • SIP in diversified mutual funds
│   • Index fund core holdings
│   • Dollar-cost averaging approach
│   
└── 🛡️ Risk Management (15%)
│   • Low-volatility index funds
│   • Government securities
│   • Emergency liquidity buffer

📊 NOTABLE MOVES:
• Successfully exited position in [Tech Stock] - 40% return in 6 months
• Identified undervalued fintech penny stock - 25% gain
• SIP strategy showing consistent 12% CAGR over 2+ years

🧠 ANALYTICAL APPROACH:
├── Technical analysis using Python scripts
├── Fundamental research through financial statements  
├── Sector rotation based on economic indicators
└── Risk assessment using portfolio correlation analysis

⚠️ DISCLAIMER: This is educational sharing, not investment advice. 
              Do your own research and consult financial advisors.

🎯 GOAL: Financial freedom through disciplined, data-informed investing
        while funding innovation projects and personal growth.
        """
        print(investments_text)

    def hobbies(self):
        """Personal interests and cultural tastes"""
        hobbies_text = """
🎵 SOUNDTRACK TO SUCCESS:

🎤 CURRENT ROTATION:
├── Kendrick Lamar: "Mr. Morale & The Big Steppers" 
│   → Strategy sessions and deep work
├── NF: "Hope" 
│   → Coding marathons and problem-solving  
├── Eminem: "The Eminem Show"
│   → Debugging and precision tasks
├── J. Cole: "The Off-Season"
│   → Business planning and reflection
├── Drake: "Dark Lane Demo Tapes" 
│   → Design work and creative flow
├── Central Cee: "Wild West"
│   → Market analysis and trading
├── Travis Scott: "Utopia"
│   → UI/UX design and creative projects
└── Playboi Carti: "Whole Lotta Red"
   → Late night coding sessions

🏀 ACTIVE INTERESTS:
├── Basketball: Analytics meets athleticism
│   • Follow NBA advanced statistics
│   • Local pickup games for cardio
│   
├── Gaming: Strategy and mechanics analysis
│   • Game development insights
│   • UI/UX inspiration from game design
│   
└── Automotive Appreciation:
   • Dream garage: Mazda MX5, AMG series
   • Motorcycles: R15, Bullet 350, Harley Sportster/48
   • Engineering and design fascination

🎬 CINEMA INFLUENCES:
├── "Wolf of Wall Street" - Market psychology
├── "Goodfellas" - Strategic thinking  
├── "The Bronx Tale" - Leadership lessons
├── "Bolt" - Never give up attitude
├── "Soul" - Purpose and passion alignment
└── Many more... (I'm a movie data point collector)

💭 WHY SHARE THIS?
Because the best solutions come from diverse inputs. Music shapes my coding rhythm,
basketball teaches team coordination, movies provide narrative frameworks,
and automotive design inspires UI elegance.

🎯 INTEGRATION: Every hobby feeds back into work - pattern recognition,
               strategic thinking, aesthetic sense, and storytelling ability.
        """
        print(hobbies_text)

    def jokes(self):
        """Enhanced joke system with personal category"""
        print("\n🎭 JOKE ARSENAL:")
        print("1. Dark & Data-Driven")
        print("2. Dad Jokes (Tech Edition)")  
        print("3. Pure Tech Humor")
        print("4. Personal Life Meets Tech")
        print("5. Surprise Me!")
        
        try:
            choice = input("\nPick your poison (1-5): ").strip()
            
            joke_map = {
                '1': 'dark',
                '2': 'dad', 
                '3': 'tech',
                '4': 'personal',
                '5': random.choice(['dark', 'dad', 'tech', 'personal'])
            }
            
            category = joke_map.get(choice, 'tech')
            joke = random.choice(self.jokes_db[category])
            
            print(f"\n😄 {joke}")
            print("\n" + "="*70)
            
        except KeyboardInterrupt:
            print("\n\nExiting joke mode... back to serious business! 😅")

    def philosophy(self):
        """Updated philosophy with investment mindset"""
        philosophy_text = """
🧠 THE SHAUN OPERATING SYSTEM:

💡 ON BUILDING:
   "Every line of code should solve a real problem. Every design choice  
    should serve the user. Every business decision should create value.
    If it doesn't do at least one of these, delete it."

🎯 ON STRATEGY:
   "Think in systems, execute in sprints. Whether it's code, investments,
    or ventures - compound growth beats heroic efforts every time."

💰 ON WEALTH:
   "Money is freedom to take bigger creative risks. Invest in assets
    that appreciate while you sleep, build products that scale without you,
    develop skills that compound over time."

🎨 ON DESIGN:
   "Beautiful interfaces aren't decoration - they're respect for the user's
    time and intelligence. Make complex things simple, not simple things complex."

⚡ ON EXECUTION:
   "MVP fast, iterate faster, but never ship broken. Your reputation
    is your most valuable asset - protect it with quality."

📊 ON DATA:
   "Let data inform decisions, not make them. Numbers tell you what happened,
    creativity tells you what's possible, wisdom tells you what to do next."

🎵 ON BALANCE:
   "Kendrick for vision, Eminem for precision, NF for persistence.
    Good music makes good code. Good code makes good money. Good money makes good options."

🏀 ON COMPETITION:
   "Play your own game, but study everyone else's. In basketball and business,
    the best defense is anticipating the other player's next move."

🚗 ON DREAMS:
   "Work toward both the MX5 and the farm. The garage and the garden.
    The CEO suite and the creative studio. Why choose when you can build toward both?"
        """
        print(philosophy_text)

    def contact(self):
        """Updated contact with investment discussion option"""
        contact_text = """
📬 LET'S CONNECT:

🎯 BEST CONVERSATIONS ABOUT:
├── AI/ML implementation challenges
├── SAAS product strategy and scaling
├── Investment analysis and portfolio theory
├── UI/UX for technical products
├── Data science in business contexts
└── Building sustainable tech ventures

💬 CONVERSATION STARTERS:
   • "I'm stuck on this AI problem..."
   • "What's your take on [current tech trend]?"  
   • "Can we discuss investment strategies?"
   • "How do you balance technical depth with business needs?"
   • "Want to collaborate on something interesting?"

📊 INVESTMENT DISCUSSIONS:
   Happy to discuss portfolio strategies, market analysis techniques,
   or data-driven investment approaches. Always learning from other perspectives.

🤝 NETWORKING PHILOSOPHY:
   Quality over quantity. Depth over breadth. Value creation over value extraction.
   I prefer solving interesting problems together over small talk.

⚡ RESPONSE STYLE:
   • Technical questions: Lightning fast
   • Business opportunities: Thoughtful and thorough  
   • Investment discussions: Data-backed opinions
   • Design challenges: Creative and practical solutions

🎵 INSIDER TIP: 
   Reference Kendrick, mention MX5s, or lead with a genuine technical 
   challenge. These get priority in my inbox.

📧 REACH OUT: [Your contact method here]
   LinkedIn: [Your LinkedIn]
   GitHub: [Your GitHub] 
   
💡 REMEMBER: Best partnerships start with good problems, not good pitches.
        """
        print(contact_text)

    def help(self):
        """Updated help menu with new sections"""
        help_text = """
🎮 NAVIGATION MENU:

📊 CORE PORTFOLIO:
   • intro       - Quick overview and current status
   • timeline    - Visual journey from college to now
   • skills      - Technical stack and expertise areas
   • projects    - Detailed project portfolio
   • about       - Full background story

🎨 SHOWCASE SECTIONS:
   • design      - UI/UX and graphic design portfolio
   • investments - Investment strategy and portfolio (educational)
   • hobbies     - Music, sports, movies, and personal interests

🎭 INTERACTIVE FEATURES:  
   • jokes       - 4 categories: dark, dad, tech, personal
   • philosophy  - Operating principles and approach
   • contact     - How to connect and collaborate

⚙️ SYSTEM COMMANDS:
   • help        - This navigation menu
   • exit        - Leave the experience

🚀 PRO TIPS:
   • Try 'jokes' → option 4 for personal tech humor
   • 'timeline' gives the complete journey overview
   • 'design' showcases visual work through ASCII art
   • 'investments' shares strategy (educational purposes)

🎯 QUICK ACCESS ALIASES:
   "U got jokes?" → jokes menu
   "show me work" → projects
   "what's your story" → timeline

Ready to explore? Pick any section that interests you!
        """
        print(help_text)

    def about(self):
        """Comprehensive about section"""
        about_text = """
🧬 THE COMPLETE STORY:

🎓 EDUCATIONAL FOUNDATION:
Data Science degree, but the real education happened through curiosity-driven
self-learning from 2nd semester through graduation. Every skill beyond
data science core came from personal interest and obsessive exploration.

⚡ THE LEARNING JOURNEY:
Started with Python in college, fell into the rabbit hole of possibilities.
Each project taught something new: automation led to business understanding,
AI work led to design thinking, personal projects led to investment insights.

🎯 CURRENT REALITY:
├── Technical: Multi-modal AI systems, XAI, full-stack development
├── Business: SAAS ventures, product management, supply chain experience  
├── Financial: Active investor with data-driven approach
├── Creative: Graphic design, UI/UX, 2D animation
└── Personal: Music-driven productivity, automotive enthusiast, movie collector

🚀 THE MINDSET EVOLUTION:
• College: "I want to learn everything"
• Early career: "I want to build everything"  
• Now: "I want to build the right things that compound"

💡 THE INTEGRATION:
Every skill reinforces others. Design improves user experience. 
Financial knowledge drives sustainable business decisions.
Technical depth enables creative solutions. Music shapes work rhythm.

🎵 PRODUCTIVITY SYSTEM:
Different music for different tasks. Kendrick for strategy, Eminem for 
precision, NF for focus. The right soundtrack makes complex work flow.

🏀 COMPETITIVE EDGE:
Basketball taught team dynamics. Gaming taught systems thinking.
Movies taught storytelling. Cars taught engineering aesthetics.
All of this feeds into better products and solutions.

🎯 WHAT'S NEXT:
Building the multi-modal AI platform while growing investment portfolio.
Always learning, always building, always improving the system.
        """
        print(about_text)

    def exit_app(self):
        """Enhanced exit with random farewell"""
        farewell_messages = [
            "🚀 Keep building the future!",
            "⚡ Until next time, stay innovative!", 
            "🎯 Go create something that compounds!",
            "💻 Happy coding, fellow builder!",
            "📊 May your returns be positive and your code bug-free!",
            "🎵 Keep grinding to the right soundtrack!"
        ]
        print(f"\n{random.choice(farewell_messages)}")
        print("🤝 Thanks for exploring Shaun's terminal universe!")
        print("💡 Remember: Build in silence, let success make the noise.")
        sys.exit(0)

    def run_interactive(self):
        """Main interactive loop with enhanced greeting"""
        greetings = [
            "🚀 Welcome to Shaun's digital universe!",
            "💻 Hey there, fellow builder and strategist!",
            "⚡ Ready to explore code, investments, and creativity?",
            "🎯 What aspect of the journey interests you today?"
        ]
        
        print(random.choice(greetings))
        print("\n💡 Start with 'intro' for overview or 'timeline' for the full journey")
        print("🎭 Try 'jokes' for laughs or 'help' for navigation")
        print("=" * 70)
        
        while True:
            try:
                command = input("\n🎯 What interests you? > ").strip().lower()
                
                # Command aliases
                aliases = {
                    'joke': 'jokes', 'u got jokes?': 'jokes', 'u got jokes': 'jokes',
                    'quit': 'exit', 'bye': 'exit', 'goodbye': 'exit',
                    'info': 'about', 'story': 'timeline', 'journey': 'timeline',
                    'portfolio': 'projects', 'work': 'projects',
                    'tech': 'skills', 'abilities': 'skills',
                    'reach': 'contact', 'connect': 'contact',
                    'money': 'investments', 'stocks': 'investments',
                    'music': 'hobbies', 'personal': 'hobbies',
                    'visual': 'design', 'ui': 'design'
                }
                
                command = aliases.get(command, command)
                
                if command in self.commands:
                    print("\n" + "=" * 70)
                    self.commands[command]()
                    print("=" * 70)
                elif command == '':
                    continue
                else:
                    suggestions = [k for k in self.commands.keys() if command in k or k in command]
                    if suggestions:
                        print(f"\n🤔 Did you mean: {', '.join(suggestions)}?")
                    else:
                        print("\n🤷 Not sure what you're looking for. Type 'help' to see all options!")
                        
            except KeyboardInterrupt:
                print("\n\n🚀 Use 'exit' for a proper goodbye! 😉")
                break
            except EOFError:
                print("\n\n👋 Thanks for visiting!")
                break

def main():
    """Entry point"""
    parser = argparse.ArgumentParser(description="Shaun's Interactive Portfolio")
    parser.add_argument('--version', action='version', version='shaun-portfolio 1.2.0')
    args = parser.parse_args()
    
    portfolio = ShaunPortfolio()
    portfolio.run_interactive()

if __name__ == "__main__":
    main()
