const GEMINI_API_KEY = 'AIzaSyAjpLBFY83INHJMqQUWO6gP_Ar9SIweu-U';
const GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent';

// Function to call Gemini API
async function callGeminiAPI(prompt) {
    try {
        const response = await fetch(GEMINI_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-goog-api-key': GEMINI_API_KEY
            },
            body: JSON.stringify({
                contents: [{
                    parts: [{
                        text: prompt
                    }]
                }]
            })
        });

        const data = await response.json();
        if (data.candidates && data.candidates[0] && data.candidates[0].content) {
            return data.candidates[0].content.parts[0].text;
        } else {
            throw new Error('Invalid response from Gemini API');
        }
    } catch (error) {
        console.error('Error calling Gemini API:', error);
        return null;
    }
}

// Function to get personalized advice
async function getPersonalizedAdvice() {
    const name = userData.name;
    const mood = userData.initialMood;
    const prompt = `As an empathetic AI counselor, provide a short, personalized message of hope and encouragement (max 3 sentences) for ${name} who is feeling ${mood}. The tone should be warm and supportive.`;
    
    const advice = await callGeminiAPI(prompt);
    if (advice) {
        document.getElementById('dailyQuote').textContent = advice;
        document.querySelector('.quote-author').textContent = '- AI Companion';
    }
}

// Function to generate personalized affirmation
async function generatePersonalizedAffirmation() {
    const name = userData.name;
    const mood = userData.initialMood;
    const recentMoods = userData.moodHistory.slice(-3);
    const avgMood = recentMoods.reduce((sum, m) => sum + m.level, 0) / (recentMoods.length || 1);
    
    let context = avgMood < 3 ? "struggling" : "making progress";
    
    const prompt = `Create a single-sentence personal affirmation for ${name} who is ${context} and initially felt ${mood}. Make it empowering and specific to their situation.`;
    
    const affirmation = await callGeminiAPI(prompt);
    if (affirmation) {
        document.getElementById('dailyAffirmation').textContent = affirmation;
    }
}

// Function to get AI response to mood change
async function getAIMoodResponse(moodLevel) {
    const prompt = `Give a short, one-sentence supportive response to someone who is feeling ${
        moodLevel === 1 ? 'very low' :
        moodLevel === 2 ? 'somewhat low' :
        moodLevel === 3 ? 'neutral' :
        moodLevel === 4 ? 'good' : 'excellent'
    }. Focus on validation and encouragement.`;
    
    const response = await callGeminiAPI(prompt);
    if (response) {
        document.getElementById('moodMessage').innerHTML = response;
    }
}

// Function to analyze gratitude entry
async function analyzeGratitudeEntry(text) {
    const prompt = `Analyze this gratitude entry: "${text}" and provide a single sentence of gentle encouragement that relates specifically to what they're grateful for.`;
    
    const analysis = await callGeminiAPI(prompt);
    if (analysis) {
        return analysis;
    }
    return "Thank you for sharing your gratitude. Every entry helps in your healing journey. 💫";
}
