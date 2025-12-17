# Feature Specification: Physical AI & Humanoid Robotics — Docusaurus Book

**Feature Branch**: `1-docusaurus-book`
**Created**: 2025-12-09
**Status**: Draft
**Input**: User description: "CREATE THE FULL SPECIFICATION FOR THIS FEATURE.

FEATURE NAME:
\"Physical AI & Humanoid Robotics — Docusaurus Book\"

PRIMARY OBJECTIVE:
Create a complete, Docusaurus-compliant specification for a documentation \"book\" on Physical AI & Humanoid Robotics. The spec must define structure, chapters, labs, navigation, and configuration so that follow-up step (/sp.plan) can turn it into a fully buildable Docusaurus site.

────────────────────────────────
MANDATORY TECHNICAL REQUIREMENTS
────────────────────────────────
1. The Docusaurus project MUST be created at the repository root as:
   npx create-docusaurus@latest book classic

2. The book MUST live entirely inside the `book/` folder with this structure:
   - book/docs/         → all content (chapters, labs, assessments, appendices)
   - book/docs/physical-ai/ → all MDX pages for this specific book
   - book/sidebars.js   → navigation definition
   - book/docusaurus.config.js → global config (site metadata, presets, plugins)

3. ALL guidance about Docusaurus MUST align with official docs:
   https://docusaurus.io/docs/

4. ALL references to installation, configuration, MDX usage, sidebars, and deployment MUST be consistent with and valid per:
   - Official Docusaurus documentation
   - Playwright MCP (for browsing docs)
   - Context7 MCP (for updated summaries)
   (You don't have to show how to call these MCPs; just assume they're used to verify correctness.)

5. The specification MUST NOT require anything Docusaurus does not officially support.

────────────────
INTENT & SCOPE
────────────────
The goal is to define the **entire book specification**:

- Overall book architecture (Parts, Chapters, Labs, Appendices)
- Mapping between book content and course weeks/modules
- File & folder layout under `book/docs/physical-ai/`
- Sidebar structure in `book/sidebars.js`
- Docusaurus configuration in `book/docusaurus.config.js`
- Plugins, presets, and deployment settings needed for a production-ready doc site

The output should be **implementation-ready**: someone else should be able to:
- Run `npx create-docusaurus@latest book classic`
- Create all MDX files as per your spec
- Configure sidebars and config files as per your spec
- Run `cd book && npm run build` with a successful build.

────────────────────────
CONTENT DOMAINS TO COVER
────────────────────────
The book MUST cover, at minimum, the following domains:

- Physical AI & Embodied Intelligence
- ROS 2 foundations
- Gazebo + Unity simulation
- NVIDIA Isaac Sim + Isaac ROS + Nav2
- Vision-Language-Action (Whisper + LLM planning)
- Humanoid robotics fundamentals
- Hardware & Lab Architecture
- Weekly breakdown (Weeks 1–13)
- Assessments:
  - ROS 2 package/project
  - Gazebo simulation
  - Isaac perception / Isaac-based pipeline
  - Capstone project assessment
- Capstone pipeline:
  Voice → VLA (Vision-Language-Action) → Navigation → Manipulation

──────────────────────
STRUCTURAL REQUIREMENTS
──────────────────────
1. The book MUST be divided hierarchically into EXACTLY 4 MODULES following your canonical pedagogical structure:
   - Module 1: THE ROBOTIC NERVOUS SYSTEM (ROS 2)
   - Module 2: THE DIGITAL TWIN (GAZEBO & UNITY)
   - Module 3: THE AI-ROBOT BRAIN (NVIDIA ISAAC™)
   - Module 4: VISION-LANGUAGE-ACTION (VLA)
   Each Module contains:
   - Chapters (core conceptual units organized by weeks)
   - Labs (hands-on, project or exercise pages)
   You may also define:
   - Appendices (hardware guides, lab setup, cloud vs on-prem, etc.)

