import React, { useState, useEffect } from 'react';
import { 
  Search, 
  Bell, 
  Calendar, 
  ChevronDown, 
  MoreVertical, 
  ArrowUpRight, 
  ArrowDownRight, 
  Filter,
  Sparkles,
  Loader2,
  Wallet,
  Target,
  BarChart3,
  CreditCard
} from 'lucide-react';
import { 
  BarChart, 
  Bar, 
  XAxis, 
  YAxis, 
  Tooltip, 
  ResponsiveContainer, 
  PieChart, 
  Pie, 
  Cell 
} from 'recharts';
import { Transaction, Subscription, DashboardStats } from '../types';
import { getFinancialInsight } from '../services/geminiService';

// --- Mock Data ---
const monthlyData = [
  { name: 'Dec', value: 16000 },
  { name: 'Jan', value: 27000 },
  { name: 'Feb', value: 9000 },
  { name: 'Mar', value: 15000 },
  { name: 'Apr', value: 26000 },
  { name: 'May', value: 24000 },
];

const categoryData = [
  { name: 'Food', value: 6156, color: '#ffffff' },
  { name: 'Invest', value: 5000, color: '#a3a3a3' },
  { name: 'Shop', value: 4356, color: '#525252' },
  { name: 'Travel', value: 3670, color: '#262626' },
];

const transactions: Transaction[] = [
  { id: '1', amount: 2100.00, category: 'Shopping', subCategory: 'Amazon', date: '31 May 2025', mode: 'UPI' },
  { id: '2', amount: 299.00, category: 'Movie', subCategory: 'IMAX', date: '28 May 2025', mode: 'UPI' },
  { id: '3', amount: 5000.00, category: 'Investment', subCategory: 'Groww', date: '24 May 2025', mode: 'Bank' },
  { id: '4', amount: 2460.00, category: 'Travel', subCategory: 'Uber', date: '20 May 2025', mode: 'Card' },
  { id: '5', amount: 678.00, category: 'Food', subCategory: 'Swiggy', date: '15 May 2025', mode: 'UPI' },
];

const subscriptions: Subscription[] = [
  { id: '1', name: 'Netflix', date: '15 June 2025', amount: 149.00, icon: 'https://picsum.photos/40/40?random=1' },
  { id: '2', name: 'Spotify', date: '24 Aug 2025', amount: 49.00, icon: 'https://picsum.photos/40/40?random=2' },
  { id: '3', name: 'Figma', date: '01 Jan 2026', amount: 3999.00, icon: 'https://picsum.photos/40/40?random=3' },
];

const stats: DashboardStats = {
  balance: 898450.00,
  monthlyExpenses: 24093.00,
  investment: 145555.00,
  goal: 75000,
  goalTarget: 145000
};

