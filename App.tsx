import React from 'react';
import { Sidebar } from './components/Sidebar';
import { Dashboard } from './components/Dashboard';

function App() {
  return (
    <div className="flex bg-background min-h-screen text-white font-sans selection:bg-white selection:text-black">
      <Sidebar />
      <Dashboard />
    </div>
  );
}

export default App;
