# Data Model: Physical AI & Humanoid Robotics Book

## Content Part
**Description**: High-level organizational unit that groups related chapters and content

**Fields**:
- id: string (unique identifier, e.g., "part-1-foundations")
- title: string (display title, e.g., "Part I: Foundations")
- description: string (brief overview of the part's content)
- order: number (sequence number for navigation)
- chapters: array of Chapter references

**Relationships**:
- Contains many Chapters
- Belongs to the overall book structure

## Chapter
**Description**: Core conceptual unit that corresponds to specific weeks/modules in the curriculum

**Fields**:
- id: string (unique identifier, e.g., "week-01-02-intro")
- title: string (display title, e.g., "Weeks 1-2: Introduction to Physical AI")
- description: string (brief overview of chapter content)
- weekRange: string (e.g., "Weeks 1-2", "Module 1", etc.)
- module: string (corresponding module, e.g., "Module 1: The Robotic Nervous System")
- learningObjectives: array of strings (specific learning goals)
- prerequisites: array of strings (required prior knowledge)
- contentPath: string (path to MDX file)
- order: number (sequence within the part)
- labs: array of Lab references

**Relationships**:
- Belongs to one Content Part
- Contains many Labs (optional)
- May reference other Chapters for cross-links

## Lab
**Description**: Hands-on exercise or project page that provides practical implementation guidance

**Fields**:
- id: string (unique identifier, e.g., "lab-ros2-package")
- title: string (display title, e.g., "ROS 2 Package Development Lab")
- description: string (brief overview of lab objectives)
- associatedChapter: string (reference to related chapter)
- duration: string (estimated completion time, e.g., "2-3 hours")
- objectives: array of strings (specific skills to practice)
- prerequisites: array of strings (required setup/knowledge)
- steps: array of objects (step-by-step instructions)
- expectedOutcome: string (what the student should achieve)
- assessmentCriteria: array of strings (how the lab will be evaluated)
- contentPath: string (path to MDX file)

**Relationships**:
- Belongs to one Chapter (optional)
- May reference multiple Chapters for concepts
- May have dependencies on other Labs

## Appendix
**Description**: Supplementary material containing hardware guides, setup instructions, and architectural decisions

**Fields**:
- id: string (unique identifier, e.g., "appendix-a-hardware")
- title: string (display title, e.g., "Appendix A: Hardware Requirements")
- description: string (brief overview of appendix content)
- category: string (type of content, e.g., "Hardware", "Setup", "Architecture")
- contentPath: string (path to MDX file)
- order: number (sequence in appendices section)

**Relationships**:
- Independent of Parts/Chapters structure
- May reference multiple Chapters for context

## MDX File
**Description**: Documentation page in MDX format that contains the educational content

**Fields**:
- path: string (relative path from book/docs/physical-ai/)
- frontmatter: object (title, description, keywords, etc.)
- content: string (MDX formatted content)
- metadata: object (author, last updated, etc.)

**Relationships**:
- Maps to one Content Part, Chapter, Lab, or Appendix
- May include references to other MDX files

## Navigation Item
**Description**: Sidebar entry that enables users to access specific content in an organized manner

**Fields**:
- id: string (unique identifier for navigation)
- label: string (display text in sidebar)
- type: string ("category" or "doc")
- link: object (for doc type: {type: "doc", id: docId}; for category: {type: "generated-index"})
- items: array of Navigation Item references (for categories)
- collapsed: boolean (initial collapsed state)
- collapsible: boolean (whether the category can be collapsed)

**Relationships**:
- Maps to Content Parts, Chapters, Labs, or Appendices
- Forms hierarchical structure in sidebar

## State Transitions

### Content Part State Transitions
- Draft → In Review → Approved → Published
- Published → Updated → Published (with version tracking)

### Chapter State Transitions
- Created → Content Draft → Technical Review → Content Review → Approved → Published
- Published → Revision Required → Revised → Approved → Published

### Lab State Transitions
- Designed → Draft → Tested → Reviewed → Approved → Published
- Published → Updated → Tested → Approved → Published

## Validation Rules

### Content Part Validation
- Title must be unique within the book
- Must have at least one Chapter
- Order must be a positive integer
- Description must be 10-200 characters

### Chapter Validation
- Title must be unique within the book
- Must have valid weekRange format
- Must belong to exactly one Content Part
- Learning objectives must be specific and measurable
- Content path must exist and be accessible

### Lab Validation
- Title must be unique within the book
- Must have estimated duration
- Steps must be in sequential order
- Must have clear expected outcome
- Content path must exist and be accessible

### Appendix Validation
- Title must be unique within appendices
- Category must be one of predefined values
- Content path must exist and be accessible

### Navigation Item Validation
- Label must be clear and descriptive
- Type must be either "category" or "doc"
- ID must be unique within the navigation structure
- Items array must not exceed reasonable depth (max 3 levels)