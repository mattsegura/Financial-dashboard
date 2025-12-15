import { GoogleGenAI } from "@google/genai";
import { Transaction, DashboardStats } from '../types';

const apiKey = process.env.API_KEY || '';
const ai = new GoogleGenAI({ apiKey });

export const getFinancialInsight = async (
  stats: DashboardStats, 
  recentTransactions: Transaction[]
): Promise<string> => {
  if (!apiKey) {
    return "Gemini API Key is missing. Please configure it to receive AI insights.";
  }

  try {
    const prompt = `
      You are a sophisticated financial advisor. Analyze the following financial snapshot concisely (max 2 sentences).
      Be witty but professional. Focus on spending habits or goal progress.
      
      Stats:
      Current Balance: ${stats.balance}
      Monthly Expenses: ${stats.monthlyExpenses}
      Investments: ${stats.investment}
      Goal Progress: ${stats.goal} / ${stats.goalTarget}

      Recent Transactions:
      ${JSON.stringify(recentTransactions.slice(0, 5))}
    `;

    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: prompt,
    });

    return response.text || "Unable to generate insight at this time.";
  } catch (error) {
    console.error("Error fetching Gemini insight:", error);
    return "Thinking process interrupted. Please try again later.";
  }
};