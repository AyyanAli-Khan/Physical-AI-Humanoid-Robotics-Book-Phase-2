# Quickstart Guide: Physical AI & Humanoid Robotics Book

## Prerequisites

- Node.js LTS (v18.12.0 or higher)
- npm or yarn package manager
- Git for version control
- Text editor or IDE

## Setup Instructions

### 1. Clone or Create the Repository
```bash
# If starting fresh
mkdir physical-ai-humanoid-robotics-book
cd physical-ai-humanoid-robotics-book
git init
```

### 2. Initialize Docusaurus Project
```bash
# Create Docusaurus project in book/ directory
npx create-docusaurus@latest book classic
# This creates the book/ directory with the basic Docusaurus structure
```

### 3. Install Additional Dependencies (if needed)
```bash
cd book
npm install
```

### 4. Set Up Project Structure
```bash
# Create the required directory structure
mkdir -p book/docs/physical-ai/{part-1-foundations,part-2-simulation,part-3-humanoid,part-4-vla,appendices}

# Create content directories for each part
mkdir -p book/docs/physical-ai/part-1-foundations
mkdir -p book/docs/physical-ai/part-2-simulation
mkdir -p book/docs/physical-ai/part-3-humanoid
mkdir -p book/docs/physical-ai/part-4-vla
mkdir -p book/docs/physical-ai/appendices
```

## Configuration Setup

### 1. Update docusaurus.config.js
Replace the default configuration with the project-specific settings:

```javascript
// book/docusaurus.config.js
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Bridging the gap between digital AI and physical robots',
  favicon: '/img/favicon.ico',

  url: 'https://physical-ai-lab.org',
  baseUrl: '/book/',
  organizationName: 'physical-ai-lab',
  projectName: 'physical-ai-humanoid-robotics-book',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/physical-ai-lab/physical-ai-humanoid-robotics-book/edit/main/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'Physical AI Logo',
        src: '/img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'part-1-foundations/week-01-02-intro',
          position: 'left',
          label: 'Book',
        },
        {
          type: 'doc',
          docId: 'appendices/appendix-a-hardware',
          position: 'left',
          label: 'Hardware',
        },
        {
          href: 'https://github.com/physical-ai-lab/physical-ai-humanoid-robotics-book',
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
              label: 'Week 1-2: Introduction',
              to: '/part-1-foundations/week-01-02-intro',
            },
            {
              label: 'Week 3-5: ROS 2',
              to: '/part-1-foundations/week-03-05-ros2',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/physical-ai-lab/physical-ai-humanoid-robotics-book',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI Lab. Built with Docusaurus.`,
    },
  },
};

module.exports = config;
```

### 2. Create Sidebar Configuration
Create `book/sidebars.js` with the hierarchical structure:

```javascript
// book/sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Part I: Foundations',
      collapsed: false,
      items: [
        'part-1-foundations/week-01-02-intro',
        'part-1-foundations/week-03-05-ros2',
        'part-1-foundations/lab-ros2-package',
      ],
    },
    {
      type: 'category',
      label: 'Part II: Simulation and Digital Twins',
      collapsed: false,
      items: [
        'part-2-simulation/week-06-07-gazebo',
        'part-2-simulation/week-08-10-isaac',
        'part-2-simulation/lab-gazebo-sim',
        'part-2-simulation/lab-isaac-pipeline',
      ],
    },
    {
      type: 'category',
      label: 'Part III: Humanoid Robotics',
      collapsed: false,
      items: [
        'part-3-humanoid/week-11-12-humanoid',
        'part-3-humanoid/lab-humanoid-control',
      ],
    },
    {
      type: 'category',
      label: 'Part IV: Vision-Language-Action',
      collapsed: false,
      items: [
        'part-4-vla/week-13-conversational',
        'part-4-vla/lab-capstone',
      ],
    },
    {
      type: 'category',
      label: 'Appendices',
      collapsed: true,
      items: [
        'appendices/appendix-a-hardware',
        'appendices/appendix-b-cloud',
        'appendices/appendix-c-architecture',
      ],
    },
  ],
};
```

## Content Creation

### 1. Create a Sample MDX File
Create `book/docs/physical-ai/part-1-foundations/week-01-02-intro.mdx`:

```md
---
title: 'Weeks 1-2: Introduction to Physical AI'
description: 'Foundations of Physical AI and embodied intelligence'
sidebar_label: 'Weeks 1-2: Introduction to Physical AI'
sidebar_position: 1
---

# Weeks 1-2: Introduction to Physical AI

## Learning Objectives
- Understand the principles of Physical AI and embodied intelligence
- Identify the key differences between digital AI and physical AI
- Recognize the potential applications of humanoid robotics

## Introduction
The future of AI extends beyond digital spaces into the physical world. This capstone quarter introduces Physical AI—AI systems that function in reality and comprehend physical laws.

## Key Concepts
- Physical AI principles
- Embodied intelligence
- Humanoid robotics landscape
- Sensor systems for robotics

## Summary
This week lays the foundation for understanding Physical AI and its applications in humanoid robotics.
```

## Development Workflow

### 1. Start Development Server
```bash
cd book
npm start
```

### 2. Build for Production
```bash
cd book
npm run build
```

### 3. Deploy to GitHub Pages
```bash
cd book
npm run deploy
```

## Validation Steps

1. **Check build**: Run `npm run build` and verify no errors
2. **Check navigation**: Test all sidebar links work correctly
3. **Check responsive design**: Verify site works on mobile devices
4. **Check SEO**: Validate meta tags and structured data
5. **Check accessibility**: Ensure proper heading hierarchy and alt text