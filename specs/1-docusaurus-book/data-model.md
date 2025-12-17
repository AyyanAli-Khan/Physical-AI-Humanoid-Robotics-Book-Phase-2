# Data Model: Physical AI & Humanoid Robotics — Docusaurus Book

## Entity: Module

### Attributes
- **id**: String (unique identifier, e.g., "module-1", "module-2", "module-3", "module-4")
- **title**: String (full title, e.g., "Module 1: The Robotic Nervous System (ROS 2)")
- **description**: String (brief overview of module content and objectives)
- **weeks**: String (associated weeks, e.g., "Weeks 1-2", "Weeks 3-5", "Weeks 8-10")
- **position**: Integer (order in the curriculum sequence: 1-4)
- **learningObjectives**: Array of String (specific learning objectives for the module)

### Relationships
- **chapters**: One-to-many with Chapter entity
- **labs**: One-to-many with Lab entity
- **appendices**: One-to-many with Appendix entity (optional)

### Validation Rules
- id must be unique across all modules
- position must be between 1 and 4
- title must follow canonical naming convention
- weeks must align with curriculum structure

## Entity: Chapter

### Attributes
- **id**: String (unique identifier, e.g., "module-1-week-01-02-intro")
- **title**: String (chapter title)
- **description**: String (brief description of chapter content)
- **moduleRef**: String (reference to parent module id)
- **week**: String (associated week, e.g., "Weeks 1-2", "Week 3", "Weeks 8-10")
- **position**: Integer (order within the module)
- **prerequisites**: Array of String (prerequisite concepts or chapters)
- **learningObjectives**: Array of String (specific learning objectives)
- **mdxPath**: String (file path relative to docs root)

### Relationships
- **module**: Many-to-one with Module entity
- **relatedLabs**: Many-to-many with Lab entity (optional)

### Validation Rules
- id must be unique across all chapters
- moduleRef must reference an existing module
- position must be positive integer
- mdxPath must exist in the file system

## Entity: Lab

### Attributes
- **id**: String (unique identifier, e.g., "module-1-lab-ros2-basics")
- **title**: String (lab title)
- **description**: String (brief description of lab objectives)
- **moduleRef**: String (reference to parent module id)
- **week**: String (associated week)
- **position**: Integer (order within the module)
- **objectives**: Array of String (specific lab objectives)
- **prerequisites**: Array of String (prerequisite concepts or chapters)
- **estimatedTime**: String (estimated completion time, e.g., "2-3 hours")
- **requiredEquipment**: Array of String (equipment needed for lab)
- **mdxPath**: String (file path relative to docs root)

### Relationships
- **module**: Many-to-one with Module entity
- **relatedChapters**: Many-to-many with Chapter entity

### Validation Rules
- id must be unique across all labs
- moduleRef must reference an existing module
- position must be positive integer
- mdxPath must exist in the file system

## Entity: Appendix

### Attributes
- **id**: String (unique identifier, e.g., "appendix-hardware", "appendix-setup")
- **title**: String (appendix title)
- **description**: String (brief description of appendix content)
- **type**: String (type of appendix: "Hardware Requirements", "Setup Guide", "Architecture", "Cloud vs On-Prem", "Learning Outcomes")
- **position**: Integer (order in appendices section)
- **mdxPath**: String (file path relative to docs root)

### Relationships
- **relatedModules**: Many-to-many with Module entity (optional)

### Validation Rules
- id must be unique across all appendices
- type must be one of the predefined values
- position must be positive integer
- mdxPath must exist in the file system

## Entity: NavigationItem

### Attributes
- **id**: String (unique identifier)
- **label**: String (display label in sidebar/navbar)
- **type**: String ("category" or "doc")
- **docId**: String (reference to document id, required if type is "doc")
- **items**: Array of NavigationItem (for categories)
- **position**: Integer (order in navigation)
- **collapsed**: Boolean (whether category is collapsed by default)

### Relationships
- **parent**: Self-referencing for nested navigation
- **document**: One-to-one with Chapter/Lab/Appendix (if type is "doc")

### Validation Rules
- If type is "doc", docId must reference an existing document
- If type is "category", items array must not be empty
- Position must be positive integer

## Entity: Configuration

### Attributes
- **title**: String (site title)
- **tagline**: String (site tagline)
- **favicon**: String (path to favicon)
- **url**: String (deployment URL)
- **baseUrl**: String (base path for deployment)
- **organizationName**: String (GitHub organization name)
- **projectName**: String (GitHub project name)
- **onBrokenLinks**: String (how to handle broken links)
- **onBrokenMarkdownLinks**: String (how to handle broken markdown links)
- **presets**: Array of Object (Docusaurus presets configuration)
- **themeConfig**: Object (theme configuration including navbar and footer)

### Validation Rules
- All required fields must be present
- URL must be a valid URL format
- Base URL must start with "/"
- Presets must follow Docusaurus format

## Entity: Deployment

### Attributes
- **provider**: String ("GitHub Pages", "Netlify", "Vercel")
- **branch**: String (deployment branch, e.g., "gh-pages")
- **buildCommand**: String (command to build the site)
- **outputDirectory**: String (directory containing build output)
- **environment**: Object (environment-specific settings)

### Validation Rules
- Provider must be one of the supported deployment providers
- Branch must be a valid Git branch name
- Build command must be executable