import React from 'react';
import MainLayout from './layout/MainLayout';
import DashboardDefault from './views/dashboard/Default';

const App = () => {
  return (
    <MainLayout>
      <DashboardDefault />
    </MainLayout>
  );
};

export default App;
