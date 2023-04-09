import { IconDashboard, IconSearch, IconActivityHeartbeat, IconMessageCircle } from '@tabler/icons';

const icons = { IconDashboard, IconSearch, IconActivityHeartbeat, IconMessageCircle };

const dashboard = {
    id: 'dashboard',
    title: 'Dashboard',
    type: 'group',
    children: [
        {
            id: 'default',
            title: 'Dashboard',
            type: 'item',
            url: '/dashboard/default',
            icon: icons.IconDashboard,
            breadcrumbs: false
        },
        {
            id: 'seo',
            title: 'SEO',
            type: 'collapse',
            icon: icons.IconSearch,
            children: [
                {
                    id: 'google_organic_serp',
                    title: 'Google Organic SERP',
                    type: 'item',
                    url: '/dashboard/google-organic-serp',
                    breadcrumbs: false
                },
                {
                    id: 'youtube_organic_serp',
                    title: 'YouTube Organic SERP',
                    type: 'item',
                    url: '/dashboard/youtube-organic-serp',
                    breadcrumbs: false
                },
                {
                    id: 'youtube_serp',
                    title: 'YouTube SERP',
                    type: 'item',
                    url: '/dashboard/youtube-serp',
                    breadcrumbs: false
                }
            ]
        }
    ]
};

export default dashboard;
