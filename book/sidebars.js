// @ts-check

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.

 @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
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
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      collapsed: false,
      items: [
        'physical-ai/module-3/weeks-8-10/nvidia-isaac-platform',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      collapsed: false,
      items: [
        'physical-ai/module-4/weeks-11-12/humanoid-development',
        'physical-ai/module-4/week-13/conversational-robotics',
      ],
    },
    {
      type: 'category',
      label: 'Appendices',
      collapsed: true,
      items: [
        'physical-ai/appendices/hardware-requirements',
      ],
    },
  ],
};

export default sidebars;
