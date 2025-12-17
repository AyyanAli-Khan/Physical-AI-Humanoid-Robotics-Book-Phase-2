# Research: Physical AI & Humanoid Robotics — Docusaurus Book

## Docusaurus Best Practices

### Project Structure
- Docusaurus projects should follow the classic template for documentation sites
- Content should be organized under `docs/` directory
- MDX files allow React components within Markdown for enhanced interactivity
- Configuration files (`docusaurus.config.js`, `sidebars.js`) control site behavior

### Configuration Patterns
- Use the classic preset for documentation sites
- Configure sidebar navigation to reflect logical content hierarchy
- Set up proper base URL for deployment scenarios
- Enable search functionality for documentation sites

### Content Organization
- Group related content into logical categories
- Use frontmatter consistently across all pages
- Implement proper navigation paths for user journey
- Follow accessibility standards for educational content

## Module-Based Navigation Research

### Canonical Module Structure
The 4-module structure aligns with pedagogical best practices:
- Module 1: Foundational concepts (ROS 2 basics)
- Module 2: Simulation concepts (Gazebo and Unity)
- Module 3: Advanced concepts (Isaac and AI)
- Module 4: Integration concepts (VLA and capstone)

### Navigation Patterns
- Hierarchical sidebar organization improves content discovery
- Week-based grouping within modules supports curriculum flow
- Lab exercises should be clearly marked and linked from relevant chapters
- Appendices should be accessible but not interfere with main content flow

## Technical Implementation Research

### Docusaurus v2 vs v3
- Docusaurus v2 is stable and well-documented
- Migration path exists from v2 to v3 if needed
- Current implementation will use v2 for maximum compatibility

### Deployment Options
- GitHub Pages offers free hosting with custom domains
- Netlify and Vercel provide enhanced features but at cost
- GitHub Pages sufficient for documentation site requirements

### Content Management
- MDX format supports both Markdown and React components
- Frontmatter enables metadata for search and navigation
- Versioning possible for future course iterations
- Translation support available if needed later

## Robotics and AI Technology Research

### ROS 2 Best Practices
- ROS 2 Foxy, Humble, or Iron are recommended versions
- Python and C++ are primary development languages
- Package structure should follow ROS 2 conventions
- Launch files and parameter management are critical concepts

### Gazebo and Simulation
- Gazebo Garden or Fortress for modern simulation
- URDF for robot description format
- SDF for world description format
- Sensor simulation best practices for educational content

### NVIDIA Isaac
- Isaac Sim for photorealistic simulation
- Isaac ROS for hardware-accelerated perception
- Nav2 for navigation stack implementation
- Sim-to-real transfer techniques for deployment

### Vision-Language-Action Systems
- Integration of speech recognition (Whisper) with robotics
- LLM integration for task planning
- Multi-modal perception systems
- End-to-end pipeline implementation

## Educational Content Research

### Pedagogical Structure
- Module-based learning supports complex topic progression
- Hands-on labs reinforce theoretical concepts
- Assessment integration provides learning validation
- Capstone projects synthesize all learning modules

### Content Accessibility
- Clear learning objectives for each chapter
- Prerequisites clearly stated for each section
- Progressive difficulty matching student skill levels
- Multiple learning pathways for different backgrounds

## Hardware Documentation Research

### Workstation Requirements
- High-performance GPUs essential for simulation work
- Ubuntu 22.04 LTS provides best ROS 2 compatibility
- RAM and storage requirements based on simulation complexity
- Multi-monitor setups recommended for development workflow

### Edge Computing
- NVIDIA Jetson series provides AI inference capabilities
- RealSense cameras offer depth and RGB sensing
- IMU sensors provide orientation and motion data
- Audio interfaces enable voice interaction

### Robot Platforms
- Unitree robots offer advanced humanoid and quadruped platforms
- ROS 2 compatibility ensures integration flexibility
- Documentation should cover multiple platform options
- Cost-benefit analysis for different implementation approaches