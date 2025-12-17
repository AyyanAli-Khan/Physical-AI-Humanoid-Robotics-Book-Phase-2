# Quickstart Guide: Physical AI & Humanoid Robotics — Docusaurus Book

## Prerequisites

### System Requirements
- Node.js LTS (v18.12.0 or higher)
- npm package manager (comes with Node.js)
- Git for version control
- Text editor or IDE
- Command line interface (Terminal on macOS/Linux, Command Prompt or PowerShell on Windows)

### Development Environment
- Ubuntu 22.04 LTS (recommended for ROS 2 compatibility) or equivalent
- Minimum 8GB RAM (16GB+ recommended for simulation work)
- Sufficient disk space for Docusaurus dependencies (~500MB)

## Setup Instructions

### 1. Clone or Create the Repository
```bash
# If starting fresh
mkdir physical-ai-humanoid-robotics-book
cd physical-ai-humanoid-robotics-book
git init

# If cloning existing repository
git clone <repository-url>
cd physical-ai-humanoid-robotics-book
```

### 2. Initialize Docusaurus Project
```bash
# Create Docusaurus project in book/ directory
npx create-docusaurus@latest book classic
# This creates the book/ directory with the basic Docusaurus structure
```

### 3. Install Additional Dependencies
```bash
cd book
npm install
```

### 4. Set Up Project Structure
```bash
# Create the required module-based directory structure
mkdir -p book/docs/physical-ai/{module-1,module-2,module-3,module-4,appendices}

# Create subdirectories for each module
mkdir -p book/docs/physical-ai/module-1/{weeks-1-2,weeks-3-5,lab-exercises}
mkdir -p book/docs/physical-ai/module-2/{weeks-6-7,lab-exercises}
mkdir -p book/docs/physical-ai/module-3/{weeks-8-10,lab-exercises}
mkdir -p book/docs/physical-ai/module-4/{weeks-11-12,week-13,lab-exercises}
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
          docId: 'physical-ai/module-1/weeks-1-2/intro-physical-ai',
          position: 'left',
          label: 'Book',
        },
        {
          type: 'doc',
          docId: 'physical-ai/appendices/hardware-requirements',
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
Create `book/sidebars.js` with the 4-module hierarchical structure:

```javascript
// book/sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      collapsed: false,
      items: [
        'physical-ai/module-1/weeks-1-2/intro-physical-ai',
        'physical-ai/module-1/weeks-3-5/ros2-fundamentals',
        'physical-ai/module-1/lab-exercises/ros2-basics',
        'physical-ai/module-1/lab-exercises/ros2-packages',
        'physical-ai/module-1/lab-exercises/urdf-definition',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      collapsed: false,
      items: [
        'physical-ai/module-2/weeks-6-7/gazebo-simulation',
        'physical-ai/module-2/lab-exercises/gazebo-robot',
        'physical-ai/module-2/lab-exercises/sensor-simulation',
        'physical-ai/module-2/lab-exercises/unity-visualization',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      collapsed: false,
      items: [
        'physical-ai/module-3/weeks-8-10/nvidia-isaac-platform',
        'physical-ai/module-3/lab-exercises/isaac-sim-setup',
        'physical-ai/module-3/lab-exercises/isaac-perception',
        'physical-ai/module-3/lab-exercises/nav2-navigation',
        'physical-ai/module-3/hardware-requirements',
        'physical-ai/module-3/lab-architecture',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      collapsed: false,
      items: [
        'physical-ai/module-4/weeks-11-12/humanoid-development',
        'physical-ai/module-4/week-13/conversational-robotics',
        'physical-ai/module-4/lab-exercises/voice-command',
        'physical-ai/module-4/lab-exercises/llm-planning',
        'physical-ai/module-4/lab-exercises/vla-demo',
        'physical-ai/module-4/capstone-autonomous-humanoid',
      ],
    },
    {
      type: 'category',
      label: 'Appendices',
      collapsed: true,
      items: [
        'physical-ai/appendices/hardware-requirements',
        'physical-ai/appendices/cloud-vs-on-prem',
        'physical-ai/appendices/learning-outcomes',
        'physical-ai/appendices/lab-architecture',
      ],
    },
  ],
};
```

## Content Creation

### 1. Create a Sample Chapter MDX File
Create `book/docs/physical-ai/module-1/weeks-1-2/intro-physical-ai.mdx`:

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

### 2. Create a Sample Lab MDX File
Create `book/docs/physical-ai/module-1/lab-exercises/ros2-basics.mdx`:

```md
---
title: 'Lab: Your First ROS 2 Node'
description: 'Hands-on lab for creating your first ROS 2 node with rclpy'
sidebar_label: 'Lab: Your First ROS 2 Node'
sidebar_position: 3
---

# Lab: Your First ROS 2 Node

## Learning Objectives
- Create a simple ROS 2 publisher node
- Create a simple ROS 2 subscriber node
- Test the communication between nodes

## Prerequisites
- ROS 2 installed and sourced
- Basic Python programming knowledge

## Lab Instructions
This lab provides hands-on experience with creating basic ROS 2 nodes using Python.

## Expected Outcomes
- A functional publisher and subscriber pair
- Understanding of ROS 2 node communication

## Assessment Criteria
- Nodes communicate successfully
- Code follows ROS 2 best practices
- Proper error handling implemented
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

### 3. Serve Built Site Locally (for testing)
```bash
cd book
npm run serve
```

## Deployment Setup

### GitHub Pages Deployment
1. Configure GitHub Pages in your repository settings
2. Set source to "Deploy from a branch"
3. Select `gh-pages` branch
4. Use the following deployment script:

```bash
# Deploy to GitHub Pages
cd book
npm run deploy
```

### Deployment Configuration
The deployment process will:
1. Build the site with `npm run build`
2. Push the build output to the `gh-pages` branch
3. GitHub Pages will automatically serve from this branch

## Validation Steps

### 1. Check Build Process
```bash
npm run build
# Verify no errors occur during build
```

### 2. Check Navigation
- Test all sidebar links work correctly
- Verify navigation between modules works
- Ensure all lab exercises are accessible

### 3. Check Responsive Design
- Test site on different screen sizes
- Verify mobile navigation works properly

### 4. Check Content Completeness
- Verify all 4 modules are represented
- Ensure all 13 weeks of content are accessible
- Confirm all lab exercises are properly linked

### 5. Check Cross-References
- Verify links between related content work
- Test links from appendices to modules
- Ensure prerequisite references are accurate

## Troubleshooting

### Common Issues
1. **Build errors**: Check for syntax errors in MDX files
2. **Navigation issues**: Verify doc IDs match sidebar references
3. **Missing content**: Ensure all file paths exist in the file system

### Verification Commands
```bash
# Check for broken links
npm run build

# Verify all files exist as referenced in sidebars.js
# Manually check each file path exists
```