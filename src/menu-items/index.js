import React from 'react';
import DashboardIcon from '@mui/icons-material/Dashboard';

const menuItems = {
    items: [
        {
            id: 'dashboard',
            title: 'Dashboard',
            type: 'group',
            children: [
                {
                    id: 'default',
                    title: 'Default',
                    type: 'item',
                    url: '/dashboard/default',
                    icon: <DashboardIcon />,
                    breadcrumbs: false
                }
            ]
        }
    ]
};

export default menuItems;