export const Dashboard: React.FC = () => {
  const [insight, setInsight] = useState<string | null>(null);
  const [loadingInsight, setLoadingInsight] = useState(false);


  const handleGetInsight = async () => {
    setLoadingInsight(true);
    const text = await getFinancialInsight(stats, transactions);
    setInsight(text);
    setLoadingInsight(false);
  };

  return (
    <div className="flex-1 min-h-screen bg-background text-white md:ml-64 transition-all p-6 md:p-8">
      {/* Header */}
      <header className="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4">
        <div>
          <h1 className="text-2xl font-bold flex items-center gap-2">
            Hi, Alex <span className="text-xl animate-pulse">👋</span>
          </h1>
          <p className="text-secondary text-sm">Track all your expenses and transactions securely.</p>
        </div>

        <div className="flex items-center gap-4 w-full md:w-auto">
          <div className="hidden md:block text-xs text-secondary font-mono border border-border px-3 py-1.5 rounded-full">
            11:11 PM | 31 June 2025 | IN
          </div>
          <div className="relative flex-1 md:w-64">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-neutral-500 w-4 h-4" />
            <input 
              type="text" 
              placeholder="Search expenses..." 
              className="w-full bg-surface border border-border rounded-full py-2 pl-10 pr-4 text-sm focus:outline-none focus:border-white transition-colors placeholder-neutral-600"
            />
          </div>
          <button className="relative p-2 rounded-full border border-border hover:bg-surfaceHighlight transition-colors">
            <Bell size={18} />
            <span className="absolute top-1 right-1 w-2 h-2 bg-white rounded-full"></span>
          </button>
          <div className="w-10 h-10 rounded-full overflow-hidden border border-border">
            <img src="https://picsum.photos/100/100" alt="Profile" className="w-full h-full object-cover grayscale" />
          </div>
        </div>
      </header>

      {/* AI Insight Section */}
      <div className="mb-8">
        {!insight ? (
           <button 
             onClick={handleGetInsight} 
             disabled={loadingInsight}
             className="flex items-center gap-2 px-4 py-2 bg-surfaceHighlight border border-border hover:border-white/50 rounded-lg text-sm transition-all text-neutral-300"
           >
             {loadingInsight ? <Loader2 className="animate-spin w-4 h-4" /> : <Sparkles className="w-4 h-4 text-white" />}
             {loadingInsight ? 'Analyzing finances...' : 'Generate AI Financial Insight'}
           </button>
        ) : (
          <div className="bg-gradient-to-r from-neutral-900 to-black border border-neutral-800 p-4 rounded-lg flex items-start gap-3 animate-in fade-in slide-in-from-top-2 duration-500">
             <div className="bg-white text-black p-1.5 rounded-md mt-0.5">
               <Sparkles className="w-4 h-4" />
             </div>
             <div>
               <h4 className="text-sm font-semibold text-white mb-1">Gemini Insight</h4>
               <p className="text-sm text-neutral-400 leading-relaxed">{insight}</p>
             </div>
             <button onClick={() => setInsight(null)} className="ml-auto text-neutral-500 hover:text-white">
                <span className="sr-only">Dismiss</span>
                &times;
             </button>
          </div>
        )}
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 mb-8">
        <StatCard 
          title="Account Balance" 
          value={`$${stats.balance.toLocaleString()}`} 
          trend="+6% vs last month" 
          positive 
          icon={<Wallet className="text-neutral-400" />}
        />
        <StatCard 
          title="Monthly Expenses" 
          value={`$${stats.monthlyExpenses.toLocaleString()}`} 
          trend="-2% vs last month" 
          positive={false} 
          icon={<Calendar className="text-neutral-400" />}
        />
        <StatCard 
          title="Total Investment" 
          value={`$${stats.investment.toLocaleString()}`} 
          extraContent={
            <div className="h-10 w-24 ml-auto">
              <MiniChart />
            </div>
          }
        />
        <div className="bg-surface border border-border p-6 rounded-2xl flex flex-col justify-between relative overflow-hidden">
          <div className="flex justify-between items-start z-10">
            <div className="flex items-center gap-2 text-secondary text-sm">
              <Target size={16} />
              <span>Goal: iPhone 17 Pro</span>
            </div>
            <MoreVertical size={16} className="text-secondary cursor-pointer" />
          </div>
          
          <div className="flex items-center gap-4 mt-4 z-10">
            <div className="relative w-14 h-14">
              <svg className="w-full h-full -rotate-90" viewBox="0 0 36 36">
                <path className="text-neutral-800" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" strokeWidth="3" />
                <path className="text-white drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]" strokeDasharray={`${(stats.goal / stats.goalTarget) * 100}, 100`} d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" strokeWidth="3" />
              </svg>
            </div>
            <div>
              <p className="text-xs text-secondary">Target: ${stats.goalTarget.toLocaleString()}</p>
              <p className="font-bold text-lg">${stats.goal.toLocaleString()}</p>
            </div>
          </div>
           {/* Decorative background blur */}
           <div className="absolute -top-10 -right-10 w-32 h-32 bg-white/5 rounded-full blur-3xl"></div>
        </div>
      </div>

      {/* Charts Row */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        <div className="lg:col-span-2 bg-surface border border-border p-6 rounded-2xl">
          <div className="flex justify-between items-center mb-6">
            <div className="flex items-center gap-2">
              <div className="p-1.5 bg-neutral-800 rounded-md"><BarChart3 size={16} /></div>
              <h3 className="font-semibold">Monthly Expenses</h3>
            </div>
            <div className="flex items-center gap-2 text-xs text-secondary bg-surfaceHighlight px-2 py-1 rounded-md border border-border">
              <span>Recent</span>
              <ChevronDown size={14} />
            </div>
          </div>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={monthlyData} barSize={32}>
                <XAxis 
                  dataKey="name" 
                  axisLine={false} 
                  tickLine={false} 
                  tick={{ fill: '#737373', fontSize: 12 }} 
                  dy={10}
                />
                <YAxis hide />
                <Tooltip 
                  cursor={{ fill: 'rgba(255,255,255,0.05)' }}
                  contentStyle={{ backgroundColor: '#000', border: '1px solid #333', borderRadius: '8px' }}
                  itemStyle={{ color: '#fff' }}
                />
                <Bar 
                  dataKey="value" 
                  radius={[6, 6, 6, 6]}
                >
                  {monthlyData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.value > 25000 ? '#ffffff' : '#333333'} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="bg-surface border border-border p-6 rounded-2xl">
          <div className="flex justify-between items-center mb-4">
             <div className="flex items-center gap-2">
              <div className="p-1.5 bg-neutral-800 rounded-md"><PieChart size={16} /></div>
              <h3 className="font-semibold">Top Category</h3>
            </div>
            <MoreVertical size={16} className="text-secondary" />
          </div>
          <div className="h-48 w-full relative">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={categoryData}
                  innerRadius={55}
                  outerRadius={75}
                  paddingAngle={5}
                  dataKey="value"
                  stroke="none"
                >
                  {categoryData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip contentStyle={{ backgroundColor: '#000', border: '1px solid #333' }} itemStyle={{color: '#fff'}} />
              </PieChart>
            </ResponsiveContainer>
            {/* Center Text */}
            <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
              <span className="text-2xl font-bold">45%</span>
            </div>
          </div>
          <div className="mt-4 space-y-3">
             {categoryData.map((cat) => (
               <div key={cat.name} className="flex items-center justify-between text-sm">
                 <div className="flex items-center gap-2">
                   <div className="w-2 h-8 rounded-full" style={{ backgroundColor: cat.color }}></div>
                   <span className="text-neutral-300">{cat.name}</span>
                 </div>
                 <span className="font-medium">${cat.value.toFixed(2)}</span>
               </div>
             ))}
          </div>
        </div>
      </div>

      {/* Bottom Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Recent Expenses Table */}
        <div className="lg:col-span-2 bg-surface border border-border p-6 rounded-2xl">
          <div className="flex justify-between items-center mb-6">
             <div className="flex items-center gap-2">
              <div className="p-1.5 bg-neutral-800 rounded-md"><ArrowDownRight size={16} /></div>
              <h3 className="font-semibold">Recent Expenses</h3>
            </div>
            <div className="flex gap-2">
              <button className="flex items-center gap-1 text-xs text-secondary border border-border px-3 py-1.5 rounded-md hover:bg-surfaceHighlight">
                <Filter size={12} /> Filter
              </button>
              <button className="flex items-center gap-1 text-xs text-secondary border border-border px-3 py-1.5 rounded-md hover:bg-surfaceHighlight">
                Recent <ChevronDown size={12} />
              </button>
            </div>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full text-sm text-left">
              <thead>
                <tr className="text-secondary border-b border-neutral-800">
                  <th className="font-medium py-3 pl-2">S.N</th>
                  <th className="font-medium py-3">Amount</th>
                  <th className="font-medium py-3">Category</th>
                  <th className="font-medium py-3">Sub Category</th>
                  <th className="font-medium py-3">Date</th>
                  <th className="font-medium py-3 text-right pr-2">Mode</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-neutral-800">
                {transactions.map((t, idx) => (
                  <tr key={t.id} className="group hover:bg-white/5 transition-colors">
                    <td className="py-4 pl-2 text-secondary">{idx + 1}.</td>
                    <td className="py-4 font-bold">${t.amount.toFixed(2)}</td>
                    <td className="py-4 text-neutral-300">{t.category}</td>
                    <td className="py-4 text-secondary">{t.subCategory}</td>
                    <td className="py-4 text-secondary">{t.date}</td>
                    <td className="py-4 text-right pr-2">
                       <span className="inline-block px-2 py-1 bg-neutral-900 border border-neutral-700 rounded text-xs text-neutral-400">
                         {t.mode}
                       </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Subscriptions */}
        <div className="bg-surface border border-border p-6 rounded-2xl">
           <div className="flex justify-between items-center mb-6">
             <div className="flex items-center gap-2">
              <div className="p-1.5 bg-neutral-800 rounded-md"><CreditCard size={16} /></div>
              <h3 className="font-semibold">Bill & Subscription</h3>
            </div>
            <MoreVertical size={16} className="text-secondary cursor-pointer" />
          </div>
          <div className="space-y-4">
            {subscriptions.map((sub) => (
              <div key={sub.id} className="flex items-center justify-between p-3 rounded-xl border border-transparent hover:border-neutral-800 hover:bg-surfaceHighlight transition-all">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-neutral-800 overflow-hidden flex items-center justify-center border border-neutral-700">
                     {/* Placeholder icon since actual brand icons might break */}
                     <span className="text-xs font-bold">{sub.name.substring(0,2).toUpperCase()}</span>
                  </div>
                  <div>
                    <h4 className="font-medium text-sm">{sub.name}</h4>
                    <p className="text-xs text-secondary">{sub.date}</p>
                  </div>
                </div>
                <div className="font-semibold text-sm">${sub.amount.toFixed(2)}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// --- Helper Components ---

const StatCard: React.FC<{
  title: string;
  value: string;
  trend?: string;
  positive?: boolean;
  icon?: React.ReactNode;
  extraContent?: React.ReactNode;
}> = ({ title, value, trend, positive, icon, extraContent }) => {
  return (
    <div className="bg-surface border border-border p-6 rounded-2xl flex flex-col justify-between hover:border-neutral-600 transition-colors">
      <div className="flex justify-between items-start mb-4">
        <div className="flex items-center gap-2 text-secondary text-sm">
          {icon && icon}
          <span>{title}</span>
        </div>
        <MoreVertical size={16} className="text-secondary cursor-pointer" />
      </div>

      <div className="flex items-end justify-between">
        <div>
          <h2 className="text-2xl font-bold tracking-tight mb-2">{value}</h2>
          {trend && (
            <div className={`text-xs flex items-center gap-1 ${positive ? 'text-white' : 'text-neutral-500'}`}>
              {positive ? <ArrowUpRight size={12} /> : <ArrowDownRight size={12} />}
              <span className={positive ? "bg-white/10 px-1.5 py-0.5 rounded" : "bg-neutral-800 px-1.5 py-0.5 rounded"}>{trend}</span>
            </div>
          )}
        </div>
        {extraContent}
      </div>
    </div>
  );
};

const MiniChart = () => (
  <ResponsiveContainer width="100%" height="100%">
    <BarChart data={[{v:3},{v:5},{v:4},{v:8},{v:6},{v:9},{v:7}]}>
       <Bar dataKey="v" fill="#ffffff" radius={[2,2,2,2]} />
    </BarChart>
  </ResponsiveContainer>
);