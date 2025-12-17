// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Bridging the gap between digital AI and physical robots',
  favicon: '/img/favicon.ico',

  url: 'https://physical-ai-lab.org',
  baseUrl: '/',
  organizationName: 'physical-ai-lab',
  projectName: 'physical-ai-humanoid-robotics-book',

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/AyyanAli-Khan/Physical-AI-Humanoid-Robotics-Book',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Physical AI & Humanoid Robotics',
        logo: {
          alt: 'Physical AI Logo',
          src: '/img/book_logo.png',
        },
        items: [
          {
            type: 'doc',
            docId: 'physical-ai/module-1/weeks-1-2/intro-physical-ai',
            position: 'left',
            label: 'Book',
          },
          {
            href: 'https://github.com/AyyanAli-Khan/Physical-AI-Humanoid-Robotics-Book/tree/main/book',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Module 1: The Robotic Nervous System',
                to: '/docs/physical-ai/module-1/weeks-1-2/intro-physical-ai',
              },
              {
                label: 'Module 2: The Digital Twin',
                to: '/docs/physical-ai/module-2/weeks-6-7/gazebo-simulation',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/AyyanAli-Khan/Physical-AI-Humanoid-Robotics-Book/tree/main/book',
              },
            ],
          },
        ],
        copyright: 'Copyright © 2025 Ayyan Ali Khan',
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