2. Each Chapter MUST:
   - Clearly indicate which Week(s) it corresponds to following the exact mapping:
     * Module 1: Weeks 1-2 (Introduction to Physical AI), Weeks 3-5 (ROS 2 Fundamentals)
     * Module 2: Weeks 6-7 (Robot Simulation with Gazebo)
     * Module 3: Weeks 8-10 (NVIDIA Isaac Platform)
     * Module 4: Weeks 11-12 (Humanoid Robot Development), Week 13 (Conversational Robotics)
   - Reference and be consistent with the weekly breakdown in the source content.

3. All final MDX pages MUST:
   - Be placed under `book/docs/physical-ai/`
   - Have clear, file-based naming conventions that reflect the module and week structure (e.g. `module-1-week-01-02-intro-physical-ai.mdx`, `module-1-lab-ros2-basics.mdx`, etc.)

4. Labs MUST:
   - Align with the assessments and weekly topics
   - Be explicitly listed as separate MDX pages (not just mentioned conceptually)
   - Follow the canonical lab structure specified in your pedagogical requirements

─────────────────────────────────────
DOCUSAURUS-SPECIFIC SPECIFICATION
─────────────────────────────────────
You MUST specify, in detail:

1. **File & Folder Layout**
   - Exact directory tree under `book/docs/`
   - All MDX file paths for:
     - Parts
     - Chapters
     - Labs
     - Assessments
     - Hardware/architecture appendices
   - Clear naming conventions for MDX files.

2. **Sidebar Structure (`book/sidebars.js`)**
   - EXACT Module-based logical grouping: \"Module 1: The Robotic Nervous System (ROS 2)\", \"Module 2: The Digital Twin (Gazebo & Unity)\", \"Module 3: The AI-Robot Brain (NVIDIA Isaac™)\", \"Module 4: Vision-Language-Action (VLA)\"
   - Relationship between sidebar items and MDX files following the 4-module structure
   - How Weeks, Modules, and Labs appear in the navigation tree with clear module groupings.

