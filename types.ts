export interface Transaction {
  id: string;
  amount: number;
  category: string;
  subCategory: string;
  date: string;
  mode: 'UPI' | 'Card' | 'Bank' | 'Cash';
  icon?: string;
}

export interface Subscription {
  id: string;
  name: string;
  date: string;
  amount: number;
  icon: string; // URL to icon
}

export interface ChartDataPoint {
  name: string;
  value: number;
  amt?: number;
}

export interface DashboardStats {
  balance: number;
  monthlyExpenses: number;
  investment: number;
  goal: number;
  goalTarget: number;
}

export enum TimeRange {
  Weekly = "Weekly",
  Monthly = "Monthly",
  Yearly = "Yearly"
}