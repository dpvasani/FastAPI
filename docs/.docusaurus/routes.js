import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/about',
    component: ComponentCreator('/about', 'ca4'),
    exact: true
  },
  {
    path: '/blog',
    component: ComponentCreator('/blog', 'f6e'),
    exact: true
  },
  {
    path: '/blog/archive',
    component: ComponentCreator('/blog/archive', '182'),
    exact: true
  },
  {
    path: '/blog/authors',
    component: ComponentCreator('/blog/authors', '0b7'),
    exact: true
  },
  {
    path: '/blog/tags',
    component: ComponentCreator('/blog/tags', '287'),
    exact: true
  },
  {
    path: '/blog/tags/documentation',
    component: ComponentCreator('/blog/tags/documentation', '7e4'),
    exact: true
  },
  {
    path: '/blog/tags/fastapi',
    component: ComponentCreator('/blog/tags/fastapi', 'd40'),
    exact: true
  },
  {
    path: '/blog/tags/welcome',
    component: ComponentCreator('/blog/tags/welcome', '269'),
    exact: true
  },
  {
    path: '/blog/welcome',
    component: ComponentCreator('/blog/welcome', 'cba'),
    exact: true
  },
  {
    path: '/search',
    component: ComponentCreator('/search', '822'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '9b9'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '3c5'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '52c'),
            routes: [
              {
                path: '/docs/Complete FastAPI Models Guide',
                component: ComponentCreator('/docs/Complete FastAPI Models Guide', '239'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Complete FastAPI Production Guide Deployment, Debugging, Testing And Logging',
                component: ComponentCreator('/docs/Complete FastAPI Production Guide Deployment, Debugging, Testing And Logging', 'b75'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Concepts',
                component: ComponentCreator('/docs/Concepts', 'b65'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Database',
                component: ComponentCreator('/docs/Database', 'f3b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Error Handling',
                component: ComponentCreator('/docs/Error Handling', 'fc3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/FastAPI Dependencies',
                component: ComponentCreator('/docs/FastAPI Dependencies', '133'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/FastAPI Project Structure',
                component: ComponentCreator('/docs/FastAPI Project Structure', 'abc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/GET Methods',
                component: ComponentCreator('/docs/GET Methods', 'ec4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/OAuth',
                component: ComponentCreator('/docs/OAuth', 'dbc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Operation Description',
                component: ComponentCreator('/docs/Operation Description', '54d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Parameters',
                component: ComponentCreator('/docs/Parameters', '97a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Routing',
                component: ComponentCreator('/docs/Routing', 'bbb'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Some More Concepts',
                component: ComponentCreator('/docs/Some More Concepts', '2a3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/UserFlow',
                component: ComponentCreator('/docs/UserFlow', 'b81'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Working With File',
                component: ComponentCreator('/docs/Working With File', 'fb2'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', 'e5f'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