3. **Docusaurus Config (`book/docusaurus.config.js`)**
   - Required site metadata:
     - title
     - tagline
     - favicon (placeholder path is fine)
   - Deployment-related fields:
     - organizationName (e.g. \"physical-ai-lab\")
     - projectName (e.g. \"physical-ai-humanoid-robotics-book\")
     - url (e.g. \"https://physical-ai-lab.org\")
     - baseUrl (e.g. \"/book/\")
   - Correct classic preset usage:
     - docs options (path, routeBasePath, sidebarPath, editUrl placeholder, etc.)
     - theme options (if needed)
   - Any official plugins needed:
     - Search (e.g. classic preset built-in search or @docusaurus/plugin-content-docs as required)
     - Other official plugins ONLY if documented on docusaurus.io (no custom or unsupported plugins).

4. **Build & Deployment Compatibility**
   - Ensure the structure you define is buildable using:
     - `cd book`
     - `npm install`
     - `npm run build`
   - Assume standard Docusaurus v2 classic template with no exotic modifications.

──────────────────────────────
SOURCE COURSE CONTENT (CANON)
──────────────────────────────
Use the following course / book content as the **canonical source**. The book's Parts, Chapters, Labs, and Assessments MUST faithfully reflect and expand this material.

TITLE / THEME:
Physical AI & Humanoid Robotics
Focus and Theme: AI Systems in the Physical World. Embodied Intelligence.
Goal: Bridging the gap between the digital brain and the physical body. Students apply their AI knowledge to control Humanoid Robots in simulated and real-world environments.

QUARTER OVERVIEW:
The future of AI extends beyond digital spaces into the physical world. This capstone quarter introduces Physical AI—AI systems that function in reality and comprehend physical laws. Students learn to design, simulate, and deploy humanoid robots capable of natural human interactions using ROS 2, Gazebo, and NVIDIA Isaac.

MODULES:
● Module 1: The Robotic Nervous System (ROS 2)
  ○ Focus: Middleware for robot control.
  ○ ROS 2 Nodes, Topics, and Services.
  ○ Bridging Python Agents to ROS controllers using rclpy.
  ○ Understanding URDF (Unified Robot Description Format) for humanoids.

● Module 2: The Digital Twin (Gazebo & Unity)
  ○ Focus: Physics simulation and environment building.
  ○ Simulating physics, gravity, and collisions in Gazebo.
  ○ High-fidelity rendering and human-robot interaction in Unity.
  ○ Simulating sensors: LiDAR, Depth Cameras, and IMUs.

● Module 3: The AI-Robot Brain (NVIDIA Isaac™)
  ○ Focus: Advanced perception and training.
  ○ NVIDIA Isaac Sim: Photorealistic simulation and synthetic data generation.
  ○ Isaac ROS: Hardware-accelerated VSLAM (Visual SLAM) and navigation.
  ○ Nav2: Path planning for bipedal humanoid movement.

● Module 4: Vision-Language-Action (VLA)
  ○ Focus: The convergence of LLMs and Robotics.
  ○ Voice-to-Action: Using OpenAI Whisper for voice commands.
  ○ Cognitive Planning: Using LLMs to translate natural language (\"Clean the room\") into a sequence of ROS 2 actions.
  ○ Capstone Project: The Autonomous Humanoid. A final project where a simulated robot receives a voice command, plans a path, navigates obstacles, identifies an object using computer vision, and manipulates it.

WHY PHYSICAL AI MATTERS:
Humanoid robots are poised to excel in our human-centered world because they share our physical form and can be trained with abundant data from interacting in human environments. This represents a significant transition from AI models confined to digital environments to embodied intelligence that operates in physical space.

LEARNING OUTCOMES:
1. Understand Physical AI principles and embodied intelligence.
2. Master ROS 2 (Robot Operating System) for robotic control.
3. Simulate robots with Gazebo and Unity.
4. Develop with NVIDIA Isaac AI robot platform.
5. Design humanoid robots for natural interactions.
6. Integrate GPT models for conversational robotics.

WEEKLY BREAKDOWN:
Weeks 1-2: Introduction to Physical AI
• Foundations of Physical AI and embodied intelligence
• From digital AI to robots that understand physical laws
• Overview of humanoid robotics landscape
• Sensor systems: LIDAR, cameras, IMUs, force/torque sensors

Weeks 3-5: ROS 2 Fundamentals
• ROS 2 architecture and core concepts
• Nodes, topics, services, and actions
• Building ROS 2 packages with Python
• Launch files and parameter management

Weeks 6-7: Robot Simulation with Gazebo
• Gazebo simulation environment setup
• URDF and SDF robot description formats
• Physics simulation and sensor simulation
• Introduction to Unity for robot visualization

Weeks 8-10: NVIDIA Isaac Platform
• NVIDIA Isaac SDK and Isaac Sim
• AI-powered perception and manipulation
• Reinforcement learning for robot control
• Sim-to-real transfer techniques

Weeks 11-12: Humanoid Robot Development
• Humanoid robot kinematics and dynamics
• Bipedal locomotion and balance control
• Manipulation and grasping with humanoid hands
• Natural human-robot interaction design

Week 13: Conversational Robotics
• Integrating GPT models for conversational AI in robots
• Speech recognition and natural language understanding
• Multi-modal interaction: speech, gesture, vision

ASSESSMENTS:
• ROS 2 package development project
• Gazebo simulation implementation
• Isaac-based perception pipeline
• Capstone: Simulated humanoid robot with conversational AI

HARDWARE REQUIREMENTS (FOR APPENDICES / LAB SETUP CHAPTERS):
This course is technically demanding. It sits at the intersection of three heavy computational loads: Physics Simulation (Isaac Sim/Gazebo), Visual Perception (SLAM/Computer Vision), and Generative AI (LLMs/VLA).

Because the capstone involves a \"Simulated Humanoid,\" the primary investment must be in High-Performance Workstations. However, to fulfill the \"Physical AI\" promise, you also need Edge Computing Kits (brains without bodies) or specific robot hardware.

1. The \"Digital Twin\" Workstation (Required per Student)
   ● GPU: NVIDIA RTX 4070 Ti (12GB VRAM) or higher (ideally RTX 3090/4090, 24GB VRAM).
   ● CPU: Intel Core i7 (13th Gen+) or AMD Ryzen 9.
   ● RAM: 64 GB DDR5 (32 GB minimum but risky).
   ● OS: Ubuntu 22.04 LTS (preferred for ROS 2 + Isaac).

2. The \"Physical AI\" Edge Kit
   ● The Brain: NVIDIA Jetson Orin Nano (8GB) or Orin NX (16GB).
   ● The Eyes: Intel RealSense D435i or D455.
   ● The Inner Ear (Balance): USB IMU (e.g., BNO055).
   ● Voice Interface: USB Mic/Speaker array (e.g., ReSpeaker).

3. The Robot Lab (Three Options)
   Option A: Proxy (Recommended for Budget)
   ● Robot: Unitree Go2 Edu (~$1,800 - $3,000).

   Option B: Miniature Humanoid
   ● Robots: Unitree G1 (~$16k), Robotis OP3 (~$12k), or budget Hiwonder TonyPi Pro (~$600; AI offloaded to Jetson).

   Option C: Premium Sim-to-Real
   ● Robot: Unitree G1 Humanoid (for full capstone deployment).

4. Summary of Architecture
   Component      → Hardware                          → Function
   Sim Rig        → PC with RTX 4080 + Ubuntu 22.04   → Runs Isaac Sim, Gazebo, Unity, VLA training.
   Edge Brain     → Jetson Orin Nano                  → Runs inference / ROS 2 stack.
   Sensors        → RealSense + LiDAR                 → Real-world data for AI.
   Actuator       → Unitree Go2/G1                    → Receives motor commands from Jetson.

CLOUD-BASED (HIGH OPEX) ALTERNATIVE:
Option 2: The \"Ether\" Lab (Cloud-Native)
1. Cloud Workstations (AWS/Azure):
   ● Instance: AWS g5.2xlarge (A10G, 24GB VRAM) or g6e.xlarge.
   ● Software: NVIDIA Isaac Sim on Omniverse Cloud.
   ● Approx. cost: ~$205/quarter (120 hours × ~$1.50/hr + storage).

2. Local \"Bridge\" Hardware (Still Required)
   ● Jetson kit (~$700 one-time).
   ● One physical robot (e.g., Unitree Go2 Standard, ~$3,000).

3. Latency Trap
   ● Real-time control from cloud is dangerous.
   ● Train in the cloud, download weights, and deploy to local Jetson.

The book should include one or more chapters/appendices that clearly describe:
- Recommended lab architecture (on-prem vs cloud-native)
- Tradeoffs (CapEx vs OpEx)
- \"Economy Jetson Student Kit\" bill of materials and cost breakdown (~$700).

────────────────────
SUCCESS CRITERIA
────────────────────
Your specification is successful if:

1. It enables /sp.plan to generate a **complete implementation plan** for:
   - Creating all MDX files under `book/docs/physical-ai/`
   - Wiring up `book/sidebars.js`
   - Configuring `book/docusaurus.config.js`
   - Running `npm run build` successfully.

2. The resulting Docusaurus documentation:
   - Fully represents the quarter's content (weeks, modules, labs, assessments, hardware).
   - Has a clear, pedagogical flow from fundamentals → simulation → Isaac → VLA → capstone.
   - Provides a coherent navigation experience (sidebars) that reflects the 13-week structure.

3. The specification is:
   - Precise enough that another engineer can implement without guessing.
   - Fully compliant with official Docusaurus capabilities and patterns."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Student Learning Experience (Priority: P1)

Student accesses the documentation to learn about Physical AI & Humanoid Robotics following the 4-module canonical curriculum (Module 1: The Robotic Nervous System (ROS 2), Module 2: The Digital Twin (Gazebo & Unity), Module 3: The AI-Robot Brain (NVIDIA Isaac™), Module 4: Vision-Language-Action (VLA)). The student navigates through the content by module, follows hands-on lab exercises, and accesses assessment materials to complete projects.

**Why this priority**: This is the primary use case for which the documentation is being created - to enable students to learn the material effectively through the structured 4-module approach.

**Independent Test**: Can be fully tested by following the complete learning path from Module 1 to Module 4 and completing all canonical labs, delivering the core educational value of the course.

**Acceptance Scenarios**:
1. **Given** student wants to learn Physical AI fundamentals, **When** they navigate to Module 1 content, **Then** they find clear, accessible explanations of Physical AI and embodied intelligence concepts
2. **Given** student wants to complete a ROS 2 lab exercise, **When** they access the Module 1 lab content, **Then** they find step-by-step instructions with expected outcomes

---

### User Story 2 - Instructor Course Delivery (Priority: P2)

Instructor uses the documentation to guide course delivery following the 4-module canonical curriculum. The instructor navigates to specific module's content to prepare lessons and references lab exercises to guide student activities.

**Why this priority**: Instructors need clear, organized content to effectively deliver the course following the structured module approach, which is essential for the educational mission.

**Independent Test**: Can be tested by navigating through each module's content and verifying that it provides sufficient detail for lesson preparation.

**Acceptance Scenarios**:
1. **Given** instructor needs to prepare for Module 3 lessons on NVIDIA Isaac, **When** they access the content, **Then** they find comprehensive material covering Isaac Sim, Isaac ROS, and Nav2 with practical examples

---

### User Story 3 - Hardware Setup and Lab Preparation (Priority: P3)

Student or administrator accesses hardware setup documentation located in Module 3 (The AI-Robot Brain) to prepare for the course. They need to understand the requirements for workstations, edge kits, and robot options.

**Why this priority**: Hardware requirements are critical for course success and need to be clearly documented in Module 3 for procurement and setup.

**Independent Test**: Can be tested by following the hardware setup guides in Module 3 and verifying that they lead to successful lab preparation.

**Acceptance Scenarios**:
1. **Given** administrator needs to set up the course lab, **When** they follow the hardware documentation in Module 3, **Then** they can successfully procure and configure all necessary equipment

---

### Edge Cases

- What happens when a student accesses the content without the required hardware specifications?
- How does the system handle students with different technical backgrounds accessing the same content?
- What if the capstone project requires additional resources not covered in earlier weeks?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST organize content hierarchically into EXACTLY 4 Modules (Module 1: The Robotic Nervous System (ROS 2), Module 2: The Digital Twin (Gazebo & Unity), Module 3: The AI-Robot Brain (NVIDIA Isaac™), Module 4: Vision-Language-Action (VLA)), with Chapters and Labs following the 13-week course structure
- **FR-002**: System MUST create all content as MDX files under `book/docs/physical-ai/` directory
- **FR-003**: Users MUST be able to navigate content by week (Weeks 1-13) and module (Modules 1-4)
- **FR-004**: System MUST include dedicated lab pages for all specified assessments following the canonical structure: Module 1 labs ("Your First ROS 2 Node", "Building a ROS 2 Package and Launch File", "Defining a Simple Humanoid URDF"), Module 2 labs ("Launching a URDF Robot in Gazebo", "Simulating Sensors", "Basic Unity Scene"), Module 3 labs ("Isaac Sim Environment Setup", "Isaac ROS Perception Pipeline", "Nav2-based Navigation"), Module 4 labs ("Whisper-Based Voice Command", "LLM Task Planner", "End-to-End VLA Demo"), plus the capstone Autonomous Humanoid project
- **FR-005**: System MUST provide comprehensive hardware documentation covering workstation, edge kit, and robot options as part of Module 3 (The AI-Robot Brain), including "Digital Twin" Workstation specs, "Physical AI" Edge Kit, Robot Lab options (A, B, C), Architecture Summary diagram, and Cloud vs On-Prem comparison
- **FR-006**: System MUST document the complete capstone pipeline: Voice → VLA → Navigation → Manipulation
- **FR-007**: System MUST be buildable using `npx create-docusaurus@latest book classic` and `npm run build`
- **FR-008**: System MUST provide clear file naming conventions for all MDX files
- **FR-009**: System MUST include sidebar navigation reflecting the pedagogical flow from fundamentals to capstone
- **FR-010**: System MUST include a dedicated "Learning Outcomes" page listing all 6 specified outcomes: Physical AI principles, ROS 2 mastery, Gazebo/Unity simulation, NVIDIA Isaac development, Humanoid robot design, and GPT integration for conversational robotics
- **FR-011**: System MUST be compatible with Docusaurus v2 classic template without exotic modifications

### Key Entities

- **Module**: High-level organizational unit following the canonical 4-module structure (Module 1: The Robotic Nervous System (ROS 2), Module 2: The Digital Twin (Gazebo & Unity), Module 3: The AI-Robot Brain (NVIDIA Isaac™), Module 4: Vision-Language-Action (VLA))
- **Chapter**: Core conceptual unit within a Module that corresponds to specific weeks
- **Lab**: Hands-on exercise or project page that provides practical implementation guidance aligned with specified assessments
- **Appendix**: Supplementary material containing hardware guides, setup instructions, and architectural decisions
- **MDX File**: Documentation page in MDX format that contains the educational content
- **Navigation Item**: Sidebar entry that enables users to access specific content in an organized manner
- **Learning Outcomes Page**: Dedicated page listing all 6 specified learning outcomes

## Success Criteria *(mandatory)*

### Measurable Outcomes

## Clarifications

### Session 2025-12-10

- Q: Should the content structure follow the 4 canonical modules? → A: Yes, align the content structure with the 4 canonical modules: Module 1: The Robotic Nervous System (ROS 2), Module 2: The Digital Twin (Gazebo & Unity), Module 3: The AI-Robot Brain (NVIDIA Isaac™), Module 4: Vision-Language-Action (VLA)
- Q: How should the content organization be updated? → A: Update the content organization to follow the 4 canonical modules with clear Part structure
- Q: Where should hardware documentation be placed? → A: Hardware documentation should be placed as part of Module 3 (The AI-Robot Brain)
- Q: Should there be a dedicated Learning Outcomes page? → A: Yes, include a dedicated Learning Outcomes page listing all 6 specified outcomes
- Q: How should lab exercises be structured? → A: Lab exercises should follow the canonical structure with specific labs for each module


- **SC-001**: Students can access all 4 Modules following the canonical pedagogical structure and find clear, pedagogically organized material covering all 13 weeks
- **SC-002**: Instructors can navigate the documentation by Module (Modules 1-4) and find comprehensive content for each module
- **SC-003**: All lab exercises following the canonical structure are documented with step-by-step instructions and can be completed successfully
- **SC-004**: Hardware requirements are clearly specified in Module 3 and enable successful lab setup with cost breakdowns provided
- **SC-005**: The complete Docusaurus site builds successfully without errors using standard Docusaurus tooling
- **SC-006**: Users can navigate from Module 1 to Module 4 following the clear pedagogical flow from fundamentals to capstone
- **SC-007**: The capstone project documentation enables students to implement the complete Voice → VLA → Navigation → Manipulation pipeline
- **SC-008**: The dedicated Learning Outcomes page clearly lists all 6 specified learning outcomes for the course