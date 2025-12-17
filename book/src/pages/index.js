import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import Heading from '@theme/Heading';
import styles from './index.module.css';

const modules = [
  {
    title: 'Module 1: Robotic Nervous System',
    description:
      'Build the control stack, low-level reflexes, and safety layers that let humanoids perceive and act.',
    to: '/docs/physical-ai/module-1/weeks-1-2/intro-physical-ai',
    badge: 'Weeks 1-2',
  },
  {
    title: 'Module 2: The Digital Twin',
    description:
      'Create high-fidelity simulations, align them with the real robot, and iterate faster with less risk.',
    to: '/docs/physical-ai/module-2/weeks-6-7/gazebo-simulation',
    badge: 'Weeks 6-7',
  },
  {
    title: 'Module 3: Embodied Intelligence',
    description:
      'Integrate planning, control, and learning systems that connect perception to purposeful motion.',
    to: '/docs/physical-ai/module-3/weeks-8-10/nvidia-isaac-platform',
    badge: 'Weeks 8-10',
  },
];

function ModuleCard({title, description, to, badge}) {
  return (
    <Link className={styles.moduleCard} to={to}>
      <div className={styles.moduleHeader}>
        <span className={styles.moduleBadge}>{badge}</span>
        <Heading as="h3" className={styles.moduleTitle}>
          {title}
        </Heading>
      </div>
      <p className={styles.moduleDescription}>{description}</p>
      <span className={styles.moduleCta}>Start learning &rarr;</span>
    </Link>
  );
}

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          Physical AI & Humanoid Robotics
        </Heading>
        <p className="hero__subtitle">
          {siteConfig.tagline} Explore hands-on modules, simulations, and whole-body control.
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/physical-ai/module-1/weeks-1-2/intro-physical-ai">
            Start with Module 1
          </Link>
          <Link
            className={clsx('button button--outline button--lg', styles.subtleButton)}
            to="/docs/physical-ai/module-2/weeks-6-7/gazebo-simulation">
            See the roadmap
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="Hands-on modules for building physical AI and humanoid robotics systems.">
      <HomepageHeader />
      <main>
        <section className={styles.moduleSection}>
          <div className="container">
            <div className={styles.sectionHeader}>
              <Heading as="h2" className={styles.sectionTitle}>
                Choose a module
              </Heading>
              <p className={styles.sectionDescription}>
                Follow the recommended order or jump into the topic that best fits your build phase.
              </p>
            </div>
            <div className={styles.moduleGrid}>
              {modules.map((module) => (
                <ModuleCard key={module.title} {...module} />
              ))}
            </div>
          </div>
        </section>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
