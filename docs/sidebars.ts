import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'get-methods',
        'operation-description',
        'routing',
        'parameters',
        'database',
      ],
    },
    {
      type: 'category',
      label: 'Advanced Topics',
      items: [
        'userflow',
        'concepts',
        'error-handling',
        'oauth',
        'working-with-file',
      ],
    },
    {
      type: 'category',
      label: 'Project Structure',
      items: [
        'fastapi-project-structure',
        'complete-fastapi-models-guide',
      ],
    },
    {
      type: 'category',
      label: 'Production',
      items: [
        'complete-fastapi-production-guide',
      ],
    },
  ],
};

export default sidebars;