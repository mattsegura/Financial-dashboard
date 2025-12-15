import React from 'react';
import { 
  LayoutDashboard, 
  Receipt, 
  CreditCard, 
  Wallet, 
  Target, 
  BarChart3, 
  PieChart, 
  Settings, 
  HelpCircle, 
  LogOut, 
  Gem,
  Headphones
} from 'lucide-react';

export const Sidebar: React.FC = () => {
  return (
    <aside className="fixed left-0 top-0 h-full w-64 bg-surface border-r border-border hidden md:flex flex-col justify-between z-20">
      <div className="p-6">
        <div className="flex items-center gap-2 mb-10">
          <div className="w-8 h-8 bg-white rounded flex items-center justify-center">
            <span className="text-black font-bold text-xl">N</span>
          </div>
          <span className="text-xl font-bold tracking-tight text-white">NOIR<span className="font-light text-secondary">FLOW</span></span>
        </div>

        <div className="space-y-8">
          <div>
            <h3 className="text-xs font-semibold text-secondary uppercase tracking-wider mb-4 px-2">General</h3>
            <nav className="space-y-1">
              <NavItem icon={<LayoutDashboard size={20} />} label="Dashboard" active />
              <NavItem icon={<Receipt size={20} />} label="All Expenses" />
              <NavItem icon={<CreditCard size={20} />} label="Bill & Subscription" />
              <NavItem icon={<Wallet size={20} />} label="Investment" />
              <NavItem icon={<Target size={20} />} label="Goals" />
            </nav>
          </div>

          <div>
            <h3 className="text-xs font-semibold text-secondary uppercase tracking-wider mb-4 px-2">Tools</h3>
            <nav className="space-y-1">
              <NavItem icon={<BarChart3 size={20} />} label="Insight" />
              <NavItem icon={<PieChart size={20} />} label="Analytics" />
            </nav>
          </div>
        </div>
      </div>

      <div className="p-6 space-y-6">
        <div className="bg-gradient-to-br from-neutral-800 to-black p-4 rounded-xl border border-neutral-700 relative overflow-hidden group cursor-pointer hover:border-neutral-500 transition-colors">
            <div className="relative z-10">
                <div className="flex items-center gap-2 mb-2 text-white">
                    <Gem size={18} />
                    <span className="font-semibold">Upgrade to PRO</span>
                </div>
                <p className="text-xs text-secondary">Unlock advanced AI insights and unlimited tracking.</p>
            </div>
            <div className="absolute -bottom-4 -right-4 w-20 h-20 bg-white/10 rounded-full blur-xl group-hover:bg-white/20 transition-all"></div>
        </div>

        <nav className="space-y-1">
            <NavItem icon={<Settings size={20} />} label="Setting" />
            <NavItem icon={<HelpCircle size={20} />} label="Help Center" />
            <NavItem icon={<LogOut size={20} />} label="Logout" />
        </nav>
      </div>
    </aside>
  );
};

interface NavItemProps {
  icon: React.ReactNode;
  label: string;
  active?: boolean;
}

const NavItem: React.FC<NavItemProps> = ({ icon, label, active }) => {
  return (
    <a 
      href="#" 
      className={`
        flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all duration-200 group
        ${active 
          ? 'bg-white text-black font-medium shadow-lg shadow-white/10' 
          : 'text-secondary hover:text-white hover:bg-white/5'
        }
      `}
    >
      <span className={active ? 'text-black' : 'text-neutral-400 group-hover:text-white transition-colors'}>
        {icon}
      </span>
      <span>{label}</span>
    </a>
  );
};